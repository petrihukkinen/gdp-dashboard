"""
DU symbolic / numeric checks (Phase A2, items 1, 2, 4, 6) + A4 construction.

Everything here is derived from the two stated DU postulates as formulated in the
task prompt (zero-energy balance c0^2 = G M''/R4 and dR4/dT = c0), NOT from the
Frontiers article text, which was not accessible in this run (egress blocked).
Where an article coefficient is quoted (0.776, 0.991, 1.1049), the identification
of the integral/definition behind it is a *candidate* and is labelled as such.

Outputs: results/symbolic_checks.json and results/symbolic_checks.txt
"""
from __future__ import annotations
import json, math, sys
import numpy as np
import sympy as sp
from scipy import integrate, constants, special

OUT = {}
lines = []
def log(s=""):
    print(s); lines.append(str(s))

# ----------------------------------------------------------------------------
# 1. Expansion branch from c0^2 = G M''/R4 and dR4/dT = c0, with G, M'' constant
# ----------------------------------------------------------------------------
log("=== 1. Expansion branch ===")
T, G, Mpp, C1 = sp.symbols("T G Mpp C1", positive=True)
R = sp.Function("R")
ode = sp.Eq(R(T).diff(T), sp.sqrt(G*Mpp/R(T)))          # dR/dT = +sqrt(GM''/R)  (expanding branch)
sol = sp.dsolve(ode, R(T))
log(f"General solution (sympy): {sol}")
# Separable form: R^{1/2} dR = sqrt(GM'') dT  ->  (2/3) R^{3/2} = sqrt(GM'') T + C1
R_explicit = ((sp.Rational(3, 2)*(sp.sqrt(G*Mpp)*T + C1))**sp.Rational(2, 3))
# choose time origin so that R4(0)=0  ->  C1 = 0
R0 = R_explicit.subs(C1, 0)
chk = sp.simplify(R0.diff(T) - sp.sqrt(G*Mpp/R0))
log(f"R4(T) with C1=0 (R4(0)=0):  R4 = {R0}")
log(f"ODE residual after substitution (should be 0): {chk}")
H = sp.simplify(R0.diff(T)/R0)
log(f"H(T) = R4'/R4 = {H}")
c0 = sp.simplify(sp.sqrt(G*Mpp/R0))
log(f"c0(T) = sqrt(GM''/R4) = {c0}   -> c0 ∝ T^(-1/3)")
assert sp.simplify(H - sp.Rational(2, 3)/T) == 0
assert sp.simplify(sp.log(c0).diff(T) + sp.Rational(1, 3)/T) == 0
OUT["expansion"] = {
    "R4_T": str(R0), "H_T": str(H), "c0_T": str(c0),
    "integration_constant": "C1 chosen = 0  <=> R4(T=0) = 0 (coordinate-time origin at R4=0).",
    "general_solution": "(2/3) R4^{3/2} = sqrt(G M'') T + C1 ; C1 != 0 just shifts the time origin, not the shape.",
}
# R4 -> 0 limit
log("Limits as T->0+ : c0 -> inf, H -> inf, R4 -> 0 (curvature singularity of the 4-radius).")
log("Kinetic energy of expansion  M c0^2  and gravitational energy -G M M''/R4 both diverge as 1/R4;")
log("their SUM is identically zero for all T (that is the postulate), so zero total energy does not")
log("regularise the R4->0 point. Contracting branch: dR/dT = -sqrt(GM''/R) gives R = [(3/2)sqrt(GM'')(T0-T)]^{2/3};")
log("joining it to the expanding branch at T0 requires dR/dT to jump from -inf to +inf: NOT a regular bounce,")
log("the sign change alone supplies no dynamics through R4=0.")
OUT["expansion"]["R4_to_0"] = ("Both energy terms diverge as 1/R4; sum is zero by postulate; velocity dR4/dT -> inf; "
                               "contraction->expansion join is a velocity discontinuity (-inf -> +inf), not a regular solution.")

