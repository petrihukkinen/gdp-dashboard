# Tutkimusraportti: Context engineering ja persistent memory Petri Jarvikselle

Tutkimuspäivä: 2026-09-12. Viittaukset `[A1]`…`[D5]` osoittavat `SOURCE_REGISTER.md`:n lähteisiin. Kattavuusmerkinnät (P/S/R) selitetty rekisterin alussa — **S**-merkityt väitteet ovat hakusynteesin varassa, ei suoraan alkuperäislähteestä varmennettuja.

Jokaisen alaluvun lopussa: **Lähteet osoittavat / Päättelen / Ehdotan Jarvikselle / Testattava vielä** -erottelu toimeksiannon vaatimuksen mukaisesti.

---

## Tausta: mitä paikallinen ympäristö tosiasiassa on

Ennen suosituksia tarkistettiin työskentelyhakemisto ja projektiohjeet. Tulos: annettu Git-repositorio (`gdp-dashboard`) on yksinkertainen Streamlit-BKT-dashboard-sovellus, jolla ei ole yhteyttä Jarvikseen. Repositoriossa ei ole `CLAUDE.md`- tai `AGENTS.md`-tiedostoa, eikä levyllä ole ennalta olemassa olevaa Jarvis-rakennetta, muistikansiota tai konfiguraatiota tässä konttiympäristössä. Tämä tutkimus on siis **puhtaasti arkkitehtuurisuositus**, ei olemassa olevan Jarvis-toteutuksen auditointi. Tämä on rajoite, jonka toimeksianto nimenomaan sallii ("tarkista paikallinen toteutus... jos se on saatavilla" — sitä ei ollut).

**Päättelen:** Kaikki tässä raportissa esitetyt "nykyinen Claude Code -toiminnallisuus" -väitteet perustuvat Anthropicin yleiseen dokumentaatioon (rekisterin A-osio), eivät tämän käyttäjän omaan, mahdollisesti jo muokattuun asetustiedostoihin. Ennen toteutusta pitää tarkistaa käyttäjän oma `~/.claude/`-hakemisto ja mahdollinen olemassa oleva Jarvis-repo erikseen.

---

## A. Context engineering

### A1. Miten tehtävään valitaan pienin riittävä konteksti?

**Lähteet osoittavat:** Anthropicin oma ohjeistus kuvaa siirtymää "hyvä prompti" -ajattelusta "mikä kontekstikonfiguraatio tuottaa halutun käyttäytymisen tässä askeleessa" -ajatteluun [A1, S]. Skills-arkkitehtuuri toteuttaa tämän käytännössä kolmiportaisena progressiivisena paljastuksena: käynnistyksessä vain nimi+kuvaus (muutama kymmenen tokenia per skilli), täysi sisältö vasta aktivoituessa, tukitiedostot vasta viitattaessa [A5, P]. Sama periaate toistuu MCP-työkalujen skeemoissa (nimet ladataan, täydet skeemat vasta tarvittaessa) ja auto memoryn kaksitasoisessa latauksessa (indeksi aina, aihetiedostot tarvittaessa) [A2, P; A7, P]. Empiirinen tuki: Context Rot -raportti osoittaa suorituskyvyn heikkenevän mitattavasti jo kaukana kontekstirajasta, riippuen häiriötekijöiden määrästä ja rakenteesta [B9, R/S], ja Lost in the Middle -tutkimus osoittaa U-muotoisen sijaintivaikutuksen — kontekstin keskellä oleva tieto käytetään huonommin [B8, S].

**Päättelen:** "Lataa kaikki mahdollisesti relevantti kontekstiin varmuuden vuoksi" on suoraan haitallinen strategia, ei vain tehoton. Oikea malli on **viite ensin, sisältö vasta tarvittaessa**: agentille annetaan polku/tunniste, ja se hakee sisällön eksplisiittisellä toimenpiteellä (tiedoston luku, hakukysely) vain kun tehtävä sitä konkreettisesti vaatii.

**Ehdotan Jarvikselle:** Kolmiportainen malli, joka on suoraan Skills-arkkitehtuurin kaltainen mutta sovellettuna projekteihin ja muistiin: (1) istunnon alussa ladataan vain projektin/päätösten **indeksi** (otsikot, tunnisteet, tila — ei täyttä sisältöä), (2) agentti pyytää yksittäisen muistiobjektin täyden sisällön kun tehtävä nimeää sen, (3) laajat viitetiedostot (esim. koko projektin historia) pysyvät levyllä ja niitä haetaan avainsanalla tai suoralla polulla, ei koskaan ladata kokonaisuudessaan oletuksena.

**Testattava vielä:** Mikä on käytännössä toimiva indeksin koko/muoto Jarviksen mittakaavassa (kymmeniä vs. satoja projekteja/päätöksiä) — ks. EVALUATION_PLAN.md.

### A2. Miten erotetaan ohjeet, käyttäjätiedot, projektitieto, työskentelytila ja työkalutulokset?

**Lähteet osoittavat:** Claude Code erottelee nämä rakenteellisesti eri mekanismeihin, ei sekoita niitä yhteen tiedostoon [A2, P; A7, P]:
| Sisältötyyppi | Mekanismi | Latautuminen |
|---|---|---|
| Pysyvät "aina noudatettavat" ohjeet | `CLAUDE.md` (managed/user/project/local) | Kokonaan joka istunto |
| Malliin sitoutumaton menetelmätieto | Skill (`SKILL.md`) | Kuvaus aina, runko tarvittaessa |
| Käyttäjän mieltymykset/korjaukset | Auto memory (`feedback`, `user`-tyypit) | Indeksi aina, yksityiskohta tarvittaessa |
| Projektin etenevä tila | Auto memory (`project`-tyyppi) / oma `PROGRESS.md` | Indeksi aina / eksplisiittinen luku |
| Ulkoiset viitteet | Auto memory (`reference`-tyyppi) | Tarvittaessa |
| Työkalutulokset | Ei pysyvää tallennusta — osa keskusteluhistoriaa, poistuu compactionissa | Ei latautumista uudelleen |

Auto memory jättää tarkoituksella pois kaiken, jonka Claude voi johtaa koodikannasta tai jonka CLAUDE.md jo sanoo [A2, P] — eksplisiittinen periaate päällekkäisen tallennuksen estämiseksi.

