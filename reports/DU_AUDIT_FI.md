# DU-AUDITOINTI — Suntola (2026), Frontiers in Astronomy and Space Sciences, DOI 10.3389/fspas.2026.1827522

Ajopäivä 2026-09-08. Roolit: EINSTEIN-tarkastus (postulaatit, määritelmät, yksiköt, havaitsijan mittaukset), HAWKING-tarkastus (globaali geometria, singulariteetit, kausaliteetti, havaintotestit), riippumaton tilastollinen tarkastaja. Roolit ovat työrooleja.

## 0. Blokkaava rajoite, joka määrää koko auditoinnin statuksen

**Artikkelin tekstiä (HTML, PDF, XML) ei voitu hakea.** Egress-proxy estää `www.frontiersin.org`, `doi.org`, `arxiv.org`, `physicsfoundations.org` sekä peilit (`ar5iv`, `archive.org`, `web.archive.org`). Sekä `curl` että WebFetch palauttivat EGRESS_BLOCKED. Ainoa saavutettu tieto artikkelista on hakukoneen katkelmatasoa (`sources/manifest.csv`). Siksi:

- Yhtään artikkelin numeroitua yhtälöä (8–17, 19, 31/36, 32–33) **ei ole varmennettu lähteestä**. Tehtävänannon suomennoksen rikkoutuneita kaavoja ei rekonstruoitu arvaamalla.
- Kaikki laskut on tehty **tehtävänannossa eksplisiittisesti annetuista muodoista** (c0² = GM''/R4, dR4/dT = c0, kertoimet 0,776 / 0,991 / 1,1049) tai **tunnetuista, riippumattomasti johdettavista määritelmistä** (Hoggin K-korjaus, Peters–Mathews, Pantheon+-likelihood).
- Väitteet, jotka riippuvat artikkelin täsmällisestä muodosta, ovat statukseltaan EHDOLLINEN tai EI TESTATTU. Tämä on kirjattu `claims/claim_register.csv`:hen jokaiselle väitteelle erikseen.

Statusluokat: TOISTETTU / RISTIRIITA / EHDOLLINEN / EI YKSILÖIDY / EI TESTATTU. "TOISTETTU" tarkoittaa, että nimetty lasku toistuu, ei että teoria olisi todistettu.

## 1. Symbolisanasto (käytetty tässä auditoinnissa)

| Symboli | Merkitys | Luokka | Huomio |
|---|---|---|---|
| R4 | 4-pallon säde (koordinaattisuure) | määritelmä | ei paikallisesti mitattava |
| M_Σ | avaruuden kokonaismassa | määritelmä | |
| M'' | "massaekvivalentti" M'' = k·M_Σ | johdanto | k = 0,776 toistuu geodeettisella 1/d-kernelillä |
| c0 | 4-säteen laajenemisnopeus dR4/dT | postulaatti/määritelmä | samastus valon nopeuteen on **lisäoletus** (C03) |
| paikallinen c | valon nopeus paikallisessa kehyksessä | DU-lisäoletus | riippuu paikallisesta gravitaatiotilasta; artikkelin muoto ei luettu |
| T | koordinaattiaika (R4=0 kun T=0) | määritelmä | ei kellon lukema |
| kellon lukema | N = ∫ f dT, f ∝ c0 (oletus A-CLOCK) | lisäoletus | ikä nykykelloissa = 1/H0 |
| lepoenergia | m c0² (DU) | DU-määritelmä | m vakio, c0 muuttuu → energia muuttuu |
| fotonienergia | h f; DU:ssa h:n skaalaus c0:lla ei varmennettu | avoin | |
| z | 1+z = R4_obs/R4_emit (λ ∝ R4) | määritelmä | |
| D (L-A) | valon kulkema polku R4o·z/(1+z) | malli L-A | |
| χ (L-B) | geodeettinen kulma ln(1+z) | malli L-B | antipodi z = e^π−1 = 22,14 |
| D_A, D_L | kulmakoko- ja luminositeettietäisyys | havainnollinen määritelmä | mallista riippuva, ks. §5 |

Paikallisesti mitattuja suureita (kellotaajuudet, atomisekunnit, valosekunnit) ei ole sekoitettu koordinaattisuureisiin: jokainen paikallisen laajenemisen ennuste (§7) on ilmaistu atomikellon tikkeinä tai dimensiottomana suhteena.

## 2. Postulaatit vs. lisäoletukset (A1)

Kahdesta postulaatista (C01 pallogeometria, C02 nollaenergiaehto) **seuraa** vain R4(T):n dynamiikka (C04) ja siitä H(T), c0(T). **Eivät seuraa**, vaan ovat itsenäisiä lisäoletuksia:

1. c0 ≡ valon nopeus (C03). Nollaenergiaehto antaa 4-suuntaisen nopeuden suuruuden; se ei sano mitään sähkömagneettisen säteilyn etenemisnopeudesta.
2. Massan vakioisuus ja lepoenergian m c0² -muoto (C09).
3. Paikalliset gravitaatiolait (1/r-kerneli S³:lla vs. kompaktin avaruuden Poisson-yhtälö; C06).
4. Kellotaajuuksien skaalaus f ∝ c0 (C05, C09).
5. Sidottujen järjestelmien laajeneminen ∝ R4 (C09, C18).
6. Valon etenemisen poikittainen geometria (C10): **osoitettu konstruktiivisesti**, että sama globaali rajoite sallii kaksi eri havaintoennustetta.

