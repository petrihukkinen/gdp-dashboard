"""
Phase A3 (local expansion, black holes): numbers derived from stated DU scalings + GR reference values.

Part 1 — 'H0 x distance' at Moon and Earth–Sun scales, then the actual observables under the DU scalings
  (as ADDITIONAL assumptions, not derivable from the two postulates): bound-system size r ∝ R4 ∝ T^{2/3},
  c0 ∝ T^{-1/3}, atomic clock rate f ∝ c0.  Observables: light round-trip time in atomic seconds, orbital
  period in atomic seconds, radial velocity via Doppler (dimensionless ratio of frequencies).
Part 2 — Injection–recovery toy: can a secular H0*r range drift be separated from tidal recession in a
  30-yr LLR-like range series with an ephemeris-style fit? Identifiability via the angular-momentum link
  between tidal recession and Earth spin-down (which an expansion-driven drift does not produce).
Part 3 — GR black-hole reference: photon sphere, ISCO from d2V_eff/dr2 = 0 (Schwarzschild, symbolic) and
  Kerr ISCO (Bardeen-Press-Teukolsky), Sgr A* periods. DU side: EI TESTATTU (article inaccessible).
"""
import json, math
import numpy as np, sympy as sp
from scipy import constants as k, optimize
G, c, Msun = k.G, k.c, 1.98847e30
yr = 365.25*86400; Mpc = 1e6*k.parsec
out = {}

# ---------------- Part 1 -----------------
H0 = 70.0*1e3/Mpc          # s^-1
r_moon = 384_400e3; r_au = k.au
print("=== Part 1: H0 x r and the DU-scaled observables (H0 = 70 km/s/Mpc) ===")
for name, r in (("Moon", r_moon), ("Earth-Sun", r_au)):
    v = H0*r
    print(f"  {name:10s}: H0*r = {v:.3e} m/s = {v*yr*100:.3f} cm/yr")
    out[f"H0r_{name}"] = dict(m_per_s=v, cm_per_yr=v*yr*100)
print("  Observed LLR lunar recession (Williams & Boggs 2016, tidal): 3.83 cm/yr [from memory of paper; flagged].")
# DU scalings: r ∝ T^{2/3}, c0 ∝ T^{-1/3}, f_clock ∝ T^{-1/3}.  d ln(.)/dT in units of H (= 2/(3T)):
T = sp.symbols("T", positive=True)
r_ = T**sp.Rational(2,3); c_ = T**sp.Rational(-1,3); f_ = T**sp.Rational(-1,3)
H_ = sp.Rational(2,3)/T
def rate_in_H(expr):  # d ln expr/dT divided by H
    return sp.simplify(sp.diff(sp.log(expr), T)/H_)
tau_rt = 2*r_/c_                 # round-trip coordinate time
ticks_rt = tau_rt*f_             # round trip measured in atomic ticks
P_orb = r_**sp.Rational(3,2)     # Kepler with G M const: P ∝ r^{3/2}
ticks_orb = P_orb*f_
ratio_orb_rt = ticks_orb/ticks_rt   # dimensionless ratio orbital period / light round-trip
print("  DU-scaled observables (rates in units of H0):")
print(f"    coordinate round-trip time 2r/c0 : {rate_in_H(tau_rt)} H")
print(f"    round-trip in atomic ticks       : {rate_in_H(ticks_rt)} H   <- LLR range in light-seconds drifts at +H0*r")
print(f"    orbital period in atomic ticks   : {rate_in_H(ticks_orb)} H")
print(f"    ratio P_orb/(round-trip)         : {rate_in_H(ratio_orb_rt)} H  <- pure dimensionless ratio: no signal")
print(f"    Doppler: d ln r/dT / c0 -> v_r = H0*r in frequency ratio terms: present, {H0*r_moon*yr*100:.2f} cm/yr for the Moon")
out["DU_scalings"] = dict(round_trip_ticks_rate="1 H (drift +H0 r)", orbital_period_ticks_rate="1 H",
                          ratio_Porb_over_roundtrip="0 (no signal)", doppler="H0 r present")