# Coordinate time -> clock time.  DU: atomic clock frequency f ∝ c0 (stated DU scaling, treated here
# as an additional assumption A-CLOCK, cf. claim register).  Ticks: N(T) = ∫ f dT.
f = sp.Symbol("f0")*c0/c0.subs(T, sp.Symbol("T0"))
Tsym0 = sp.Symbol("T0", positive=True)
N = sp.integrate(f, (T, 0, Tsym0))
age_in_present_clock_units = sp.simplify(N/f.subs(T, Tsym0))
log(f"Clock ticks accumulated since R4=0, divided by present clock rate: {age_in_present_clock_units}  (= 3/2 T0)")
log("With H0 = 2/(3 T0)  ->  T0 = 2/(3 H0)  ->  age in present-clock units = (3/2)(2/(3H0)) = 1/H0.")
OUT["expansion"]["age_coordinate_time"] = "T0 = 2/(3 H0)"
OUT["expansion"]["age_present_clock_units"] = "1/H0  (requires extra assumption f_clock ∝ c0)"
for H0 in (67.4, 70.0, 73.0):
    H0_s = H0*1e3/(constants.parsec*1e6)
    Gyr = 1e9*365.25*86400
    log(f"  H0={H0}: coordinate age 2/(3H0) = {2/(3*H0_s)/Gyr:.2f} Gyr ; present-clock age 1/H0 = {1/H0_s/Gyr:.2f} Gyr")

# ----------------------------------------------------------------------------
# 2. 3-sphere gravitational potential integral: candidate kernels for 0.776 / 0.991
# ----------------------------------------------------------------------------
log("\n=== 2. 3-sphere potential integral: candidate distance kernels ===")
# Uniform mass M_Sigma on S^3 of radius R.  Mass fraction at geodesic angle theta: (2/pi) sin^2(theta) dtheta.
# Potential at a point:  Phi = -(G M_Sigma / R) * k,  k = (2/pi) ∫_0^pi sin^2(theta) / (d(theta)/R) dtheta
def k_factor(kernel):
    val, err = integrate.quad(lambda th: (2/math.pi)*math.sin(th)**2/kernel(th), 0, math.pi, limit=400)
    return val, err
cands = {
    "arc length on S^3 (d = R*theta)":            lambda th: th,
    "chord in R^4 (d = 2R sin(theta/2))":         lambda th: 2*math.sin(th/2),
    "projected chord (d = R sin theta) [1/sin]":  lambda th: math.sin(th) if th not in (0.0, math.pi) else 1e-300,
    "4D Newton 1/d^2 kernel, chord":              lambda th: (2*math.sin(th/2))**2,
    "1/d^2 kernel, arc":                          lambda th: th**2,
}
ker = {}
for name, kf in cands.items():
    try:
        v, e = k_factor(kf)
    except Exception as ex:
        v, e = float("nan"), float("nan")
    ker[name] = v
    log(f"  k = {v:.6f} (quad err {e:.1e})  <- {name}")
# closed form for the arc-length kernel: (2/pi)∫ sin^2/θ = (1/pi)[ln(2π) + γ - Ci(2π)]
closed = (math.log(2*math.pi) + np.euler_gamma - special.sici(2*math.pi)[1])/math.pi
log(f"  closed form (arc kernel) = (1/pi)[ln 2pi + gamma - Ci(2pi)] = {closed:.6f}")
# Also 2-sphere analogue (for completeness): fraction (1/2) sin θ dθ, arc kernel: Si(pi)/2
two_sphere_arc = special.sici(math.pi)[0]/2
log(f"  2-sphere analogue, arc kernel: Si(pi)/2 = {two_sphere_arc:.6f}")
OUT["potential_kernels"] = {**ker, "closed_form_arc": closed, "two_sphere_arc": two_sphere_arc}
log("IDENTIFICATION: 0.776 = (2/pi)∫_0^pi sin^2(theta)/theta dtheta, i.e. uniform S^3 with GEODESIC (arc-length)")
log("  1/d kernel. The chord kernel gives 0.849, the 4D 1/d^2 kernel gives exactly 1.  No candidate here gives 0.991;")
log("  the origin of 0.991 is NOT IDENTIFIED in this run (article text inaccessible).")
log("NOTE: 1/d with d = geodesic distance is the flat-space Newtonian kernel transplanted onto S^3. It is NOT the")
log("  Green's function of the Laplacian on S^3 (which on a compact manifold requires a zero-mean source and has the")
log("  form ∝ (π-θ)cotθ). Whether 0.776 double counts self-energy depends on whether E_g is summed over all pairs")
log("  (factor 1/2) or per test mass (no 1/2): the per-test-mass form used in c0^2 = GM''/R4 has no 1/2.")
# Green's function on S^3 check: G(θ) = (π-θ)cotθ. Radial Laplacian on S^3: (1/sin^2θ) d/dθ( sin^2θ dG/dθ ).
th = sp.symbols("theta", positive=True)
Gs3 = (sp.pi - th)*sp.cot(th)
lap = sp.simplify(sp.diff(sp.sin(th)**2*sp.diff(Gs3, th), th)/sp.sin(th)**2)
log(f"  S^3 candidate Green's function (π-θ)cotθ: Laplacian away from θ=0 = {lap} (a CONSTANT) ->")
log("  Δ_S3 G = const + δ : the compact-space Poisson equation Δφ = 4πG(ρ - ρ̄) is solved by this kernel, not by 1/θ.")
log("  Hence 'Poisson on S^3' and 'flat 1/d kernel on S^3' are different local field laws; 0.776 assumes the latter.")
OUT["potential_kernels"]["S3_green_function_laplacian_const"] = str(lap)

