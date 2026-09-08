"""
Bilfinger Performance Outsourcing — SYNTHETIC dynamic prototype (Phase B3).

This is a methodological transfer (system boundary, traceable assumptions, state-space dynamics, measurement vs
interpretation, uncertainty, pre-registered rejection criteria). It is NOT a physics analogy, NOT a proven ROI, and
uses NO company, customer, personnel or contract data. All parameters are synthetic and listed in PARAMS.

State x(t) = [h asset health (0-1), b risk-weighted backlog (norm. hours), s critical competence (0-1),
              d latent integrity debt (>=0), q data quality (0-1)]
Control u(t) = [pm preventive-maintenance effort, corr corrective capacity used, train competence investment,
                integ integrity-work effort, capex_request flag, data investment]
Exogenous w(t) = [load, condition shocks, attrition shock, demand fraction, capex approval delay (client decision)]
theta = uncertain parameters (sampled per Monte Carlo path; identical across policies = common random numbers)
Observation y(t) = availability, backlog reported, cost, events (with measurement noise / possible gaming)

Three policies with the SAME initial state and SAME shock realisations:
  P0 baseline (client in-house, as-is), P1 short-term-cost control, P2 lifecycle-performance control.
Value accounting (B2): joint incremental value = ΔPV(production margin) + ΔPV(resource savings)
  − PV(transition & development cost) − ΔPV(expected residual loss).  Fee only redistributes.
"""
from __future__ import annotations
import json, math, copy
import numpy as np, pandas as pd

SEED = 20260908
NMC, HORIZON = 2000, 60                       # paths, months
PARAMS = dict(
    # dynamics
    degr_rate=0.009,          # calibrated so that P0 is near-stationary (see README of results)          # base monthly health loss at load=1
    backlog_health_coupling=0.6,
    pm_effect=0.040,          # health regained per unit pm effort at full competence
    arrival_rate=0.45,         # backlog arrivals per month at h=1, load=1 (norm. hours)
    arrival_health_gain=1.2,  # arrivals grow as health falls
    corr_capacity=1.0,        # backlog burn per month at capacity 1, competence 1
    attrition=0.003, train_effect=0.05,
    debt_from_deferral=0.35,  # share of deferred backlog turning into latent integrity debt
    integ_effect=0.25,        # debt reduced per unit integrity effort
    event_lambda=0.008,       # monthly event prob = 1-exp(-lambda*d)
    event_downtime=0.12,      # availability lost in event month
    event_loss=1.5e6,         # EUR direct loss (repair, HSE, regulatory) per event
    # availability
    A_max=0.96, a_h=0.25, a_b=0.012,   # backlog effect capped at b=10
    # economics (EUR)
    hours_month=720.0, contribution_margin_per_hour=6000.0,
    demand_fraction=0.93,      # sales-limited: availability above this earns nothing
    cost_per_pm_unit=180e3, cost_per_corr_unit=220e3, cost_per_train_unit=250e3, cost_per_integ_unit=200e3,
    cost_data=40e3, capex_amount=6e6, capex_health_gain=0.25, client_capex_lag=12,
    transition_cost=1.8e6, transition_months=6, transition_eff=0.7,
    discount_annual=0.08,
    # fee (P1/P2 = outsourced): fixed + gain share of verified margin uplift vs baseline
    fee_fixed_month=300e3, gain_share=0.35,   # fixed fee ≈ client's as-is opex level; gain share on verified uplift
    # measurement
    A_noise=0.005, backlog_noise=0.05,
)
STRESS = {
    "none": {},
    "latent_debt": dict(event_lambda=0.03),
    "capex_delay": dict(client_capex_lag=24),
    "skills_shortage": dict(attrition_shock_month=24, attrition_shock=0.05),
    "poor_data": dict(A_noise=0.02, backlog_noise=0.25, missing_frac=0.2),
    "demand_shock": dict(demand_shock=(30, 42, 0.70)),
    "transition_delay": dict(transition_months=12, transition_eff=0.6),
    "kpi_gaming": dict(gaming_bias=0.02),
    "end_of_contract": dict(eoc_defer=True),
}

