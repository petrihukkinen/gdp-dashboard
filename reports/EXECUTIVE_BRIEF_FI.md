# JOHDON TIIVISTELMÄ — DU-tutkimus ja Bilfinger Performance Outsourcing (päivitetty ulkoisesti toimitetulla näytöllä)

Ajo 2026-09-08. Koodi, testit, tulokset: `src/`, `tests/`, `results/`. Väiterekisteri 25 väitettä, falsifiointimatriisi 11 riviä, avoimet asiat 19.

## Kysymys 1: Mikä on DU:n evidentiaalinen tila uusien testien jälkeen?

**Ydinviesti:** DU:n kaksi julkaistua kvantitatiivista havaintoennustetta, jotka voitiin testata, ovat kumpikin ristiriidassa datan kanssa yli 8σ:lla. Jäljelle jäävä teoria on joko vahvassa jännitteessä tai ei vielä ennustava. Mikään testi ei tue DU:ta ΛCDM:ää paremmin. Koko teoriaa ei julisteta kumotuksi; sen **nykyisin muotoillut** ennusteet eivät kestä.

| Testi | Tulos | Status |
|---|---|---|
| Pantheon+ (1590 SN, STAT+SYS), julkaistun tekstimuunnoksen implikoima relaatio p = 1,5 | Δχ² = +3491 vs ΛCDM, jäännöstiltti −4,4 mag/dex, 59σ parhaasta p:stä | **FALSIFIED AS CURRENTLY FORMULATED** |
| Pantheon+, bolometrinen DU p = 0,5 | Δχ² = +82 (0 muotoparametria), 8σ | TENSION |
| Pantheon+, vapaa p = 0,623 ± 0,015 | Δχ² = +14 samalla parametrimäärällä; test-χ² 254 vs 222 | ei pelasta |
| PSR J1738+0333 (Tier-1), DU-32-ONLY | ennuste 0 mittausvirheen sisällä (raja: prefaktorisuhde ≥ 1830 vaadittaisiin) vs −25,9 ± 3,2 fs/s → 8,1σ | **FALSIFIED AS CURRENTLY FORMULATED** |
| PSR J1738+0333, DU-PLUS-QUADRUPOLE | kaksikomponenttisovitus: κ = 1,0005 ± 0,0005; yhtälö 32 ≤ 0,2–0,8 % B1913+16:sta | NOT YET PREDICTIVE (pelastus vie yhtälöltä 32 sisällön) |
| Capotauro | Liu ym. 2026: ominaisliike 37,6 mas/v, ekstragalaktinen suljettu >6σ | tuki poistettu |
| Kulmakoot / antipodi | postulaatit eivät määrää D_A(z); L-B hylätty SN:llä | NOT YET PREDICTIVE (antipodi säilyy ehdollisena) |
| LLR / paikallinen laajeneminen | signaali ei katoa; erottelu LOD-taseesta | TENSION (ehdollinen) |
| CMB, BBN, GW | ei DU-johdantoja | NOT YET PREDICTIVE |
| Laajenemislaki, ikä 1/H0 | suuruusluokka oikea | SUPPORTED (heikosti, ei ainutlaatuinen) |

K-korjaus (Hogg 2002, ulkoisesti vahvistettu määritelmä) on kaistamuunnos; se ei poista kosmologisia laimennustekijöitä. Lisätermin +2,5 log10[(1+z)²] perustelu ei pidä, ja termi tuottaa falsifioidun relaation. Mitä kirjattiin: ΛCDM:n Ωm-toisto (0,332 ± 0,018) on tehty, ei suojattu; avoin ΛCDM ei paranna merkitsevästi.

**Provenienssi:** artikkelin lausumat, J1738:n arvot, Liu ym. ja Hogg-määritelmä on toimitettu ulkoisesti varmennettuina; tämä ympäristö ei hakenut niitä (egress-esto). Renderöityä yhtälöä 32 tai 36 ei ole nähty; numeerinen DU-32-ONLY-arvo on UNRESOLVED, ja p = 1,5 on "tekstimuunnoksen implikoima relaatio".