**Päättelen:** Sisällöntyypin ja latautumismekanismin **eriyttäminen on tarkoituksellinen suunnitteluvalinta**, ei vahinko. Yhteen tiedostoon (esim. yksi suuri "muistilista") kaikkea sekoittava ratkaisu rikkoo progressiivisen latauksen edut ja tekee tiedosta vaikeasti validoitavaa.

**Ehdotan Jarvikselle:** Sama viisijako, mutta Jarvis-tasolla: (1) **ohjeet** = ihmisen kirjoittama, versionhallittu skeema/sääntötiedosto (analogia CLAUDE.md:lle), (2) **käyttäjätieto** = harvoin muuttuva profiili (mieltymykset, roolit) erillisenä tiedostona, (3) **projektitieto** = per-projekti kansio, jossa oma päätös/tehtävälogi, (4) **työskentelytila** = istuntokohtainen, ei pysyvä (checkpoint-tiedosto, joka *voidaan* päivittää pysyväksi vain eksplisiittisellä validoinnilla), (5) **työkalutulokset** = ei tallenneta suoraan pysyväksi tiedoksi ilman ihmisen/agentin validointiaskelta (ks. MEMORY_DESIGN.md validointiportti).

**Testattava vielä:** Ei mitään — tämä on suoraan sovellettavissa nyt.

### A3. Milloin käytetään suoraa tiedostohakua, avainsanahakua, vektorihakua, hybridihakua tai graafia?

**Lähteet osoittavat:** Anthropicin oma ohjeistus painottaa "just-in-time"-hakua (viitteen kautta, ei esiladattua) yhdistettynä kevyeen esihaettuun ydintietoon — nimenomaan **hybridi** tarkoittaa tässä "pieni pakollinen ydin + laaja viitteinen haku", ei "avainsana + vektori yhdessä" [A1, S; A3, P]. CogCanvas-tutkimus osoittaa suoraan, että sanatarkka pätkähaku (verrattavissa avainsanahakuun/suoraan tiedostohakuun) voitti LLM:n poimimat jäsennellyt artefaktit (jotka usein rakennetaan vektorihaun/tietograafin päälle) merkittävällä erolla molemmissa testatuissa benchmarkeissa [B6, S] — ts. monimutkaisempi haku ei automaattisesti voita yksinkertaista. Graphiti/Zep-arkkitehtuuri käyttää hybridiä (semanttinen + BM25-avainsana + graafi-BFS) nimenomaan tapauksessa, jossa data on jatkuvasti evolvoiva, ajallisesti sidottu ja entiteettien väliset suhteet ovat itsessään kysymysten kohde [B2, R].

**Päättelen:** Hakumenetelmän valinta riippuu **aineiston koosta ja kyselytyypistä**, ei teknologian trendikkyydestä:
- Suora tiedostohaku/avainsana riittää kun aineisto on kohtuun kokoinen (kymmeniä-satoja tiedostoja, ei miljoonia) ja kyselyt ovat tunnisteperustaisia ("mikä päätettiin projektista X") — tämä on Jarviksen todennäköinen mittakaava yhdellä käyttäjällä.
- Vektorihaku tuo lisäarvoa kun kyselyt ovat semanttisia ja epätarkkoja ("mitä sanoimme jostain tämän kaltaisesta ongelmasta") aineistossa, joka on niin suuri, ettei avainsana/grep löydä osumaa kohtuullisessa ajassa.
- Graafi tuo lisäarvoa kun kysymys itsessään koskee **suhteita ajassa** monen entiteetin välillä (esim. "mikä yritysrakenne korvasi mikä ja milloin, ketkä olivat osakkaita missä vaiheessa") — tämä on harvinaisempi kyselytyyppi yhden käyttäjän Chief-of-Staff-kontekstissa kuin monen käyttäjän asiakaspalvelujärjestelmässä.

**Ehdotan Jarvikselle:** Aloita suoralla tiedostohaulla + avainsanahaulla (grep-tyyppinen) koko projektikannan yli. Lisää vektorihaku **vain**, kun konkreettinen epäonnistunut hakutapaus on dokumentoitu (agentti ei löytänyt relevanttia päätöstä avainsanalla, koska kysymys ja tallennettu teksti käyttivät eri sanastoa). Älä ota käyttöön tietograafia ellei konkreettinen tehtävä vaadi moniportaista suhdepäättelyä ajassa (esim. "kuka omisti mitä milloin usean sukupolven cap table -muutoksen yli") — tällaista tarvetta ei ole osoitettu nykyisessä kuvauksessa.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "haun laatu" — mittaa ensin avainsanahaun epäonnistumisaste oikeilla Jarvis-kyselyillä ennen vektorihaun lisäämistä.

### A4. Miten pitkä konteksti, häiritsevä tieto ja tiedon sijainti vaikuttavat suoritukseen?

**Lähteet osoittavat:** Kaksi riippumatonta havaintolinjaa vahvistavat toisiaan: Lost in the Middle (2023–2024, Stanford, vertaisarvioitu) osoitti U-muotoisen sijaintivaikutuksen [B8, S], ja Context Rot (2025, Chroma) osoitti tuoreemmilla malleilla (Claude 4 -sarja mukana), että heikkeneminen alkaa **kauan ennen** kontekstirajaa ja riippuu häiriötekijöiden samankaltaisuudesta relevantin tiedon kanssa [B9, R/S]. Manus-tuotantoraportin mukaan (S-tasoinen) mallin huomion "muistuttaminen" (esim. `todo.md`-tyyppinen tavoitteen toisto) auttaa vastustamaan ajautumista pitkissä tehtävissä [D2, S].

**Päättelen:** Ilmiö on riippumattomasti toistettu vuosien 2023–2025 aikana eri malleilla — ei yksittäisen mallin ohimenevä puute. Jarvis-suunnittelussa tämä tarkoittaa: **kontekstin määrä ei ole vain kustannuskysymys, se on laatukysymys.** Enemmän kontekstia voi tuottaa huonompia vastauksia, ei vain hitaampia.