## 3. Laajenemishaara, singulariteetti, ikä (A2.1) — TOISTETTU / EHDOLLINEN

Tiedosto: `src/du_symbolic_checks.py` → `results/symbolic_checks.txt`.

- dR4/dT = √(GM''/R4) ⇒ (2/3)R4^{3/2} = √(GM'')·T + C1. Valinta C1 = 0 ⇔ R4(0) = 0. R4 = [(3/2)√(GM'')T]^{2/3}, H = 2/(3T), c0 ∝ T^{-1/3}. Sympy-residuaali 0. **TOISTETTU.**
- R4 → 0: c0 → ∞, H → ∞; molemmat energiatermit divergoivat 1/R4; niiden summa on identtisesti nolla postulaatin nojalla, joten nollaenergia **ei regularisoi** singulariteettia. Supistuvan ja laajenevan haaran liittäminen vaatii nopeushypyn −∞ → +∞: ±-merkki ei ole säännöllinen pomppuratkaisu. **HAWKING-huomio: kausaalinen rakenne R4=0:ssa on määrittelemätön ilman lisäteoriaa.**
- Ikä: koordinaattiaika T0 = 2/(3H0) = 9,3 Gyr (H0=70); nykykelloissa (f ∝ c0) 1/H0 = 14,0 Gyr. Ikävertailut on tehtävä jälkimmäisellä. **EHDOLLINEN** (A-CLOCK-oletus).

## 4. 3-pallon potentiaali ja kertoimet 0,776 / 0,991 (A2.2)

- Tasaisen massan S³:lla, massaosuus (2/π)sin²θ dθ, **geodeettisella** 1/d-kernelillä: k = (2/π)∫₀^π sin²θ/θ dθ = (1/π)[ln 2π + γ − Ci(2π)] = **0,775929**. Kerroin 0,776 toistuu → kernelin tunnistus on ehdokas (artikkelia ei luettu). Jänne-kerneli antaa 0,849, 4D-Newtonin 1/d² tasan 1,000.
- **0,991 ei toistunut** millään testatulla kernelillä (0,776 / 0,849 / 0,903 / 1,000 / 1,273 / 2-pallon 0,926). **EI YKSILÖIDY.**
- 1/θ-kerneli on tasaisen avaruuden Newton-kerneli siirrettynä S³:lle; se **ei ole** S³:n Laplacen Greenin funktio. Tarkistettu: G(θ) = (π−θ)cotθ toteuttaa Δ_{S³}G = 2 (vakio) + δ, eli kompaktin avaruuden Poisson-yhtälön Δφ = 4πG(ρ−ρ̄). Oletettu 1/r-kerneli ja johdettu paikallinen kenttälaki ovat siis **eri asioita**; artikkelin on valittava toinen ja perusteltava. Kaksoislaskenta: c0² = GM''/R4 -muoto on testimassaa kohti (ei ½-tekijää), mikä on sisäisesti johdonmukaista mutta silloin M'' ei ole "avaruuden itseisenergia" vaan potentiaalikertoimen määritelmä.

## 5. Yhtälöt 8–17, kompleksivektori, beta-suhde, PPN (A2.3) — EI TESTATTU

Yhtälöitä ei voitu lukea. Tarkastuslista, joka on ajettava kun teksti on saatavilla: (i) onko E = |E_vektori| vai komponentti; (ii) beta_i (paikallinen) vs beta (kantakehys): jos beta_i = v_i/c_i ja c_i ≠ c0, sarjakehitelmät (1−β²)^{-1/2} eivät ole samassa kertaluvussa; (iii) PPN-vertailu vaatii DU:n metrisen ekvivalentin tai eksplisiittisen operatiivisen mittausmallin (kellot, tutkakaiut). Ilman näitä "vertailu GR:ään" ei ole määritelty.

## 6. Hienorakennevakio, yhtälö 19 (A2.4) — TOISTETTU numeerisesti, alkuperä EI YKSILÖIDY

1/(1,1049·4π³) = **0,007297387644402** (tehtävänannon esitarkistus toistuu). CODATA: 0,0072973525643. Tekstin 0,00729735254 on **mitattu arvo**, ei kaavan arvo. Ero 4,8·10⁻⁶ selittyy **täsmälleen** kertoimen pyöristyksellä: tarkka kerroin olisi 1,104905. Kyse on painovirheestä/pyöristyksestä, ei sellaisenaan teorian kumoutumisesta. Avoin: onko 1,104905 johdettu riippumattomasti (SPIE-katkelman mukaan "Maxwellin yhtälöistä dipolisäteilylle") vai kalibroitu mitattuun α:aan. Lähde estetty → EI YKSILÖIDY.

## 7. Paikallinen laajeneminen (A3) — RISTIRIITA väitteelle "ei havaittava"