print("  => Under these scalings a DU expansion of the Moon's orbit IS observable in LLR range (light-seconds) and in")
print("     the orbital period measured in atomic seconds; it is invisible only in the ratio of the two. The claim that")
print("     'expansion is unobservable locally' therefore depends on which observable is used; LLR is not one of them.")
# Kepler-consistency of tidal vs expansion recession: tidal recession changes P_orb via Kepler (P ∝ a^{3/2}) with G M fixed;
# DU expansion changes a AND (under the scalings) the clock, giving the same 1 H rate for both a and P in ticks:
print("  Kepler check: tidal da/a -> dP/P = 1.5 da/a ; DU expansion da/a = H, dP/P(ticks) = H  (not 1.5 H) ->")
print("     the ratio dP/P : da/a is 1.5 for tides but 1.0 for DU expansion: a second discriminating observable.")
out["kepler_discriminator"] = "tidal: dlnP = 1.5 dln a ; DU: dlnP = 1.0 dln a (ticks)"

# ---------------- Part 2: injection-recovery toy -----------------
print("\n=== Part 2: injection–recovery toy (synthetic, 30 yr, monthly normal points) ===")
rng = np.random.default_rng(20260908)
t = np.arange(0, 30*12)/12.0                       # years
a0 = r_moon
tidal_rate = 3.83e-2                               # m/yr  (total observed secular rate, nominal)
du_rate = H0*r_moon*yr                             # m/yr  (2.75 cm/yr)
sigma_range = 0.002                                # 2 mm normal-point precision (modern LLR)
# Model: range(t) = a0 + (k_tidal + k_du) t + seasonal/periodic terms ; only the SUM of linear rates is identifiable
X = np.column_stack([np.ones_like(t), t, np.sin(2*np.pi*t), np.cos(2*np.pi*t)])
truth_tidal = tidal_rate - du_rate  # if DU is right, tidal part is the remainder
y = a0 + (truth_tidal + du_rate)*t + 0.01*np.sin(2*np.pi*t) + rng.normal(0, sigma_range, t.size)
beta, *_ = np.linalg.lstsq(X, y, rcond=None)
cov = sigma_range**2*np.linalg.inv(X.T@X)
print(f"  recovered total secular rate = {beta[1]*100:.4f} ± {math.sqrt(cov[1,1])*100:.4f} cm/yr (injected {tidal_rate*100:.2f})")
print("  A range-only fit recovers the SUM; a separate DU term is a column identical to t -> design matrix singular:")
Xs = np.column_stack([X, t]); print(f"  rank of [1, t, sin, cos, t_DU] = {np.linalg.matrix_rank(Xs)} of 5 columns -> NOT identifiable from range alone.")
# Identifiability restored by the angular momentum budget: tidal recession <-> Earth spin-down (LOD).
# L_orb = mu sqrt(G M a); dL_orb/dt = (mu/2) sqrt(GM/a) da/dt = -dL_earth/dt = -C_earth dOmega/dt.
M_e, M_m = 5.9722e24, 7.3458e22; mu = M_e*M_m/(M_e+M_m); Mtot = M_e+M_m
C_earth = 8.034e37     # kg m^2 (polar moment of inertia)
Omega = 7.292115e-5
def lod_rate_ms_per_century(da_dt_m_per_yr):
    dLdt = 0.5*mu*math.sqrt(G*Mtot/a0)*da_dt_m_per_yr/yr           # kg m^2 s^-2
    dOmega_dt = -dLdt/C_earth
    dLOD_dt = -2*math.pi/Omega**2*dOmega_dt                          # s per s
    return dLOD_dt*1e3*100*yr
