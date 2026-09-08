# BILFINGER PERFORMANCE OUTSOURCING — itsenäisesti testattava mallin prototyyppi (Vaihe B)

Ajopäivä 2026-09-08. Konteksti: Petrin kehitystyö, ei väite Bilfingerillä hyväksytystä organisaatiomallista. **Kaikki numerot ovat synteettisiä** (`src/bilfinger_prototype.py`, PARAMS-lohko); yritys-, asiakas-, henkilöstö- tai sopimustietoa ei ole käytetty. Tämä on menetelmällinen siirto DU-auditoinnista: järjestelmärajat, oletusten jäljitettävyys, tilamalli, mittauksen ja tulkinnan erottaminen, epävarmuus, ennakkoon määritellyt hylkäyskriteerit. Yritys ei ole nollaenergiajärjestelmä eikä kumppanuus nollasummapeli; DU:n oikeellisuus tai hylkääminen ei vaikuta tähän.

## B1. Mitattava järjestelmä ja vastuu

**Järjestelmäraja:** asiakkaan tuotantolaitoksen kunnossapito- ja käyttövarmuusjärjestelmä (laitteet, työjono, osaaminen, data) + Bilfingerin toimitusorganisaatio. **Ulkopuolella:** markkinakysyntä ja hinnat, raaka-aine, viranomaisvaatimusten muutokset, asiakkaan investointipäätökset (rajapinta: ehdotus → päätös viiveellä), työmarkkina.

Kolme toimintamallia erotetaan eksplisiittisesti; pelkkä pitkä sopimus, henkilöstösiirto tai kiinteä hinta ei tee mallista tulosvastuullista:

| Malli | Bilfinger vastaa | Näyttö vaaditaan |
|---|---|---|
| Työn myynti | tunnit, laatu | — |
| Hallittu palvelu | prosessi, SLA | prosessimittarit |
| **Suorituskykyvastuu** | sovittu tulos (käyttövarmuus, elinkaarikustannus) | **hallittavuusmatriisi** jokaiselle tuloslupaukselle |

**Hallittavuusmatriisi** (täytettävä Feasibility-portissa jokaiselle lupaukselle): Bilfinger ohjaa (PM-intensiteetti, työjonon purku, osaaminen, integrity-työ, data) / yhteisvastuu (kriittisyysluokitus, seisokkisuunnittelu) / asiakas päättää (capex, ajotapa, kuormitus) / ulkoinen (kysyntä, olosuhteet). **Hylkäysehto:** lupaus, jonka ajureista yli puolet on asiakkaan tai ulkoisen hallinnassa, ei saa olla tulosvastuullinen ilman vastaavaa päätösvaltaa, resurssia ja tiedonsaantia. Prototyypissä tämä näkyy suoraan: `capex_delay`-stressissä (asiakas viivyttää 24 kk) P2:n arvo ei muutu olennaisesti vain siksi, että malli ei anna Bilfingerin vastata capexista.

Asset Management & Lifecycle on globaali ydindimensio (tilamuuttujat h, b, s). Asset Integrity & Process Safety on mukana latenttina integrity-velkana d ja tapahtumaprosessina: front-endissä riskiperusteinen screening (portti Feasibility), toimituksessa tarpeen mukainen AIM-syvyys (P2:n `integ`-ohjaus skaalautuu d:n mukaan). Turvallisuus, lakisääteiset velvoitteet ja integrity-red lines ovat **sitovia rajoitteita**, eivät optimoinnin termejä: malli ei tee HSEQ- tai oikeudellisia hyväksyntöjä.

## B2. Arvonluonnin ja arvonjaon erillinen laskenta

Ehdotettu laskentakehikko (ei luonnonlaki):

YHTEINEN LISÄARVO = PV(Δ tuotannon lisäkate) + PV(Δ resurssisäästö) − PV(siirtymä- ja kehityskustannus) − PV(Δ odotettu jäännösmenetys)

