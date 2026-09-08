"""Independent-reviewer role: check that numbers quoted in the reports match the machine results.
Exit code 1 on any mismatch. Run after all src/ scripts."""
import json, re, sys, os, math
root = os.path.join(os.path.dirname(__file__), "..")
J = lambda n: json.load(open(os.path.join(root, "results", n)))
reports = "".join(open(os.path.join(root, "reports", f), encoding="utf-8").read() for f in
                  ("DU_AUDIT_FI.md", "DU_RESEARCH_RESULT.md", "EXECUTIVE_BRIEF_FI.md", "BILFINGER_MODEL_FI.md"))
sym, pan, bd, kc = J("symbolic_checks.json"), J("pantheon_fit.json"), J("binary_decay.json"), J("kcorrection_audit.json")
import pandas as pd
mc = pd.read_csv(os.path.join(root, "results", "bilfinger_mc_summary.csv"))
none = mc[mc.stress == "none"].set_index("policy")
ev = lambda s: eval(s)
checks = [
 ("Omega_m 0.332", abs(pan["flat_LCDM"]["Om"] - 0.332) < 0.001 and "0,332" in reports),
 ("Omega_m error 0.018", abs((pan["flat_LCDM"]["Om_hi"] - pan["flat_LCDM"]["Om_lo"])/2 - 0.018) < 0.001),
 ("chi2 LCDM 1402.9", abs(pan["flat_LCDM"]["chi2"] - 1402.9) < 0.1 and "1402,9" in reports),
 ("DU q=+1 dchi2 +82", abs(pan["DU_fixed_q"]["1"] - pan["flat_LCDM"]["chi2"] - 82.1) < 0.2 and "+82" in reports),
 ("DU q free 1.246", abs(pan["DU_q_free"]["q"] - 1.246) < 0.001 and "1,246" in reports),
 ("DU q free dchi2 +14", abs(pan["DU_q_free"]["chi2"] - pan["flat_LCDM"]["chi2"] - 14.0) < 0.2 and "+14" in reports),
 ("C2 LB dchi2 +277", abs(pan["DU_fixed_q"]["LB"] - pan["flat_LCDM"]["chi2"] - 277.4) < 0.2 and "+277" in reports),
 ("prediction test 222 / 254", abs(pan["prediction_test"]["LCDM"]["chi2_test"] - 222.1) < 0.2 and abs(pan["prediction_test"]["DU_qfree"]["chi2_test"] - 254.4) < 0.2 and "254" in reports and "222" in reports),
 ("alpha formula", abs(sym["alpha"]["formula_1p1049"] - 0.007297387644402) < 1e-15 and "0,007297387644402" in reports),
 ("alpha exact coef 1.104905", abs(sym["alpha"]["coef_exact_for_codata"] - 1.104905) < 1e-6 and "1,104905" in reports),
 ("kernel 0.775929", abs(sym["potential_kernels"]["arc length on S^3 (d = R*theta)"] - 0.775929) < 1e-6 and "0,775929" in reports),
 ("antipode z 22.14", abs(sym["A4_nonuniqueness"]["z_antipode_LB"] - 22.141) < 0.001 and "22,14" in reports),
 ("J1738 sigma 8.1", abs(bd["constraint"]["J1738_sigma_nonzero"] - 8.1) < 0.05 and "8,1σ" in reports),
 ("J1738 ratio 0.94", abs(bd["PSR J1738+0333"]["ratio_obs_over_GR_here"] - 0.943) < 0.002),
 ("B1913 reproduction 0.9998", abs(bd["PSR B1913+16"]["Pbdot_GR_here"]/bd["PSR B1913+16"]["Pbdot_GR_published"] - 0.9998) < 0.0002 and "0,9998" in reports),
 ("K independent of D", all(max(c["K"]) - min(c["K"]) < 1e-8 for c in kc["cases"])),
 ("Bilfinger P2 joint +2.6", abs(ev(none.loc["P2", "joint_incremental_value_MEUR"])[0] - 2.6) < 0.1 and "+2,6" in reports),
 ("Bilfinger P2 p10 -3.5", abs(ev(none.loc["P2", "joint_incremental_value_MEUR"])[1] + 3.5) < 0.1 and "−3,5" in reports),
 ("Bilfinger P1 Bilfinger +6.1", abs(ev(none.loc["P1", "bilfinger_net_MEUR"])[0] - 6.1) < 0.1 and "+6,1" in reports),
 ("Bilfinger P1 client -29.5", abs(ev(none.loc["P1", "client_incremental_MEUR"])[0] + 29.5) < 0.1 and "−29,5" in reports),
 ("Bilfinger P0 availability 0.867", abs(none.loc["P0", "mean_availability"] - 0.867) < 0.001 and "0,867" in reports),
 ("Bilfinger accounting identity", J("bilfinger_prototype_meta.json")["checks"]["fee redistributes only: client_inc + bilfinger_net == joint (P2, exact identity)"]),
 ("Bilfinger p10 check recorded as FAIL in report", (not J("bilfinger_prototype_meta.json")["checks"]["P2 joint value p10 > 0 (robustness)"]) and "FAIL" in reports),
]
bad = [n for n, ok in checks if not ok]
for n, ok in checks: print(f"  [{'OK' if ok else 'MISMATCH'}] {n}")
print(f"{len(checks)-len(bad)}/{len(checks)} consistent")
sys.exit(1 if bad else 0)
