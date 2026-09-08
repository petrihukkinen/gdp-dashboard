# JOHDON TIIVISTELMÄ — DU-tutkimus ja Bilfinger Performance Outsourcing (päivitetty ulkoisesti toimitetulla näytöllä)

Ajo 2026-09-08. Koodi, testit, tulokset: `src/`, `tests/`, `results/`. Väiterekisteri 25 väitettä, falsifiointimatriisi 11 riviä, avoimet asiat 19.

## Kysymys 1: Mikä on DU:n evidentiaalinen tila varmennuskierroksen jälkeen?

**Ydinviesti (korjattu).** Yksi DU:n julkaistusta tekstimuunnoksesta johdettu supernovarelaatio (p = 1,5) on falsifioitu sellaisena kuin se on muotoiltu, ehdollisesti sille, että ulkoisesti toimitettu muunnos on täydellinen. Eksentrisyyteen perustuva hidastumisluokka on vahvassa ehdollisessa jännitteessä J1738+0333:n kanssa, mutta ilman varmennettua yhtälöä 32 sitä ei julisteta falsifioiduksi. Muut DU-kohdat eivät ole vielä ennustavia. Mikään testi ei tue DU:ta ΛCDM:ää paremmin. Aiempi lause "kaksi ennustetta ristiriidassa yli 8σ:lla" on vedetty takaisin liian vahvana.

| Testi | Tulos | Status |
|---|---|---|
| Pantheon+, tekstimuunnoksen implikoima p = 1,5 | Δχ² = +3491, χ²/dof 3,08, tiltti −4,4 mag/dex | **FALSIFIED AS CURRENTLY FORMULATED** (ehdollinen provenienssille) |
| Pantheon+, bolometrinen p = 0,5 | Δχ² = +82, χ²/dof 0,935 (absoluuttisesti hyväksyttävä), Wald 8,3σ parhaasta p:stä | TENSION |
| Pantheon+, vapaa p = 0,623 ± 0,015 | Δχ² = +14 samalla k; held-out-diagnostiikka heikompi | ei pelasta |
| J1738+0333, DU-32-ONLY | H_32 (nolla virheen sisällä) vs. havaittu −25,9 ± 3,2 fs/s: 8,1σ; ehdollinen analyyttisyydelle ja prefaktorille | TENSION (vahva, ehdollinen) |
| DU-PLUS-QUADRUPOLE | κ = 1,0005 ± 0,0005 ja yht. 32 ≤ 0,8 % **vain** muistista otetulla J0737-suhteella; ilman ≤ 29 % | NOT YET PREDICTIVE |
| Capotauro | Liu ym. 2026 (EXT): Y-kääpiö, ekstragalaktinen suljettu >6σ | tuki poistettu |
| Kulmakoot / antipodi | postulaatit eivät määrää D_A(z); L-B hylätty SN:llä | NOT YET PREDICTIVE |
| LLR / paikallinen laajeneminen | signaali ei katoa; erottelu LOD-taseesta (kirjallisuusarvot muistista) | TENSION (ehdollinen) |
| CMB, BBN, GW | ei DU-johdantoja | NOT YET PREDICTIVE |
| Laajenemislaki, ikä 1/H0 | suuruusluokka oikea, ei ainutlaatuinen | SUPPORTED (heikosti) |

Luokkamäärät johdettu matriisista (12 riviä): SUPPORTED 1 · NOT DISCRIMINATING 2 · TENSION 3 · FALSIFIED 1 · NOT YET PREDICTIVE 5.

**Varmennuksen tila.** Alkuperäislähteet (artikkeli, pulsarijulkaisut) ovat edelleen saavuttamattomia; yhtälöitä 32 ja 36 ei ole nähty renderöityinä. EXTERNALLY SUPPLIED -tiedot säilyttävät provenienssinsa ilman riippumatonta varmennusta. Laskenta on toistettavaa (testit 13/13, ristiintarkistus), lähteet eivät ole varmennettuja, johtopäätökset ovat ehdollisia edellä kuvatulla tavalla.