# ----------------------------------------------------------------------------
# 4. Fine-structure constant: alpha = 1/(1.1049 * 4 pi^3)
# ----------------------------------------------------------------------------
log("\n=== 4. Fine structure constant with coefficient 1.1049 ===")
alpha_formula = 1/(1.1049*4*math.pi**3)
alpha_codata = constants.fine_structure
coef_exact = 1/(alpha_codata*4*math.pi**3)
log(f"  1/(1.1049 * 4 pi^3)      = {alpha_formula:.15f}")
log(f"  scipy CODATA alpha        = {alpha_codata:.15f}  (scipy {__import__('scipy').__version__}; CODATA set: {constants.codata.__name__})")
log(f"  article text value (as quoted in task) = 0.00729735254")
log(f"  relative diff formula vs CODATA = {(alpha_formula/alpha_codata-1):.3e}")
log(f"  coefficient needed to reproduce CODATA exactly: {coef_exact:.9f}  (1.1049 is this rounded to 5 s.f.)")
log(f"  rounding 1.1049 vs {coef_exact:.6f}: relative {(1.1049/coef_exact-1):.2e}  -> explains the alpha discrepancy exactly.")
OUT["alpha"] = {"formula_1p1049": alpha_formula, "codata": alpha_codata, "text_value": 0.00729735254,
                "coef_exact_for_codata": coef_exact, "rel_diff": alpha_formula/alpha_codata-1,
                "verdict": "Discrepancy = rounding of coefficient. Whether 1.1049(05) is derived independently or "
                           "calibrated to measured alpha could not be checked (article/book inaccessible): EI YKSILÖIDY."}

# ----------------------------------------------------------------------------
# 6. Dimensionless process rates vs expansion: N_process = ∫ Γ dT
# ----------------------------------------------------------------------------
log("\n=== 6. Process rates relative to expansion ===")
# Γ_atomic ∝ c0 ∝ T^{-1/3} (DU clock assumption A-CLOCK).  Γ_grav = sqrt(G rho), rho = M/(2 pi^2 R4^3), G,M const -> ∝ T^{-1}
# Γ_exp = H = 2/(3T).
Ta, Tb = sp.symbols("Ta Tb", positive=True)
N_atomic = sp.integrate(T**sp.Rational(-1, 3), (T, Ta, Tb))
N_grav = sp.integrate(1/T, (T, Ta, Tb))
N_exp = sp.integrate(sp.Rational(2, 3)/T, (T, Ta, Tb))
log(f"  N_atomic(Ta->Tb) ∝ {N_atomic}")
log(f"  N_grav  (Ta->Tb) ∝ {N_grav}   (free-fall rate sqrt(G rho))")
log(f"  N_exp   (Ta->Tb) = {N_exp}   (e-folds of R4)")
log("  Γ_grav/H = const  -> gravitational collapse per e-fold of expansion is epoch-independent (same as EdS).")
log("  Γ_atomic/H ∝ T^{2/3} -> atomic processes per e-fold were FEWER early on, not more.")
log("  => a larger early c0 does not, by itself, imply faster structure formation; the claim needs a separate")
log("     local dynamical law in which the collapse rate scales with c0. Not derivable from the two postulates.")
OUT["process_rates"] = {"N_atomic": str(N_atomic), "N_grav": str(N_grav), "N_exp": str(N_exp),
                        "conclusion": "Gamma_grav/H constant; Gamma_atomic/H ∝ T^(2/3)."}