- Yksiköt EUR, kuukausiaskel, 60 kk, diskonttaus 8 %/v (kk-muunnos). Etumerkit: säästö positiivinen, kustannus negatiivinen. Riskit: Monte Carlo (2000 polkua), θ-parametrit log-normaalisti ±25 %, yhteiset satunnaisluvut kaikille politiikoille.
- **Kysyntärajoite:** myyty tuotanto = min(käytettävyys, kysyntäosuus 0,93). Käytettävyys kysynnän yli ei tuota mitään; menetystä ei lasketa myyntihinnalla vaan toteutuvalla lisäkatteella (6 000 €/h synteettinen).
- **Ei kaksoislaskentaa:** käyttövarmuushyöty lasketaan yhden kerran katteen kautta; tapahtumamenetys (1,5 M€/tapahtuma) sisältää vain suorat kulut, ei uudelleen menetettyä katetta (se on jo käytettävyyden pudotuksessa 12 pp tapahtumakuukautena).
- **Palvelumaksu jakaa, ei luo:** identiteetti asiakas_inkr + Bilfinger_netto = yhteinen lisäarvo tarkistetaan koodissa (tarkka, `checks`).

Kassavirrat erikseen: Asiakas = kate − tapahtumamenetys − capex − (oma opex | palvelumaksu). Bilfinger = palvelumaksu − toimitusopex − siirtymäkustannus. Maksu = kiinteä 0,30 M€/kk (≈ asiakkaan as-is-opex) + 35 % **todennetusta** kateparannuksesta suhteessa vertailutilaan.

## B3. Dynaaminen prototyyppi

x(t+1) = f(x(t), u(t), w(t), θ) + prosessikohina; y(t) = g(x(t)) + mittausvirhe.

| Tila x | Ohjaus u | Ulkoinen w | θ (epävarma) |
|---|---|---|---|
| h asset health (0–1) | pm ennakoiva ylläpito | kuorma (N(1, 0,08)) | degradaationopeus |
| b riskipainotettu backlog | corr korjauskapasiteetti | olosuhdeshokit (exp) | PM-teho |
| s kriittinen osaaminen | train | poistuma-shokki | tapahtumaintensiteetti λ |
| d latentti integrity-velka | integ | kysyntäosuus | vikojen saapumisnopeus |
| q datan laatu | capex-ehdotus (asiakas päättää viiveellä 12 kk), data | asiakkaan capex-viive | |

Havaintomalli: käytettävyys mitataan kohinalla (σ = 0,5 pp, pienenee datan laadun myötä); KPI-pelaaminen mallinnetaan raportoidun ja todellisen käytettävyyden erona. Selittävä muuttuja (h, b, s, d) ja mitattu seuraus (käytettävyys, kustannus, tapahtumat, kate) on erotettu; taulukko `results/bilfinger_kpi_observation_model.csv`.

Kolme skenaariota samalla lähtötilalla (h=0,75, b=1,5, s=0,70, d=0,5) ja samoilla shokeilla: **P0** as-is (kiinteä mix, reaktiivinen backlogiin), **P1** lyhyen aikavälin kustannus (budjettikatto, lykkäys kun backlog kasvaa, ei koulutusta, sopimuksen lopussa lisälykkäys), **P2** elinkaarisuorituskyky (riskiperusteinen PM, integrity-työ, osaaminen, aikaisempi capex-ehdotus, data; siirtymäkustannus 1,8 M€ / 6 kk tehokkuudella 0,7). Vertailijaa P0 ei ole rakennettu huonoksi: se on lähes stationaarinen (käytettävyys 0,867, h 0,75→0,70).

### Tulokset (synteettinen, PV 60 kk, M€; keskiarvo [p10])

