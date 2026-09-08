"""
Verification round (step 4): pulsar test — provenance tiers, theory dependence, and sensitivity of the tiered results.

Provenance tiers of the inputs used (see sources/manifest.csv):
  EXT  = externally supplied by the user 2026-09-08 (verified externally; not fetched here)
  SNIP = confirmed at search-snippet level (abstract text)
  MEM  = from memory of the publication; NOT verified in this run
Original publications could not be fetched (egress blocked) -> no MEM value was upgraded.
"""
import json, math, numpy as np
from binary_decay import f_e, systems
prov = {
 "PSR J1738+0333": dict(e="EXT", Pbdot_int="EXT", Pbdot_GR="EXT", masses="SNIP (Antoniadis+2012 abstract)", Pb="MEM", kinematic_corr="SNIP (abstract: subtracted using proper motion + parallax)",
                        mass_method="WD optical spectroscopy + mass ratio: weakly theory-dependent (no GR PK parameters used)"),
 "PSR B1913+16": dict(e="MEM", Pbdot_int="MEM", Pbdot_GR="SNIP/MEM", masses="SNIP (1.438/1.390)", ratio="SNIP (0.9983±0.0016)", Pb="MEM", kinematic_corr="MEM (Galactic acceleration correction is the dominant systematic; distance-dependent)",
                     mass_method="GR post-Keplerian (omega-dot, gamma): theory-DEPENDENT; the Pbdot test is a GR self-consistency test"),
 "PSR J0737-3039A/B": dict(e="SNIP (0.088)", Pbdot_int="MEM", ratio="MEM (0.999963±0.000063; snippet: 'agreement within 0.013%')", masses="MEM", Pb="MEM",
                           mass_method="GR post-Keplerian + mass ratio R (theory-independent) : partly theory-dependent"),
}
print("Provenance and theory-dependence of inputs:")
for k_, v in prov.items():
    print(f"  {k_}: " + "; ".join(f"{a}={b}" for a, b in v.items()))
# --- J1738 conditional bound, step by step -------------------------------------------------------------
J = systems["PSR J1738+0333"]; B = systems["PSR B1913+16"]
print("\nJ1738 conditional bound, stepwise:")
print("  S1 (EXT statement): eccentricity factor F(e) of Eq. 32 satisfies F(0) = 0.                        -> guarantees only lim_{e->0} Pbdot_32 = 0")
print("  S2 (assumption A-ANALYTIC): F analytic at e=0 -> F(e) = a_n e^n + O(e^{n+1}), n>=1.               -> needed to convert the limit into a RATE of vanishing")
print("  S3 (assumption A-CALIB, favourable to DU): Eq. 32 alone reproduces B1913+16's full decay -> fixes a_n via |Pbdot_32(B1913)| = 2.398e-12 s/s")
print("  S4 (unknown X): non-eccentricity prefactor ratio J1738/B1913 = X.                                 -> bound |Pbdot_32(J1738)| <= 2.398e-12 (e_J/e_B)^n X")
rows = []
for n_ in (0.5, 1, 2):
    for e_J in (3.4e-7, 4.5e-7):
        base = abs(B["obs_int"])*(e_J/B["e"])**n_
        Xc = J["obs_err"]/base
        rows.append(dict(n=n_, e_J=e_J, bound_X1=base, X_needed_for_1sigma=Xc))
        print(f"    n={n_:<3} e_J={e_J:.1e}: bound at X=1 -> {base:.2e} s/s ; X needed to reach 1-sigma error (3.2e-15): {Xc:.3g}")