**Ehdotan Jarvikselle:** (1) Kontekstibudjetti asetetaan tehtävätyypeittäin (ks. A6), (2) kriittisin tieto (nykyinen tehtävä, aktiiviset päätökset) sijoitetaan aina kontekstin alkuun/loppuun, ei keskelle, (3) laajaa historiaa ei koskaan ladata "varmuuden vuoksi" — vain eksplisiittisen haun tulos.

**Testattava vielä:** Ei suoraan testattavissa synteettisellä Jarvis-aineistolla helposti — tämä on yleinen mallikäyttäytymisen ominaisuus, ei Jarvis-spesifinen. Hyväksy se annettuna reunaehtona.

### A5. Miten compaction ja summarization toteutetaan menettämättä päätöksiä, lähteitä, epävarmuutta ja avoimia tehtäviä?

**Lähteet osoittavat:** Palvelinpuolen compaction API:ssa tekee automaattisen tiivistyksen kynnysarvon ylittyessä ja **korvaa kaiken tiivistelmää edeltävän sisällön kokonaan** [A4, P] — oletuspromptin tarkoitus on nimenomaisesti säilyttää "state, next steps, and learnings needed to continue the task", ja mukautetut ohjeet korvaavat oletuksen **täysin**, joten mukautetussa promptissa täytyy eksplisiittisesti listata mitä säilytetään. Claude Code -tasolla projektijuuren CLAUDE.md luetaan levyltä uudelleen compactionin jälkeen — se siis selviää automaattisesti — mutta alikansioiden CLAUDE.md ja polkukohtaiset säännöt eivät palaudu automaattisesti [A2, P]. Dokumentti suosittelee eksplisiittisesti yhdistämään compactionin ja pysyvän muistityökalun: "compaction keeps the active context small... memory preserves the information that must survive summarization" [A4, P].

**Päättelen:** Compaction on **häviöllinen** operaatio riippumatta siitä mitä ohjeita sille annetaan — se on LLM:n oma tulkinta keskustelusta, ei deterministinen tallennus. Kaikki, joka *täytyy* säilyä täsmällisesti (päätöksen sanamuoto, lähdeviite, epävarmuuden aste), täytyy olla kirjoitettuna **pysyvään tiedostoon ennen** compactionia tapahtuu, ei toivottavasti mukana compactionin lopputuloksessa.

**Ehdotan Jarvikselle:** Compaction/tiivistys ei ole Jarviksen ensisijainen tallennusmekanismi lainkaan. Sen sijaan: (1) päätökset ja avoimet tehtävät kirjataan **rakenteisiin tiedostoihin** (ei vain keskusteluun) sitä mukaa kun ne syntyvät, ei odoteta istunnon loppua tai compactionia, (2) istunnon `SessionStart`/`PreCompact`/`SessionEnd`-koukkuja käytetään pakottamaan tämä kirjaus deterministisesti (ei mallin harkinnan varassa) [A6, P], (3) jos compaction tapahtuu kesken työn, ainoa vaadittu ominaisuus on että agentti pystyy lukemaan pysyvän tilan takaisin — ei että compaction-tiivistelmä itsessään on täydellinen.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "avoimen tehtävän jatkaminen uudessa istunnossa" — tämä testaa juuri tätä mekanismia suoraan.

### A6. Miten kontekstibudjetti ja progressiivinen tiedon lataus suunnitellaan?

**Lähteet osoittavat:** Claude Code -dokumentaatio antaa eksplisiittisen kontekstikustannustaulukon eri ominaisuustyypeille (CLAUDE.md = joka pyyntö, Skills = matala kunnes käytetty, MCP = matala kunnes käytetty, Subagentit = eristetty, Hookit = nolla) [A7, P]. Skill-ohjeistus antaa konkreettisen numeerisen ohjenuoran: SKILL.md-runko alle 500 riviä, CLAUDE.md alle 200 riviä, MEMORY.md-indeksi rajattu 200 riviin/25 KB:iin — ylimenevä osa pudotetaan seuraavalla latauksella [A2, P; A5, P].

**Päättelen:** "Progressiivinen tiedon lataus" ei ole abstrakti periaate Anthropicin omissa järjestelmissä — se on toteutettu **konkreettisilla, dokumentoiduilla numeerisilla rajoilla**, jotka on syytä ottaa suoraan malleina eikä keksiä omia lukuja tyhjästä.

**Ehdotan Jarvikselle:** Ota käyttöön samankaltaiset kovakoodatut rajat MEMORY_DESIGN.md:ssä: indeksitiedosto rajattu (esim. 150–200 riviä), yksittäinen päätös/tehtävätiedosto pieni (muutama kymmenen riviä), koko projektin aktiivinen konteksti rajattu erikseen. Jos raja ylittyy, se on signaali *arkistoida* vanhentunut sisältö pois indeksistä, ei kasvattaa rajaa.

**Testattava vielä:** Todelliset raja-arvot Jarviksen käytössä — aloita Claude Coden omilla luvuilla ja säädä havaitun käytön perusteella.

---

## B. Pysyvä muisti

### B1. Mitkä muistityypit kannattaa erottaa?

