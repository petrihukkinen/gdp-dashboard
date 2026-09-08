"""
Verification round (step 3): statistical audit of the supernova test.
 (a) parametrisation check: q (pantheon_fit: D_L ∝ z(1+z)^{q/2}) vs p (decisive: D_L ∝ z(1+z)^p) -> p = q/2, verified numerically
 (b) absolute goodness of fit: chi2/dof and chi2 tail probability for each model (Gaussian likelihood, fixed covariance)
 (c) separation of: parameter-deviation sigma (Wald, 1 dof), relative model comparison (dchi2, dBIC), absolute fit
 (d) held-out subset diagnostic done PROPERLY: Gaussian conditional prediction of the z>=0.4 block given the z<0.4 block
     (uses the cross-covariance), compared with the earlier block-only evaluation; labelled as a same-dataset diagnostic
 (e) sensitivity to the BBC bias correction (m_b_corr includes biasCor_m_b derived with a reference cosmology):
     refit with the bias correction removed as a bounding exercise (this is NOT a better dataset)
 (f) sensitivity to selection: zmin = 0.023 and exclusion of the Cepheid-host calibrators
"""
import json, math, numpy as np, pandas as pd
from scipy import optimize, stats
from pantheon_common import load, chi2_profiled, mu_lcdm, mu_du_p
out = {}
D = load(); n = D["N"]
dat = pd.read_csv("sources/Pantheon+SH0ES.dat", sep=r"\s+"); sel = dat["zHD"].values > 0.01
# (a)
p_test = 0.7
mu_q = 5*np.log10(D["z"]) + 2.5*(2*p_test)*np.log10(1+D["zhel"])   # pantheon_fit convention with q = 2p
mu_p = mu_du_p(D, p_test)
assert np.allclose(mu_q, mu_p); out["parametrisation"] = "verified: mu(q=2p) == mu(p); p is the exponent of (1+z) in D_L, q/2 = p"
print("(a) parametrisation: q = 2p verified numerically")
# (b),(c)
def fit(fn, bounds):
    r = optimize.minimize_scalar(lambda x: chi2_profiled(D, fn(x))[0], bounds=bounds, method="bounded", options=dict(xatol=1e-6)); return r.x, r.fun
Om, c2_l = fit(lambda x: mu_lcdm(D, x), (0.05, 0.9)); pbest, c2_p = fit(lambda x: mu_du_p(D, x), (-2, 3))
models = {"D flat LCDM": (c2_l, 2), "A DU p=0.5": (chi2_profiled(D, mu_du_p(D, 0.5))[0], 1), "B DU p=1.5": (chi2_profiled(D, mu_du_p(D, 1.5))[0], 1), "C DU free p": (c2_p, 2)}
print("\n(b,c) absolute vs relative:")
print(f"{'model':14s} {'chi2':>9s} {'k':>2s} {'dof':>5s} {'chi2/dof':>9s} {'P(chi2>=obs|dof)':>17s} {'dchi2':>9s} {'dBIC':>9s}")
tab = {}
for name, (c2, k) in models.items():
    dof = n - k; pval = stats.chi2.sf(c2, dof)
    tab[name] = dict(chi2=c2, k=k, dof=dof, chi2_dof=c2/dof, p_abs=pval, dchi2=c2 - c2_l, dBIC=(c2 + k*math.log(n)) - (c2_l + 2*math.log(n)))
    print(f"{name:14s} {c2:9.2f} {k:2d} {dof:5d} {c2/dof:9.3f} {pval:17.2e} {c2-c2_l:+9.2f} {tab[name]['dBIC']:+9.2f}")
wald_A = math.sqrt(models['A DU p=0.5'][0] - c2_p); wald_B = math.sqrt(models['B DU p=1.5'][0] - c2_p)
print(f"  Wald-type parameter deviation (nested in free p, 1 dof): p=0.5 -> {wald_A:.1f} sigma ; p=1.5 -> {wald_B:.1f} sigma")
print("  Interpretation rules: dchi2/dBIC compare models on the same data; chi2/dof and P(chi2) judge absolute fit given the")
print("  released covariance (which already contains an intrinsic-scatter term calibrated in the Pantheon+ pipeline);")
print("  the Wald sigma refers to the deviation of a fixed p from the best-fit p, not to a 'sigma of falsification'.")
out["table"] = tab; out["wald_sigma"] = dict(A=wald_A, B=wald_B)
# (d) proper conditional held-out diagnostic
z = D["z"]; tr = z < 0.4; te = ~tr; C = D["C"]; m = D["m"]
Ctt = C[np.ix_(tr, tr)]; Cee = C[np.ix_(te, te)]; Cet = C[np.ix_(te, tr)]
Ctt_inv = np.linalg.inv(Ctt); K = Cet @ Ctt_inv; Ccond = Cee - K @ Cet.T; Ccond_inv = np.linalg.inv(Ccond); Cee_inv = np.linalg.inv(Cee)
def heldout(fn, bounds=None, fixed=None):
    if fixed is None:
        r = optimize.minimize_scalar(lambda x: chi2_profiled(D, fn(x), tr)[0], bounds=bounds, method="bounded"); x = r.x
    else: x = fixed
    _, Mhat = chi2_profiled(D, fn(x), tr)
    r_tr = m[tr] - fn(x)[tr] - Mhat; r_te = m[te] - fn(x)[te] - Mhat
    r_cond = r_te - K @ r_tr
    return dict(param=float(x), chi2_block=float(r_te @ Cee_inv @ r_te), chi2_conditional=float(r_cond @ Ccond_inv @ r_cond), n_test=int(te.sum()), mean_res=float(r_te.mean()))
