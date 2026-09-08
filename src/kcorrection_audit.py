"""
K-correction audit (Phase A3).  Question: does the K-correction (Hogg et al. 2002, astro-ph/0210394) 'remove two
factors of (1+z)' (photon-energy and arrival-rate dilution) from catalog magnitudes, so that a theory's bolometric
distance modulus must be increased by 5 log10(1+z) before comparison with Pantheon+?

Method: build everything from the definitions (no cosmology-specific input beyond 'wavelengths stretch by 1+z').
  observed spectral flux density  f_nu^obs(nu_o) = (1+z) * L_nu(nu_o (1+z)) / (4 pi D_X^2)
    - the explicit (1+z) is the bandwidth-compression factor (dnu_e = (1+z) dnu_o), present in ANY theory where
      wavelengths stretch by (1+z);
    - D_X^2 collects the theory's total bolometric dilution:  F_bol = L_bol/(4 pi D_X^2)  (this DEFINES D_X = D_L).
  apparent AB magnitude in filter R:  m_R = -2.5 log10[ ∫ f_nu^obs R dnu/nu / ∫ g_nu R dnu/nu ]
  absolute AB magnitude in rest filter Q at 10 pc: M_Q = -2.5 log10[ ∫ L_nu Q dnu/nu / (4 pi (10pc)^2 ∫ g_nu Q dnu/nu) ]
  K_QR := m_R - M_Q - 5 log10(D_X / 10 pc)                                        (Hogg eq. 1)
Result: K_QR depends only on the SED shape, filters and z; it is independent of D_X, hence of the cosmological
dilution model. A theory's catalog-frame prediction is therefore m_R = M_Q + 5 log10(D_X/10pc) + K_QR with the
SAME K: nothing further is to be added. The (1+z)^2 of standard cosmology lives inside D_L = (1+z) D_M, not in K.
"""
import json, math
import numpy as np
from scipy import integrate, constants as k
h, c, kB, pc = k.h, k.c, k.k, k.parsec

def planck_L_nu(nu, T=10000.0, R=1e12):       # blackbody photosphere luminosity density (W/Hz), arbitrary scale
    x = h*nu/(kB*T)
    return 4*math.pi**2*R**2*(2*h*nu**3/c**2)/np.expm1(np.clip(x, 1e-9, 700))
def tophat(nu, lam_c_nm, width_nm):
    lam = c/nu*1e9
    return ((lam > lam_c_nm-width_nm/2) & (lam < lam_c_nm+width_nm/2)).astype(float)
g_AB = lambda nu: 3631e-26*np.ones_like(nu)   # AB reference: 3631 Jy flat in f_nu

nu_grid = np.logspace(math.log10(c/3000e-9), math.log10(c/100e-9), 200000)
def band_int(fnu, filt):
    y = fnu*filt/nu_grid
    return np.trapezoid(y, nu_grid)

def M_Q(Lnu_fn, Q):
    Lq = band_int(Lnu_fn(nu_grid), Q)/(4*math.pi*(10*pc)**2)
    return -2.5*math.log10(Lq/band_int(g_AB(nu_grid), Q))

def m_R(Lnu_fn, R, z, D_X):
    fobs = (1+z)*Lnu_fn(nu_grid*(1+z))/(4*math.pi*D_X**2)
    return -2.5*math.log10(band_int(fobs, R)/band_int(g_AB(nu_grid), R))

def K_QR(Lnu_fn, Q, R, z, D_X):
    return m_R(Lnu_fn, R, z, D_X) - M_Q(Lnu_fn, Q) - 5*math.log10(D_X/(10*pc))