def policy(name, t, x, P, st):
    """Returns control vector for a whole MC vector of states (vectorised)."""
    h, b, s, d, q = x
    n = h.size
    u = dict(pm=np.zeros(n), corr=np.zeros(n), train=np.zeros(n), integ=np.zeros(n),
             capex_req=np.zeros(n, bool), data=np.zeros(n))
    if name == "P0":            # as-is: fixed mix, reactive on backlog
        u["pm"][:] = 0.35; u["corr"][:] = np.clip(0.6 + 0.4*(b > 2.0), 0, 1.0)
        u["train"][:] = 0.01; u["integ"][:] = 0.05
        u["capex_req"] = h < 0.55
    elif name == "P1":          # short-term cost: budget cap, defer when backlog high, no training
        u["pm"][:] = 0.20; u["corr"][:] = 0.55
        u["train"][:] = 0.0; u["integ"][:] = 0.02
        defer = (b > 2.5)
        u["corr"][defer] = 0.45                # 'saving': fewer hours -> deferral
        if st.get("eoc_defer") and t >= HORIZON - 12:
            u["pm"][:] = 0.10; u["corr"][:] = 0.40; u["integ"][:] = 0.0
        u["capex_req"] = h < 0.45
    elif name == "P2":          # lifecycle: risk-based pm, integrity work, competence, early capex, data
        risk = (1 - h) + 0.15*b + 0.3*d
        u["pm"][:] = np.clip(0.30 + 0.5*risk, 0.3, 0.8)
        u["corr"][:] = np.clip(0.6 + 0.3*(b > 1.5), 0, 1.0)
        u["train"][:] = 0.03; u["integ"][:] = np.clip(0.08 + 0.3*d, 0.08, 0.4)
        u["capex_req"] = h < 0.70
        u["data"][:] = 1.0
    return u

def simulate(name, P, st, rng_streams):
    P = {**P, **{k: v for k, v in st.items() if k in P}}
    disc = (1 + P["discount_annual"])**(-1/12)
    n = NMC
    # theta: uncertain parameters per path (log-normal ±25 %)
    th = rng_streams["theta"]
    degr = P["degr_rate"]*th[0]; pm_eff = P["pm_effect"]*th[1]; lam = P["event_lambda"]*th[2]; arr = P["arrival_rate"]*th[3]
    h = np.full(n, 0.75); b = np.full(n, 1.5); s = np.full(n, 0.70); d = np.full(n, 0.5); q = np.full(n, 0.6)
    capex_pending = np.full(n, -1)          # month when capex will land (client decision lag)
    rec = dict(A=[], A_rep=[], margin=[], cost=[], events=[], b=[], h=[], d=[], s=[], fee=[], transition=[])
    pv_margin = np.zeros(n); pv_cost = np.zeros(n); pv_capex = np.zeros(n); pv_loss = np.zeros(n); pv_trans = np.zeros(n); pv_fee = np.zeros(n)
    outsourced = name in ("P1", "P2")
    for t in range(HORIZON):
        w_load = rng_streams["load"][t]; w_cond = rng_streams["cond"][t]; w_evt = rng_streams["evt"][t]
        demand = P["demand_fraction"]
        if "demand_shock" in st and st["demand_shock"][0] <= t < st["demand_shock"][1]:
            demand = st["demand_shock"][2]
        u = policy(name, t, (h, b, s, d, q), P, st)
        eff = np.ones(n)
        if outsourced and t < P["transition_months"]:
            eff[:] = P["transition_eff"]; pv_trans += (P["transition_cost"]/P["transition_months"])*disc**t
        s_eff = eff*(0.5 + 0.5*s)
        # dynamics ------------------------------------------------------------------
        arrivals = arr*w_load*(1 + P["arrival_health_gain"]*(1-h))
        burn = P["corr_capacity"]*u["corr"]*s_eff
        deferred = np.clip(arrivals - burn, 0, None)
        h_new = h - degr*w_load*(1 + P["backlog_health_coupling"]*np.clip(b, 0, 5)/5) + pm_eff*u["pm"]*s_eff - w_cond
        # capex: request -> client decides after lag -> health jump
        newreq = u["capex_req"] & (capex_pending < 0)
        capex_pending[newreq] = t + P["client_capex_lag"]
        landing = (capex_pending == t)
        h_new[landing] += P["capex_health_gain"]; capex_cost = landing*P["capex_amount"]
        capex_pending[landing] = 10**6      # one capex per horizon
        b_new = np.clip(b + arrivals - burn, 0, None)
        attr = P["attrition"] + (st.get("attrition_shock", 0) if t >= st.get("attrition_shock_month", 10**6) else 0)
        s_new = np.clip(s - attr + P["train_effect"]*u["train"], 0.05, 1)
        d_new = np.clip(d + P["debt_from_deferral"]*deferred*(1-h) - P["integ_effect"]*u["integ"]*s_eff, 0, None)
        q_new = np.clip(q + 0.03*u["data"] - 0.005, 0.2, 1)
        # events (latent debt realised) ----------------------------------------------
        p_evt = 1 - np.exp(-lam*d_new)
        evt = w_evt < p_evt
        A = np.clip(P["A_max"] - P["a_h"]*(1-h_new) - P["a_b"]*np.minimum(b_new, 10) - P["event_downtime"]*evt, 0.3, 1)
        # observation model -------------------------------------------------------------
        noise = rng_streams["meas"][t]*P["A_noise"]*(1.5 - q_new)     # better data -> less noise
        A_rep = A + noise + (st.get("gaming_bias", 0) if name == "P1" else 0)
        # economics -------------------------------------------------------------------
        sold = np.minimum(A, demand)                                   # demand-limited
        margin = sold*P["hours_month"]*P["contribution_margin_per_hour"]
        opex = (u["pm"]*P["cost_per_pm_unit"] + u["corr"]*P["cost_per_corr_unit"] + u["train"]*P["cost_per_train_unit"]
                + u["integ"]*P["cost_per_integ_unit"] + u["data"]*P["cost_data"])
        cost = opex + capex_cost
        loss = evt*P["event_loss"]
        df = disc**t
        pv_margin += margin*df; pv_cost += opex*df; pv_capex += capex_cost*df; pv_loss += loss*df
        if outsourced: pv_fee += P["fee_fixed_month"]*df
        for k_, v_ in (("A", A), ("A_rep", A_rep), ("margin", margin), ("cost", cost), ("events", evt.astype(float)),
                       ("b", b_new), ("h", h_new), ("d", d_new), ("s", s_new)):
            rec[k_].append(v_.copy())
        h, b, s, d, q = np.clip(h_new, 0.05, 1), b_new, s_new, d_new, q_new
    rec = {k_: np.array(v_) for k_, v_ in rec.items() if v_}
    return dict(pv_margin=pv_margin, pv_cost=pv_cost, pv_capex=pv_capex, pv_loss=pv_loss, pv_trans=pv_trans, pv_fee_fixed=pv_fee,
                rec=rec, final=dict(h=h, b=b, s=s, d=d))

