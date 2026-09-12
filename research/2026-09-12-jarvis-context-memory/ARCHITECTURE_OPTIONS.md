# Arkkitehtuurivaihtoehdot: Jarviksen persistent memory

Viittaukset ks. `SOURCE_REGISTER.md`. Tämä dokumentti vertailee kolmea arkkitehtuuria toimeksiannon kahdeksalla kriteerillä ja antaa perustellun suosituksen.

## Vaihtoehdot

- **A — Markdown/Obsidian + Git + suora tiedosto- ja avainsanahaku.** Kaikki muisti tavallisina `.md`-tiedostoina versionhallinnassa, ei mitään lisäkoneistoa. Haku = `grep`/tiedostonimet/agentin oma Read-työkalu.
- **B — Sama perusta + rakenteinen metatieto/SQLite + tarvittaessa hybridihaku.** Markdown-tiedostot pysyvät ainoana ihmisluettavana totuuden lähteenä, mutta niiden rinnalla ylläpidetään kevyt, **johdettu** ja **uudelleenrakennettava** indeksi (SQLite tai YAML-frontmatter + skripti), joka kantaa metatietoa (tyyppi, projekti, aikaleimat, scope, korvaussuhteet, verification_status) rakenteisessa muodossa hakua ja eheystarkistuksia varten. Vektorihaku lisätään moduulina vain, jos avainsanahaku osoitetaan riittämättömäksi.
- **C — Erillinen muistipalvelu tai ajallinen tietograafi.** Esim. Letta-palvelin, Zep/Graphiti-tyyppinen tietograafi (Neo4j/FalkorDB) tai Mem0-tyyppinen vektorimuistipalvelu omana prosessina/pilvipalveluna.

## Vertailutaulukko

| Kriteeri | A: Markdown+Git | B: Markdown+Git+metadata/SQLite | C: Erillinen muistipalvelu/graafi |
|---|---|---|---|
| **Tiedon oikeellisuus ja ajantasaisuus** | Hyvä — ihminen näkee koko sisällön suoraan, muutokset ilmeisiä diffissä. Ei automaattista vanhentumisen havaitsemista. | Hyvä+ — metadata (`valid_until`, `superseded_by`) tekee vanhentumisen eksplisiittiseksi ja kyselytettäväksi. | Vaihtelee — riippuu palvelun omasta validointilogiikasta; kaupallisten tuotteiden (Zep, Mem0) oma benchmark-luvut ovat kiistanalaisia [B7], ei syytä luottaa "sisäänrakennettuun oikeellisuuteen" sokeasti. |
| **Lähdejäljitettävyys ja korjattavuus** | Erinomainen — Git-historia on suoraan lähde/muutosloki [D1]. Korjaus = muokkaa tiedostoa + commit. | Erinomainen — sama Git-pohja + metadata tekee jäljitettävyydestä kyselytettävän (kuka/milloin/miksi korvattu). | Vaihtelee palveluittain — moni tuote ei tarjoa ihmisluettavaa, diffattavaa historiaa; palautus vaatii palvelun oman backup/restore-mekanismin, ei tavallista `git revert`. |
| **Haun laatu** | Riittävä pienelle/keskisuurelle aineistolle ja tunnisteperusteisille kyselyille; epätarkka semanttisissa kyselyissä (eri sanasto). | Parempi — rakenteinen suodatus (projekti, tyyppi, scope, aikaväli) SQL:llä + avainsana; hybridi lisättävissä ilman arkkitehtuurin vaihtoa. | Parhaimmillaan paras semanttisissa/suhdekyselyissä (graafi, monihoppinen päättely), mutta CogCanvas-tutkimus [B6] osoittaa jäsenneltyjen artefaktien hävinneen sanatarkalle raakatekstille kahdessa benchmarkissa — "parempi haku" ei ole itsestäänselvä. |
| **Ylläpitotyö ja kustannukset** | Matalin — ei riippuvuuksia, ei palvelinta, ei API-avaimia. | Matala/kohtalainen — SQLite on tiedosto, ei palvelin; skripti indeksin uudelleenrakennukseen. Vektorihaku (jos lisätään) tuo upotusmallin API-kustannuksen. | Korkein — vaatii graafitietokannan/palvelimen ylläpidon, LLM-riippuvaisen poiminnan (jokainen kirjoitus = LLM-kutsu [B2, B5]), versiopäivitykset, mahdollisen kuukausimaksun (Zep/Mem0 pilvipalvelut). |
| **Viive ja kontekstin kulutus** | Matala — suora tiedostonluku, ei verkkokutsua. | Matala — paikallinen SQL-kysely on millisekunteja. | Kohtalainen/korkea — verkkokutsu palveluun, mahdollinen LLM-välivaihe kirjoituksessa; Mem0 raportoi itse p95 ~0,2s [B5, S] mutta tämä on valmistajan oma luku. |
| **Käyttöoikeudet ja siirrettävyys** | Erinomainen — tavallinen tiedostojärjestelmän oikeus, täysin siirrettävissä (kopioi kansio). | Erinomainen — samat tiedostot + yksi SQLite-tiedosto, molemmat siirrettävissä. | Heikko — tila lukittu palvelun omaan tietokantaan/formaattiin; vientimekanismi palvelu- ja versiokohtainen. |
| **Toimittajariippuvuus** | Ei mitään — plain text, mikä tahansa työkalu lukee. | Ei mitään merkittävää — SQLite on avoin standardi, ei palveluriippuvuutta. | Korkea — sidottu tuotteen (Letta/Zep/Mem0) API:in, hinnoitteluun, ylläpitoon ja jatkuvuuteen. |
| **Soveltuvuus yhden käyttäjän Jarvikseen** | Hyvä perusta, mutta ei tue bi-temporaalisuutta/scope-suodatusta/validointitilaa rakenteisesti — vaatii kurinalaisuutta käsin. | **Parhaiten sopiva** — antaa rakenteen (skeema, kyselytettävyys) menettämättä yksinkertaisuutta, Git-pohjaisuutta tai siirrettävyyttä. | Ylimitoitettu — ratkaisee ongelmia (miljoonat muistot, monikäyttäjä, monimutkaiset entiteettisuhteet ajassa), joita yhden käyttäjän Jarvis ei toimeksiannon kuvauksen perusteella kohtaa. |

