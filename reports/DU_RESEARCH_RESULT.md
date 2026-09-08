# DU RESEARCH RESULT (Phase A4) — one bounded problem, actually computed

Date 2026-09-08. Language: English for the research record; Finnish conclusions in `DU_AUDIT_FI.md` and `EXECUTIVE_BRIEF_FI.md`.

## Problem chosen

**Does the global zero-energy constraint (c0² = GM''/R4, dR4/dT = c0) together with "light propagates at c0 tangentially and wavelengths scale with R4" determine the observable distance–redshift relations?** If not, what closure is missing, and can a testable completion be built?

This was chosen because (i) it is cheap, (ii) it is the hinge on which the article's supernova, angular-size and antipode claims all turn, and (iii) it can be settled by explicit construction rather than by argument.

## Result 1 — Non-uniqueness demonstrated by construction (new, bounded)

Two local light-propagation models were built that share every global ingredient (same R4(T) ∝ T^{2/3}, same c(T) = dR4/dT, same 1+z = R4_o/R4_e) and differ only in how the transverse S³ geometry enters the observation:

| | Model L-A (path length) | Model L-B (geodesic angle) |
|---|---|---|
| Rule | distance = light path ∫c dT = R4_o − R4_e | angle χ = ∫c dT/R4 = ln(1+z), transverse size via R4 sin χ |
| D_A | R4_o · z/(1+z) | R4_o · sin(ln(1+z))/(1+z) |
| z→0 | R4_o z | R4_o z (agree) |
| z=1 | 0.500 R4_o | 0.320 R4_o (−36 %) |
| antipode | none | z = e^π − 1 = 22.14, sin χ<0 beyond (parity flip) |
| Etherington | D_L = D_A(1+z)² only if flux ∝ (1+z)^{-4} | holds with photon conservation + (1+z) energy + (1+z) rate |

Both are consistent with the stated postulates. Hence **the postulates do not fix D_A(z)**; an additional closure postulate is needed that states how a transverse proper length at emission maps to an observed angle. This is a concrete, checkable statement: anyone can add a third model. File: `src/du_symbolic_checks.py` (section A4), `results/symbolic_checks.json["A4_nonuniqueness"]`.

Time dilation in L-B: coordinate arrival-interval stretch is (1+z)^{3/2}; in local clock units (f ∝ c0 ∝ R^{-1/2}) it is (1+z), identical to FRW proper-time dilation. This matters for the supernova light-curve width test, which DU therefore does **not** automatically fail — but only under the A-CLOCK assumption.

## Result 2 — Independent observational pipeline for the supernova test

`src/pantheon_fit.py`, Pantheon+ release data (1701 SNe, STAT+SYS covariance), zHD > 0.01 (N = 1590), D_L = (1+z_hel) D_M(z_HD), M profiled analytically.

| Model | shape params | χ² | Δχ² vs flat ΛCDM | ΔAIC |
|---|---|---|---|---|
| flat ΛCDM (Ωm = 0.332 ± 0.018; published 0.334 ± 0.018) | 1 | 1402.9 | 0 | 0 |
| open ΛCDM (Ωm=0.295, ΩΛ=0.613) | 2 | 1402.4 | −0.5 | +1.5 |
| DU q=+1: D_L ∝ z(1+z)^{1/2} (Suntola & Day 2004 form) | 0 | 1485.0 | +82.1 | +80.1 |
| DU q free: q = 1.246 ± 0.030 | 1 | 1416.9 | +14.0 | +14.0 |
| DU q=−1 (bolometric candidate) | 0 | 7111.8 | +5709 | — |
| DU q=+3 (double-added 5log(1+z)) | 0 | 4893.6 | +3491 | — |
| Candidate C2: L-B + Etherington, D_L = R sin(ln(1+z))(1+z) | 0 | 1680.3 | +277 | +275 |
| EdS reference (Ωm=1) | 0 | 2101.2 | +698 | — |

Out-of-sample: train z<0.4 (N=1282), test z≥0.4 (N=308): test χ² ΛCDM 222.1, DU q-free 254.4, DU q=+1 253.7; mean test residual −0.007 / −0.060 / +0.074 mag.

