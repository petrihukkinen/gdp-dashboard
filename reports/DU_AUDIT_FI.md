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