| Stressi | P1 yhteinen | P2 yhteinen | P2 asiakas | P2 Bilfinger | P1 Bilfinger | P2 käytett. | P(tapahtuma) P0/P1/P2 |
|---|---|---|---|---|---|---|---|
| none | −23,5 [−30,0] | **+2,6 [−3,5]** | +1,6 | +1,0 | **+6,1** | 0,906 | 0,16/0,57/0,04 |
| latent_debt | −26,5 | +3,3 [−3,0] | +2,2 | +1,0 | +6,1 | 0,906 | 0,47/0,91/0,13 |
| capex_delay | −23,9 | +2,6 [−3,5] | +1,5 | +1,1 | +6,1 | 0,905 | 0,16/0,59/0,04 |
| skills_shortage | −20,1 | +3,5 [−1,8] | +3,4 | +0,1 | +6,1 | 0,891 | 0,21/0,61/0,05 |
| poor_data | −23,5 | +2,6 [−3,5] | +1,6 | +1,0 | +6,1 | 0,906 | 0,16/0,57/0,04 |
| demand_shock | −17,9 | +0,7 [−3,7] | −0,3 | +1,0 | +6,1 | 0,906 | 0,16/0,57/0,04 |
| transition_delay | −26,8 | **−0,9 [−5,8]** | −0,2 | −0,6 | +6,2 | 0,897 | 0,16/0,62/0,05 |
| kpi_gaming | −23,5 | +2,6 | +1,6 | +1,0 | +6,1 | 0,906 | 0,16/0,57/0,04 |
| end_of_contract | −23,4 | +2,6 | +1,6 | +1,0 | +6,4 | 0,906 | 0,16/0,57/0,04 |

Lähde: `results/bilfinger_mc_summary.csv`; kuva `results/bilfinger_mean_paths.png`.

### Ennakkoon määritellyt tarkistukset (synteettinen ajo)

| Tarkistus | Tulos |
|---|---|
| P1 näyttää säästön ensimmäisenä 12 kk (1,79 vs 2,76 M€) | OK — "säästö" syntyy lykkäyksestä |
| P1 päättyy suurempaan latenttiin velkaan (4,2 vs 0,3) | OK — piilevä integrity-velka realisoituu tapahtumina (57 % vs 16 %) |
| P2 yhteinen lisäarvo keskiarvo > 0 | OK (+2,6 M€) |
| **P2 yhteinen lisäarvo p10 > 0** | **FAIL** (−3,5 M€; P(negatiivinen) = 29 %) |
| Maksu vain jakaa: asiakas + Bilfinger = yhteinen | OK (tarkka identiteetti) |
| KPI-pelaaminen havaittavissa (raportoitu − tosi > 3σ) | OK — ristiintarkistus tuotantolaskureihin |

**Tulkinta:** näillä synteettisillä parametreilla elinkaarimalli on odotusarvoltaan positiivinen mutta **ei robusti**; sen arvo kääntyy negatiiviseksi siirtymäviiveellä ja kysyntäshokissa asiakkaan osuus menee nollaan. Tämä ei ole Bilfingerin ROI vaan osoitus siitä, että päätös vaatii kohdekohtaisen kalibroinnin ja että p10-kriteeri on oikea portin ehto.

### Kannustinlöydös (tärkein)

Kiinteä maksu + kustannusleikkaus (P1) tuottaa **Bilfingerille +6,1 M€ ja asiakkaalle −29,5 M€**. Gain-share ei aktivoidu, koska parannusta ei ole, mutta kiinteä maksu kattaa alennetun toimitusopexin. Sopimusrakenne, jossa kiinteä osa ylittää toimituskustannuksen ilman alarajaa käytettävyydelle ja integrity-velalle, **palkitsee lykkäämisestä**. Sopimuksen lopussa (end_of_contract) P1:n lykkäys kasvaa: Bilfinger +6,4. Korjaus: (i) kiinteä osa ≤ todennettu toimituskustannus, (ii) integrity-velka- ja backlog-ikäindikaattori sitovana rajana, (iii) handback-kunto mitattuna ja sanktioituna, (iv) gain-share vain todennetusta, ristiintarkistetusta katteesta.

## B4. Kytkentä E2E-portteihin

