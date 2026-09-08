# JOHDON TIIVISTELMÄ — DU-tutkimus ja Bilfinger Performance Outsourcing -prototyyppi

Ajo 2026-09-08. Koodi, testit ja tulokset: `src/`, `tests/`, `results/`. Väiterekisteri: `claims/claim_register.csv` (24 väitettä). Avoimet asiat: `reports/OPEN_LOOPS.csv` (17).

## Ydinviesti

1. **Artikkelin tekstiä ei saatu** (frontiersin.org, arxiv.org, physicsfoundations.org egress-estetty). Kaikki artikkelin yhtälöihin sidotut väitteet ovat EHDOLLISIA tai EI TESTATTU. Mikään tässä ei perustu hakukatkelmiin muuten kuin nimettynä.
2. **Mikä laskettiin ja toistui:** laajenemishaara R4 ∝ T^{2/3}, H = 2/(3T), c0 ∝ T^{-1/3}; ikä 1/H0 nykykelloissa (ehdollinen kello-oletukselle); kerroin 0,776 geodeettisena 1/d-integraalina; α = 1/(1,1049·4π³) = 0,0072973876 ja sen 4,8·10⁻⁶ ero CODATAan täsmälleen kertoimen pyöristyksestä; Pantheon+ flat ΛCDM Ωm = 0,332 ± 0,018 (julkaistu 0,334 ± 0,018); GR:n Peters–Mathews toistaa B1913+16:n ja J1738+0333:n julkaistut arvot.
3. **Mikä oli ristiriidassa:** (a) DU-magnitudimuoto z√(1+z) häviää ΛCDM:lle Δχ² = +82 (ΔAIC +80) Pantheon+-datalla täydellä kovarianssilla; vapaa eksponentti q = 1,25 ± 0,03 jää Δχ² = +14 jälkeen samalla parametrimäärällä ja ennustaa huonommin (χ²_test 254 vs 222). Väite "vähintään yhtä hyvä kuin ΛCDM" ei toistu millään kokeillulla muodolla. (b) K-korjaus **ei** poista kosmologista (1+z)²-laimennusta; +5 log10(1+z) on kaksoislaskenta määritelmän suhteen. (c) Capotauro on esipainoksen 2608.07461 mukaan ruskea kääpiö (ominaisliike 37,6 mas/v); ei DU-todiste. (d) Väite paikallisen laajenemisen katoamisesta koordinaattimuunnoksessa: DU-skaalauksilla LLR-etäisyys ja ratajakso atomisekunteina ajautuvat +H0·r; vain suhde on invariantti.
4. **Uusi rajattu tulos:** globaali nollaenergiarajoite + c = dR4/dT **ei määrää** kulmakokoetäisyyttä: kaksi eksplisiittistä mallia (polun pituus vs. geodeettinen kulma) eroavat 36 % z=1:ssä; geodeettinen malli tuo antipodin z = 22,1:een ja hylätään Pantheon+:lla (Δχ² +277). Puuttuva sulkuehto on nimetty. Kaksi täydennysehdokasta kokeiltu ja molemmat epäsuotuisat.
5. **Ehdollinen ristiriita:** jos artikkelin yhtälö 32 häviää e → 0, PSR J1738+0333 (Ṗb = −25,9 ± 3,2 fs/s, 8,1σ) hylkää sen yksin.
6. **Epäonnistunut yritys:** kertoimen 0,991 alkuperää ei löydetty kuudesta kernelivariantista.

## Bilfinger

- Prototyyppi on toimiva, synteettinen tilamalli (5 tilaa, 6 ohjausta, Monte Carlo 2000, 9 stressitestiä, 3 politiikkaa). Se **ei ole ROI-laskelma**.
- Tulos: elinkaarimalli (P2) +2,6 M€ odotusarvo, mutta p10 = −3,5 M€ → ennakkoon määritelty robustisuuskriteeri **ei täyty**; siirtymäviive kääntää sen negatiiviseksi.
- Tärkein löydös: kiinteä maksu ilman käytettävyys-/integrity-alarajaa **palkitsee lykkäämisestä** (P1: Bilfinger +6,1 M€, asiakas −29,5 M€). Sopimusrakenne on korjattava ennen pilottia.
- **Pilotoitavaa:** hallittavuusmatriisi jokaiselle tuloslupaukselle; P10-portti Feasibilityssä; integrity-velkaindikaattori sitovana rajana; KPI-ristiintarkistus tuotantolaskureihin; handback-kunto sanktioituna.
- **Ei siirrettävää:** fysiikan analogia, synteettiset numerot, käyrien silmämääräinen vertailu.

## Seuraava testi, eniten tietoa per kustannus

Artikkelin PDF käsin `sources/`-hakemistoon (tai egress-lupa). Sen jälkeen kaksi tunnin töitä: (1) yhtälöt 31/36 sijoitetaan q-perheeseen tai toteutetaan sellaisenaan ja `pantheon_fit.py` ajetaan uudelleen (7 s); (2) yhtälön 32 e → 0 -raja luetaan ja väite C14 suljetaan. Molemmat ovat erottelevia eivätkä vaadi uutta dataa.

## Mitä ei väitetä

DU:ta, ΛCDM:ää tai Bilfingerin business casea ei ole ratkaistu yksittäisellä testillä. ΛCDM:n Ωm-sovitus on toistettu, ei suojattu: avoin ΛCDM antaa Ωm=0,295, ΩΛ=0,613 ilman merkitsevää parannusta (Δχ² −0,5 yhdellä lisäparametrilla).