def run_all():
    rng = np.random.default_rng(SEED)
    streams = dict(theta=np.exp(rng.normal(0, 0.25, (4, NMC))),
                   load=np.clip(rng.normal(1.0, 0.08, (HORIZON, NMC)), 0.6, 1.4),
                   cond=np.clip(rng.exponential(0.002, (HORIZON, NMC)), 0, 0.05),
                   evt=rng.uniform(0, 1, (HORIZON, NMC)),
                   meas=rng.normal(0, 1, (HORIZON, NMC)))
    summary = []; series = {}
    for stress, st in STRESS.items():
        res = {p: simulate(p, PARAMS, st, streams) for p in ("P0", "P1", "P2")}
        base = res["P0"]
        for p, r in res.items():
            # JOINT incremental value vs P0 (fee cancels): Δmargin − Δopex − Δcapex − Δloss − transition
            joint = ((r["pv_margin"] - base["pv_margin"]) - (r["pv_cost"] - base["pv_cost"]) - (r["pv_capex"] - base["pv_capex"])
                     - (r["pv_loss"] - base["pv_loss"]) - r["pv_trans"])
            # gain-share fee on REPORTED availability uplift vs the P0 counterfactual (in a real contract: vs a contractual baseline)
            uplift_rep = np.clip(((r["rec"]["A_rep"] - base["rec"]["A"]).clip(0) * PARAMS["hours_month"]*PARAMS["contribution_margin_per_hour"]).sum(0), 0, None)
            fee_total = (r["pv_fee_fixed"] + PARAMS["gain_share"]*uplift_rep) if p != "P0" else np.zeros(NMC)
            # Bilfinger (outsourced policies): fee − delivery opex − transition. Client: margin − loss − capex − (fee | own opex)
            bilf = fee_total - r["pv_cost"] - r["pv_trans"] if p != "P0" else np.zeros(NMC)
            client = r["pv_margin"] - r["pv_loss"] - r["pv_capex"] - (r["pv_cost"] if p == "P0" else fee_total)
            client_inc = client - (base["pv_margin"] - base["pv_loss"] - base["pv_capex"] - base["pv_cost"])
            def q_(a): return [float(np.mean(a)), float(np.percentile(a, 10)), float(np.percentile(a, 90))]
            summary.append(dict(stress=stress, policy=p,
                joint_incremental_value_MEUR=q_(joint/1e6), client_incremental_MEUR=q_(client_inc/1e6),
                bilfinger_net_MEUR=q_(bilf/1e6), fee_total_MEUR=q_(fee_total/1e6),
                pv_opex_MEUR=q_(r["pv_cost"]/1e6), pv_capex_MEUR=q_(r["pv_capex"]/1e6), pv_loss_MEUR=q_(r["pv_loss"]/1e6),
                mean_availability=float(r["rec"]["A"].mean()), mean_reported_availability=float(r["rec"]["A_rep"].mean()),
                p_any_event=float((r["rec"]["events"].sum(0) > 0).mean()), events_per_path=float(r["rec"]["events"].sum(0).mean()),
                final_health=float(r["final"]["h"].mean()), final_backlog=float(r["final"]["b"].mean()),
                final_debt=float(r["final"]["d"].mean()), final_competence=float(r["final"]["s"].mean()),
                cost_first12_MEUR=float(r["rec"]["cost"][:12].sum(0).mean()/1e6), cost_last12_MEUR=float(r["rec"]["cost"][-12:].sum(0).mean()/1e6),
                p_joint_negative=float((joint < 0).mean())))
            if stress in ("none", "end_of_contract", "kpi_gaming"):
                series[(stress, p)] = dict(A=r["rec"]["A"].mean(1), h=r["rec"]["h"].mean(1), d=r["rec"]["d"].mean(1), b=r["rec"]["b"].mean(1), cost=r["rec"]["cost"].mean(1))
    return pd.DataFrame(summary), series