Interpretation (bounded): the claim seen in the search snippet — that the DU curve "traces the data at least as well as the two-parameter ΛCDM fit" — is **not reproduced** for any candidate identification of the DU form tried here. Visual similarity of curves ≠ statistical equivalence: the q=+1 curve is within ~0.07 mag of ΛCDM over 0.3<z<0.9, which looks fine by eye but costs Δχ² = 82 against a 1590-point covariance-weighted dataset. **Caveat**: the article's exact eq. 31/36 form is unverified (source blocked). If it is not in the family z(1+z)^{q/2}, the test must be re-run.

## Result 3 — K-correction audit settles the direction of the "+5 log10(1+z)" term

`src/kcorrection_audit.py`. From Hogg's definition m_R = M_Q + DM + K_QR, with a synthetic blackbody SED and top-hat filters, K_QR was computed for three different assumed dilution distances D_X spanning 2.5 dex: K is identical to 1e-9 mag. Hence **K carries no information about the cosmological (1+z)² dilution**; that dilution lives in D_L by definition. A theory must supply its own photon-energy and arrival-rate factors inside its D_L; adding 5 log10(1+z) "because the K-correction removed them" double counts. The only (1+z) inside K is the bandwidth term (−2.5 log10(1+z) in the f_ν/AB convention), handled inside SALT2/SNANA model integration. This is definitional, independent of the inaccessible article text; what remains unverified is whether the article's argument is exactly the one paraphrased in the snippet.

## Result 4 — Near-circular orbit constraint (conditional on eq. 32's e-dependence)

`src/binary_decay.py`. Two independent GR implementations agree to 1e-12; they reproduce the published GR values for B1913+16 (0.9998×) and J1738+0333 (0.99×, within the mass-uncertainty range 0.94–1.06). PSR J1738+0333 (e = 3.4e-7) has an intrinsic decay of −25.9 ± 3.2 fs/s: nonzero at 8.1σ, and f(e) − 1 = 8e-13 so the GR value is e-independent here. **Any decay law vanishing as e → 0 is excluded by this system alone.** Whether the article's eq. 32 is such a law could not be read; the article reportedly leaves a quadrupole effect open, so the test is registered as conditional: "eq. 32 alone" vs "eq. 32 + supplement" must be treated separately, and any supplement must not double the decay in B1913+16 (ratio 0.9983 ± 0.0016) or the double pulsar (0.999963 ± 0.000063; numbers from memory → OPEN LOOP).

## Candidate completions tried (max two, as required) — both labelled NEW CANDIDATES, not Suntola's results

**C1 — free flux-dilution exponent.** New assumption: bolometric flux ∝ D^{-2}(1+z)^{-q} with q free (L-A geometry). Parameter cost 1. Preserved: H = 2/(3T), age 1/H0. Fit: q = 1.246 ± 0.030, Δχ² = +14 vs ΛCDM at equal parameter count; worse out of sample. q ≈ 1.25 does not correspond to any simple photon-counting integer (1, 2, 4). **Disfavoured; not a rescue.** New discriminating test: the light-curve width–z relation fixes the arrival-rate factor independently (must be (1+z)^1 for the A-CLOCK version), leaving the energy factor to be compared with q − 1 ≈ 0.25 — an unphysical fractional energy loss unless a new mechanism is specified.

**C2 — geodesic S³ propagation with Etherington.** New assumption: transverse geometry enters via R4 sin χ, χ = ln(1+z), photon number conserved. Parameter cost 0. Preserved: everything global; adds antipode at z = 22.14 and a large lensing factor at JWST redshifts (×15 at z=10, ×33 at z=14). Fit: Δχ² = +277. **Excluded by Pantheon+.** Its JWST prediction (large, bright, parity-flipped images beyond z≈22) is therefore moot unless χ(z) is changed — which would require abandoning c = dR4/dT or λ ∝ R4.

## Failed attempt, recorded

An attempt to identify the coefficient 0.991 from the S³ potential integral failed: six kernel variants gave 0.776, 0.849, 0.903, 1.000, 1.273 and (2-sphere) 0.926. Without the article text the origin of 0.991 is unknown.