`src/local_expansion_and_bh.py`. H0·r: Kuu 2,75 cm/v, Maa–Aurinko 10,7 m/v (H0=70). DU-skaalauksilla (r ∝ R4, c0 ∝ T^{-1/3}, f ∝ c0):

| Havaittava | Ajautumisnopeus |
|---|---|
| Edestakainen valoaika atomisekunteina (LLR) | +1·H0 (= +2,75 cm/v Kuulle) |
| Ratajakso atomisekunteina | +1·H0 |
| Suhde P_orb / valoaika | 0 |
| Doppler (taajuussuhde) | v_r = H0·r läsnä |

Signaali **ei katoa koordinaattimuunnoksessa**; se katoaa vain yhdestä dimensiottomasta suhteesta. Injektointi–palautus (30 v synteettinen LLR-sarja, 2 mm): etäisyyssarja palauttaa vain **summan** vuorovesi + DU (rank-vaje, ei identifioituva). Identifioitavuus palautuu kulmaliikemäärätaseesta: jos koko 3,83 cm/v on vuorovettä, vuorovesi-LOD ≈ 2,1 ms/vs (tässä laskussa; kirjallisuus ~2,3–2,4, muistista → OPEN LOOP); jos vain 1,08 cm/v, ≈ 0,6 ms/vs, jolloin ei-vuorovesiterminen (GIA/ydin) pitäisi olla ≈ +1,1 ms/vs väärällä etumerkillä. Toinen erottelija: Keplerin suhde d ln P : d ln a = 1,5 (vuorovesi) vs 1,0 (DU). Vuorovesikitkaa ei ole oletettu vakioksi 10⁸ vuoden yli; vertailu on 2700 vuoden pimennysaineistoon.

## 8. Mustat aukot (A3) — GR-referenssi TOISTETTU, DU EI TESTATTU

Schwarzschild: ympyräradat L² = Mr²/(r−3M); d²V/dr² = 0 ⇒ ISCO r = 6GM/c² (symbolinen); fotonirata 3GM/c²; horisontti 2GM/c². Kerr ISCO (BPT): a*=0,9 → 2,32 (pro) / 8,72 (retro). Sgr A* ISCO-periodi 32,6 min (Schw.), 9,8 min (a*=0,9 pro). DU:n stabiilisuus vaatii artikkelin efektiivisen potentiaalin; rata- ja pakonopeuden vertailu ei riitä.

## 9. Kattavuusauditointi: CMB, BAO, BBN, rakenteet, GW — EI TESTATTU

Ei saatavilla DU-johdantoja. Täydellinen DU-ennuste vaatisi: (a) paikallisen kenttäyhtälön (§4), (b) häiriöyhtälöt (tiheyskontrasti, nopeus, potentiaali) DU-taustalla, (c) rekombinaatiofysiikan muuttuvalla c0:lla ja h:lla (dimensiottomat suhteet, ks. §10), (d) säteilysiirron, (e) GW-emission ja -etenemisen. Pelkkä H(z):n vaihto CAMB/CLASS-tyyppiseen koodiin **ei ole** DU-ennuste.

## 10. Muuttuvat vakiot dimensiottomina (A2.6) — EI YKSILÖIDY (väite "rakenteet nopeammin")

Γ_grav = √(Gρ) ∝ 1/T ⇒ Γ_grav/H = vakio: gravitaatiokollapsi per e-fold on epookista riippumaton (kuten EdS). Γ_atomic/H ∝ T^{2/3}: atomiprosessit per e-fold olivat varhain **harvempia**. Suurempi varhainen c0 ei siis itsessään nopeuta rakenteiden muodostumista; väite vaatii erillisen paikallisen lain.

## 11. Havaintotestit — tiivistelmä

| Testi | Tiedosto | Status | Tulos |
|---|---|---|---|
| Pantheon+ flat ΛCDM toisto | `src/pantheon_fit.py` | TOISTETTU | Ωm = 0,332 ± 0,018 (julk. 0,334 ± 0,018), χ² = 1402,9 / 1588 |
| DU q=+1 (z√(1+z)) | sama | RISTIRIITA | Δχ² = +82, ΔAIC = +80 (0 muotoparametria) |
| DU q vapaa | sama | EHDOLLINEN (heikko) | q = 1,246 ± 0,030, Δχ² = +14 samalla k |
| DU q=−1 ("bolometrinen") / q=+3 | sama | RISTIRIITA | Δχ² = +5709 / +3491 |
| L-B geodeettinen + Etherington | sama | RISTIRIITA | Δχ² = +277 |
| Ennustetesti z≥0,4 (opetus z<0,4) | sama | — | χ²_test: ΛCDM 222, DU q vapaa 254, DU q=+1 254 |
| K-korjaus poistaa (1+z)²? | `src/kcorrection_audit.py` | RISTIRIITA | K riippumaton D_X:stä; +5log(1+z) on kaksoislaskenta |
| Lähes ympyrärata (J1738+0333) | `src/binary_decay.py` | EHDOLLINEN RISTIRIITA | Ṗb ≠ 0 8,1σ:lla; mikä tahansa e→0-häviävä laki hylätään |
| GR Peters–Mathews toisto | sama | TOISTETTU | B1913+16 0,9998×julk.; J1738 0,99×julk. |
| Capotauro z≈32 | manifest | RISTIRIITA (abstraktitaso) | ominaisliike 37,6 mas/v → ruskea kääpiö (2608.07461, esipainos) |