## Suositus: Vaihtoehto B

**Mitä lähteet osoittavat:** Yksikään tutkittu lähde ei osoita, että vektoritietokanta tai tietograafi olisi *välttämätön* pienelle, yhden käyttäjän hallinnoimalle tietomäärälle. Sen sijaan useat lähteet osoittavat päinvastaista: CogCanvas [B6] mittasi jäsenneltyjen artefaktien (tyypillinen graafi/vektorihaun esikäsittelyvaihe) hävinneen sanatarkalle tekstille; Karpathyn LLM wiki -malli [D3] ja Anthropicin oma "just-in-time"-periaate [A1, A3] perustuvat molemmat tiedostopohjaiseen, ei tietokantapohjaiseen, rakenteeseen; ja `cwc-long-running-agents` [D1] osoittaa tuotantotasoisen agenttiharnessin toimivan Git+Markdown-pohjalta ilman erillistä muistipalvelua.

**Päättelen:** Bi-temporaalinen skeema (B4/B2-käsite) ja scope/validointikentät (D2/D3, B3) ovat arvokkaita **skeeman ominaisuuksia**, eivät tietokantateknologian ominaisuuksia — ne toteutuvat yhtä hyvin YAML-frontmatterissa + SQLite-indeksissä kuin Neo4j-graafissa, huomattavasti pienemmällä ylläpitokustannuksella ja täydellä siirrettävyydellä.

**Ehdotan Jarvikselle:** Vaihtoehto B, tarkka toteutus MEMORY_DESIGN.md:ssä:
- Ainoa totuuden lähde on Markdown/YAML-tiedostot Git-repossa (linjassa toimeksiannon "projektikohtainen tieto kuuluu projektiin" ja "ei ylläpidä samaa tietoa käsin monessa paikassa" -periaatteiden kanssa: yksi kirjoitus, monta johdettua näkymää).
- SQLite (tai vastaava kevyt indeksi) on **puhtaasti johdettu**: se voidaan tuhota ja rakentaa uudelleen tiedostoista milloin tahansa, se ei koskaan kanna tietoa jota ei ole myös Markdown-tiedostossa.
- Avainsanahaku (grep/FTS5 SQLite:ssä) on oletushakumenetelmä.
- Vektorihaku on **ehdollinen laajennus** — ei osa MVP:tä. Ks. laukaiseva ehto alla.
- Tietograafi/erillinen muistipalvelu **ei ole perusteltu** nykyisellä kuvatulla mittakaavalla ja käyttötapauksella.