Portit, miniminäyttö, omistaja-/hyväksyjäroolit (ei nimiä eikä nykyisiä valtuuksia), hylkäysehto ja seuraava toimenpide: `results/bilfinger_gates.csv`. Ydin:

- **Feasibility ei ole vihreä lomakkeen perusteella.** Vaaditaan: normalisoitu baseline (≥24 kk), hallittavuusmatriisi täytettynä, datan laatupisteytys, capability-näyttö, siirtymävalmius, arvomalli P10/P50/P90, integrity-screening (refining/oil & gas/chemicals), ja ihmisen tekemä riskihyväksyntä. Hylkäys: P10 < 0; baseline-kohina > odotettu vaikutus; lupaus, jota Bilfinger ei hallitse.
- **Operate & Improve:** kaksi peräkkäistä kvartaalia alle P10-arvopolun tai KPI-ajautuma suhteessa tuotantolaskureihin → korjaussuunnitelma / re-baselining / exit-triggeri.

### Pilotti

Rajattu kohde (yksi yksikkö/alue), historiadata ≥ 24 kk (käytettävyys, työmääräykset kriittisyydellä, tarkastusten myöhästymät, opex, tapahtumat, tuotantolaskurit). Baseline-normalisointi kuormaan ja tuotemixiin. Vertailuasetelma: rinnakkainen vertailuyksikkö samassa laitoksessa (jos on) tai keskeytetty aikasarja; **kausaalinen vaikutusarvio (DiD / synteettinen kontrolli) vain jos rinnakkaistrendioletus todennetaan pre-periodilla**. Seuranta ennen–jälkeen 12 + 12 kk. Hyväksymiskriteerit ennakkoon: käytettävyyden nousu > 2× baseline-kohina, backlogin ikäprofiili paranee, integrity-myöhästymät nollaan, opex ≤ suunnitelma, ei red-line-rikkomuksia. **Mallia muutetaan tai hylätään, jos:** parannus ei erotu kohinasta 12 kk:ssa; parannus näkyy vain raportoidussa KPI:ssä (ei tuotantolaskureissa); integrity-indikaattori heikkenee vaikka käytettävyys paranee; asiakas-/Bilfinger-kassavirtojen summa ei vastaa yhteistä arvoa.

### BTS-vaihtoehto (Improve / + Intelligence Layer / Replace)

Ei valintaa ilman aineistoa. Vertailukriteerit: (1) datan lineage ja KPI-laskennan toistettavuus, (2) kriittisyys- ja riskiluokituksen tuki, (3) integrity-velan seuranta (myöhästyneet tarkastukset, MOC), (4) osaamismatriisi, (5) rajapinnat historian/DCS:iin ja ERP:hen, (6) auditointiketju KPI-pelaamista vastaan, (7) TCO ja siirtymäriski. Tietotarpeet: nykyjärjestelmän kenttäkattavuus vs. `bilfinger_kpi_observation_model.csv`, integraatioinventaario, käyttäjämäärät, lisenssit. Intelligence Layer on perusteltu vasta, kun kohtien 1 ja 6 puutteet on todettu eikä niitä voi korjata konfiguraatiolla.

## Mitä EI pidä siirtää liiketoimintamalliin

- Fysiikan analogiaa (nollaenergia, laajeneminen) — ei ole. Siirretty on vain menetelmä.
- Simulaation numeroita — synteettisiä.
- "Näyttää hyvältä" -käyriä ilman kovarianssia/kohinaa: sama virhe kuin DU-vertailussa, jossa silmämääräinen samankaltaisuus ei ollut tilastollista tasavertaisuutta.

---

# OSA 2 — PERFORMANCE OUTSOURCING DECISION ENGINE (TASK D)

