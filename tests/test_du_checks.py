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
