"""
TASK A — decisive supernova test.

Externally supplied statement of the article's Pantheon conversion (provenance: user-supplied 2026-09-08, verified
externally; NOT fetched by this environment):
    bolometric DU luminosity distance  D_L = z sqrt(1+z) R4
    followed by adding 2.5 log10[(1+z)^2] = 5 log10(1+z) to the magnitude.

Derivation of the implied relation:
    m_bol = M + 5 log10(D_L/10pc) = M + 5 log10(R4/10pc) + 5 log10 z + 2.5 log10(1+z)
    m_cat = m_bol + 5 log10(1+z)   = M + 5 log10(R4/10pc) + 5 log10 z + 7.5 log10(1+z)
          = M + 5 log10( R4 z (1+z)^{3/2} / 10pc )
Hence, absent any other term, the catalog-frame relation is EXACTLY that of an effective distance
    D_eff = R4 z (1+z)^{3/2}      (p = 1.5 in D_L ∝ z(1+z)^p ; q = 3 in the src/pantheon_fit.py convention D_L ∝ z(1+z)^{q/2}).
This is 'the relation implied by the published textual transformation', not a transcription of a rendered equation.

Models (identical data: Pantheon+ zHD>0.01, N=1590; identical STAT+SYS covariance; identical analytic profiling of M):
    A  raw/bolometric DU      p = 0.5
    B  implied K-corrected DU p = 1.5
    C  free p
    D  flat LCDM (Omega_m)
"""
import json, math
import numpy as np
from scipy import optimize
from pantheon_common import load, chi2_profiled, mu_lcdm, mu_du_p, dc_flat
np.random.seed(20260908)
D = load(); n = D["N"]; z = D["z"]; zhel = D["zhel"]; m = D["m"]
print(f"N = {n}, zHD range {z.min():.4f}..{z.max():.3f}")

def fit_scalar(fn, bounds):
    r = optimize.minimize_scalar(lambda x: chi2_profiled(D, fn(x))[0], bounds=bounds, method="bounded", options=dict(xatol=1e-6))
    f = lambda x: chi2_profiled(D, fn(x))[0] - r.fun - 1
    lo = optimize.brentq(f, bounds[0], r.x); hi = optimize.brentq(f, r.x, bounds[1])
    return r.x, r.fun, lo, hi

Om, c2_l, Om_lo, Om_hi = fit_scalar(lambda x: mu_lcdm(D, x), (0.05, 0.9))
p_best, c2_p, p_lo, p_hi = fit_scalar(lambda x: mu_du_p(D, x), (-2, 3))
c2_A, M_A = chi2_profiled(D, mu_du_p(D, 0.5)); c2_B, M_B = chi2_profiled(D, mu_du_p(D, 1.5))
_, M_l = chi2_profiled(D, mu_lcdm(D, Om)); _, M_p = chi2_profiled(D, mu_du_p(D, p_best))
def ic(c2, k): return dict(chi2=c2, k=k, AIC=c2 + 2*k, BIC=c2 + k*math.log(n), dchi2=c2 - c2_l, dAIC=c2 + 2*k - (c2_l + 4), dBIC=c2 + k*math.log(n) - (c2_l + 2*math.log(n)))
table = {"A_DU_bolometric_p0.5": ic(c2_A, 1), "B_DU_implied_Kcorr_p1.5": ic(c2_B, 1), "C_DU_free_p": ic(c2_p, 2), "D_flat_LCDM": ic(c2_l, 2)}
print(f"\n{'model':28s} {'chi2':>9s} {'dchi2':>9s} {'k':>2s} {'AIC':>9s} {'dAIC':>9s} {'BIC':>9s} {'dBIC':>9s}")
for k_, v in table.items():
    print(f"{k_:28s} {v['chi2']:9.2f} {v['dchi2']:+9.2f} {v['k']:2d} {v['AIC']:9.2f} {v['dAIC']:+9.2f} {v['BIC']:9.2f} {v['dBIC']:+9.2f}")
print(f"\nD: Omega_m = {Om:.4f} (+{Om_hi-Om:.4f}/-{Om-Om_lo:.4f})")
print(f"C: p = {p_best:.4f} (+{p_hi-p_best:.4f}/-{p_best-p_lo:.4f})  [= q/2 with q = {2*p_best:.3f} in src/pantheon_fit.py convention]")
print(f"B: p=1.5 is {(1.5-p_best)/((p_hi-p_lo)/2):.0f} sigma from the best-fit p ; A: p=0.5 is {(p_best-0.5)/((p_hi-p_lo)/2):.0f} sigma.")
# chi2/dof and Gaussian tail of dchi2 for the nested comparison C vs B (B is C with p fixed): p-value of dchi2 with 1 dof
from scipy import stats
for name, c2 in (("A", c2_A), ("B", c2_B)):
    d = c2 - c2_p
    print(f"  nested test {name} vs free p: dchi2 = {d:.1f} (1 dof) -> p = {stats.chi2.sf(d, 1):.1e}")