print("  S5 (reference for X): a prefactor with GR-like scaling (Pb^-5/3 m_p m_c M^-1/3) gives X = 0.136; no DU value of X is available.")
print("  RESULT: exact prediction UNRESOLVED (Eq. 32 unavailable). Conditional upper bound under S1–S4: for n>=1 the bound is")
print("          below the measurement error unless X >= ~1800 (n=1) or ~3e9 (n=2). For a NON-analytic n=1/2 factor the bound")
print("          would need only X >= ~1.8 and is NOT robust. Illustrative null prediction Pbdot=0 vs observed: 8.1 sigma")
print("          is the significance of the OBSERVED decay against ZERO, i.e. of hypothesis H_32 := 'Pbdot(J1738)=0 within error'.")
out = dict(provenance=prov, bound_rows=rows, GR_like_X=0.136,
           tested_hypothesis="H_32: Pbdot_int(J1738) = 0 within 3.2e-15 s/s (consequence of DU-32-ONLY under S1-S4)",
           significance_of_observed_vs_zero=abs(J["obs_int"])/J["obs_err"])
# --- DU-PLUS-QUADRUPOLE sensitivity ----------------------------------------------------------------------
Dp = systems["PSR J0737-3039A/B"]
data_all = [("J1738", J["e"], J["obs_int"]/J["pub_GR"], J["obs_err"]/abs(J["pub_GR"]), "EXT"),
            ("B1913", B["e"], B["ratio_pub"][0], B["ratio_pub"][1], "SNIP"),
            ("J0737", Dp["e"], Dp["ratio_pub"][0], Dp["ratio_pub"][1], "MEM")]
def fit(data, n_):
    A = np.array([[1.0, e**n_/f_e(e)] for _, e, _, _, _ in data]); y = np.array([r for *_, r, _, _ in data]); w = np.array([1/s for *_, s, _ in data])
    Aw = A*w[:, None]; coef, *_ = np.linalg.lstsq(Aw, y*w, rcond=None); cov = np.linalg.inv(Aw.T @ Aw)
    kappa, beta = coef; sk, sb = np.sqrt(np.diag(cov)); corr = cov[0, 1]/(sk*sb)
    fracB = beta*B["e"]**n_/f_e(B["e"]); fracB_err = sb*B["e"]**n_/f_e(B["e"])
    return dict(kappa=kappa, kappa_err=sk, beta=beta, beta_err=sb, corr_kappa_beta=corr, fracB=fracB, fracB_2sig_upper=fracB + 2*fracB_err, dof=len(data) - 2)
print("\nDU-PLUS-QUADRUPOLE two-component fit: sensitivity to which systems (and provenance tiers) are included")
sens = {}
for label, data in (("all three (EXT+SNIP+MEM)", data_all), ("without J0737 (drop MEM ratio)", data_all[:2]), ("J1738 + J0737 (drop B1913)", [data_all[0], data_all[2]])):
    for n_ in (1, 2):
        r = fit(data, n_); sens[f"{label} n={n_}"] = r
        print(f"  {label:32s} n={n_}: kappa = {r['kappa']:.5f} ± {r['kappa_err']:.5f}, beta = {r['beta']:+.3f} ± {r['beta_err']:.3f}, corr(kappa,beta) = {r['corr_kappa_beta']:+.2f}, ecc share of B1913 <= {r['fracB_2sig_upper']*100:.1f} % (2σ), dof={r['dof']}")
print("  READING: kappa is pinned by whichever high-precision system is included (J0737 MEM, or B1913 SNIP); J1738 (EXT) alone")
print("  gives kappa = 0.94 ± 0.12 and no information on beta. The '<= 0.8 %' bound rests on the B1913 ratio (snippet) and the")
print("  J0737 ratio (memory). Without J0737 the bound weakens to the value shown above. kappa's 0.05 % precision is an EMPIRICAL")
print("  constraint on the amplitude of any added GR-like term; it is not by itself a statement about theoretical fine-tuning.")
print("  What the data say about the ORIGINAL DU mechanism: wherever precise decay data exist (e = 3e-7, 0.088, 0.617), the")
print("  eccentricity-driven term contributes at most a few per mille of the observed decay if a GR-like term is present.")
out["two_component_sensitivity"] = sens
json.dump(out, open("results/binary_decay_sensitivity.json", "w"), indent=2)
print("written results/binary_decay_sensitivity.json")