Huomautus tilastosta: AIC/BIC on laskettu samalle datalle, samalle Gaussin likelihoodille kiinteällä kovarianssilla; k sisältää profiloidun M:n. Ωm ja q ovat kumpikin yksi muotoparametri. H0 ja M ovat täysin degeneroituneet (SN-only), ja ne on profiloitu identtisesti kaikille malleille. Osajoukkojen korrelaatiot on huomioitu käyttämällä koko STAT+SYS-kovarianssin alimatriiseja myös ennustetestissä.

## 12. JWST, galaksien koot, antipodi (A3) — EHDOLLINEN

- Capotauro: elokuun 2026 esipainos (2608.07461) raportoi 132 ± 20 mas liikkeen 3,5 vuodessa → ekstragalaktinen suljettu >6σ → Y-kääpiö ~500 pc. Alkuperäinen z≈32 (2509.01664) oli ehdollinen. Historiallisesti oikea kuvaus: kandidaatti, joka on sittemmin kumottu. **Ei DU-todiste.**
- Kulmakoot: L-B-mallissa linssikerroin 1/sin(ln(1+z)) on z=10:ssä 15× ja z=14:ssä 33× "euklidiseen" L-A:han nähden; antipodi z=22,14, jonka yli pariteetti kääntyy. L-A:ssa kulmakoko → d/R4o (lähes vakio). **Mallit ennustavat eri asiat samasta rajoitteesta** (C10). Koon kehityksen (2410.16354: ~3500 galaksia, 3≤z<9, 7 kaistaa), PSF:n, pintakirkkausvalinnan ja Kron- vs efektiivisen säteen mallinnusta **ei tehty** (aineisto estetty) — EI TESTATTU.
- Antipodaalinen kaksoiskuva: ehdollinen L-B:lle; emissioajat eroavat (χ vs 2π−χ), kohde kehittyy, vastakkaisen kentän syvyys rajoittaa. Kuvan puuttuminen hylkää vain lasketulla havaitsemistodennäköisyydellä — laskua ei tehty.

## 13. Virhetyyppien erottelu

| Kohta | Tyyppi |
|---|---|
| α:n numero | painovirhe/pyöristys (ei teoriavirhe) |
| 0,991 | datan puute (lähde estetty) |
| K-korjaus +5log(1+z) | fysikaalinen ristiriita / kaksoislaskenta määritelmän kanssa |
| 1/θ-kerneli S³:lla | epäselvä määritelmä (kenttälaki vs. kerneli) |
| c0 = valon nopeus, f ∝ c0, r ∝ R4 | lisäoletukset, eivät johdantoja |
| D_A(z) | puuttuva sulkuehto (osoitettu konstruktiolla) |
| yht. 8–17, 32–33 | ei testattu (lähde estetty) |

Jokaisen kohdan lähde, kaava ja tulostiedosto: `claims/claim_register.csv`.

---

# PÄIVITYS 2 (2026-09-08, sama ajo): ulkoisesti toimitettu näyttö ja ratkaisevat testit

**Provenienssi.** Seuraavat lausumat on toimitettu ulkoisesti varmennettuina (käyttäjä, 2026-09-08). Tämä ympäristö **ei** ole hakenut niitä; ne on kirjattu `sources/manifest.csv`:hen tunnuksella "EXTERNALLY SUPPLIED": (1) artikkeli: yhtälö 32 ennustaa hidastumista vain eksentrisille radoille, eksentrisyystekijä on nolla ympyräradalle, kvadrupolivaikutusta ei suljeta pois; (2) PSR J1738+0333: e = (3,4 ± 1,1)·10⁻⁷, Ṗb_int ≈ (−25,9 ± 3,2)·10⁻¹⁵ s/s, GR ≈ −27,7·10⁻¹⁵ (Freire ym. 2012); (3) Capotauro: Liu ym., arXiv:2608.07461 (7.8.2026), ominaisliike 37,6 (+5,5/−5,6) mas/v, ekstragalaktinen suljettu >6σ, Y-kääpiö; (4) artikkelin Pantheon-muunnos: bolometrinen D_L = z√(1+z)·R4, sitten magnitudiin +2,5 log10[(1+z)²]; (5) Hogg ym. 2002: K-korjaus on kaistamuunnos havaitun ja lepokehyksen välillä.

## 14. Ratkaiseva supernovatesti (TASK A) — `src/pantheon_decisive_test.py`

**Johdanto tekstimuunnoksesta.** m_bol = M + 5 log10(R4 z (1+z)^{1/2}/10 pc). Lisäys +2,5 log10[(1+z)²] = +5 log10(1+z) antaa m_cat = M + 5 log10(R4 z (1+z)^{3/2}/10 pc). Ilman muuta piilotermiä luettelomuoto on **täsmälleen** D_eff ∝ z(1+z)^{3/2}, eli p = 1,5 konventiossa D_L ∝ z(1+z)^p (= q = 3 aiemmassa `pantheon_fit.py`-konventiossa D_L ∝ z(1+z)^{q/2}; aiempi q=+1 ⇔ p = 0,5). Tämä on **julkaistun tekstimuunnoksen implikoima relaatio**, ei renderöidyn yhtälön 36 transkriptio.