lod_full = lod_rate_ms_per_century(tidal_rate); lod_du = lod_rate_ms_per_century(truth_tidal)
print(f"  If ALL 3.83 cm/yr is tidal: tidal LOD increase = {lod_full:.2f} ms/century (literature tidal value ≈ 2.3–2.4 ms/cy [flagged, from memory]).")
print(f"  If only {truth_tidal*100:.2f} cm/yr is tidal (DU takes 2.75): tidal LOD increase = {lod_du:.2f} ms/century.")
print("  The eclipse-record LOD trend (+1.7–1.8 ms/cy total, from memory; flagged) is explained by tidal 2.3–2.4 minus a")
print("  non-tidal (GIA/core) −0.5–0.6 ms/cy. Under the DU split the non-tidal term would have to be ≈ +1.1 ms/cy of the")
print("  opposite sign. This is the discriminating observable; the caveat is the poorly known non-tidal budget and")
print("  variability of tidal dissipation over ~10^8 yr (not needed here: the LOD comparison is over 2700 yr).")
out["injection_recovery"] = dict(recovered_rate_cm_yr=beta[1]*100, err=math.sqrt(cov[1,1])*100, identifiable_from_range_alone=False,
                                 lod_ms_cy_if_all_tidal=lod_full, lod_ms_cy_if_DU_split=lod_du,
                                 status="EHDOLLINEN: numbers for literature LOD/tidal values from memory; verify before use.")

# ---------------- Part 3: GR black hole reference -----------------
print("\n=== Part 3: GR reference for compact-object orbits ===")
r, M_, L_ = sp.symbols("r M L", positive=True)
# Schwarzschild effective potential (G=c=1) for massive particle: V = (1-2M/r)(1+L^2/r^2)
V = (1-2*M_/r)*(1+L_**2/r**2)
dV = sp.diff(V, r); d2V = sp.diff(V, r, 2)
# circular orbits: dV=0 -> L^2 = M r^2/(r-3M); stability: d2V>0 ; marginal at ISCO
L2circ = sp.solve(sp.Eq(dV, 0), L_**2)[0]
d2V_circ = sp.simplify(d2V.subs(L_**2, L2circ))
isco = sp.solve(sp.Eq(sp.numer(sp.together(d2V_circ)), 0), r)
print(f"  Schwarzschild: L^2(circ) = {L2circ};  d2V/dr2 on circular orbits = {d2V_circ}")
print(f"  ISCO from d2V/dr2 = 0: r = {isco} (in GM/c^2) ; photon sphere r = 3 GM/c^2 ; horizon r = 2 GM/c^2")
def kerr_isco(a, prograde=True):
    Z1 = 1 + (1-a**2)**(1/3)*((1+a)**(1/3) + (1-a)**(1/3)); Z2 = math.sqrt(3*a**2 + Z1**2)
    return 3 + Z2 - (1 if prograde else -1)*math.sqrt((3-Z1)*(3+Z1+2*Z2))
kerr = {a: (kerr_isco(a, True), kerr_isco(a, False)) for a in (0.0, 0.5, 0.9, 0.98)}
for a, (p, rr) in kerr.items(): print(f"  Kerr a*={a}: ISCO prograde {p:.3f}, retrograde {rr:.3f} GM/c^2")
M_sgr = 4.297e6*Msun    # GRAVITY collaboration 2022 (from memory; flagged)
rg = G*M_sgr/c**2
def period_min(r_over_rg, a=0.0):  # Kerr equatorial prograde orbital period as seen at infinity
    r_ = r_over_rg
    Om = 1/(r_**1.5 + a)               # in units c^3/(GM)
    return 2*math.pi/Om*rg/c/60
print(f"  Sgr A* (M=4.297e6 Msun): ISCO period Schwarzschild = {period_min(6):.1f} min ; a*=0.9 prograde ISCO ({kerr[0.9][0]:.2f} rg) = {period_min(kerr[0.9][0],0.9):.1f} min")
print("  GRAVITY flare periods ~30–45 min (from memory; flagged) sit near the Schwarzschild ISCO period — the observed")
print("  period is a Kerr-ISCO-type diagnostic only with spin and inclination modelled; horizon, photon sphere, ISCO are")
print("  distinct radii and must not be conflated. DU side (local c -> 0, 'no horizon'): EI TESTATTU in this run.")
out["GR_reference"] = dict(schwarzschild_isco=str(isco), kerr_isco=kerr, sgrA_isco_period_min=period_min(6))
json.dump(out, open("results/local_expansion_and_bh.json", "w"), indent=2, default=str)
print("written results/local_expansion_and_bh.json")