ho = {"A DU p=0.5": heldout(lambda x: mu_du_p(D, x), fixed=0.5), "B DU p=1.5": heldout(lambda x: mu_du_p(D, x), fixed=1.5),
      "C DU free p": heldout(lambda x: mu_du_p(D, x), bounds=(-2, 3)), "D flat LCDM": heldout(lambda x: mu_lcdm(D, x), bounds=(0.05, 0.9))}
print(f"\n(d) held-out subset diagnostic (train z<0.4, N={tr.sum()}; test z>=0.4, N={te.sum()}; SAME dataset and covariance):")
print(f"{'model':14s} {'param':>7s} {'chi2 block-only':>16s} {'chi2 conditional':>17s} {'mean res':>9s}")
for k_, v in ho.items(): print(f"{k_:14s} {v['param']:7.3f} {v['chi2_block']:16.2f} {v['chi2_conditional']:17.2f} {v['mean_res']:+9.3f}")
print("  Block-only ignores the train–test cross-covariance; the conditional form accounts for it. This is a same-dataset")
print("  subset diagnostic with one pre-chosen split, not an independent prediction test; systematics are shared.")
out["heldout"] = ho
# (e) bias-correction sensitivity
bias = dat["biasCor_m_b"].values[sel]
print(f"\n(e) BBC bias correction in the selected sample: mean {bias.mean():+.4f}, min {bias.min():+.4f}, max {bias.max():+.4f} mag")
D2 = dict(D); D2["m"] = D["m"] + bias      # remove the applied correction (bounding exercise only)
Om2, c2_l2 = (lambda r: (r.x, r.fun))(optimize.minimize_scalar(lambda x: chi2_profiled(D2, mu_lcdm(D2, x))[0], bounds=(0.05, 0.9), method="bounded"))
p2, c2_p2 = (lambda r: (r.x, r.fun))(optimize.minimize_scalar(lambda x: chi2_profiled(D2, mu_du_p(D2, x))[0], bounds=(-2, 3), method="bounded"))
c2_A2 = chi2_profiled(D2, mu_du_p(D2, 0.5))[0]; c2_B2 = chi2_profiled(D2, mu_du_p(D2, 1.5))[0]
print(f"  without bias correction: Omega_m = {Om2:.3f}; dchi2 A = {c2_A2-c2_l2:+.1f} (was {tab['A DU p=0.5']['dchi2']:+.1f}); dchi2 B = {c2_B2-c2_l2:+.1f}; free p = {p2:.3f}, dchi2 C = {c2_p2-c2_l2:+.1f}")
out["bias_sensitivity"] = dict(bias_mean=float(bias.mean()), bias_min=float(bias.min()), bias_max=float(bias.max()), Om_nobias=Om2, dchi2_A=c2_A2-c2_l2, dchi2_B=c2_B2-c2_l2, p_free=p2, dchi2_C=c2_p2-c2_l2)
# (f) selection sensitivity
for label, zmin, drop_cal in (("zmin=0.023", 0.023, False), ("zmin=0.01, no calibrators", 0.01, True)):
    Dx = load(zmin=zmin)
    if drop_cal:
        cal = dat["IS_CALIBRATOR"].values[dat["zHD"].values > zmin] == 1
        keep = ~cal
        Dx = dict(z=Dx["z"][keep], zhel=Dx["zhel"][keep], m=Dx["m"][keep], C=Dx["C"][np.ix_(keep, keep)], Cinv=np.linalg.inv(Dx["C"][np.ix_(keep, keep)]), N=int(keep.sum()))
    Omx, c2lx = (lambda r: (r.x, r.fun))(optimize.minimize_scalar(lambda x: chi2_profiled(Dx, mu_lcdm(Dx, x))[0], bounds=(0.05, 0.9), method="bounded"))
    px, c2px = (lambda r: (r.x, r.fun))(optimize.minimize_scalar(lambda x: chi2_profiled(Dx, mu_du_p(Dx, x))[0], bounds=(-2, 3), method="bounded"))
    c2Ax = chi2_profiled(Dx, mu_du_p(Dx, 0.5))[0]; c2Bx = chi2_profiled(Dx, mu_du_p(Dx, 1.5))[0]
    print(f"(f) {label}: N={Dx['N']}, Omega_m={Omx:.3f}, dchi2 A={c2Ax-c2lx:+.1f}, B={c2Bx-c2lx:+.1f}, free p={px:.3f} (dchi2 {c2px-c2lx:+.1f})")
    out[f"selection_{label}"] = dict(N=Dx["N"], Om=Omx, dchi2_A=c2Ax-c2lx, dchi2_B=c2Bx-c2lx, p_free=px, dchi2_C=c2px-c2lx)
json.dump(out, open("results/pantheon_robustness.json", "w"), indent=2)
print("written results/pantheon_robustness.json")