Sama data (1590 SN, zHD > 0,01), sama STAT+SYS-kovarianssi, sama analyyttinen M-profilointi kuin ΛCDM-toistossa:

| Malli | χ² | Δχ² vs ΛCDM | k | ΔAIC | ΔBIC | test-χ² (z ≥ 0,4; opetus z < 0,4) | keskijäännös test |
|---|---|---|---|---|---|---|---|
| A: DU bolometrinen p = 0,5 | 1485,0 | +82,1 | 1 | +80,1 | +74,7 | 253,7 (vs 222,1) | +0,073 mag |
| **B: DU implikoitu K-korjattu p = 1,5** | **4893,6** | **+3490,6** | 1 | +3488,6 | +3483,3 | 2947 (vs 222) | −0,665 mag |
| C: DU vapaa p = 0,623 ± 0,015 | 1416,9 | +14,0 | 2 | +14,0 | +14,0 | 254,4 | −0,060 mag |
| D: flat ΛCDM Ωm = 0,332 ± 0,018 | 1402,9 | 0 | 2 | 0 | 0 | 222,1 | −0,007 mag |

Jäännökset z:n funktiona (`results/pantheon_decisive_residuals.png`): B:n jäännös kulkee +0,34 mag (z ≈ 0,015) → −1,97 mag (z ≈ 2): tiltti −4,41 mag/dex log10(1+z):ssä, mikä on lähes koko lisätyn 5 log10(1+z) -termin suuruus (M-profilointi kompensoi vain vakion). p = 1,5 on 59σ:n etäisyydellä parhaasta p:stä; sisäkkäinen testi B vs C: Δχ² = 3477 (1 vapausaste), p-arvo numeerisesti 0. A (p = 0,5) on 8σ:n päässä (Δχ² 68,1, p = 1,6·10⁻¹⁶).

**Tulkinta.** Julkaistun tekstimuunnoksen implikoima relaatio on **falsifioitu sellaisena kuin se on muotoiltu**. K-korjauksen määritelmä (§ kcorrection_audit; ulkoisesti vahvistettu Hogg-määritelmä) ei tuota lisätermiä. Bolometrinen muoto ilman lisätermiä on vahvassa jännitteessä (Δχ² +82, ei parametreja). Paras yhden parametrin DU-muoto (p ≈ 0,62) jää Δχ² +14 ΛCDM:stä samalla parametrimäärällä eikä vastaa mitään kokonaislukuista fotonilaskentaa.

## 15. Lähes ympyrärata, tasoitettu testi (TASK B) — `src/binary_decay_tiers.py`

PSR J1738+0333 nostetaan **Tier-1-erottelevaksi havainnoksi** (C14). Erottelu:

**DU-32-ONLY** (julkaistu eksentrisyys-/periastronimekanismi). Tarkkaa yhtälöä 32 ei ole → numeerinen ennuste **UNRESOLVED**. Rigoröösi rajalausuma: julkaistu lausuma kiinnittää F(0) = 0; jos F on analyyttinen e = 0:ssa (kaikki e:stä, √(1−e²):sta ja periastronitermeistä rakennetut suljetun muodon tekijät ovat), F = O(eⁿ), n ≥ 1. Kalibroimalla yhtälö 32 DU:lle edullisimmin B1913+16:n koko hidastumaan: |Ṗb_32(J1738)| ≤ 2,40·10⁻¹² · (e_J/e_B)ⁿ · X, missä X on massa/jakso-prefaktorien suhde. Raja saavuttaa mittausvirheen 3,2·10⁻¹⁵ vain, jos X ≥ 1830 (n = 1, e + 1σ); GR-tyyppinen prefaktori antaa X = 0,14 (J1738:n prefaktori on *pienempi*). Siis DU-32-ONLY ennustaa Ṗb(J1738) = 0 mittausvirheen sisällä; havaittu −25,9 ± 3,2 → 8,1σ nollahypoteesia H_32 vastaan. *(Päivityksessä 2 tämä luokiteltiin FALSIFIED AS CURRENTLY FORMULATED; Päivityksessä 3 status on korjattu TENSION (vahva, ehdollinen), koska analyyttisyys ja prefaktori ovat varmentamattomia lisäoletuksia, ks. §19–20.)*

**DU-PLUS-QUADRUPOLE** (mainittu, ei kvantifioitu). Kaksikomponenttinen fenomenologia Ṗb = κ·Ṗb_GR(e) + β·(GR:n ympyräprefaktori)·eⁿ sovitettuna J1738 (e = 3,4·10⁻⁷), J0737−3039 (0,088), B1913+16 (0,617):

| n | κ | β | eksentrisyystermin osuus B1913+16:sta (2σ yläraja) | χ² (1 dof) |
|---|---|---|---|---|
| 1 | 0,9955 ± 0,0043 | +0,054 ± 0,051 | 0,8 % | 0,27 |
| 2 | 1,00045 ± 0,00048 | −0,067 ± 0,065 | 0,2 % | 0,32 |

