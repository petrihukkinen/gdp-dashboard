"""
Pantheon+ pilot (Phase A3): replicate the flat-LCDM SN-only result of Brout et al. 2022 (Omega_m = 0.334 +/- 0.018)
with the released data and STAT+SYS covariance, then fit the DU-type magnitude-redshift family

    mu_DU(z; q) = 5 log10( z_HD ) + 2.5 q log10(1+z_hel) + const        (const absorbs M and c/H0)

q = -1 : 'bolometric' DU form (D_L = R z (1+z)^{-1/2})        [candidate identification of the article's bolometric distance]
q = +1 : Suntola & Day 2004 (astro-ph/0412701) form, D_L = R z (1+z)^{1/2}  = q=-1 form + 5 log10(1+z)
q = +3 : q=+1 form with a further 5 log10(1+z) (double application)
q free : one shape parameter, to compare fairly with flat LCDM (Omega_m).

IMPORTANT: The mapping of q to the article's equations 31/36 is UNVERIFIED (article inaccessible). The search-snippet
statement that the article adds 5 log10(1+z) 'because the K-correction removes two (1+z) factors' is audited separately
in src/kcorrection_audit.py.  Distance-modulus convention: D_L = (1+z_hel) D_M(z_HD) for LCDM (Pantheon+ convention).
M is analytically profiled (min over M) for every model; H0 and M are fully degenerate for SN-only fits.
"""
import json, math, sys
import numpy as np, pandas as pd
from scipy import integrate, optimize
np.random.seed(20260908)

dat = pd.read_csv("sources/Pantheon+SH0ES.dat", sep=r"\s+")
N = len(dat); assert N == 1701
cov_raw = np.loadtxt("sources/Pantheon+SH0ES_STAT+SYS.cov")
assert int(cov_raw[0]) == N
C_full = cov_raw[1:].reshape(N, N)
asym = np.abs(C_full - C_full.T).max()
print(f'max |C - C^T| in released file = {asym:.3e} (file precision); symmetrised as (C+C^T)/2')
C_full = 0.5*(C_full + C_full.T)
assert np.all(np.linalg.eigvalsh(C_full) > 0), 'covariance not positive definite'

# Selection as in Brout et al. 2022 SN-only fit: zHD > 0.01
sel = (dat["zHD"].values > 0.01)
z = dat["zHD"].values[sel]; zhel = dat["zHEL"].values[sel]; m = dat["m_b_corr"].values[sel]
C = C_full[np.ix_(sel, sel)]
Cinv = np.linalg.inv(C)
one = np.ones_like(m)
oCo = one @ Cinv @ one
print(f"N selected (zHD>0.01) = {sel.sum()}  ; z range {z.min():.4f}..{z.max():.3f}")

def chi2_profiled(mu_shape):
    """chi2 minimised analytically over the additive constant (M, or M + 5log10(c/H0))."""
    r = m - mu_shape
    oCr = one @ Cinv @ r
    return r @ Cinv @ r - oCr**2/oCo, oCr/oCo

# ---- flat LCDM -------------------------------------------------------------
def dc_flat(zz, Om):
    E = lambda x: 1/math.sqrt(Om*(1+x)**3 + (1-Om))
    return np.array([integrate.quad(E, 0, zi, epsabs=1e-10)[0] for zi in zz])
zgrid = np.unique(np.concatenate([[0], z]))
def mu_lcdm(Om):
    dc = dc_flat(z, Om)
    return 5*np.log10((1+zhel)*dc)          # + const (5log10(c/H0/10pc) + M) profiled out
res = optimize.minimize_scalar(lambda Om: chi2_profiled(mu_lcdm(Om))[0], bounds=(0.05, 0.9), method="bounded", options=dict(xatol=1e-5))
Om_best = res.x; chi2_lcdm = res.fun
# 1-sigma from Delta chi2 = 1
f = lambda Om: chi2_profiled(mu_lcdm(Om))[0] - chi2_lcdm - 1
Om_lo = optimize.brentq(f, 0.05, Om_best); Om_hi = optimize.brentq(f, Om_best, 0.9)
print(f"flat LCDM: Omega_m = {Om_best:.4f} (+{Om_hi-Om_best:.4f} / -{Om_best-Om_lo:.4f}), chi2 = {chi2_lcdm:.2f}, N={sel.sum()}, params(shape)=1 (+M)")
print("   Brout et al. 2022 published SN-only: Omega_m = 0.334 +/- 0.018")