**Lähteet osoittavat:** Kaksi riippumatonta arkkitehtuuria päätyvät samankaltaiseen jaotteluun eri sanastolla: MemGPT/Letta erottaa **pääkontekstin** (työmuisti: system-ohjeet + työskentelyikkuna) ja **ulkoisen tallennuksen** (recall storage = kaikki menneet viestit, archival storage = pitkäaikainen tieto) [B3, S/R]. Zep/Graphiti erottaa **episodi-alagraafin** (raa'at, aikaleimatut tapahtumat), **entiteetti-alagraafin** (jalostetut, validoidut faktat suhteineen) ja **yhteisö-alagraafin** (korkean tason koosteet) [B2, R]. Claude Code auto memory erottaa neljä tyyppiä käyttötarkoituksen mukaan: `user`, `feedback`, `project`, `reference` [A2, P]. Anthropicin harnesses-malli lisää erillisen **päätösten/tehtävien tilan** (feature list + progress log, jossa eksplisiittinen "valmis"-tila vasta varmennuksen jälkeen) [D1, R].

**Päättelen:** Yhdistäen näistä nousee **kuusi** erotettavaa tyyppiä, ei viisi eikä neljä — toimeksianto mainitsi työmuisti/tapahtumat/pysyvät faktat/toimintamenetelmät/päätökset/tehtävät, ja tämä jaottelu on tutkimuksen valossa perusteltu, kunhan tapahtumat (episodinen, raaka, muuttumaton loki) ja pysyvät faktat (validoitu, päivittyvä) pidetään erillään — tämä on juuri se ero, jonka CogCanvas-tutkimus [B6] osoittaa kriittiseksi (raaka säilyy, tulkinta voi olla väärä).

**Ehdotan Jarvikselle:** Kuusi tyyppiä MEMORY_DESIGN.md:n skeemassa:
1. **Työmuisti** (istuntokohtainen, ei pysyvä oletuksena)
2. **Tapahtumat/episodit** (append-only loki — mitä tapahtui, milloin, lähde — ei koskaan muokata jälkikäteen)
3. **Pysyvät faktat** (validoitu, yksi lähde per fakta, voi vanhentua/korvautua)
4. **Toimintamenetelmät** (= skillit — projektiriippumattomat, uudelleenkäytettävät)
5. **Päätökset** (aikaleimattu, lähteistetty, korvaussuhteineen)
6. **Tehtävät** (tila: avoin/valmis/hylätty, liitos päätökseen ja projektiin)

**Testattava vielä:** Ei mitään merkittävää — tämä jaottelu on suoraan käyttöönotettavissa.

### B2. Mikä ansaitsee tallennuksen, ja mikä jätetään tallentamatta?

**Lähteet osoittavat:** Auto memory -dokumentaatio antaa eksplisiittisen negatiivisen säännön: "Claude skips anything it can derive from the codebase... It also skips anything your CLAUDE.md files already say... Claude doesn't save something every session. It decides what's worth remembering based on whether the information would be useful in a future conversation." [A2, P]. Tämä on tarkoituksellinen deduplikaatioperiaate.

**Päättelen:** Tallennuskynnyksen tulisi olla **"hyödyllinen tulevaisuudessa JA ei johdettavissa muualta"**, ei "kaikki mitä agentti tuotti tänään". Tämä estää muistin paisumisen ja päällekkäisen totuuden (kaksi lähdettä samalle tiedolle) — suoraan toimeksiannon periaatteen "yksi selkeä ensisijainen tietolähde per pysyvä tieto" mukaisesti.

**Ehdotan Jarvikselle:** Tallenna pysyväksi vain: (a) päätökset, joilla on liiketoiminnallinen tai strateginen vaikutus, (b) avoimet tehtävät joita ei voida päätellä koodista/dokumenteista, (c) käyttäjän eksplisiittiset korjaukset/mieltymykset, (d) ulkoiset viitteet joita ei muuten löydy. Älä tallenna: keskustelun sivupolkuja, työkalutuloksia sellaisenaan, mitä tahansa jonka voi laskea/johtaa jo tallennetusta.

**Testattava vielä:** Konkreettinen "tallennuskynnys"-heuristiikka vaatii käyttäjän oman arvion kalibrointia — ehdota alkuun matala kynnys (tallenna helposti) ja lisää poisto/yhdistämismenettely, ei tiukkaa etukäteissuodatinta, koska liian tiukka suodatin riskeeraa hyödyllisen tiedon menettämisen.

### B3. Miten muistiehdokas validoidaan ennen pysyväksi tiedoksi hyväksymistä?

**Lähteet osoittavat:** Muistin myrkytystä käsittelevä tutkimus (S-tasoinen, ei täysin luettu) toteaa, että puolustus täytyy rakentaa **kirjoitusreitille**, ei syöttörajalle, koska haitallinen sisältö on semanttisesti erottamaton laillisesta [C2, S — ei täysin luettu]. Lethal trifecta -periaate [C1, S] vahvistaa: kun agentilla on samassa istunnossa pääsy luottamattomaan sisältöön ja kirjoitusoikeus pysyvään muistiin, syntyy hyökkäyspinta. `cwc-long-running-agents`-repo toteuttaa konkreettisen "default-FAIL"-sopimuksen: jokainen väitetty valmis tila alkaa `false`-arvolla, ja `PreToolUse`-hook **estää** tuloksen kirjaamisen ennen kuin agentti on avannut todistetta (näyttöä, lokia) — tämä on rakenteellinen pakko, ei promptiohje [D1, R].

**Päättelen:** Validointi ei voi olla "agentti päättää itse tuntuuko tieto luotettavalta" — se on juuri se malli, jonka lethal trifecta ja muistin myrkytys -tutkimukset osoittavat riittämättömäksi. Validoinnin täytyy olla **rakenteellinen porras** ennen kirjoitusta pysyvään varastoon.

**Ehdotan Jarvikselle:** Kolmivaiheinen putki (yksityiskohdat MEMORY_DESIGN.md:ssä): (1) agentti tuottaa **ehdotuksen** väliaikaiseen "candidate"-tilaan, ei suoraan pysyvään tiedostoon, (2) ehdotus sisältää pakollisen lähdeviitteen (mistä tieto tulee — käyttäjän suora lausunto, dokumentti, päättely), (3) siirto pysyvään tilaan vaatii eksplisiittisen hyväksynnän — käyttäjän suoralta lausunnolta syntyvä ehdotus voidaan hyväksyä automaattisesti kevyemmin kriteerein, ulkoisesta/luottamattomasta sisällöstä (esim. web-hakutulos, sähköposti) syntyvä ehdotus vaatii aina ihmisen kuittauksen ennen pysyväksi merkitsemistä.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "haitallisen lähdeohjeen torjuminen" — testaa suoraan tätä porttia.

### B4. Miten ristiriidat, vanhentuminen, korvaavat päätökset ja poistaminen käsitellään?

**Lähteet osoittavat:** Zep/Graphitin bi-temporaalinen malli antaa suoraan käyttökelpoisen ratkaisun: jokainen fakta/edge kantaa oman voimassaoloikkunansa (milloin tuli voimaan, milloin invalidoitui) erillään siitä milloin se **kirjattiin** järjestelmään [B2, R]. Kun uusi fakta ristiriitaisee vanhan kanssa, vanha ei poistu — se merkitään invalidoiduksi ja uusi korvaa sen aikajanalla, säilyttäen jäljitettävyyden ("mitä uskoimme milloin"). MemGPT/Letta-mallissa vastaava käsite on itse-editoiva muisti funktiokutsuin, mutta ei eksplisiittistä bi-temporaalista merkintää [B3, S].

**Päättelen:** Bi-temporaalinen malli (tapahtuma-aika/voimassaoloaika vs. tallennusaika) on arvokas käsite **riippumatta siitä käytetäänkö tietograafia** — se on tietue-skeeman ominaisuus, ei tietokantateknologian ominaisuus. Tämä vastaa suoraan toimeksiannon kysymykseen "miten erotetaan tapahtuma-aika, tallennusaika ja tiedon voimassaolo".

**Ehdotan Jarvikselle:** Ota bi-temporaalinen skeema käyttöön Markdown/metadata-tasolla (ei vaadi graafitietokantaa): joka muistiobjektilla kentät `valid_from`, `valid_until` (milloin fakta on/oli totta) ja `recorded_at` (milloin kirjattu järjestelmään) erillään. Korvaava päätös ei poista vanhaa tiedostoa — se asettaa vanhan `valid_until`-kentän ja `superseded_by`-viittauksen uuteen. Poisto (todellinen, ei looginen) on erillinen, harvinaisempi operaatio (ks. B7).

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "uuden päätöksen tunnistaminen vanhan korvaajaksi" ja "ristiriitaisten tietojen käsittely".

### B5. Miten erotetaan tapahtuma-aika, tallennusaika ja tiedon voimassaolo?

**Lähteet osoittavat:** Käsitelty B4:ssä — Zep-paperin bi-temporaalinen malli on ainoa lähde, jossa tämä on eksplisiittisesti nimetty ja formalisoitu [B2, R].

**Päättelen/Ehdotan:** Ks. B4 ja MEMORY_DESIGN.md-skeema — kolme erillistä aikaleimakenttää per muistiobjekti, ei yhtä "timestamp"-kenttää.

**Testattava vielä:** —

### B6. Miten estetään AI:n oman tulkinnan muuttuminen myöhemmin näennäiseksi faktaksi?

**Lähteet osoittavat:** Tämä on tutkimuksen **vahvimmin tuettu yksittäinen löydös**. CogCanvas-ablaatiotutkimus osoittaa suoraan mitattuna, että LLM:n poimima jäsennelty artefakti häviää sanatarkalle raakatekstille merkittävällä erolla molemmissa testatuissa benchmarkeissa, koska poiminta on häviöllistä tislausta, joka hukkaa yksityiskohtaa jonka raaka pätkä säilyttäisi [B6, S]. Toimeksianto itsessään nimeää tämän suunnitteluperiaatteeksi ("Erota alkuperäisaineisto, tulkinta, varmennettu tieto..."), ja Karpathyn LLM wiki -malli toteuttaa saman jaon rakenteellisesti (`raw/` vs. `wiki/`) [D3, S].

**Päättelen:** Tämä ei ole vain teoreettinen huoli — se on mitattu ilmiö. Kun tulkinta kirjoitetaan "faktana" ilman viittausta alkuperäiseen, seuraava agentti (tai seuraava istunto) ei voi erottaa "tämä on suoraan käyttäjän sanoma" ja "tämä on aiemman agentin päätelmä käyttäjän sanomasta". Ajan myötä nämä sekoittuvat ja virheellinen tulkinta vahvistuu toistolla.

**Ehdotan Jarvikselle:** **Ehdoton sääntö MEMORY_DESIGN.md:ssä**: jokainen tallennettu "fakta" tai "päätös" kantaa pakollisen `source`-kentän, joka erottaa neljä tasoa — (1) suora lainaus/käyttäjän oma sanamuoto, (2) dokumentista poimittu (viittaus dokumenttiin+kohtaan), (3) agentin päättely/tulkinta (merkitty eksplisiittisesti "tulkinta", ei "fakta"), (4) validoitu ulkoinen lähde. Taso (3) ei koskaan nouse tasoksi "varmennettu fakta" automaattisesti — nousu vaatii eksplisiittisen käyttäjän vahvistuksen, joka muuttaa `verification_status`-kentän. Alkuperäinen sanamuoto/dokumentti säilytetään aina rinnalla, ei korvata tiivistelmällä.

**Testattava vielä:** Ei erillistä testiä tarvita — tämä on rakenteellinen skeemavaatimus, todennettavissa suoraan skeeman tarkastuksella.

### B7. Miten johdetut tiivistelmät ja hakuindeksit päivitetään, kun lähde muuttuu tai poistetaan?

**Lähteet osoittavat:** Ei löytynyt yhtä eksplisiittistä lähdettä, joka käsittelisi tätä suoraan pysyvän muistin kontekstissa. Lähimpänä analogiana Karpathyn LLM wiki -mallin `lint`-operaatio (eheystarkistus, roikkuvat viitteet) [D3, S] ja Claude Coden CLAUDE.md-uudelleenlataus compactionin jälkeen (osoittaa että johdettu tila voi jäädä vanhentuneeksi kunnes eksplisiittisesti päivitetty) [A2, P].

**Päättelen:** Tämä on suunnittelukysymys, ei tutkimuskysymys, jolle löytyisi valmis vastaus — mutta johdettu indeksi/tiivistelmä on aina **toissijainen** alkuperäiseen nähden, joten sen on ehdottomasti oltava **uudelleengeneroitava** alkuperäisestä, ei itsenäisesti ylläpidetty.

**Ehdotan Jarvikselle:** Hakuindeksi (esim. avainsanaindeksi tai SQLite-metadata) merkitään aina johdetuksi tuotteeksi, joka voidaan tuhota ja rakentaa uudelleen alkuperäisistä Markdown-tiedostoista milloin tahansa — ei koskaan ainoana tiedon lähteenä. Kun lähdetiedosto poistetaan, poisto-operaatio sisältää aina indeksin päivityksen samassa transaktiossa (ks. MEMORY_DESIGN.md), ja EVALUATION_PLAN.md testaa juuri tätä ("poistetun tiedon poistuminen myös hausta").

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "poistetun tiedon poistuminen myös hausta".

### B8. Miten istunnon checkpoint ja seuraavan istunnon aloitus toteutetaan?

**Lähteet osoittavat:** Tämä on tutkimuksen toiseksi vahvimmin lähteistetty osa-alue. Kolme yhtenevää lähdettä: (1) Anthropicin memory tool -dokumentaatio antaa valmiin promptimallin: "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE... ASSUME INTERRUPTION: Your context window might be reset at any moment" [A3, P]; (2) "multisession software development pattern" -kuvaus: alustajaistunto perustaa edistymislokin ja ominaisuuslistan, jokainen seuraava istunto lukee ne ensin, istunnon lopussa päivitetään loki [A3, P; D1, R]; (3) `cwc-long-running-agents` toteuttaa tämän hook-tasolla (`SessionStart` lukee, `SessionEnd`/`commit-on-stop` kirjoittaa) [D1, R; A6, P].

**Päättelen:** Tämä on ainoa osa-alue, jossa on **kolme riippumatonta, yhtenevää, dokumentoitua lähdettä** samasta mallista — vahvin perusta koko tutkimuksessa yksittäiselle suositukselle.

**Ehdotan Jarvikselle:** Suoraan sovellettava, minimimuutoksin: istunnon aloitus = pakollinen (hook-tasolla toteutettu, ei promptin varassa) luku projektin `PROGRESS.md`/`CHECKPOINT`-tiedostosta ja aktiivisten tehtävien listasta; istunnon lopetus = pakollinen kirjoitus samaan tiedostoon (mitä tehtiin, mikä on seuraava askel, mitä ei ratkaistu). Ks. MEMORY_DESIGN.md tarkka menettely.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "avoimen tehtävän jatkaminen uudessa istunnossa".

---

## C. Claude Code ja järjestelmien välinen käyttö

### C1. Mitkä Claude Coden nykyiset muistitoiminnot ovat dokumentoituja, ja mitkä vaativat oman toteutuksen?

**Lähteet osoittavat — dokumentoitu, valmis toiminnallisuus [A2, P; A6, P; A8, P]:**
- CLAUDE.md-hierarkia (managed/user/project/local) + `@path`-importit + `.claude/rules/` polkukohtaisilla säännöillä.
- Auto memory (`MEMORY.md` + aihetiedostot), neljä tyyppiä, konekohtainen tallennus.
- `/memory`-komento tarkasteluun/muokkaukseen, `/context` lataustilanteen tarkasteluun.
- Hookit (`SessionStart`, `PreCompact`, `PostCompact`, `SessionEnd`) kontekstin injektointiin/tallennukseen.
- `/export` ja `-p --resume`-rajapinnat ohjelmalliseen pääsyyn (JSONL-transkriptit **ei** ole vakaa integraatiopinta [A8, P]).

**Vaatii oman toteutuksen (ei ole valmiina):**
- **Järjestelmienvälinen** (Claude Code ↔ ChatGPT ↔ Copilot) pysyvä muisti — mitään näistä ei synkronoi toistensa kanssa [A2, P; D4, S; D5, S].
- Bi-temporaalinen versiointi, korvaussuhteet, validointitila — auto memory on plain Markdown, ei kanna näitä kenttiä valmiiksi.
- Käyttöoikeusrajaus per muistiobjekti (auto memory on koko projektin laajuinen, ei kenttäkohtainen).
- Ristiriitojen automaattinen tunnistus/ratkaisu.

**Päättelen:** Claude Code antaa **hyvän perustan** (lataushierarkia, progressiivinen paljastus, hook-pisteet) mutta **ei anna** rakenteista, validoitua, järjestelmienvälistä muistimallia. Tämä täytyy rakentaa erillisenä kerroksena tiedostojen/skeeman muodossa, joka *hyödyntää* Claude Coden mekanismeja (CLAUDE.md, skillit, hookit) mutta ei odota niiden ratkaisevan koko ongelmaa.

**Ehdotan Jarvikselle:** Rakenna Jarviksen oma muistikerros tavallisina Markdown/YAML-tiedostoina versionhallinnassa (ei auto memory -kansion sisään, koska se on konekohtainen ja epävakaan sisäisen formaatin varassa) — käytä Claude Coden CLAUDE.md/skills/hooks-mekanismeja **liitäntäkerroksena** tähän omaan tallennukseen, ei tallennuksena itsessään.

**Testattava vielä:** Käyttäjän oman `~/.claude/`-asetusten ja mahdollisen olemassa olevan Jarvis-repon tarkistus ennen toteutusta (ei ollut saatavilla tässä tutkimusympäristössä).

### C2. Miten CLAUDE.md, skills, projektitiedostot ja mahdolliset muistitoiminnot kannattaa työnjaollisesti järjestää?

**Lähteet osoittavat:** A7:n päätöstaulukko on suoraan vastaus: "A repeated mistake or a recurring review comment is a CLAUDE.md edit, not a one-off correction in chat"; "a workflow you keep tweaking by hand is a skill" [A7, P].

**Ehdotan Jarvikselle** (tiivistetty taulukko):
| Sisältö | Sijainti |
|---|---|
| Jarviksen yleiset toimintaperiaatteet (aina voimassa) | `CLAUDE.md` (projektitaso, versionhallinnassa) |
| Käyttäjän henkilökohtaiset työskentelymieltymykset | `~/.claude/CLAUDE.md` (käyttäjätaso) tai Jarviksen oma käyttäjäprofiili |
| Toistettava menetelmä (esim. "näin arvioidaan Series A -termsheet") | Skilli |
| Projektikohtainen fakta/päätös/tehtävä | Jarviksen oma projektikansio (ei CLAUDE.md, ei skilli — nämä eivät ole tarkoitettu muuttuvalle datalle) |
| Istunnon työskentelytila | `PROGRESS.md`/checkpoint per projekti, ei CLAUDE.md |

**Testattava vielä:** —

### C3. Mikä tieto säilytetään mallista riippumattomassa muodossa?

**Lähteet osoittavat:** Kaikki edellä käsitellyt pysyvän tallennuksen mekanismit (CLAUDE.md, PROGRESS.md, auto memory -tiedostot) ovat **plain Markdown/tekstitiedostoja** — ei mallikohtaista binääriformaattia [A2, P]. Sen sijaan istunnon oma transkripti (JSONL) on nimenomaisesti **mallista/versiosta riippuvainen** eikä vakaa [A8, P].

**Päättelen:** Raja on selvä: kaikki, jonka *pitää* säilyä yli mallinvaihdon/version, kirjoitetaan aina ihmisluettavaan, muokattavaan tekstiformaattiin — ei koskaan luoteta sisäiseen transkriptiformaattiin tai mallikohtaiseen tilaan.

**Ehdotan Jarvikselle:** Jarviksen koko pysyvä muisti (päätökset, tehtävät, faktat, menetelmät) on Markdown/YAML-frontmatter-tiedostoja Git-repossa. Mikään Jarviksen kriittinen tila ei riipu Claude Coden auto memory -kansiosta (konekohtainen), transkriptiformaatista (versioriippuvainen) tai ChatGPT:n/Copilotin omasta muistista (tuntematon, ei-vientikelpoinen, ks. D4/D5).

**Testattava vielä:** —

### C4. Mitä voidaan siirtää ChatGPT:n, Claude Coden ja Copilotin välillä tiedostoina, ja mikä vaatii erillisen integraation?

**Lähteet osoittavat:** OpenAI:n muisti [D4, S] ja Microsoft Copilotin muisti [D5, S] ovat molemmat **suljettuja, tilikohtaisia palveluita** ilman dokumentoitua ohjelmallista vientirajapinnaa valikoivaan, rakenteiseen muotoon. Copilotin muisti on lisäksi sidottu Exchange-postilaatikkoon ja yrityksen compliance-kehykseen [D5, S].

**Päättelen:** **Ei pidä olettaa** näiden järjestelmien välillä olevan tai tulevan yhteistä muistia. Tämä on toimeksiannon oma varoitus ("Älä oleta, että näillä järjestelmillä on yhteinen muisti") ja tutkimus vahvistaa sen.

**Ehdotan Jarvikselle:** Siirrettävissä tiedostoina: tavalliset dokumentit (Markdown, PDF, taulukot) jotka käyttäjä itse lataa/liittää kuhunkin järjestelmään manuaalisesti tai skriptillä. **Ei siirrettävissä** ohjelmallisesti ilman erillistä integraatiota: ChatGPT:n "saved memories", Copilotin personointimuisti, Claude Coden auto memory (konekohtainen). Jarviksen ydinmuisti pysyy Jarviksen omassa Git/Markdown-kannassa; jokainen työkalu (Claude Code, ChatGPT, Copilot) **lukee siitä tarvittaessa** (esim. käyttäjä liittää relevantin tiedoston/otteen), mutta mikään työkalu ei ole ydinmuistin ainoa säilytyspaikka.

**Testattava vielä:** Onko Copilotilla (yritysympäristössä) Microsoft Graph -tason API, joka mahdollistaisi ohjelmallisen luvun/kirjoituksen — ei varmennettu tässä tutkimuksessa, `learn.microsoft.com` oli estetty.

### C5. Miten rinnakkaiset kirjoitukset, versiointi ja palautuminen hallitaan?

**Lähteet osoittavat:** Ei löytynyt Claude Code -spesifistä pysyvän muistin lukitusmekanismia rinnakkaisille kirjoituksille — auto memory on yhden koneen, yhden käyttäjän sisäinen tila, ei suunniteltu rinnakkaiskäyttöön [A2, P]. Sessiot voivat kuitenkin **haarautua** (`/branch`) ja jatkaa rinnakkain, mikä tarkoittaa että sama alusta konteksti voi johtaa kahteen erilliseen, mahdollisesti ristiriitaiseen tilaan [A8, P, sessions-dokumentti].

**Päättelen:** Git-versionhallinta on Anthropicin omassa "harnesses"-mallissa jo se mekanismi, jolla rinnakkainen/peräkkäinen tila hallitaan ohjelmistokehityksessä [D1, R] — commit-historia on totuuden lähde, ei agentin oma muisti.

**Ehdotan Jarvikselle:** Käytä samaa periaatetta: Jarviksen pysyvä muisti versionhallitaan Gitissä. Rinnakkaiset kirjoitukset (esim. kaksi istuntoa samanaikaisesti) ratkaistaan tavallisilla Git-mekanismeilla (commit, merge-konflikti näkyy eksplisiittisesti, ei hiljaisesti ylikirjoita). Kriittisille, useasti rinnakkain kirjoitettaville kentille (esim. tehtävän tila) harkitse yksinkertaista optimistista lukitusta (versionumero per objekti, kirjoitus hylätään jos versio on muuttunut — sama malli kuin tämän Artifact-työkalun `if_version`-mekanismi).

**Testattava vielä:** Ei kriittinen MVP:ssä yhdelle käyttäjälle yhdellä koneella kerrallaan — merkitse laajennusehdoksi IMPLEMENTATION_BACKLOG.md:ssä.

---

## D. Luotettavuus ja tietojen rajaus

### D1. Miten ulkoisesta aineistosta tuleva prompt injection estetään muuttumasta pysyväksi ohjeeksi tai muistiksi?

**Lähteet osoittavat:** Lethal trifecta [C1, S]: vaarallinen yhdistelmä on pääsy yksityiseen dataan + altistus luottamattomalle sisällölle + kyky viestiä ulos samassa istunnossa; detektiopohjainen suoja (99 % tarkkuus) ei riitä agenttikontekstissa. Claude Coden oma tietoturvadokumentaatio vahvistaa rakenteellisen lähestymistavan: luottamaton sisältö käsitellään aina dataksi tool_result-lohkoissa, ei ohjeena system promptissa [C3, P]. Muistin myrkytys -tutkimus (osittain lukematta) väittää puolustuksen kuuluvan kirjoitusreitille [C2, S].

**Päättelen:** Yksikään näistä lähteistä ei ehdota, että ongelma ratkeaisi "parantamalla tunnistusta" — kaikki kolme osoittavat rakenteelliseen erotteluun.

**Ehdotan Jarvikselle:** (1) Ulkoinen, luottamaton sisältö (web-hakutulos, saapunut sähköposti, toisen henkilön kommentti) merkitään aina eksplisiittisesti dataksi, ei koskaan tulkita ohjeeksi. (2) Pysyvään muistiin kirjoittaminen **ulkoisen sisällön perusteella** kulkee aina B3:n validointiportin läpi — ei koskaan suoraan automaattisesti. (3) Jos samassa toimenpiteessä yhdistyy luottamaton sisältö ja kirjoitusoikeus pysyvään muistiin, vaaditaan ihmisen kuittaus ennen kirjoitusta.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "haitallisen lähdeohjeen torjuminen".

### D2. Miten henkilökohtainen tieto ja yrityskohtainen tieto erotetaan haussa ja tallennuksessa?

**Lähteet osoittavat:** Ei löytynyt Jarvis-tasoista suoraa lähdettä. Lähin analogia: Copilotin muisti on sidottu tenant-rajaan (yrityksen Microsoft 365 -ympäristö) erillään henkilökohtaisesta ChatGPT-muistista [D4, D5, S] — järjestelmätasolla erottelu on jo olemassa eri palveluiden välillä, ei saman palvelun sisällä.

**Päättelen:** Tämä on ensisijaisesti Jarviksen omaa tietomallia koskeva päätös, ei tutkimuskysymys, jolle olisi valmis vastaus toimialalta.

**Ehdotan Jarvikselle:** Jokainen projektikansio/muistiobjekti kantaa eksplisiittisen `scope`-kentän (`henkilökohtainen` / `yritys-X` / `yritys-Y`), ja haku rajataan oletuksena nykyisen kontekstin scope-arvoon. Ristiin hakeminen (esim. henkilökohtaisen sijoitussalkun ja yrityksen taloustietojen välillä) vaatii eksplisiittisen, molemminpuolisen pyynnön — ei tapahdu oletuksena.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "käyttöoikeusrajan säilyminen".

### D3. Miten käyttöoikeudet säilyvät myös johdetuissa muisteissa ja hakutuloksissa?

**Lähteet osoittavat:** Ei suoraa Jarvis-tasoista lähdettä löytynyt (OWASP LLM08 Vector/Embedding Weaknesses -sivu, joka olisi käsitellyt tätä suoraan monikäyttäjä-RAG-kontekstissa, oli estetty — merkitty lukemattomaksi rekisterissä).

**Päättelen:** Yhden käyttäjän Jarvis-järjestelmässä (kuten toimeksianto kuvaa) monikäyttäjä-RAG:n käyttöoikeusongelma on lievempi kuin yritys-SaaS-kontekstissa, mutta scope-erottelu (D2) on silti tarpeen henkilökohtainen/yritys-A/yritys-B-rajojen vuoksi.

**Ehdotan Jarvikselle:** Johdettu indeksi (ks. B7) kantaa aina alkuperäisen objektin `scope`-kentän mukana — indeksin rakentaminen ei koskaan "litistä" scope-tietoa pois. Hakutulos suodatetaan scope-kentän mukaan ennen kuin sitä näytetään agentille, ei jälkikäteen.

**Testattava vielä:** Ks. EVALUATION_PLAN.md testi "käyttöoikeusrajan säilyminen".

### D4. Miten lähdeviitteet, lokitus, varmuuskopiointi ja palautus tukevat virheiden korjaamista?

**Lähteet osoittavat:** Git-pohjainen malli (D1: `cwc-long-running-agents`) antaa tämän ilmaiseksi: jokainen muutos on commit, jolla on aikaleima, tekijä ja diff — palautus on `git revert`/`git log` [D1, R]. Bi-temporaalinen malli (B2/B4) antaa lisäksi sovellustason jäljitettävyyden (mikä uskottiin milloin) erillään Git-historiasta (kuka muutti tiedostoa milloin).

**Päättelen:** Näitä ei tarvitse rakentaa tyhjästä — Git-versionhallinta **on** lokitus- ja palautusmekanismi tiedostotasolla, ja bi-temporaaliset kentät antavat sovellustason historian sen päälle.

**Ehdotan Jarvikselle:** Koko muistikanta versionhallitaan Gitissä (commit per merkittävä muutos, ei per pieni automaattikirjoitus — liiallinen commit-tiheys hukkaa signaalin). Varmuuskopiointi = normaali Git-remote-push. Palautus = `git revert` tiedostotasolla + `superseded_by`-ketjun purku sovellustasolla jos korvaus pitää perua.

**Testattava vielä:** —

---

## Yhteenveto: mitä tutkimus tukee vahvimmin vs. heikoimmin

| Löydös | Tuen vahvuus |
|---|---|
| Istunnon checkpoint (lue alussa, kirjoita lopussa) | **Vahva** — 3 riippumatonta, yhtenevää lähdettä (A3, A6, D1) |
| Säilytä alkuperäinen, erottele tulkinta faktasta | **Vahva** — mitattu tutkimus (B6) + toimeksiannon oma periaate + arkkitehtuurianalogia (D3) |
| Progressiivinen lataus / minimikonteksti | **Vahva** — dokumentoitu, numeroin varustettu Anthropic-arkkitehtuuri (A2, A5, A7) |
| Pitkä/häiritsevä konteksti heikentää suoritusta | **Vahva** — kaksi riippumatonta, ajallisesti erillistä tutkimusta (B8 2023-24, B9 2025) |
| Bi-temporaalinen aikamalli | **Kohtalainen** — yksi preprint-tasoinen lähde (B2), mutta käsite on yleispätevä ja looginen |
| Vektorihaku/graafi tarpeen vain osoitetulla tarpeella | **Kohtalainen** — suora empiirinen tuki yhdestä ablaatiotutkimuksesta (B6), tukee toimeksiannon omaa varovaisuusperiaatetta |
| Kaupallisten muistituotteiden (Zep, Mem0) benchmark-luvut | **Heikko/kiistanalainen** — toimittajien keskinäinen benchmark-riita (B7) osoittaa itse lukujen epäluotettavuuden |
| Lethal trifecta / muistin myrkytys -torjunta | **Kohtalainen** — yksi laajasti siteerattu asiantuntijalähde (C1) + yksi osittain lukematta jäänyt paperi (C2) |
| Järjestelmienvälinen (ChatGPT/Copilot) muistin siirrettävyys | **Vahva negatiivinen löydös** — molemmat viralliset dokumentaatiot (D4, D5) vahvistavat ettei vientirajapintaa ole |