Kvadrupolitermin on oltava GR:n kaltainen 0,05–0,4 %:n tarkkuudella, ja yhtälön 32 termi saa selittää enintään 0,2–0,8 % B1913+16:n hidastumisesta. **Pelastus on mahdollinen mutta se vie yhtälöltä 32 sen empiirisen sisällön.** Puuttuva teoria ennen kuin laajennus on ennuste: (i) DU:n kenttäyhtälö aikariippuville lähteille (mikä etenee, millä nopeudella c0 vs paikallinen c, mikä polarisaatiosisältö); (ii) energiahäviöfunktionaali dE/dt nollaenergiakirjanpidossa ja sen kerroin suhteessa G⁴μ²M³/(c⁵a⁵):een; (iii) eksentrisyysvahvistus g(e), jonka on toistettava Peters–Mathewsin f(e) 0,16 %:iin (e = 0,617) ja 0,006 %:iin (e = 0,088); (iv) kaksoislaskennan kielto yhtälön 32 ja kvadrupolitermin välillä; (v) post-Kepler-parametrien (γ, r, s, ω̇) DU-yhteensopiva massakartoitus. (J0737:n ja B1913:n numerot osin muistista → OPEN LOOP; J1738:n arvot ulkoisesti vahvistettu.)

## 16. Falsifiointimatriisi (TASK C) — `results/falsification_matrix.csv`

| TESTI | STATUS | Pelastettavissa uudella oletuksella? | Oletuksen kustannus |
|---|---|---|---|
| Pantheon+ implikoitu luettelorelaatio (p = 1,5) | **FALSIFIED AS CURRENTLY FORMULATED** | vain poistamalla +5 log10(1+z) → p = 0,5 (TENSION) tai uusi vuolaimennuslaki | K-korjaus ei voi antaa termiä; p ≈ 0,62 ei vastaa mekanismia |
| Pantheon+ bolometrinen (p = 0,5) | TENSION (Δχ² +82, 8σ) | vapaa p (Δχ² +14 samalla k) | 1 parametri, ei mekanismia, huonompi ennuste |
| PSR J1738+0333 (Tier-1) | DU-32-ONLY: TENSION (vahva, ehdollinen; korjattu Päivityksessä 3, aiemmin FALSIFIED); DU-PLUS-QUADRUPOLE: NOT YET PREDICTIVE | kvadrupolitermi | κ = 1 ± 0,0005 ja yhtälö 32 ≤ 0,2–0,8 % vain J0737-syötteellä (muistista); ilman ≤ 29 % |
| PSR B1913+16 | NOT DISCRIMINATING (yksin) | — | — |
| Capotauro | NOT DISCRIMINATING (tuki poistettu; Galaktinen Y-kääpiö) | n/a | n/a |
| Kulmakokorelaatio | NOT YET PREDICTIVE (L-A vs L-B; L-B hylätty SN:llä) | sulkupostulaatti | 1 postulaatti, on toteutettava SN ja koot samanaikaisesti |
| LLR / paikallinen laajeneminen | TENSION (ehdollinen LOD-budjetille) | lisäkumoutuminen kelloskaalauksessa | ristiriita ikäargumentin (1/H0) kanssa |
| CMB TT/TE/EE | NOT YET PREDICTIVE | vaatii kenttä- ja häiriöteorian | koko häiriösektori |
| BBN | NOT YET PREDICTIVE | ydinreaktionopeuksien skaalauslaki | uusi dimensioton laki |
| GW-aaltomuodot | NOT YET PREDICTIVE | sama säteilysektori kuin DU-PLUS-QUADRUPOLE | sama |
| Laajenemislaki / ikä 1/H0 | SUPPORTED (heikosti; ei DU:lle ainutlaatuinen) | — | — |

Luokat (johdettu korjatusta matriisista, 12 riviä, yksi status per rivi; J1738 jaettu DU-32-ONLY- ja DU-PLUS-QUADRUPOLE-riveiksi): SUPPORTED 1 · NOT DISCRIMINATING 2 · TENSION 3 · FALSIFIED AS CURRENTLY FORMULATED 1 · NOT YET PREDICTIVE 5. Aiempi versio ilmoitti 11 riviä ja 12 luokkaa, koska J1738-rivi kantoi kahta statusta; tämä on korjattu (`results/falsification_matrix_counts.json`).

