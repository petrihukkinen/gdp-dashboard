"""
Near-circular orbital decay test (Phase A3).

GR reference: Peters & Mathews (1963) / Peters (1964) quadrupole formula
  dPb/dt = -(192 pi/5) (2 pi G / Pb)^{5/3} m_p m_c (m_p+m_c)^{-1/3} c^{-5} f(e),
  f(e) = (1 + 73/24 e^2 + 37/96 e^4) / (1-e^2)^{7/2}.
Independent second implementation: energy-loss route  dE/dt = -(32/5) G^4 mu^2 M^3 /(c^5 a^5) f(e),
  with E = -G m_p m_c/(2a) and Kepler's law -> dPb/dt, checked to agree with the first.

The article's equation 32 could NOT be read in this run (source egress-blocked). The test is therefore
formulated as a constraint on ANY formula whose e->0 limit vanishes: PSR J1738+0333 (e ~ 3e-7) has a
measured intrinsic decay -25.9 +/- 3.2 fs/s, i.e. a nonzero decay at 8.1 sigma.
"""
import json, math
import numpy as np
from scipy import constants as k
G, c, Msun = k.G, k.c, 1.98847e30
DAY = 86400.0

def f_e(e):
    return (1 + 73/24*e**2 + 37/96*e**4)/(1-e**2)**3.5

def pbdot_PM(Pb_s, mp, mc, e):
    M = mp+mc
    return -(192*math.pi/5)*(2*math.pi*G/Pb_s)**(5/3)*mp*mc*M**(-1/3)*c**-5*f_e(e)

def pbdot_energy_route(Pb_s, mp, mc, e):
    """Independent implementation via dE/dt and Kepler's third law."""
    M = mp+mc; mu = mp*mc/M
    a = (G*M*Pb_s**2/(4*math.pi**2))**(1/3)
    dEdt = -(32/5)*G**4*mu**2*M**3/(c**5*a**5)*f_e(e)
    E = -G*mp*mc/(2*a)
    # E ∝ -a^{-1}, Pb ∝ a^{3/2}  ->  dPb/Pb = (3/2) da/a = -(3/2) dE/E  (dE/E >0 when |E| grows)
    return Pb_s*(-1.5)*dEdt/E