## Milloin lisäkomponentti olisi perusteltu — ja mikä ongelma sen pitäisi ratkaista

Toimeksianto kieltää suosittelemasta vektoritietokantaa/graafia/moniagenttirakennetta ilman osoitettua tarvetta. Tässä konkreettiset, tarkistettavat laukaisuehdot:

| Lisäkomponentti | Laukaiseva ehto (konkreettinen, havaittu ongelma) | Ratkaisematon ongelma jos ei oteta käyttöön |
|---|---|---|
| **Vektorihaku** | Dokumentoitu tapaus, jossa avainsanahaku epäonnistui, koska kysely ja tallennettu teksti käyttivät eri sanastoa semanttisesti samasta asiasta, JA tapaus toistuu useammin kuin satunnaisesti. | Muutama epäonnistunut haku kuukaudessa, korjattavissa manuaalisella uudelleensanoituksella — ei riitä perusteeksi. |
| **Tietograafi** | Konkreettinen kysymys, joka vaatii moniportaista suhdepäättelyä ajassa yli usean entiteetin (esim. "listaa kaikki henkilöt, jotka olivat osakkaita yhtiössä X jonain hetkenä välillä 2020–2024, ja missä muissa yhtiöissä he olivat samaan aikaan osakkaina") JA tämä kysymystyyppi toistuu, ei ole kertaluonteinen. | Yksittäinen monimutkainen kysymys kerran vuodessa — ratkaistavissa manuaalisella analyysillä tai kertaluonteisella skriptillä ilman pysyvää graafi-infrastruktuuria. |
| **Erillinen muistipalvelu (Letta/Zep/Mem0-tyyppinen)** | Muistin määrä kasvaa mittakaavaan, jossa SQLite-indeksin täysi uudelleenrakennus tai kysely muuttuu havaittavasti hitaaksi (sekunteja) TAI tarvitaan usean samanaikaisen käyttäjän/agentin kirjoitusoikeus samaan muistiin reaaliajassa. | Yhden käyttäjän, yhden koneen käyttö kymmenien/satojen projektien mittakaavassa — SQLite käsittelee tämän ongelmitta. |
| **Moniagenttirakenne muistin hallintaan** | Konkreettinen tarve ajaa useita rinnakkaisia, toisistaan riippumattomia validointi-/hakuprosesseja samanaikaisesti suurella kuormalla. | Yksi käyttäjä, yksi Jarvis-istunto kerrallaan tyypillisesti — subagentti (Claude Coden sisäinen, ei erillinen rakenne) riittää kontekstin eristämiseen tarvittaessa [A7]. |

**Testattava vielä:** Kaikki neljä laukaisuehtoa vaativat käytön havainnointia — niitä ei voida osoittaa toteen tai vääriksi etukäteen ilman oikeaa käyttöhistoriaa. IMPLEMENTATION_BACKLOG.md sisältää nämä "myöhemmät laajennukset, selkeät ehdot" -kohtana.

## Yhteenveto perusteluista taulukkona

| | A | B (suositus) | C |
|---|---|---|---|
| Vastaa "pidä arkkitehtuuri mahdollisimman yksinkertaisena" | Kyllä | Kyllä | Ei |
| Tukee bi-temporaalista/validointi-/scope-skeemaa suoraan | Osittain (käsin) | Kyllä (rakenteisesti) | Kyllä, mutta korkealla kustannuksella |
| Vaatii uusia riippuvuuksia | Ei | Vähän (SQLite = stdlib-tasoinen useimmissa kielissä) | Kyllä, useita |
| Toimittajariippuvuus | Ei | Ei | Kyllä |
| Osoitettu tarve nykyisellä kuvauksella | — | Kyllä | Ei |
