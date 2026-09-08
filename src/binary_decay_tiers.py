"""
TASK B — near-circular binary falsification test, tiered.

Externally supplied statements (provenance: user-supplied 2026-09-08, verified externally; not fetched here):
  * Article: DU Eq. 32 predicts orbital decay only for eccentric orbits; its eccentricity factor gives zero decay
    for circular orbits; DU does not exclude a possible quadrupole-moment effect (not quantitatively specified).
  * PSR J1738+0333 (Freire et al. 2012, MNRAS 423, 3328): e = (3.4 ± 1.1)e-7; Pbdot_int = (-25.9 ± 3.2)e-15 s/s;
    GR prediction ≈ -27.7e-15 s/s.

DU-32-ONLY: exact Eq. 32 is NOT available -> numerical prediction UNRESOLVED. What can be stated rigorously:
  (i)  the published statement fixes F(0) = 0 for the eccentricity factor F(e);
  (ii) if F is analytic at e=0 (any closed-form factor built from e, sqrt(1-e^2), periastron-advance terms is),
       then F(e) = a_n e^n + O(e^{n+1}) with n >= 1;
  (iii) the mechanism is stated to be the eccentricity / periastron-rotation one; periastron is undefined for e=0,
        consistent with (i).
  Bound: |Pbdot_32(J1738)| <= |Pbdot_32(ref)| * (e_J/e_ref)^n * X, where X is the ratio of the non-eccentricity
  prefactor (masses, period) between the systems. X is unknown without Eq. 32; we tabulate the bound for
  X in {1, 1e2, 1e4, 1e6} and n in {1, 2}, calibrating |Pbdot_32(ref)| to the FULL observed decay of B1913+16
  (the most favourable choice for DU-32-ONLY: it assumes Eq. 32 alone explains B1913+16).

DU-PLUS-QUADRUPOLE: two-component phenomenology  Pbdot = kappa * Pbdot_GR(e) + beta * Pbdot_GR,circ-prefactor * e^n
  fitted to the three systems' observed/GR ratios. This quantifies how much room an eccentricity-driven term has
  once a GR-like quadrupole term is admitted. (Numbers for B1913+16 and J0737-3039 partly from memory -> flagged.)
"""
import json, math, numpy as np
from binary_decay import f_e, pbdot_PM, systems, Msun, DAY
out = {}
J = systems["PSR J1738+0333"]; B = systems["PSR B1913+16"]; Dp = systems["PSR J0737-3039A/B"]
sig_J = abs(J["obs_int"])/J["obs_err"]
print("=== DU-32-ONLY: limiting statement (numerical prediction UNRESOLVED without Eq. 32) ===")
print(f"J1738+0333: observed intrinsic decay {J['obs_int']:.3e} ± {J['obs_err']:.1e} s/s -> nonzero at {sig_J:.1f} sigma")
e_ref, pb_ref = B["e"], abs(B["obs_int"])
rows = []
for n_ in (1, 2):
    for X in (1, 1e2, 1e4, 1e6):
        bound = pb_ref*(J["e"]/e_ref)**n_*X
        rows.append(dict(n=n_, X=X, bound_s_per_s=bound, bound_over_obs_err=bound/J["obs_err"]))
        print(f"  n={n_}, prefactor ratio X={X:8.0e}: |Pbdot_32(J1738)| <= {bound:.2e} s/s  = {bound/J['obs_err']:.1e} x measurement error")