Bband = tophat(nu_grid, 440, 90)      # rest-frame 'B'-like top-hat
out = {"cases": []}
print("K_QR for a T=10000 K blackbody, rest filter Q=B-like tophat(440±45 nm).")
print("Case 1: observer filter R = Q redshifted exactly (R(λ)=Q(λ/(1+z))): K should be pure bandwidth term -2.5log10(1+z).")
for z in (0.1, 0.5, 1.0, 2.0):
    Rz = tophat(nu_grid, 440*(1+z), 90*(1+z))
    Ks = [K_QR(planck_L_nu, Bband, Rz, z, D) for D in (1e24, 1e25, 3e26)]   # three different 'D_X'
    print(f"  z={z:4.1f}: K = {Ks[0]:+.5f} {Ks[1]:+.5f} {Ks[2]:+.5f} (three D_X values)   -2.5log10(1+z) = {-2.5*math.log10(1+z):+.5f}")
    out["cases"].append(dict(case="R=Q shifted", z=z, K=Ks, expected=-2.5*math.log10(1+z)))
    assert np.ptp(Ks) < 1e-9, "K depends on D_X -> would be an error"
    assert abs(Ks[0] + 2.5*math.log10(1+z)) < 5e-4, 'top-hat edge discretisation tolerance exceeded'
print("Case 2: R = fixed observer 'R'-like tophat(640±70 nm), Q = B: K carries SED-slope term, still no D_X dependence.")
Rfix = tophat(nu_grid, 640, 140)
for z in (0.1, 0.3, 0.45):
    Ks = [K_QR(planck_L_nu, Bband, Rfix, z, D) for D in (1e24, 3e26)]
    print(f"  z={z:4.2f}: K = {Ks[0]:+.5f} (D_X=1e24 m) {Ks[1]:+.5f} (D_X=3e26 m)")
    out["cases"].append(dict(case="R fixed", z=z, K=Ks))
    assert np.ptp(Ks) < 1e-9

# Now: what happens if a theory's bolometric dilution is F = L/(4 pi D^2 (1+z)^p) ?
# Then D_X = D (1+z)^{p/2}; m_R = M_Q + 5log10(D/10pc) + 2.5 p log10(1+z) + K_QR.  Nothing else.
print("\nTheory with bolometric flux L/(4πD²(1+z)^p): catalog-frame m_R = M_Q + 5log10(D/10pc) + 2.5·p·log10(1+z) + K_QR.")
print("Standard FRW: p=2 (energy + rate). Adding a *further* 5log10(1+z) 'for the K-correction' counts (1+z)^2 twice.")
print("The only (1+z) inside K itself is the bandwidth term (-2.5 log10(1+z) in the f_nu/AB convention), which SALT2/")
print("SNANA handle in the model integration; it is not the energy/arrival-rate dilution.")
# Sanity: bolometric check: integrated observed flux over all nu equals L_bol/(4 pi D_X^2) exactly (bandwidth factor cancels)
z = 1.0; D = 1e25
fobs = (1+z)*planck_L_nu(nu_grid*(1+z))/(4*math.pi*D**2)
Fbol_obs = np.trapezoid(fobs, nu_grid); Lbol = np.trapezoid(planck_L_nu(nu_grid*(1+z)), nu_grid*(1+z))
print(f"\nBolometric consistency at z=1: ∫f_obs dν / (L_bol/4πD_X²) = {Fbol_obs/(Lbol/(4*math.pi*D**2)):.6f} (should be 1: the bandwidth (1+z) is not a dilution factor)")
out["conclusion"] = ("K_QR is independent of D_X; it contains only bandpass/SED terms and the bandwidth (1+z). "
                     "The cosmological (1+z)^2 dilution is part of D_L by definition (Hogg eq.1), not part of K. "
                     "Adding 5log10(1+z) to a theory's bolometric distance modulus 'because of the K-correction' is a double count "
                     "unless the theory's 'bolometric' D omitted those factors in the first place — in which case the correct fix is "
                     "to derive the theory's own photon-energy and arrival-rate factors, not to invoke the K-correction.")
json.dump(out, open("results/kcorrection_audit.json", "w"), indent=2)
print("written results/kcorrection_audit.json")