# ---- non-flat LCDM (Omega_m, Omega_L) 2-parameter, for the 'two-parameter LCDM' comparison ------
def dm_curved(zz, Om, OL):
    Ok = 1-Om-OL
    E = lambda x: 1/math.sqrt(max(Om*(1+x)**3 + Ok*(1+x)**2 + OL, 1e-12))
    dc = np.array([integrate.quad(E, 0, zi, epsabs=1e-10)[0] for zi in zz])
    if abs(Ok) < 1e-8: return dc
    sk = math.sqrt(abs(Ok))
    return np.sinh(sk*dc)/sk if Ok > 0 else np.sin(sk*dc)/sk
def chi2_curved(p):
    Om, OL = p
    if Om < 0 or Om > 1.5 or OL < -1 or OL > 2: return 1e9
    return chi2_profiled(5*np.log10((1+zhel)*dm_curved(z, Om, OL)))[0]
rc = optimize.minimize(chi2_curved, x0=[0.33, 0.67], method="Nelder-Mead", options=dict(xatol=1e-4, fatol=1e-4))
print(f"open LCDM: Omega_m = {rc.x[0]:.3f}, Omega_L = {rc.x[1]:.3f}, chi2 = {rc.fun:.2f}, params(shape)=2 (+M)")

# ---- DU family ---------------------------------------------------------------
def mu_du(q):
    return 5*np.log10(z) + 2.5*q*np.log10(1+zhel)
du = {}
for q in (-1, 0, 1, 2, 3):
    c2, Mhat = chi2_profiled(mu_du(q)); du[q] = c2
    print(f"DU q={q:+d}: D_L ∝ z (1+z)^{q/2:+.1f}  chi2 = {c2:.2f}  (Δchi2 vs flat LCDM = {c2-chi2_lcdm:+.2f}), params(shape)=0 (+M)")
rq = optimize.minimize_scalar(lambda q: chi2_profiled(mu_du(q))[0], bounds=(-4, 6), method="bounded")
q_best, chi2_q = rq.x, rq.fun
fq = lambda q: chi2_profiled(mu_du(q))[0] - chi2_q - 1
q_lo = optimize.brentq(fq, -4, q_best); q_hi = optimize.brentq(fq, q_best, 6)
print(f"DU q free: q = {q_best:.3f} (+{q_hi-q_best:.3f}/-{q_best-q_lo:.3f}), chi2 = {chi2_q:.2f} (Δ vs flat LCDM {chi2_q-chi2_lcdm:+.2f}), params(shape)=1 (+M)")

# ---- A4 candidate completions (zero shape parameters each) ------------------------------------------
# C2 'L-B geodesic + Etherington': D_L = R sin(ln(1+z)) (1+z)    (from symbolic_checks A4 model L-B)
mu_LB = 5*np.log10(np.sin(np.log(1+z))*(1+zhel))
chi2_LB, _ = chi2_profiled(mu_LB)
# Reference: EdS (Omega_m=1, constant c) = closed-form D_L = 2 c/H0 (1+z)(1 - 1/sqrt(1+z))
mu_EdS = 5*np.log10((1+zhel)*2*(1-1/np.sqrt(1+z)))
chi2_EdS, _ = chi2_profiled(mu_EdS)
print(f"Candidate C2 (L-B geodesic, Etherington): chi2 = {chi2_LB:.2f} (Δ vs flat LCDM {chi2_LB-chi2_lcdm:+.2f}), params(shape)=0")
print(f"Reference EdS (Omega_m=1):                chi2 = {chi2_EdS:.2f} (Δ vs flat LCDM {chi2_EdS-chi2_lcdm:+.2f}), params(shape)=0")
du["LB"] = chi2_LB; du["EdS"] = chi2_EdS