systems = {
 "PSR J1738+0333": dict(Pb_d=0.3547907398724, e=3.4e-7, mp=1.46, mc=0.181,
      mp_err=(0.05,0.06), mc_err=(0.005,0.007),
      obs_int=-25.9e-15, obs_err=3.2e-15, pub_GR=-27.7e-15, pub_GR_err=(1.9e-15,1.5e-15),
      src="Freire et al. 2012 MNRAS 423,3328 (arXiv:1205.1450) abstract; masses Antoniadis et al. 2012 (arXiv:1204.3948) abstract. "
          "Pb value from memory of the paper's Table 1 (8.5 h confirmed by abstract) -> flagged in OPEN_LOOPS."),
 "PSR B1913+16": dict(Pb_d=0.322997448918, e=0.6171340, mp=1.438, mc=1.390,
      mp_err=(0.001,0.001), mc_err=(0.001,0.001),
      obs_int=-2.398e-12, obs_err=0.004e-12, pub_GR=-2.40263e-12, pub_GR_err=(0.00005e-12,0.00005e-12),
      ratio_pub=(0.9983,0.0016),
      src="Weisberg & Huang 2016 ApJ 829,55: masses and ratio 0.9983+/-0.0016 confirmed via search snippet; "
          "Pb, e, and the GR value -2.4025e-12 from snippet/memory -> flagged."),
 "PSR J0737-3039A/B": dict(Pb_d=0.10225156248, e=0.0877775, mp=1.338185, mc=1.248868,
      mp_err=(1e-5,1e-5), mc_err=(1e-5,1e-5),
      obs_int=-1.247920e-12, obs_err=0.000078e-12, pub_GR=None, pub_GR_err=None,
      ratio_pub=(0.999963,0.000063),
      src="Kramer et al. 2021 PRX 11,041050; e=0.088 and 'agreement within 0.013%' confirmed via snippet; "
          "other numbers from memory of the paper -> flagged."),
}
out = {}
print(f"{'system':20s} {'e':>10s} {'f(e)':>8s} {'Pbdot_GR(PM)':>14s} {'Pbdot_GR(E)':>14s} {'published GR':>14s} {'observed':>14s} {'obs/GR':>8s}")
for name, s in systems.items():
    Pb = s["Pb_d"]*DAY; mp = s["mp"]*Msun; mc = s["mc"]*Msun
    pm = pbdot_PM(Pb, mp, mc, s["e"]); er = pbdot_energy_route(Pb, mp, mc, s["e"])
    assert abs(pm/er-1) < 1e-12, "two implementations disagree"
    # mass-uncertainty propagation (asymmetric, simple corner evaluation)
    lo = pbdot_PM(Pb, (s["mp"]-s["mp_err"][0])*Msun, (s["mc"]-s["mc_err"][0])*Msun, s["e"])
    hi = pbdot_PM(Pb, (s["mp"]+s["mp_err"][1])*Msun, (s["mc"]+s["mc_err"][1])*Msun, s["e"])
    ratio = s["obs_int"]/pm; ratio_err = s["obs_err"]/abs(pm)
    pub = s["pub_GR"]
    print(f"{name:20s} {s['e']:10.3e} {f_e(s['e']):8.4f} {pm:14.4e} {er:14.4e} {str(pub):>14s} {s['obs_int']:14.4e} {ratio:6.3f}±{ratio_err:.3f}")
    out[name] = dict(e=s["e"], f_e=f_e(s["e"]), Pbdot_GR_here=pm, Pbdot_GR_here_mass_range=[hi, lo],
                     Pbdot_GR_published=pub, Pbdot_obs_intrinsic=s["obs_int"], obs_err=s["obs_err"],
                     ratio_obs_over_GR_here=ratio, ratio_err=ratio_err, ratio_published=s.get("ratio_pub"),
                     source=s["src"])
    if pub:
        print(f"    reproduction of published GR value: here/published = {pm/pub:.4f} (mass-range {hi/pub:.4f}..{lo/pub:.4f})")

# e -> 0 limit and the constraint on any formula vanishing at e=0
j = systems["PSR J1738+0333"]
sig_nonzero = abs(j["obs_int"])/j["obs_err"]
print(f"\nPSR J1738+0333: intrinsic decay is nonzero at {sig_nonzero:.1f} sigma. f(e)-1 = {f_e(j['e'])-1:.2e} -> GR decay is e-independent here.")
print("Any decay law with dPb/dt -> 0 as e -> 0 (e.g. ∝ e^n, n>0) predicts |dPb/dt| < 1e-20 s/s for e=3.4e-7 and is excluded")
print(f"at {sig_nonzero:.1f} sigma by this system alone; the double pulsar (e=0.088) adds an independent constraint.")
# eccentricity dependence check at e=0.616 (B1913+16): ratio of f(e) to circular
print(f"f(0.6171) = {f_e(0.6171):.4f}: GR decay for B1913+16 is 11.86x the circular-orbit value with the same Pb and masses.")
# What e-scaling would be needed for a purely e-driven law to hit both B1913 and J1738?
# If law = A e^n: B1913 fixes A e^n = 2.40e-12 ; J1738 needs 2.6e-14 -> e^n ratio = 0.0108 with e ratio 5.5e-7
n_needed = math.log(2.59e-14/2.40e-12)/math.log(3.4e-7/0.6171)   # ignores mass/Pb differences: illustrative only
print(f"Illustrative: a pure power law in e reproducing both would need n = {n_needed:.3f} (i.e. essentially e-independent).")
out["constraint"] = dict(J1738_sigma_nonzero=sig_nonzero, statement="Any dPb/dt law vanishing as e->0 is excluded at >8 sigma by PSR J1738+0333.",
                         status_eq32="EI TESTATTU sellaisenaan: artikkelin yhtälöä 32 ei voitu lukea (lähde estetty). Testi on ehdollinen: JOS yhtälö 32 -> 0 kun e -> 0, NIIN se on ristiriidassa J1738+0333:n kanssa.")
json.dump(out, open("results/binary_decay.json","w"), indent=2)
print("written results/binary_decay.json")