**Seuraava erotteleva testi per kustannus:** renderöity yhtälö 36 (onko muita termejä) ja yhtälö 32 (numeerinen J1738-ennuste). Kummankin uudelleenajo on sekunteja.

## Kysymys 2: Mitkä konkreettiset suunnitteluperiaatteet parantavat Bilfinger Performance Outsourcing 2030:a?

Synteettisiä rahalukuja ei käytetä näyttönä. Menetelmästä siirtyy **Performance Outsourcing Decision Engine**: 12 pakollista kerrosta (järjestelmäraja, baseline/vastatilanne, hallittavuusmatriisi, HSEQ/integrity-red lines, siirtymävalmius, arvonluontimalli, P10, hyödyn attribuutio, KPI-anti-gaming, arvonjako, jatkuva validointi, uusinta/exit), kullakin INPUT / LASKENTA / OMISTAJAROOLI / NÄYTTÖ / GREEN–AMBER–RED / VIKATILA / TIETOTARVE / BTS-KYVYKKYYS, kartoitettuna Qualification → Feasibility → Due Diligence → Contracting → Transition → Operate & Improve → Renewal/Exit (`results/po_decision_engine_layers.csv`, `po_gate_mapping.csv`).

Periaatteet, jotka nousivat suoraan tutkimusmenetelmästä:

1. **Tuloslupaus = väite, jolla on hylkäysehto.** Sama rakenne kuin väiterekisterissä: oletukset, ajurit, mittari, testi, status.
2. **P10-portti, ei P50-päätös.** Prototyypissä P50 oli positiivinen ja P10 negatiivinen; ilman P10-kriteeriä tämä olisi näyttänyt vihreältä.
3. **Hallittavuus on sulkuehto.** Globaali arvolupaus ei määrää paikallista ohjausta, kuten DU:n globaali tase ei määrää havaintoa. Vastuu ilman päätösvaltaa on RED.
4. **Mittaus ≠ tulkinta.** Jokaiselle tulos-KPI:lle kaksi riippumatonta lähdettä, audit trail, ajautumatesti. Raportoitu käytettävyys ei ole todennettu käytettävyys.
5. **Kannustintesti lykkäyspolitiikalla** ennen allekirjoitusta: sopimusrakenne, jossa toimittaja hyötyy lykkäyksestä (kiinteä maksu ≥ toimituskustannus ilman integrity-/backlog-alarajaa), on RED riippumatta P50:stä.
6. **Ei kaksoislaskentaa, oikea suure.** Kate ei myyntihinta; kysyntärajoite; jäännösmenetys kerran; maksu jakaa arvoa eikä luo sitä (identiteetti tarkistetaan).
7. **Integrity-red lines sitovina rajoitteina**, eivät optimoinnin termeinä; ihmisen HSEQ-/oikeudellinen hyväksyntä.
8. **Attribuutio vain todennetuin oletuksin** (rinnakkaistrendi pre-periodilla), muuten kuvaileva.
9. **BTS-päätös vasta vaatimus–kyvykkyys–puute-vertailun jälkeen.** Ratkaisevat rivit: audit trail & kaksilähteinen täsmäytys, integrity-seuranta, master data. Korvaamista ei oleteta.
10. **Avoimet asiat näkyviin** WHAT/OWNER/STATUS/NEXT/DUE/DEPENDENCY-muodossa; tuntematon omistaja merkitään tuntemattomaksi.

**Pilotoitavaa heti:** hallittavuusmatriisi yhdelle olemassa olevalle kohteelle; baseline-kohinan σ vs. odotettu vaikutus; kannustintesti nykyisille sopimusmalleille. Nämä eivät vaadi uutta järjestelmää eivätkä luottamuksellista dataa ulkoisille malleille.
