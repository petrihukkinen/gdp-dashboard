"""Code-correctness tests (NOT physics-validity tests). Run: python -m pytest -q tests"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
R = lambda name: json.load(open(os.path.join(os.path.dirname(__file__), "..", "results", name)))

def test_expansion_branch_symbolic():
    d = R("symbolic_checks.json")["expansion"]
    assert d["H_T"].replace(" ", "") == "2/(3*T)"
    assert "T**(2/3)" in d["R4_T"] and "T**(1/3)" in d["c0_T"]

def test_potential_kernel_0776_closed_form():
    from scipy import special
    closed = (math.log(2*math.pi) + np.euler_gamma - special.sici(2*math.pi)[1])/math.pi
    assert abs(closed - 0.775929) < 1e-6
    k = R("symbolic_checks.json")["potential_kernels"]
    assert abs(k["arc length on S^3 (d = R*theta)"] - closed) < 1e-9
    assert abs(k["4D Newton 1/d^2 kernel, chord"] - 1.0) < 1e-9

def test_alpha_rounding_explains_discrepancy():
    a = R("symbolic_checks.json")["alpha"]
    assert abs(a["formula_1p1049"] - 0.007297387644402) < 1e-15
    assert abs(a["coef_exact_for_codata"] - 1.1049053) < 1e-6
    assert abs(a["rel_diff"]) < 1e-5

def test_peters_mathews_two_implementations_and_reproduction():
    import binary_decay as bd
    Msun = 1.98847e30
    pm = bd.pbdot_PM(0.322997448918*86400, 1.438*Msun, 1.390*Msun, 0.6171340)
    er = bd.pbdot_energy_route(0.322997448918*86400, 1.438*Msun, 1.390*Msun, 0.6171340)
    assert abs(pm/er - 1) < 1e-12
    assert abs(pm/(-2.40263e-12) - 1) < 2e-3          # reproduces published GR value for B1913+16
    j = R("binary_decay.json")["PSR J1738+0333"]
    assert 0.9 < j["Pbdot_GR_here"]/j["Pbdot_GR_published"] < 1.1
    assert R("binary_decay.json")["constraint"]["J1738_sigma_nonzero"] > 8

def test_pantheon_replication_of_brout2022():
    p = R("pantheon_fit.json")
    assert p["N"] == 1590
    assert abs(p["flat_LCDM"]["Om"] - 0.334) < 0.018            # within published 1 sigma
    assert 0.015 < (p["flat_LCDM"]["Om_hi"] - p["flat_LCDM"]["Om_lo"])/2 < 0.021
    assert p["DU_fixed_q"]["1"] - p["flat_LCDM"]["chi2"] > 50     # DU q=+1 disfavoured by >50 in chi2

def test_kcorrection_independent_of_distance():
    for case in R("kcorrection_audit.json")["cases"]:
        assert np.ptp(case["K"]) < 1e-8
        if case["case"] == "R=Q shifted":
            assert abs(case["K"][0] - case["expected"]) < 5e-4

def test_bilfinger_accounting_identity_and_checks():
    meta = R("bilfinger_prototype_meta.json")
    assert meta["checks"]["fee redistributes only: client_inc + bilfinger_net == joint (P2, exact identity)"]
    assert meta["checks"]["P1 shows early cost saving vs P0 (first 12 months)"]
    assert meta["checks"]["P1 ends with higher latent debt than P0"]

def test_decisive_pantheon_test_consistent_with_pantheon_fit():
    d = R("pantheon_decisive_test.json"); p = R("pantheon_fit.json")
    t = d["table"]
    assert abs(t["D_flat_LCDM"]["chi2"] - p["flat_LCDM"]["chi2"]) < 1e-6          # same likelihood, same result
    assert abs(t["A_DU_bolometric_p0.5"]["chi2"] - p["DU_fixed_q"]["1"]) < 1e-6     # p=0.5 == q=1
    assert abs(t["B_DU_implied_Kcorr_p1.5"]["chi2"] - p["DU_fixed_q"]["3"]) < 1e-6  # p=1.5 == q=3
    assert abs(2*d["p_free"]["best"] - p["DU_q_free"]["q"]) < 1e-3
    assert t["B_DU_implied_Kcorr_p1.5"]["dchi2"] > 3000

def test_implied_relation_algebra():
    # m_bol + 5log10(1+z) with D_L = z sqrt(1+z) R  ==  5log10(z (1+z)^1.5 R)
    import numpy as np
    z = np.array([0.1, 0.5, 1.0, 2.0])
    lhs = 5*np.log10(z*np.sqrt(1+z)) + 5*np.log10(1+z)
    rhs = 5*np.log10(z*(1+z)**1.5)
    assert np.allclose(lhs, rhs)

def test_binary_tiers_bound_and_two_component_fit():
    b = R("binary_decay_tiers.json")
    assert b["DU_32_ONLY"]["X_critical_for_detectability"] > 1000
    f2 = b["DU_PLUS_QUADRUPOLE"]["fits"]["n=2"]
    assert abs(f2["kappa"] - 1) < 3*f2["kappa_err"] and f2["kappa_err"] < 1e-3
    assert f2["frac_B1913_2sigma_upper"] < 0.01