if __name__ == "__main__":
    df, series = run_all()
    df.to_csv("results/bilfinger_mc_summary.csv", index=False)
    pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
    cols = ["stress", "policy", "joint_incremental_value_MEUR", "client_incremental_MEUR", "bilfinger_net_MEUR", "mean_availability",
            "p_any_event", "final_health", "final_debt", "cost_first12_MEUR", "cost_last12_MEUR", "p_joint_negative"]
    print(df[cols].to_string(index=False))
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(11, 7))
    for (stress, p), sr in series.items():
        if stress != "none": continue
        ax[0, 0].plot(sr["A"], label=p); ax[0, 1].plot(sr["h"], label=p); ax[1, 0].plot(sr["d"], label=p); ax[1, 1].plot(sr["cost"]/1e3, label=p)
    for a, ttl in zip(ax.flat, ("availability (true)", "asset health", "latent integrity debt", "monthly cost kEUR")):
        a.set_title(ttl); a.set_xlabel("month"); a.legend()
    plt.suptitle("SYNTHETIC prototype — mean paths, stress=none"); plt.tight_layout()
    plt.savefig("results/bilfinger_mean_paths.png", dpi=120)
    # pre-registered rejection checks on the synthetic run (for the method, not for Bilfinger's business case)
    none = df[df.stress == "none"].set_index("policy")
    checks = {
        "P1 shows early cost saving vs P0 (first 12 months)": bool(none.loc["P1", "cost_first12_MEUR"] < none.loc["P0", "cost_first12_MEUR"]),
        "P1 ends with higher latent debt than P0": bool(none.loc["P1", "final_debt"] > none.loc["P0", "final_debt"]),
        "P2 joint incremental value mean > 0": bool(none.loc["P2", "joint_incremental_value_MEUR"][0] > 0),
        "P2 joint value p10 > 0 (robustness)": bool(none.loc["P2", "joint_incremental_value_MEUR"][1] > 0),
        "fee redistributes only: client_inc + bilfinger_net == joint (P2, exact identity)": bool(abs(none.loc["P2", "client_incremental_MEUR"][0] + none.loc["P2", "bilfinger_net_MEUR"][0] - none.loc["P2", "joint_incremental_value_MEUR"][0]) < 1e-6),
    }
    gaming = df[(df.stress == "kpi_gaming") & (df.policy == "P1")].iloc[0]
    checks["KPI gaming detectable: reported − true availability > 3σ_noise"] = bool((gaming.mean_reported_availability - gaming.mean_availability) > 3*PARAMS["A_noise"]/math.sqrt(HORIZON))
    print("\nPre-registered synthetic checks:"); [print(f"  [{'OK' if v else 'FAIL'}] {k}") for k, v in checks.items()]
    json.dump(dict(params=PARAMS, stress=STRESS, checks=checks, seed=SEED, nmc=NMC, horizon=HORIZON), open("results/bilfinger_prototype_meta.json", "w"), indent=2, default=str)
    print("written results/bilfinger_mc_summary.csv, results/bilfinger_prototype_meta.json, results/bilfinger_mean_paths.png")
