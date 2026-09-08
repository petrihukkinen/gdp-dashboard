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
dt = J("pantheon_decisive_test.json"); bt = J("binary_decay_tiers.json")
checks += [
 ("decisive B dchi2 +3491", abs(dt["table"]["B_DU_implied_Kcorr_p1.5"]["dchi2"] - 3490.6) < 0.2 and "+3491" in reports),
 ("decisive free p 0.623", abs(dt["p_free"]["best"] - 0.623) < 0.001 and "0,623" in reports),
 ("decisive tilt -4.41", abs(dt["residual_tilt_B_mag_per_dex"] + 4.41) < 0.01 and "−4,41" in reports),
 ("decisive test chi2 B 2947", abs(dt["train_test"]["B"]["chi2_test"] - 2947.2) < 0.5 and "2947" in reports),
 ("tiers X_crit 1830", abs(bt["DU_32_ONLY"]["X_critical_for_detectability"] - 1830) < 1 and "1830" in reports),
 ("tiers kappa n=2 1.00045", abs(bt["DU_PLUS_QUADRUPOLE"]["fits"]["n=2"]["kappa"] - 1.00045) < 1e-5 and "1,00045" in reports),
 ("tiers ecc share n=1 0.8 %", abs(bt["DU_PLUS_QUADRUPOLE"]["fits"]["n=1"]["frac_B1913_2sigma_upper"]*100 - 0.8) < 0.05 and "0,8 %" in reports),
 ("falsification matrix rows", sum(1 for _ in open(os.path.join(root, "results", "falsification_matrix.csv"), encoding="utf-8")) >= 12),
]
rb = J("pantheon_robustness.json"); bs = J("binary_decay_sensitivity.json"); fc = J("falsification_matrix_counts.json")
checks += [
 ("counts match report (TENSION 3, FALSIFIED 1)", fc["counts"]["TENSION"] == 3 and fc["counts"]["FALSIFIED AS CURRENTLY FORMULATED"] == 1 and "TENSION 3" in reports and "FALSIFIED AS CURRENTLY FORMULATED 1" in reports),
 ("chi2/dof A 0.935 / B 3.08", abs(rb["table"]["A DU p=0.5"]["chi2_dof"] - 0.935) < 0.001 and abs(rb["table"]["B DU p=1.5"]["chi2_dof"] - 3.08) < 0.005 and "0,935" in reports and "3,08" in reports),
 ("Wald 8.3 sigma", abs(rb["wald_sigma"]["A"] - 8.3) < 0.05 and "8,3σ" in reports),
 ("conditional held-out 229/258/264/3027", abs(rb["heldout"]["D flat LCDM"]["chi2_conditional"] - 229.0) < 0.1 and abs(rb["heldout"]["A DU p=0.5"]["chi2_conditional"] - 258.1) < 0.1 and abs(rb["heldout"]["B DU p=1.5"]["chi2_conditional"] - 3026.9) < 0.1 and "229" in reports and "258" in reports),
 ("bias sensitivity 110 / 17", abs(rb["bias_sensitivity"]["dchi2_A"] - 110.5) < 0.2 and abs(rb["bias_sensitivity"]["dchi2_C"] - 17.1) < 0.2 and "110" in reports),
 ("no-J0737 bound 29 %", abs(bs["two_component_sensitivity"]["without J0737 (drop MEM ratio) n=1"]["fracB_2sig_upper"]*100 - 29.4) < 0.2 and "29 %" in reports),
 ("X for n=1 e=3.4e-7 is 2400", abs([r for r in bs["bound_rows"] if r["n"] == 1 and abs(r["e_J"] - 3.4e-7) < 1e-9][0]["X_needed_for_1sigma"] - 2420) < 10 and "2400" in reports),
 ("withdrawn statement present", "vedetty takaisin" in reports),
]
bad = [n for n, ok in checks if not ok]
for n, ok in checks: print(f"  [{'OK' if ok else 'MISMATCH'}] {n}")
print(f"{len(checks)-len(bad)}/{len(checks)} consistent")
sys.exit(1 if bad else 0)