# ---- Information criteria (same data, same likelihood, Gaussian with fixed covariance) ---------------
n = sel.sum()
def ic(chi2, kpar):  # kpar includes M
    return dict(chi2=chi2, k=kpar, AIC=chi2+2*kpar, BIC=chi2+kpar*math.log(n))
ICs = {"flat_LCDM": ic(chi2_lcdm, 2), "open_LCDM": ic(rc.fun, 3), "DU_q=+1": ic(du[1], 1), "DU_q=-1": ic(du[-1], 1),
       "DU_q=+3": ic(du[3], 1), "DU_q_free": ic(chi2_q, 2), "C2_LB_geodesic": ic(chi2_LB, 1), "EdS": ic(chi2_EdS, 1)}
print("\nModel comparison (k counts the profiled M):")
for k_, v in ICs.items():
    print(f"  {k_:12s} chi2={v['chi2']:8.2f} k={v['k']} AIC={v['AIC']:8.2f} BIC={v['BIC']:8.2f}  ΔAIC={v['AIC']-ICs['flat_LCDM']['AIC']:+7.2f}")

# ---- Out-of-sample prediction test: fit shape+M on z<0.4, evaluate on z>=0.4 ----------------------------
zsplit = 0.4
tr = z < zsplit; te = ~tr
def fit_predict(mu_fn, bounds):
    Ctr = C[np.ix_(tr, tr)]; Ctr_inv = np.linalg.inv(Ctr); otr = np.ones(tr.sum())
    def chi2tr(p):
        r = m[tr] - mu_fn(p)[tr]; oCr = otr @ Ctr_inv @ r
        return r @ Ctr_inv @ r - oCr**2/(otr @ Ctr_inv @ otr)
    rr = optimize.minimize_scalar(chi2tr, bounds=bounds, method="bounded")
    p = rr.x; r = m[tr] - mu_fn(p)[tr]
    Mhat = (otr @ Ctr_inv @ r)/(otr @ Ctr_inv @ otr)
    Cte_inv = np.linalg.inv(C[np.ix_(te, te)])
    rte = m[te] - mu_fn(p)[te] - Mhat
    return p, rr.fun, rte @ Cte_inv @ rte, rte
p_l, c_l_tr, c_l_te, r_l = fit_predict(lambda Om: mu_lcdm(Om), (0.05, 0.9))
p_q, c_q_tr, c_q_te, r_q = fit_predict(lambda q: mu_du(q), (-4, 6))
c_1_te = None
# fixed q=+1: only M fitted on train
Ctr_inv = np.linalg.inv(C[np.ix_(tr, tr)]); otr = np.ones(tr.sum())
r = m[tr]-mu_du(1)[tr]; M1 = (otr@Ctr_inv@r)/(otr@Ctr_inv@otr)
rte1 = m[te]-mu_du(1)[te]-M1; c_1_te = rte1 @ np.linalg.inv(C[np.ix_(te, te)]) @ rte1
print(f"\nPrediction test (train z<{zsplit}: N={tr.sum()}, test z>={zsplit}: N={te.sum()}):")
print(f"  flat LCDM : Omega_m(train)={p_l:.3f}, test chi2 = {c_l_te:.2f}, mean test residual = {r_l.mean():+.4f} mag")
print(f"  DU q free : q(train)={p_q:.3f},        test chi2 = {c_q_te:.2f}, mean test residual = {r_q.mean():+.4f} mag")
print(f"  DU q=+1   : (M only)                 test chi2 = {c_1_te:.2f}, mean test residual = {rte1.mean():+.4f} mag")

# ---- binned residuals vs best flat LCDM and DU q=+1 ------------------------------------------------------
_, M_l = chi2_profiled(mu_lcdm(Om_best)); _, M_1 = chi2_profiled(mu_du(1)); _, M_q = chi2_profiled(mu_du(q_best))
res_l = m - mu_lcdm(Om_best) - M_l; res_1 = m - mu_du(1) - M_1; res_q = m - mu_du(q_best) - M_q
edges = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.2, 1.6, 2.4])
rows = []
sig_diag = np.sqrt(np.diag(C))
for a, b in zip(edges[:-1], edges[1:]):
    kk = (z >= a) & (z < b)
    if kk.sum() == 0: continue
    w = 1/sig_diag[kk]**2
    rows.append(dict(z_lo=a, z_hi=b, n=int(kk.sum()),
                     res_LCDM=float(np.sum(w*res_l[kk])/w.sum()), res_DU_q1=float(np.sum(w*res_1[kk])/w.sum()),
                     res_DU_qfree=float(np.sum(w*res_q[kk])/w.sum()), err_diag=float(1/math.sqrt(w.sum()))))