Prototyypin synteettisiä rahalukuja **ei käytetä näyttönä**. Alla oleva on menetelmän muunnos toimintamallilogiikaksi: 12 pakollista kerrosta, kullekin INPUT / LASKENTA TAI HARKINTA / OMISTAJAROOLI / VAADITTU NÄYTTÖ / GREEN–AMBER–RED / VIKATILA / TIETOTARVE / BTS-KYVYKKYYS. Täysi taulukko: `results/po_decision_engine_layers.csv`. Porttikartoitus: `results/po_gate_mapping.csv`. BTS-vaatimusmatriisi: `results/po_bts_requirements.csv`. Roolit ovat rooleja, eivät nimiä tai nykyisiä valtuuksia.

## Kerrokset (tiivistelmä; koko sisältö CSV:ssä)

| # | Kerros | Ydinlaskenta / harkinta | GREEN-kriteeri | Tyypillinen vikatila |
|---|---|---|---|---|
| 1 | SYSTEM BOUNDARY | in-scope laitteet, prosessit, päätösoikeudet; eksogeeniset ajurit listattu | kaikki tulos-KPI:t kytkeytyvät rajan sisäisiin ajureihin | rajan hiipuminen, syyttely ulkoisista |
| 2 | BASELINE / COUNTERFACTUAL | ≥24 kk normalisoitu historia, kohina σ, as-is-trajektori (ikääntyminen mukana) | σ_baseline < 0,5 × odotettu vaikutus | parannus ei erotu kohinasta; regressio keskiarvoon myydään hyötynä |
| 3 | CONTROLLABILITY MATRIX | ajurit: Bilfinger / yhteinen / asiakas / ulkoinen, herkkyyspainot | >60 % KPI-herkkyydestä Bilfinger/yhteinen + eskalaatio | vastuu ilman valtaa (capex, ajotapa) |
| 4 | HSEQ / ASSET-INTEGRITY RED LINES | sitovat rajoitteet, ihmisen hyväksyntä; ei vaihdettavissa arvoon | 0 myöhässä olevaa SCE-tarkastusta/MOC:ia | latentti integrity-velka KPI-fokuksen takana |
| 5 | TRANSITION READINESS | osaamiskattavuus, datayhteydet, Day-1 | kriittinen osaaminen ≥90 %, data live ennen Day 1 | siirtymäkuoppa pidempi kuin suunniteltu |
| 6 | VALUE CREATION MODEL | YHTEINEN ARVO = ΔPV(kate, kysyntärajattu) + ΔPV(resurssi) − PV(siirtymä) − ΔPV(jäännösmenetys); ei kaksoislaskentaa | P50 > 0 dokumentoiduin ajurein | menetys myyntihinnalla; kysynnän ylittävä käytettävyys |
| 7 | VALUE-AT-RISK / P10 | Monte Carlo / skenaariot; stressit: lykkäys, velka, capex-viive, osaajat, data, kysyntä, siirtymä, pelaaminen, sopimuksen loppu | P10 > 0 | päätös pelkällä P50:llä |
| 8 | BENEFIT ATTRIBUTION | normalisoitu ennen–jälkeen; kausaalinen estimaatti vain jos rinnakkaistrendi todennettu | vaikutus > 2σ ja oletukset todennettu | markkina-/kuormavaikutus luetaan palvelun ansioksi |
| 9 | KPI ANTI-GAMING | kaksi riippumatonta lähdettä per tulos-KPI; ristiintäsmäytys; WO-otantatarkastus | raportoitu − riippumaton ≤ 2σ | raportoitu käytettävyys paisuttaa gain-sharea; kriittisyyden uudelleenkoodaus |
| 10 | VALUE SPLIT | asiakas- ja toimittajakassavirrat erikseen; identiteetti asiakas + toimittaja = yhteinen; kannustintesti lykkäyspolitiikalla | molemmat P50 > 0 **eikä** toimittaja hyödy lykkäyksestä | kiinteä maksu ≥ toimituskustannus palkitsee lykkäämisestä |
| 11 | CONTINUOUS VALIDATION | arvopolku vs P10/P50-kaistat; ajautumatestit; kvartaalin riippumaton todennus; BTS-puutekatselmus | P50-kaistassa, integrity GREEN | vihreä dashboard täytetyistä lomakkeista |
| 12 | RENEWAL / EXIT | handback-kunto vs sopimus; viimeisen 12 kk panosprofiili | handback ≥ sopimus, panos tasainen | sopimuksen lopun lykkäys |