# e uncertainty: use e + 1 sigma = 4.5e-7 for the most conservative bound
e_hi = 3.4e-7 + 1.1e-7
worst = pb_ref*(e_hi/e_ref)*1e6
X_crit = J["obs_err"]/(pb_ref*(e_hi/e_ref))
print(f"  with e+1sigma={e_hi:.1e} and n=1 the bound reaches the measurement error only for X >= {X_crit:.0f}.")
print("  => For any analytic F with F(0)=0, DU-32-ONLY predicts Pbdot(J1738) = 0 within measurement error unless the")
print(f"     non-eccentricity prefactor is > ~{X_crit:.0f} times LARGER for J1738 than for B1913+16. Any prefactor with GR-like")
print("     mass/period scaling goes the other way (J1738's is SMALLER, see next line), so the bound is robust.")
pref_ratio_GR = pbdot_PM(J["Pb_d"]*DAY, J["mp"]*Msun, J["mc"]*Msun, 0)/pbdot_PM(B["Pb_d"]*DAY, B["mp"]*Msun, B["mc"]*Msun, 0)
print(f"     (GR circular-orbit prefactor ratio J1738/B1913 = {pref_ratio_GR:.3e})")
out["DU_32_ONLY"] = dict(X_critical_for_detectability=float(X_crit), status="UNRESOLVED numerically (Eq. 32 not available); limiting statement rigorous under F(0)=0 + analyticity",
                         J1738_sigma_nonzero=sig_J, bounds=rows, GR_prefactor_ratio_J1738_over_B1913=pref_ratio_GR,
                         verdict="Prediction 0 (within error) vs observation -25.9±3.2e-15: excluded at 8.1 sigma. Tier-1 discriminating observation.")

print("\n=== DU-PLUS-QUADRUPOLE: two-component fit  ratio_i = kappa + beta * e_i^n / f(e_i) ===")
# observed/GR ratios with errors (J1738 from this run; B1913 and J0737 published ratios, partly memory -> flagged)
data = [("J1738+0333", J["e"], J["obs_int"]/J["pub_GR"], J["obs_err"]/abs(J["pub_GR"])),
        ("B1913+16", B["e"], B["ratio_pub"][0], B["ratio_pub"][1]),
        ("J0737-3039", Dp["e"], Dp["ratio_pub"][0], Dp["ratio_pub"][1])]
fits = {}
for n_ in (1, 2):
    A = np.array([[1.0, e**n_/f_e(e)] for _, e, _, _ in data]); y = np.array([r for *_, r, _ in data]); w = np.array([1/s for *_, s in data])
    Aw = A*w[:, None]; yw = y*w
    coef, *_ = np.linalg.lstsq(Aw, yw, rcond=None); cov = np.linalg.inv(Aw.T @ Aw)
    kappa, beta = coef; sk, sb = np.sqrt(np.diag(cov))
    resid = (A @ coef - y)*w; chi2 = float(resid @ resid)
    # fraction of B1913+16's decay attributable to the eccentricity term
    frac_B = beta*B["e"]**n_/f_e(B["e"])
    fits[f"n={n_}"] = dict(kappa=kappa, kappa_err=sk, beta=beta, beta_err=sb, chi2=chi2, dof=1, frac_B1913_from_ecc_term=frac_B, frac_B1913_2sigma_upper=frac_B + 2*sb*B["e"]**n_/f_e(B["e"]))
    print(f"  n={n_}: kappa = {kappa:.5f} ± {sk:.5f}; beta = {beta:+.4f} ± {sb:.4f}; chi2 = {chi2:.2f} (1 dof)")
    print(f"        eccentricity-term share of B1913+16 decay = {frac_B:+.4f} (2-sigma upper {fits[f'n={n_}']['frac_B1913_2sigma_upper']:.4f})")
print("  => Admitting a GR-like quadrupole term forces kappa = 1 to 0.4-0.05 % and confines any eccentricity-driven term to")
print("     <= 0.8 % (n=1) or <= 0.2 % (n=2) of B1913+16's decay at 2 sigma. The 'rescue' costs Eq. 32 its empirical content.")
out["DU_PLUS_QUADRUPOLE"] = dict(fits=fits, missing_theory=[
    "A DU field equation for time-dependent sources (radiative sector): what propagates, at which speed (c0 or local c), with what polarisation content.",
    "An energy-loss functional dE/dt[source] in the zero-energy bookkeeping: does radiated energy reduce orbital energy, and with what coefficient relative to G^4 mu^2 M^3/(c^5 a^5)?",
    "The eccentricity enhancement g(e) of that term; empirically it must reproduce Peters–Mathews f(e) to 0.16 % at e=0.617 and to 0.006 % at e=0.088.",
    "A no-double-counting rule between Eq. 32 and the quadrupole term (their sum, not either alone, is constrained).",
    "Post-Keplerian parameter mapping (gamma, r, s, omega-dot) so that the masses used in the prediction are DU-consistent, not GR-derived."])
json.dump(out, open("results/binary_decay_tiers.json", "w"), indent=2)
print("written results/binary_decay_tiers.json")