**Kriittiset avoimet riippuvuudet:** (1) renderöity yhtälö 36 — onko muita termejä; (2) yhtälön 32 analyyttisyys ja prefaktori — TENSION → FALSIFIED vaatii nämä; (3) J0737:n Ṗb-suhde alkuperäislähteestä — DU-PLUS-QUADRUPOLE-raja riippuu siitä.

## Kysymys 2: Mitkä konkreettiset suunnitteluperiaatteet parantavat Bilfinger Performance Outsourcing 2030:a?

Synteettisiä rahalukuja ei käytetä näyttönä. Kaikki alla oleva on **ehdotus**, ei empiirisesti validoitu liiketoimintamalli eikä Bilfingerin hyväksymä sääntö; integrity-/HSEQ-hyväksynnän omistajuus on roolitason oletus, jota ei ole vahvistettu, ja BTS:n korvaamista ei oleteta. Menetelmästä siirtyy ehdotettu **Performance Outsourcing Decision Engine**: 12 pakollista kerrosta (järjestelmäraja, baseline/vastatilanne, hallittavuusmatriisi, HSEQ/integrity-red lines, siirtymävalmius, arvonluontimalli, P10, hyödyn attribuutio, KPI-anti-gaming, arvonjako, jatkuva validointi, uusinta/exit), kullakin INPUT / LASKENTA / OMISTAJAROOLI / NÄYTTÖ / GREEN–AMBER–RED / VIKATILA / TIETOTARVE / BTS-KYVYKKYYS, kartoitettuna Qualification → Feasibility → Due Diligence → Contracting → Transition → Operate & Improve → Renewal/Exit (`results/po_decision_engine_layers.csv`, `po_gate_mapping.csv`).

Periaatteet, jotka nousivat suoraan tutkimusmenetelmästä:

1. **Tuloslupaus = väite, jolla on hylkäysehto.** Sama rakenne kuin väiterekisterissä: oletukset, ajurit, mittari, testi, status.
2. **P10-portti, ei P50-päätös (ehdotettu riskipolitiikka, ei yleispätevä sääntö).** Prototyypissä P50 oli positiivinen ja P10 negatiivinen; ilman P10-kriteeriä tämä olisi näyttänyt vihreältä.
3. **Hallittavuus on sulkuehto.** Globaali arvolupaus ei määrää paikallista ohjausta, kuten DU:n globaali tase ei määrää havaintoa. Vastuu ilman päätösvaltaa on RED.
4. **Mittaus ≠ tulkinta.** Jokaiselle tulos-KPI:lle kaksi riippumatonta lähdettä, audit trail, ajautumatesti. Raportoitu käytettävyys ei ole todennettu käytettävyys.
5. **Kannustintesti lykkäyspolitiikalla** ennen allekirjoitusta: sopimusrakenne, jossa toimittaja hyötyy lykkäyksestä (kiinteä maksu ≥ toimituskustannus ilman integrity-/backlog-alarajaa), on RED riippumatta P50:stä.
6. **Ei kaksoislaskentaa, oikea suure.** Kate ei myyntihinta; kysyntärajoite; jäännösmenetys kerran; maksu jakaa arvoa eikä luo sitä (identiteetti tarkistetaan).
7. **Integrity-red lines sitovina rajoitteina**, eivät optimoinnin termeinä; ihmisen HSEQ-/oikeudellinen hyväksyntä.
8. **Attribuutio vain todennetuin oletuksin** (rinnakkaistrendi pre-periodilla), muuten kuvaileva.
9. **BTS-päätös vasta vaatimus–kyvykkyys–puute-vertailun jälkeen.** Ratkaisevat rivit: audit trail & kaksilähteinen täsmäytys, integrity-seuranta, master data. Korvaamista ei oleteta.
10. **Avoimet asiat näkyviin** WHAT/OWNER/STATUS/NEXT/DUE/DEPENDENCY-muodossa; tuntematon omistaja merkitään tuntemattomaksi.

**Pilotoitavaa heti:** hallittavuusmatriisi yhdelle olemassa olevalle kohteelle; baseline-kohinan σ vs. odotettu vaikutus; kannustintesti nykyisille sopimusmalleille. Nämä eivät vaadi uutta järjestelmää eivätkä luottamuksellista dataa ulkoisille malleille.