## Novelty check (limited)

Search-engine level only (arxiv/ADS blocked): no result was found treating the non-uniqueness of D_A(z) under the DU postulates explicitly; Suntola & Day (2004) and the 2026 article use a single form. The K-correction argument (that K excludes the cosmological dilution) is standard (Hogg et al. 2002) and is not new; its application to the article's term is. The J1738+0333 constraint on e-dependent decay laws is standard in the scalar–tensor literature (Freire et al. 2012); its application to DU is new here but conditional.

## Next test with best information per cost

Obtain the article text (or the author's own code) and (1) place eqs. 31/36 in the q-family or state its actual form, then re-run `pantheon_fit.py` (7 s); (2) read the e→0 limit of eq. 32 and close claim C14. Both are hours of work once the source is accessible; no new data are needed.

---

# Update 2 — externally supplied article statements and the decisive tests

Provenance: the article statements and the Liu et al. / Freire et al. numbers below were supplied by the user on 2026-09-08 as externally verified; this environment did not fetch them (`sources/manifest.csv`, rows marked EXTERNALLY SUPPLIED).

## A. Derivation of the implied relation and decisive Pantheon+ run (`src/pantheon_decisive_test.py`)

Published textual transformation: bolometric D_L = z√(1+z) R4, then add 2.5 log10[(1+z)²] to the magnitude.

m_bol = M + 5 log10(R4 z (1+z)^{1/2}/10pc); m_cat = m_bol + 5 log10(1+z) = M + 5 log10(R4 z (1+z)^{3/2}/10pc).

Absent another hidden term this is exactly D_eff ∝ z(1+z)^{3/2}, i.e. p = 1.5 in D_L ∝ z(1+z)^p (q = 3 in the earlier `pantheon_fit.py` convention). It is "the relation implied by the published textual transformation", not the rendered Eq. 36.

Identical data (N = 1590), covariance, and M-profiling as the ΛCDM reproduction:

| Model | χ² | Δχ² | k | ΔAIC | ΔBIC | test χ² (z≥0.4) | mean test residual |
|---|---|---|---|---|---|---|---|
| A raw DU p=0.5 | 1485.02 | +82.10 | 1 | +80.10 | +74.73 | 253.7 | +0.073 |
| B implied K-corrected DU p=1.5 | 4893.55 | +3490.63 | 1 | +3488.63 | +3483.26 | 2947.2 | −0.665 |
| C free p = 0.623 ± 0.015 | 1416.94 | +14.02 | 2 | +14.02 | +14.02 | 254.4 | −0.060 |
| D flat ΛCDM Ωm = 0.332 ± 0.018 | 1402.92 | 0 | 2 | 0 | 0 | 222.1 | −0.007 |

Residuals vs z for B run from +0.34 mag at z≈0.015 to −1.97 mag at z≈2 (tilt −4.41 mag/dex in log10(1+z)); p = 1.5 sits 59σ from the best-fit p. **B is falsified as currently formulated. A is in strong tension (8σ). C does not rescue (ΔAIC +14 at equal k, worse out of sample).** The K-correction cannot generate the extra term (definitional audit; consistent with the externally confirmed Hogg definition).

## B. Tiered near-circular test (`src/binary_decay_tiers.py`)

PSR J1738+0333 is now a Tier-1 discriminating observation (claim C14).

*DU-32-ONLY.* Exact Eq. 32 unavailable → numerical prediction UNRESOLVED. Rigorous limit: published F(0) = 0; analytic F ⇒ F = O(eⁿ), n ≥ 1. Calibrating Eq. 32 to the whole B1913+16 decay (most favourable), |Ṗb_32(J1738)| ≤ 2.40e-12 (e_J/e_B)ⁿ X; the bound reaches the 3.2e-15 measurement error only for a prefactor ratio X ≥ 1830 (n = 1, e+1σ); a GR-like prefactor gives X = 0.14. Prediction 0 vs −25.9 ± 3.2 fs/s: 8.1σ against H_32. *(Update 2 classified this as falsified; Update 3 downgrades it to TENSION (strong, conditional) because analyticity and the prefactor are unverified assumptions.)*

*DU-PLUS-QUADRUPOLE.* Two-component fit Ṗb = κ Ṗb_GR(e) + β (GR circular prefactor) eⁿ to J1738 / J0737−3039 / B1913+16: κ = 0.9955 ± 0.0043 (n=1), 1.00045 ± 0.00048 (n=2); eccentricity-term share of B1913+16 ≤ 0.8 % (n=1) / 0.2 % (n=2) at 2σ. The rescue requires a GR-identical quadrupole term and strips Eq. 32 of empirical content *— conditional on the memory-sourced J0737 ratio; without it the bound is ≤ 29 % (Update 3).* Missing theory before it is a prediction: DU radiative field equation (what propagates, at which speed, which polarisations); energy-loss functional in the zero-energy bookkeeping with its coefficient; eccentricity enhancement g(e) reproducing Peters–Mathews to 0.16 %/0.006 %; a no-double-counting rule; DU-consistent post-Keplerian mass mapping. (B1913 and J0737 inputs partly from memory → OPEN LOOP.)

## C. Falsification matrix

`results/falsification_matrix.csv` (11 rows). Counts: SUPPORTED 1 (expansion law/age, not unique to DU) · NOT DISCRIMINATING 2 (B1913+16 alone; Capotauro, support removed — Liu et al. 2026: μ = 37.6 mas/yr, extragalactic excluded >6σ) · TENSION 2 (bolometric SN form; LLR conditional) · FALSIFIED AS CURRENTLY FORMULATED 2 (implied SN catalog relation; DU-32-ONLY at J1738) · NOT YET PREDICTIVE 5 (angular sizes, CMB, BBN, GW, DU-PLUS-QUADRUPOLE).

The generic antipodal double-image prediction is kept as a conditional DU prediction (model L-B), noting L-B is itself excluded by Pantheon+ (Δχ² +277); a surviving closure postulate would have to be found first.


---

# Update 3 — verification round (2026-09-08): corrections to strength of conclusions

- Sources remain egress-blocked; Eq. 32 and Eq. 36 were not seen rendered. D_eff ∝ z(1+z)^{3/2} is a *text-derived conditional interpretation*; the p = 1.5 falsification is conditional on the externally supplied transformation being complete.
- Statistical audit (`src/pantheon_robustness.py`): q = 2p verified; absolute fit χ²/dof: ΛCDM 0.883, A 0.935, B 3.08, C 0.892 — A is an acceptable absolute fit that is relatively disfavoured; B fails absolutely. Wald deviations (8.3σ, 59σ) are parameter deviations from the best-fit p, not falsification sigmas. The z ≥ 0.4 evaluation is a same-dataset held-out diagnostic; the proper conditional χ² (with train–test cross-covariance) is ΛCDM 229.0, A 258.1, C 263.6, B 3026.9. Bias-correction and selection sensitivity do not change any conclusion (Δχ²(A) 82→110 without the BBC correction; Δχ²(C) 14→17).
- Pulsar tiers (`src/binary_decay_sensitivity.py`): J1738's zero-decay bound rests on S1 (external statement), S2 analyticity (unverified; a non-analytic n = 1/2 factor would void the bound), S3 calibration to B1913+16, S4 unknown prefactor ratio (X ≥ 1830–2400 needed for n = 1; GR-like X = 0.136). The 8.1σ attaches to H_32: "Ṗb(J1738) = 0 within error". **Status downgraded** from FALSIFIED to TENSION (strong, conditional) because Eq. 32's coefficient is not verified. The two-component fit is fully degenerate (corr −1.00); the ≤ 0.8 % bound on the eccentricity term requires the memory-sourced J0737 ratio; without it the bound is ≤ 29 %. κ's 0.05 % precision is an empirical amplitude constraint, not a fine-tuning statement.
- Falsification matrix restructured to 12 single-status rows; counts derived programmatically: SUPPORTED 1, NOT DISCRIMINATING 2, TENSION 3, FALSIFIED AS CURRENTLY FORMULATED 1, NOT YET PREDICTIVE 5.
- Withdrawn: "two published quantitative predictions contradict the data at > 8σ".