# ----------------------------------------------------------------------------
# A4. Two explicit light-propagation models with the same global constraint
# ----------------------------------------------------------------------------
log("\n=== A4. Two local light-propagation models, same global R4(T) ===")
log("Shared: R4(T) ∝ T^{2/3}, tangential light speed c(T) = c0(T) = dR4/dT, wavelength ∝ R4 => 1+z = R4_obs/R4_emit.")
log("Model L-A (path-length): observable distance = light path length D = ∫ c dT = R4_o - R4_e = R4_o z/(1+z).")
log("Model L-B (geodesic):   angular separation χ = ∫ c dT / R4 = ln(1+z); transverse metric distance = R4_o sin χ.")
z = np.array([0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 14.0, 20.0, 22.0, 30.0])
D_A_LA = z/(1+z)/(1+z)                 # source size at emission subtends d/(D) with D in units R4_o; D_A = D/(1+z)?  see note
# Careful: in L-A the 'distance' D is the path length at observation epoch; angular size of a source of proper size d
# (at emission) in L-A: θ = d/D  (Suntola-type Euclidean rule) -> D_A^{LA} = D = z/(1+z) (units R4_o).
D_A_LA = z/(1+z)
D_A_LB = np.sin(np.log(1+z))/(1+z)     # D_A = R4_e sin χ = R4_o sin χ /(1+z)
ratio = D_A_LB/D_A_LA
log("   z      D_A(L-A)/R4o   D_A(L-B)/R4o    ratio LB/LA")
for zi, a, b, r in zip(z, D_A_LA, D_A_LB, ratio):
    log(f"  {zi:5.2f}    {a:9.4f}     {b:9.4f}     {r:8.4f}")
z_antipode = math.e**math.pi - 1
log(f"  L-B antipode at χ = π  ->  z = e^π - 1 = {z_antipode:.3f};  sin χ < 0 for z > {z_antipode:.2f} (parity flip).")
log("  L-A never reaches the antipode (D -> R4_o as z->inf).")
log("  Both models are consistent with the two postulates + 'c = dR4/dT'; they differ at z=1 by "
    f"{(1-ratio[3])*100:.0f}% in D_A. => the global constraint does not fix the observable; a closure postulate")
log("  on how the angular/transverse geometry of S^3 enters the observation is required.")
OUT["A4_nonuniqueness"] = {"z": z.tolist(), "D_A_LA": D_A_LA.tolist(), "D_A_LB": D_A_LB.tolist(),
                           "z_antipode_LB": z_antipode,
                           "note": "Both models constructed from the same postulates; differ in D_A(z)."}
# Time dilation in L-B in coordinate vs clock time
log("  L-B arrival-interval stretch in coordinate time: Δt_o/Δt_e = H_e/H_o = (1+z)^{3/2};")
log("  in local-clock units (f∝c0∝R^{-1/2}): (1+z)^{3/2} (1+z)^{-1/2} = (1+z). Same as FRW in proper time.")
OUT["A4_nonuniqueness"]["time_dilation_LB_clock_units"] = "(1+z)"

# Etherington check: L-B with photon-number conservation on S^3 and clock-time dilation (1+z) and energy (1+z):
# F = L/(4π R4_o^2 sin^2χ (1+z)^2)  -> D_L = R4_o sinχ (1+z) = D_A (1+z)^2  : Etherington holds for L-B.
# L-A: F = L/(4π D^2 (1+z)^q): D_L = D (1+z)^{q/2}; Etherington (D_L = D_A(1+z)^2) holds only if q = 4 with D_A=D.
log("  Etherington: L-B (photon conservation on S^3 + (1+z) energy + (1+z) rate) gives D_L = D_A (1+z)^2 -> holds.")
log("  L-A with D_A = D and F ∝ D^{-2}(1+z)^{-q} gives D_L = D (1+z)^{q/2}: reciprocity holds only for q = 4.")
log("  For the Suntola-type q=1 (D_L = R z (1+z)^{1/2}/(1+z)... see pantheon_fit) reciprocity is violated ->")
log("  the violated assumption is photon-number conservation through the flux tube / transverse S^3 geometry.")

with open("results/symbolic_checks.json", "w") as fh:
    json.dump(OUT, fh, indent=2, default=str)
with open("results/symbolic_checks.txt", "w") as fh:
    fh.write("\n".join(lines))
print("\nwritten results/symbolic_checks.{json,txt}")