**Evidentiaalinen tila (korjattu varmennuskierroksella, ks. Päivitys 3).** Yksi DU:n julkaistusta tekstimuunnoksesta johdettu relaatio (p = 1,5) on falsifioitu sellaisena kuin se on muotoiltu — ehdollisesti sille, että ulkoisesti toimitettu muunnos on täydellinen (renderöityä yhtälöä 36 ei ole nähty). Eksentrisyyteen perustuva hidastumisluokka (DU-32-ONLY) ennustaa eksplisiittisten lisäoletusten (analyyttisyys, prefaktori) alla nollahidastuman J1738+0333:lle, jossa hidastuma on mitattu 8,1σ:lla nollasta; koska yhtälön 32 kerrointa ei ole varmennettu, tämä kirjataan vahvana ehdollisena jännitteenä, ei falsifiointina. Bolometrinen SN-muoto on jännitteessä (Δχ² +82) mutta absoluuttisesti hyväksyttävä sovitus (χ²/dof 0,935). Muut kohdat eivät ole vielä ennustavia. Mikään testi ei tue DU:ta ΛCDM:ää paremmin. Aiempi lause "kaksi julkaistua kvantitatiivista ennustetta ovat ristiriidassa yli 8σ:lla" on **vedetty takaisin** liian vahvana: toinen ennusteista ei ole yksikäsitteinen, ja 8,1σ on havainnon merkitsevyys nollaa vastaan, ei DU-käyrän χ².


---

# PÄIVITYS 3 (2026-09-08): evidenssin varmennus- ja viimeistelykierros

## 17. Lähteiden varmennus — tulos

Alkuperäislähteiden haku yritettiin uudelleen: frontiersin.org, doi.org, arxiv.org ja physicsfoundations.org palauttavat edelleen 000 (egress-esto). **Yhtälöitä 32 ja 36, niiden muuttujamääritelmiä, soveltamisehtoja ja renderöityjä muotoja ei ole varmennettu.** Kaikki EXTERNALLY SUPPLIED -tiedot säilyttävät alkuperäisen provenienssinsa; riippumatonta varmennusta ei saatu (`sources/manifest.csv`, rivi "verification round 3"). Seuraukset: (i) D_eff ∝ z(1+z)^{3/2} on **tekstistä johdettu ehdollinen tulkinta**, ei varmennettu DU-ennuste; (ii) yhtälö 32 ei mahdollista yksikäsitteistä J1738-ennustetta tässä ajossa.

Erottelu: **laskennan toistettavuus** (kaikki skriptit ajettavia, testit 13/13) ≠ **lähteiden varmennus** (artikkeli ja pulsarijulkaisut: ei) ≠ **johtopäätösten pätevyys** (ehdollinen, alla).

## 18. Supernovatestin tilastollinen tarkastus (`src/pantheon_robustness.py`)

- **Parametrisoinnit:** `pantheon_fit.py` käyttää q:ta (D_L ∝ z(1+z)^{q/2}), `pantheon_decisive_test.py` p:tä (D_L ∝ z(1+z)^p); p = q/2, numeerisesti varmennettu. Tehtävänannon "raw q = 0,5 / K-korjattu q = 1,5" vastaa p-konventiota.
- **Vapaat parametrit ja BIC:** n = 1590; k sisältää profiloidun M:n: ΛCDM 2, kiinteä p 1, vapaa p 2.
- **Kolme eri asiaa erotettuna:**

| Malli | χ²/dof (absoluuttinen) | P(χ² ≥ obs) | Δχ² / ΔBIC (suhteellinen) | Wald-poikkeama parhaasta p:stä |
|---|---|---|---|---|
| D ΛCDM | 0,883 | 1,00 | 0 / 0 | — |
| A p = 0,5 | 0,935 | 0,97 | +82 / +75 | 8,3σ |
| B p = 1,5 | 3,08 | 0 | +3491 / +3483 | 59σ |
| C p vapaa | 0,892 | 1,00 | +14 / +14 | — |

  Wald-σ kuvaa kiinteän p:n etäisyyttä parhaasta p:stä (1 dof, sisäkkäinen malli); se **ei** ole "falsifioinnin σ". Absoluuttinen sovitus riippuu julkaistusta kovarianssista, joka sisältää Pantheon+-putkessa kalibroidun intrinsic scatterin. A on absoluuttisesti hyväksyttävä mutta suhteellisesti selvästi heikompi; B hylätään myös absoluuttisesti.
- **Held-out z ≥ 0,4** on **saman aineiston osajoukkodiagnostiikka**, ei riippumaton ennustetesti: systematiikat ovat yhteisiä ja opetus–testi-ristikovarianssi on nollasta poikkeava. Oikea ehdollinen Gaussin ennuste (ristikovarianssi mukana): ΛCDM 229,0 · A 258,1 · C 263,6 · B 3026,9 (aiemmin lohkokohtaisesti 222 · 254 · 254 · 2947). Järjestys ei muutu. Jako z = 0,4 valittiin kerran etukäteen.
- **Vertailukelpoisuus:** m_b_corr sisältää BBC-bias-korjauksen, joka on laskettu referenssikosmologialla (keskiarvo −0,011 mag, vaihteluväli −0,54…+0,37). Rajaava herkkyysajo ilman korjausta (ei "parempi data"): Δχ²(A) 82 → 110, Δχ²(B) 3491 → 3329, Δχ²(C) 14 → 17. Valinta zmin = 0,023: A +81, B +3284; ilman Cepheid-kalibraattoreita: A +81, B +3490. **Johtopäätökset eivät riipu näistä.** Havaintosuureen (K-korjattu rest-frame B -magnitudi, SALT2-standardoitu) vertaaminen mallien D_L:iin on perusteltua, kun kukin malli antaa oman bolometrisen laimennuksensa D_L:ssä (§14, K-korjausauditointi).
- Aiempaa laskentaa ei muutettu: konkreettista virhettä ei löytynyt; held-out-tulos nimettiin uudelleen ja täydennettiin ehdollisella muodolla.