## Kartoitus E2E-portteihin

| Portti | Kerrokset, joiden oltava GREEN/AMBER | Hard stop, jos RED | Päätöstuotos |
|---|---|---|---|
| Qualification | 1, 3 (alustava), 4 (screening) | 1, 4 | go/no-go feasibilityyn; rajacharter |
| Feasibility | 1–7 | 2, 3, 4, 7 | arvo-case P10:llä; pilottisuunnitelma; hallittavuuden hyväksyntä |
| Due Diligence | 2 (jäädytetty), 4 (syvä), 5, 6, 10 | 4, 10 | term sheet; red-line-rekisteri |
| Contracting | 3 (päätösoikeudet sopimuksessa), 8, 9, 10, 12 | 9, 10, 12 | sopimus todennettavin KPI:in, kannustintesti läpäisty |
| Transition / Day 1 | 5, 9 (putket live), 2 (baseline allekirjoitettu) | 5 | Day-1-vapautus; arvonseuranta alkaa |
| Operate & Improve | 8, 9, 11, 4 | 4; 11 (RED kaksi kvartaalia) | korjaus / re-baselining / exit-triggeri |
| Renewal / Exit | 12, 8, 2 (uusi baseline) | 12 | uusinta, uudelleenrajaus tai exit handback-selvityksellä |

## BTS-vaatimusmatriisi (Improve / + Intelligence Layer / Replace)

BTS:ää **ei oleteta korvattavaksi**. Matriisi (`results/po_bts_requirements.csv`) listaa 10 vaatimusta kerroksista 1–12 ja kullekin, mitä Improve-, Intelligence Layer- ja Replace-vaihtoehto tarkoittaa sekä mikä tieto tarvitaan päätökseen. Ratkaisevat rivit: (a) kaksilähteinen KPI-täsmäytys ja muuttumaton audit trail (kerrokset 9, 11) — harvoin natiivisti BTS:ssä, Intelligence Layerin ydin, Replace vain jos audit trailia ei voi pakottaa lähteessä; (b) integrity-red-line-seuranta (kerros 4) — IDMS/RBI-moduulin olemassaolo ratkaisee; (c) master data & kriittisyys (kerrokset 1, 3) — yleensä Improve. Valinta tehdään vasta kenttäinventaarion, integraatioinventaarion ja audit-trail-testin jälkeen.

## Suunnitteluperiaatteet, jotka tutkimusmenetelmä tuo Performance Outsourcing 2030:een

1. **Väiterekisteri sopimukselle:** jokainen tuloslupaus = väite, jolla on oletukset, ajurit, mittari, testi ja hylkäysehto — sama rakenne kuin `claim_register.csv`.
2. **Ennakkoon määritellyt hylkäyskriteerit** (P10, integrity-red lines, KPI-ajautuma) ennen sopimusta, ei jälkikäteen.
3. **Mittaus erotetaan tulkinnasta:** raportoitu KPI ≠ todellinen; kaksi lähdettä; audit trail.
4. **Ei kaksoislaskentaa eikä väärää suuretta:** kate, ei myyntihinta; kysyntärajoite; jäännösmenetys kerran.
5. **Kannustintesti lykkäyspolitiikalla** on pakollinen portin ehto: sopimusrakenne, jossa toimittaja hyötyy lykkäyksestä, on RED.
6. **Sulkuehto vs. globaali rajoite:** kuten DU:ssa globaali tase ei määrää paikallista havaintoa, laitostason arvolupaus ei määrää yksikkötason ohjausta — hallittavuusmatriisi on sulkuehto.
7. **Kaikki avoimet asiat näkyvissä** (WHAT/OWNER/STATUS/NEXT/DUE/DEPENDENCY) — puuttuva omistaja merkitään tuntemattomaksi, ei piiloteta.