# Residuals vs redshift (binned, diagonal weights for display) -------------------------------------------------
sig = np.sqrt(np.diag(D["C"]))
edges = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.2, 1.6, 2.4])
res = {"A": m - mu_du_p(D, 0.5) - M_A, "B": m - mu_du_p(D, 1.5) - M_B, "C": m - mu_du_p(D, p_best) - M_p, "D": m - mu_lcdm(D, Om) - M_l}
rows = []
print(f"\n{'z_lo':>5s} {'z_hi':>5s} {'n':>4s} {'A p=0.5':>8s} {'B p=1.5':>8s} {'C free':>8s} {'D LCDM':>8s} {'±':>6s}")
for a, b in zip(edges[:-1], edges[1:]):
    kk = (z >= a) & (z < b)
    if not kk.any(): continue
    w = 1/sig[kk]**2
    r_ = {k_: float(np.sum(w*v[kk])/w.sum()) for k_, v in res.items()}
    rows.append(dict(z_lo=a, z_hi=b, n=int(kk.sum()), err=float(1/math.sqrt(w.sum())), **r_))
    print(f"{a:5.2f} {b:5.2f} {kk.sum():4d} {r_['A']:+8.3f} {r_['B']:+8.3f} {r_['C']:+8.3f} {r_['D']:+8.3f} {1/math.sqrt(w.sum()):6.3f}")
# Slope of residual vs log10(1+z) for B: quantifies the systematic tilt
X = np.column_stack([np.ones(n), np.log10(1+z)])
Wd = np.diag(1/sig**2)
beta_B = np.linalg.solve(X.T @ Wd @ X, X.T @ Wd @ res["B"])
print(f"\nB residual tilt: d(res)/d log10(1+z) = {beta_B[1]:+.3f} mag/dex  (a pure extra 5 log10(1+z) would tilt by 5.0 if uncompensated by M)")

# Train/test (same split as pantheon_fit.py) --------------------------------------------------------------------
tr = z < 0.4; te = ~tr
def train_test(fn, bounds=None, fixed=None):
    if fixed is None:
        r = optimize.minimize_scalar(lambda x: chi2_profiled(D, fn(x), tr)[0], bounds=bounds, method="bounded"); x = r.x
    else: x = fixed
    _, Mhat = chi2_profiled(D, fn(x), tr)
    rte = m[te] - fn(x)[te] - Mhat
    return x, float(rte @ np.linalg.inv(D["C"][np.ix_(te, te)]) @ rte), float(rte.mean())
tt = {"A": train_test(lambda x: mu_du_p(D, x), fixed=0.5), "B": train_test(lambda x: mu_du_p(D, x), fixed=1.5),
      "C": train_test(lambda x: mu_du_p(D, x), bounds=(-2, 3)), "D": train_test(lambda x: mu_lcdm(D, x), bounds=(0.05, 0.9))}
print(f"\nTrain z<0.4 (N={tr.sum()}), test z>=0.4 (N={te.sum()}):")
for k_, (x, c2t, mr) in tt.items(): print(f"  {k_}: param={x:.3f}  test chi2 = {c2t:8.2f}  mean test residual = {mr:+.3f} mag")

import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 4.5)); zc = [(r_["z_lo"]*r_["z_hi"])**0.5 for r_ in rows]
for k_, lab, mk in (("A", "A: DU bolometric p=0.5", "s"), ("B", "B: DU implied K-corr p=1.5", "^"), ("C", f"C: DU free p={p_best:.2f}", "v"), ("D", f"D: flat ΛCDM Ωm={Om:.3f}", "o")):
    ax.errorbar(zc, [r_[k_] for r_ in rows], yerr=[r_["err"] for r_ in rows], fmt=mk, label=lab, capsize=2)
ax.axhline(0, color="k", lw=0.5); ax.set_xscale("log"); ax.set_xlabel("z_HD"); ax.set_ylabel("binned residual m − model (mag)"); ax.legend(fontsize=8)
ax.set_title("Pantheon+ (N=1590, STAT+SYS): decisive DU test"); plt.tight_layout(); plt.savefig("results/pantheon_decisive_residuals.png", dpi=130)
json.dump(dict(N=n, convention="D_L = R4 z (1+z)^p ; p = q/2 relative to pantheon_fit.py", implied_relation="m_cat = M + 5log10(R4 z (1+z)^1.5 /10pc) <=> p=1.5 (derived from user-supplied textual transformation, not from a rendered equation)",
               table=table, Om=dict(best=Om, lo=Om_lo, hi=Om_hi), p_free=dict(best=p_best, lo=p_lo, hi=p_hi), residual_tilt_B_mag_per_dex=float(beta_B[1]),
               binned_residuals=rows, train_test={k_: dict(param=v[0], chi2_test=v[1], mean_res=v[2]) for k_, v in tt.items()},
               provenance="Article statements externally supplied by user (2026-09-08); environment could not fetch the article."),
          open("results/pantheon_decisive_test.json", "w"), indent=2)
print("written results/pantheon_decisive_test.json, results/pantheon_decisive_residuals.png")