## 19. Pulsaritestin varmennus (`src/binary_decay_sensitivity.py`)

**Syötteiden provenienssi:** J1738: e, Ṗb_int, Ṗb_GR = EXT; massat, kinemaattinen korjaus = abstraktitaso; Pb = muistista. B1913+16: massat ja suhde 0,9983 ± 0,0016 abstraktitaso; Pb, e, Ṗb muistista. J0737: e = 0,088 ja "0,013 %" abstraktitaso; suhde 0,999963(63) ja muut muistista. Alkuperäisjulkaisuja ei saatu.

**Teoriariippuvuus:** B1913+16:n ja J0737:n massat johdetaan GR:n post-Kepler-parametreista (ω̇, γ) → niiden Ṗb-testi on GR:n itsekonsistenssitesti, ja DU-testissä ne edellyttäisivät DU:n omat PK-kaavat. J1738:n massat tulevat WD-spektroskopiasta ja massasuhteesta → **vähiten teoriariippuva**, mikä tukee sen Tier-1-asemaa. Kinemaattiset korjaukset (Shklovskii, Galaktinen kiihtyvyys) ovat klassisia ja etäisyysriippuvia; J1738:lle vähennetty parallaksilla (abstraktitaso).

**J1738-raja vaiheittain:** S1 (EXT) F(0) = 0 takaa vain raja-arvon lim Ṗb_32 → 0. S2 analyyttisyys (**lisäoletus**) antaa häviämisnopeuden eⁿ, n ≥ 1. S3 kalibrointi B1913:n koko hidastumaan (**lisäoletus**, DU:lle edullinen). S4 prefaktorisuhde X (**tuntematon**). Tulos: n = 1 vaatii X ≥ 2400 (e = 3,4·10⁻⁷) tai X ≥ 1830 (e + 1σ); n = 2 vaatii X ≥ 3·10⁹; GR-tyyppinen skaalaus antaa X = 0,136. **Jos F ei ole analyyttinen (n = 1/2), raja vaatii vain X ≥ 1,8 eikä ole robusti** — siksi S2 on kriittinen ja varmentamaton. Kolme eri väitettä: tarkka ennuste = UNRESOLVED; ehdollinen yläraja = edellä; havainnollistava nollaennuste = H_32: "Ṗb(J1738) = 0 virheen sisällä", jota vastaan havainto on 8,1σ. **8,1σ sitoutuu H_32:een**, ei DU-käyrän χ²-testiin.

**DU-PLUS-QUADRUPOLE:** κ ja β ovat lähes täysin degeneroituneet (korrelaatio −1,00). κ = 1,00045 ± 0,00048 ja eksentrisyystermi ≤ 0,2–0,8 % B1913:sta **vain J0737-suhteella** (muistista; tarkkuustaso 0,013 % abstraktitason vahvistama). Ilman J0737:ää: κ = 0,935 ± 0,116 ja eksentrisyystermi ≤ 29 % (dof 0). κ:n 0,05 %:n tarkkuus on **empiirinen rajoite lisätermin amplitudille**, ei teoreettinen hienosäätövaatimus. Aineisto kertoo alkuperäisestä DU-mekanismista: jos GR-tyyppinen termi on läsnä, eksentrisyystermi on enintään promilleluokkaa (J0737 mukana) tai kymmenesosaluokkaa (ilman) havaituista hidastumista. Aiempi muotoilu "pelastus vie yhtälöltä 32 empiirisen sisällön" **lievennetään**: se pätee J0737-syötteen ehdolla.

## 20. Korjatut ja lievennetyt väitteet

| Aiempi | Korjattu |
|---|---|
| "Kaksi julkaistua kvantitatiivista ennustetta ristiriidassa >8σ" | Vedetty takaisin. Yksi tekstistä johdettu relaatio (p = 1,5) falsifioitu ehdollisesti provenienssille; DU-32-ONLY on vahva ehdollinen jännite (H_32 vs. 8,1σ havainto), ei falsifiointi ennen yhtälön 32 varmennusta. |
| J1738 DU-32-ONLY: FALSIFIED AS CURRENTLY FORMULATED | TENSION (vahva, ehdollinen); puuttuva kerroin ei yksin ole falsifiointi. |
| "Yhtälö 32 ≤ 0,2–0,8 % B1913:sta" | Pätee vain muistista otetulla J0737-suhteella; ilman sitä ≤ 29 %. |
| "Ennustetesti z ≥ 0,4" | Saman aineiston osajoukkodiagnostiikka; ehdollinen χ² ristikovarianssilla lisätty. |
| Falsifiointimatriisi 11 riviä / 12 luokkaa | 12 riviä, yksi status per rivi; luvut johdettu koneellisesti. |
| "p = 0,5 on 8σ" | Wald-poikkeama parhaasta p:stä 8,3σ; absoluuttinen sovitus hyväksyttävä (χ²/dof 0,935). |