print("\nBinned weighted-mean residuals (mag; diagonal weights, for display only):")
print(f"{'z_lo':>6s} {'z_hi':>6s} {'n':>5s} {'LCDM':>8s} {'DU q=+1':>8s} {'DU qfit':>8s} {'±':>7s}")
for r_ in rows:
    print(f"{r_['z_lo']:6.2f} {r_['z_hi']:6.2f} {r_['n']:5d} {r_['res_LCDM']:+8.4f} {r_['res_DU_q1']:+8.4f} {r_['res_DU_qfree']:+8.4f} {r_['err_diag']:7.4f}")

import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
ax[0].errorbar(z, m - M_l, yerr=sig_diag, fmt=".", ms=2, alpha=0.3, color="gray", label="Pantheon+ (zHD>0.01)")
zz = np.logspace(-2, math.log10(2.4), 200); zzh = zz
ax[0].plot(zz, 5*np.log10((1+zzh)*dc_flat(zz, Om_best)), label=f"flat ΛCDM Ωm={Om_best:.3f}")
ax[0].plot(zz, 5*np.log10(zz)+2.5*1*np.log10(1+zzh) + (M_1-M_l), "--", label="DU q=+1 (z√(1+z))")
ax[0].plot(zz, 5*np.log10(zz)+2.5*q_best*np.log10(1+zzh) + (M_q-M_l), ":", label=f"DU q={q_best:.2f}")
ax[0].set_xscale("log"); ax[0].set_ylabel("m_b_corr − M̂ (LCDM offset)"); ax[0].legend()
zc = [(r_['z_lo']*r_['z_hi'])**0.5 for r_ in rows]
ax[1].errorbar(zc, [r_['res_LCDM'] for r_ in rows], yerr=[r_['err_diag'] for r_ in rows], fmt="o", label="ΛCDM")
ax[1].errorbar(zc, [r_['res_DU_q1'] for r_ in rows], yerr=[r_['err_diag'] for r_ in rows], fmt="s", label="DU q=+1")
ax[1].errorbar(zc, [r_['res_DU_qfree'] for r_ in rows], yerr=[r_['err_diag'] for r_ in rows], fmt="^", label=f"DU q={q_best:.2f}")
ax[1].axhline(0, color="k", lw=0.5); ax[1].set_xlabel("z_HD"); ax[1].set_ylabel("binned residual (mag)"); ax[1].legend()
plt.tight_layout(); plt.savefig("results/pantheon_hubble_residuals.png", dpi=130)

json.dump(dict(N=int(n), selection="zHD>0.01", flat_LCDM=dict(Om=Om_best, Om_lo=Om_lo, Om_hi=Om_hi, chi2=chi2_lcdm),
               published_Brout2022=dict(Om=0.334, err=0.018), open_LCDM=dict(Om=rc.x[0], OL=rc.x[1], chi2=rc.fun),
               DU_fixed_q={str(k_): v for k_, v in du.items()}, DU_q_free=dict(q=q_best, q_lo=q_lo, q_hi=q_hi, chi2=chi2_q),
               IC=ICs, prediction_test=dict(zsplit=zsplit, Ntrain=int(tr.sum()), Ntest=int(te.sum()),
                   LCDM=dict(Om_train=p_l, chi2_test=c_l_te, mean_res=float(r_l.mean())),
                   DU_qfree=dict(q_train=p_q, chi2_test=c_q_te, mean_res=float(r_q.mean())),
                   DU_q1=dict(chi2_test=c_1_te, mean_res=float(rte1.mean()))),
               binned_residuals=rows), open("results/pantheon_fit.json", "w"), indent=2)
print("written results/pantheon_fit.json, results/pantheon_hubble_residuals.png")
