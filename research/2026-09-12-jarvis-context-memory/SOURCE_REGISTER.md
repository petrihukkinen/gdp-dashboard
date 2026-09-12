# Lähderekisteri — Context engineering & persistent memory (Jarvis)

Tutkimuspäivä: **2026-09-12**. Haku- ja lukuympäristö: agenttiverkon egress-välityspalvelin sallii vain rajatun listan verkkotunnuksia (mm. `code.claude.com`, `platform.claude.com`, `github.com`, `huggingface.co` ei; `arxiv.org`, `anthropic.com`, `manus.im`, `trychroma.com`, `simonwillison.net`, `blog.getzep.com`, `web.archive.org`, `help.openai.com`, `learn.microsoft.com`, `genai.owasp.org` estetty). Tämä rajoite kirjattu näkyviin kunkin lähteen kattavuus-kenttään. Missä alkuperäinen sivu ei avautunut, käytetty hakukoneen (WebSearch) synteesiä sekundäärilähteenä — merkitty selvästi, ei esitetä ensikäden lukuna.

Kattavuusluokat: **P** = luettu kokonaan alkuperäisestä lähteestä (WebFetch onnistui). **S** = ei avautunut suoraan; tieto hakukoneen tulossynteesistä (sekundäärinen, ei alkuperäisvarmennettu). **R** = luettu GitHub-repositorion README/issue kokonaan (alkuperäinen, mutta ei tieteellinen julkaisu).

---

## A. Anthropic — viralliset context engineering- ja muistidokumentit

### A1. "Effective context engineering for AI agents" — Anthropic Engineering
- **Tekijä/organisaatio:** Anthropic. **URL:** anthropic.com/engineering/effective-context-engineering-for-ai-agents. **Julkaistu:** 2025 (tarkkaa päivää ei voitu varmentaa, sivu estetty).
- **Tyyppi ja kattavuus:** Virallinen tekninen blogikirjoitus. **S** — alkuperäinen sivu palautti `EGRESS_BLOCKED`; tieto perustuu WebSearch-synteesiin ja useiden riippumattomien tiivistelmien (MachineLearningMastery, Cronus-blogi) yhteneväiseen kuvaukseen, joita ei myöskään voitu itse avata suoraan (samoin estetty).
- **Keskeinen väite ja näyttö:** Context engineering on prompt engineeringin seuraaja: konteksti-ikkuna on rajallinen ja hyvin arvokas resurssi ("context rot" — suorituskyky heikkenee kun kontekstiin kasautuu epäolennaista tai vanhaa tietoa, ei vain kun ikkuna täyttyy). Suositukset: pidä system prompt "oikealla korkeudella" (ei liian tarkka eikä liian yleinen), suunnittele työkalut niin että niiden kuvaukset eivät ole päällekkäisiä, käytä "just-in-time"-hakua (agentti hakee tiedon vasta kun tarvitsee, viitteiden — tiedostopolkujen, URL:ien — kautta) yhdistettynä esihaettuun ydintietoon (hybridi), ja pidä compaction/tiivistämisessä talteen arkkitehtuuripäätökset, ratkaisemattomat virheet ja toteutustason yksityiskohdat, hylkää vanhat työkalutulokset. Rakenteinen muistiinpanojen tekeminen (esim. NOTES.md -tiedosto tai vastaava) mainitaan tapana säilyttää tila kontekstin resetoituessa.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Suoraa lainausta ei voitu varmentaa alkuperäisestä tekstistä — käsittele väitteet suuntaa antavina, ei sanatarkkoina. Soveltuu suoraan Jarviksen kontekstinhallinnan periaatteisiin (progressiivinen lataus, minimimäärä kontekstia per tehtävä).

### A2. Claude Code — "How Claude remembers your project" (Memory-dokumentti)
- **Tekijä/organisaatio:** Anthropic (Claude Code -dokumentaatio). **URL:** code.claude.com/docs/en/memory.
- **Tyyppi ja kattavuus:** Virallinen tuotedokumentaatio. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Claude Code:ssa on kaksi täydentävää muistijärjestelmää: **CLAUDE.md**-tiedostot (käyttäjän kirjoittamat pysyväisohjeet, latautuvat kokonaan joka istunnon alussa hakemistohierarkian mukaisesti — managed > user > project > local, kaikki additiivisia) ja **auto memory** (Claude kirjoittaa itse neljää tyyppiä muistiinpanoja: `user`, `feedback`, `project`, `reference`; tallennus `~/.claude/projects/<project>/memory/`; `MEMORY.md`-indeksi latautuu joka istunnon alkuun ensimmäiset 200 riviä / 25 KB, aihekohtaiset tiedostot luetaan tarpeen mukaan). CLAUDE.md suositellaan alle 200 riviksi; yli 4 MiB tiedosto jätetään lataamatta kokonaan. Compaktion jälkeen projektijuuren CLAUDE.md luetaan levyltä uudelleen ja injektoidaan takaisin — se selviää tiivistämisestä, mutta alikansioiden CLAUDE.md ja polkukohtaiset säännöt eivät automaattisesti palaudu ennen kuin niitä koskeva tiedosto avataan uudelleen.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Auto memory on **konekohtainen** (machine-local) — ei synkronoidu koneiden välillä, ei siis toimi Jarviksen "yksi totuuden lähde"-periaatteen mukaisena pysyvänä varastona useiden laitteiden/järjestelmien (Claude Code, ChatGPT, Copilot) yli. Erittäin relevantti Jarviksen Claude Code -kerroksen suunnitteluun, mutta ei ratkaisu järjestelmienväliseen muistiin.

### A3. Memory tool (Claude API) — "memory_20250818"
- **Tekijä/organisaatio:** Anthropic (Claude Platform -dokumentaatio). **URL:** platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.
- **Tyyppi ja kattavuus:** Virallinen API-dokumentaatio + esimerkkikoodi. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Memory tool on asiakaspään (client-side) työkalu: Claude pyytää tiedosto-operaatioita (`view`, `create`, `str_replace`, `insert`, `delete`, `rename`) `/memories`-hakemistoon, sovellus suorittaa ja palauttaa tuloksen — tallennustila on kokonaan kehittäjän omassa infrastruktuurissa. Tukee "just-in-time"-hakua: agentti ei lataa kaikkea etukäteen, vaan kirjaa oppimansa muistitiedostoihin ja lukee ne tarvittaessa takaisin. Yhdistettynä context editing -ominaisuuteen mittauksissa **29 % suorituskykyparannus** context editingillä yksinään ja **39 %** context editing + memory tool -yhdistelmällä perustilanteeseen verrattuna (luku Anthropicin omasta blogimerkinnästä "Managing context on the Claude Developer Platform" — ei voitu avata suoraan, WebSearch-synteesi; käsiteltävä suuntaa antavana). Turvallisuusohjeistus korostaa polkujen validointia (path traversal -suojaus), tiedostokoon rajoittamista ja herkän tiedon suodattamista ennen kirjoitusta.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Tämä on API-primitiivi, ei valmis tuote — soveltuu suoraan vain jos Jarvis rakennetaan suoraan Claude API:n varaan omalla agenttikehyksellä; Claude Code -käytössä vastaava toiminnallisuus on auto memory / CLAUDE.md, ei tämä työkalu. Malli (client-side, kehittäjän oma tallennus) vahvistaa periaatteen: pysyvä muisti kuuluu sovelluksen/käyttäjän omaan infrastruktuuriin, ei mallin sisään.

### A4. Server-side compaction (Claude API)
- **Tekijä/organisaatio:** Anthropic (Claude Platform -dokumentaatio). **URL:** platform.claude.com/docs/en/build-with-claude/compaction. **Beta-header:** `compact-2026-01-12`.
- **Tyyppi ja kattavuus:** Virallinen API-dokumentaatio. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** API tarkkailee syötetokenien määrää kynnysarvoa vasten (oletus 150 000 tokenia, minimi 50 000), generoi tiivistelmän ja palauttaa `compaction`-lohkon; seuraavilla pyynnöillä API pudottaa kaiken tämän lohkon edeltä sisällön. Oletusprompti säilyttää tilan, seuraavat askeleet ja jatkamiseen tarvittavat opit; mukautetut ohjeet **korvaavat** oletuksen kokonaan. Dokumentti suosittelee nimenomaisesti yhdistämään compactionin muistityökaluun: "compaction keeps the active context small without client-side bookkeeping, and memory preserves the information that must survive summarization."
- **Rajoitukset ja soveltuvuus Jarvikseen:** Vahvistaa arkkitehtuuriperiaatteen: automaattinen tiivistys ja pysyvä muisti ovat **kaksi eri mekanismia eri tarkoituksiin** — tiivistys ei ole korvike validoidulle, hakukelpoiselle pysyvälle tiedolle. Claude Code -käytössä vastaa `/compact`-komentoa; ks. A2 compactionin ja CLAUDE.md:n vuorovaikutuksesta.

### A5. Agent Skills — Skill authoring best practices
- **Tekijä/organisaatio:** Anthropic (Claude Platform -dokumentaatio). **URL:** platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.
- **Tyyppi ja kattavuus:** Virallinen ohjeistus. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Progressiivinen paljastus kolmella tasolla: (1) käynnistyksessä latautuu vain nimi+kuvaus (kymmeniä tokeneita per skilli), (2) SKILL.md-runko latautuu kun skilli aktivoituu, (3) tukitiedostot latautuvat vasta kun niihin viitataan. SKILL.md suositellaan alle 500 riviksi; viittaukset pidettävä yhden tason syvyisinä SKILL.md:stä (ei ketjutettuja viittauksia), sillä agentti saattaa lukea syvät viittausketjut osittaisina (`head -100`). Kuvauskenttä on kriittinen — kirjoitettava kolmannessa persoonassa, sisällytettävä sekä *mitä* että *milloin*.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Suoraan sovellettavissa: projektikohtainen toistettava menettely → skilli (progressiivinen lataus, ei kuluta kontekstia ennen tarvetta); projektikohtainen fakta/päätös → ei skilliin vaan projektin omaan muistiin (CLAUDE.md/muistitiedosto), koska skilli on tarkoitettu menetelmätiedolle, ei muuttuvalle projektidatalle.

### A6. Claude Code — hakkien (hooks) tapahtumaluettelo
- **Tekijä/organisaatio:** Anthropic (Claude Code -dokumentaatio). **URL:** code.claude.com/docs/en/hooks.
- **Tyyppi ja kattavuus:** Virallinen dokumentaatio. **P** — luettu kokonaan (tapahtumataulukko + `SessionStart`/`PreCompact`/`SessionEnd`/`PostCompact` -yksityiskohdat).
- **Keskeinen väite ja näyttö:** `SessionStart` (matchers: startup/resume/clear/compact/fork) ja `UserPromptSubmit` voivat injektoida kontekstia (`additionalContext`); `PreCompact` ja `PostCompact` eivät voi injektoida kontekstia mutta voivat lokittaa/tallentaa tilaa juuri ennen/jälkeen tiivistyksen; `SessionEnd` voi arkistoida transkriptin. Tämä antaa deterministisen (ei promptin varassa olevan) koukun istunnon aloitus- ja lopetusmenettelylle.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Suoraan hyödynnettävä Jarviksen istunnon checkpoint-mekanismiin: `SessionStart`-hook voi pakolla lukea ja injektoida MEMORY.md/CHECKPOINT-tiedoston, `SessionEnd`-hook voi pakolla kirjoittaa sen — tämä on **enforcement**, ei promptivihje, joten se ei riipu mallin muistista tai tulkinnasta.

### A7. Claude Code — Extend Claude Code / "Match features to your goal"
- **Tekijä/organisaatio:** Anthropic (Claude Code -dokumentaatio). **URL:** code.claude.com/docs/en/features-overview.
- **Tyyppi ja kattavuus:** Virallinen dokumentaatio. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Antaa suoran päätöstaulukon CLAUDE.md vs. skill vs. subagent vs. hook vs. MCP: "CLAUDE.md loads every session — persistent context"; "Skill loads on demand — reusable knowledge/workflow"; "Subagent — isolated context that returns summary"; "Hook — deterministic automation on lifecycle event, zero context cost unless it returns output." Nimenomainen sääntö: "A repeated mistake or a recurring review comment is a CLAUDE.md edit, not a one-off correction in chat."
- **Rajoitukset ja soveltuvuus Jarvikseen:** Tämä on Claude Code -spesifinen työnjako, ei yleispätevä muistiarkkitehtuuri — mutta se on suoraan sovellettavissa kysymykseen C ("miten CLAUDE.md, skills, projektitiedostot kannattaa työnjaollisesti järjestää").

### A8. Claude Code — Sessions (transkriptit, resume, export)
- **Tekijä/organisaatio:** Anthropic (Claude Code -dokumentaatio). **URL:** code.claude.com/docs/en/sessions.
- **Tyyppi ja kattavuus:** Virallinen dokumentaatio. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Transkriptit tallentuvat JSONL-muodossa `~/.claude/projects/<project>/<session-id>.jsonl`; sisäinen formaatti muuttuu versioittain — dokumentti nimenomaan varoittaa: "scripts that parse these files directly can break on any release. To build on session data, use `/export` or the script interfaces instead." 30 päivän oletusretentio (`cleanupPeriodDays`).
- **Rajoitukset ja soveltuvuus Jarvikseen:** Tärkeä negatiivinen löydös: **transkriptien raakaformaatti ei ole vakaa integraatioalusta**. Jarviksen ei pidä rakentaa pysyvää muistia parsimaan `.jsonl`-transkriptitiedostoja suoraan, vaan käyttää `/export`-komentoa tai auto memory / CLAUDE.md -mekanismeja tarkoituksellisena tallennuskanavana.

---

## B. Alkuperäiset tutkimuspaperit — pitkäkestoinen agenttimuisti ja kontekstin käyttö

### B1. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory
- **Tekijät:** Di Wu ym. (yhteensä useita tekijöitä, ml. Snap Inc./UCSB-tausta). **Julkaisu:** arXiv:2410.10813, lokakuu 2024; hyväksytty **ICLR 2025**. **URL:** arxiv.org/abs/2410.10813 (peruslähde estetty egress-suodattimessa).
- **Tyyppi ja kattavuus:** Vertaisarvioitu (ICLR 2025) tutkimuspaperi. **R** (GitHub-repo `xiaowu0162/LongMemEval` README luettu kokonaan) + **S** (abstrakti/luvut WebSearch-synteesin varassa, arXiv/ACL Anthology estetty).
- **Keskeinen väite ja näyttö:** 500 kysymystä, viisi muistikykyä: tiedon poiminta, monisessioinen päättely, ajallinen päättely, tiedon päivitys ja **abstaino** (kieltäytyminen vastaamasta kun tietoa ei ole). LongMemEval_S (~115k tokenia, ~40 historiaistuntoa) ja LongMemEval_M-versiot. Väitetty tulos: kaupalliset chat-avustimet ja pitkän kontekstin LLM:t näyttävät **~30 %:n tarkkuuspudotuksen** kun tieto on haudattu pitkään historiaan verrattuna suoraan kysymykseen. Kolmivaiheinen kehys: indeksointi, hakeminen, lukeminen; optimoinnit (istuntojen pilkkominen, fakta-avainten laajennus, ajkohtatietoinen kyselylaajennus) parantavat molempia.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Tämä on **suoraan käyttökelpoinen benchmark-malli** EVALUATION_PLAN.md:aa varten — erityisesti abstaino-kategoria vastaa suoraan toimeksiannon "perusteltu tietoa ei ole -vastaus" -testiin ja tiedon päivitys -kategoria "uuden päätöksen tunnistaminen vanhan korvaajaksi" -testiin. Numeroita (30 % pudotus) ei ole itse varmennettu alkuperäisestä taulukosta — käsiteltävä suuntaa antavana viitelukuna, ei tarkkana faktana.

### B2. Zep: A Temporal Knowledge Graph Architecture for Agent Memory
- **Tekijät:** Preston Rasmussen ym. (Zep AI). **Julkaisu:** arXiv:2501.13956, tammikuu 2025. **URL:** arxiv.org/abs/2501.13956 (estetty).
- **Tyyppi ja kattavuus:** Preprint (ei vertaisarvioitu tiedossa). **R** (GitHub `getzep/graphiti` README luettu kokonaan) + **S** (paperin luvut WebSearch-synteesin varassa).
- **Keskeinen väite ja näyttö:** Graphiti-moottori rakentaa bi-temporaalisen tietograafin (episodi-alagraafi = raa'at tapahtumat aikaleimoin, entiteetti-alagraafi, yhteisö-alagraafi); jokainen fakta kantaa validiteettiaikaikkunan (milloin tuli voimaan, milloin korvattiin) erillään tallennusajasta. Hyödyntää hybridihakua (semanttinen + BM25-avainsana + graafi-BFS). Väitetty tulos DMR-benchmarkissa 94,8 % vs. MemGPT:n 93,4 %; LongMemEvalissa parannuksia ja ~90 % latenssin pienennys pitkän kontekstin lähestymistapaan verrattuna (numerot WebSearch-synteesistä, ei taulukosta varmennettu).
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Merkittävä varoitus (ks. B7):** Zepin LoCoMo-benchmark-tulokset (84 % → riippumattoman haastajan mukaan 58,44 %) ovat kiistanalaisia — käsittele kaikki Zepin itse raportoimat vertailuluvut varauksella. Arkkitehtuurisesti Graphiti vaatii jäsennellyn tulosteen tukevan LLM:n (OpenAI/Anthropic/Gemini-tasoinen), erillisen graafitietokannan (Neo4j/FalkorDB/Neptune) ja ylläpidettävän palvelun — tämä on merkittävä operatiivinen lisäkustannus yhden käyttäjän Jarvis-järjestelmälle. Bi-temporaalinen malli (voimassaoloaika vs. tallennusaika) on käsitteellisesti arvokas ja suoraan lainattavissa MEMORY_DESIGN.md:hen **ilman** että pitää ottaa käyttöön koko graafitietokantaa.

### B3. MemGPT: Towards LLMs as Operating Systems
- **Tekijät:** Charles Packer, Vivian Fang, Shishir G. Patil ym. (UC Berkeley). **Julkaisu:** arXiv:2310.08560, lokakuu 2023. **URL:** arxiv.org/abs/2310.08560 (estetty).
- **Tyyppi ja kattavuus:** Preprint/konferenssipaperi. **R** (GitHub `letta-ai/letta` README luettu, lyhyt) + **S** (paperin sisältö WebSearch-synteesin varassa).
- **Keskeinen väite ja näyttö:** Virtuaalinen kontekstinhallinta käyttöjärjestelmäanalogialla: pääkonteksti (system prompt + työskentelymuisti + FIFO-jono, analogia RAM:iin) ja ulkoinen tallennus (recall storage = hakukelpoinen historia kaikista viesteistä, archival storage = vektori-indeksoitu arkisto). Malli hallitsee omaa muistiaan funktiokutsuilla ("self-editing memory"), keskeytysten (interrupts) avulla ohjataan kontrollivuota käyttäjän ja järjestelmän välillä. Projekti on evoluutioitunut **Lettaksi** — tuotantovalmiiksi kehykseksi PostgreSQL-persistenssillä.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Käyttöjärjestelmäanalogia (työmuisti vs. arkisto) on käsitteellisesti hyödyllinen kysymys B:hen ("mitkä muistityypit kannattaa erottaa"), mutta Letta on **erillinen agenttipalvelu** (oma palvelin, tietokanta, API) — ei kevyt lisäys olemassa olevaan Markdown/Git-työkulkuun. Ei perusteltua tarvetta yhden käyttäjän Jarvikselle ottaa käyttöön koko Letta-palvelinta pelkän muistimallin vuoksi; malli (ei toteutus) on lainattavissa.

### B4. Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)
- **Tekijät:** Adyasha Maharana ym. **Julkaisu:** arXiv:2402.17753, helmikuu 2024; **ACL 2024** (long paper). **URL:** arxiv.org/abs/2402.17753 (estetty).
- **Tyyppi ja kattavuus:** Vertaisarvioitu (ACL 2024). **S** — WebSearch-synteesin varassa, alkuperäistä ei avattu.
- **Keskeinen väite ja näyttö:** LoCoMo-aineisto: erittäin pitkiä keskusteluja (keskimäärin ~600 vuoroa, ~16K tokenia, jopa 32 istuntoa), rakennettu LLM-agenttien persoonaprofiileihin ja ajallisiin tapahtumagraafeihin perustuvalla hybridiputkella, ihmisen kuratoimana. Havainto: mallit kamppailevat pitkän aikavälin ajallisten ja kausaalisten yhteyksien kanssa; pitkä konteksti / RAG parantaa mutta jää selvästi ihmistasosta.
- **Rajoitukset ja soveltuvuus Jarvikseen:** LoCoMo on ollut keskeinen **kiistanalainen** benchmark (ks. B7 — Zep vs. Mem0 -kiista laskentavirheistä), ja lisäksi CogCanvas-tutkimus (B8) osoittaa menetelmällisiä heikkouksia LoCoMo:n hyödyntämisessä. Käytettävissä ideana ("pitkä, moni-istuntoinen, ajallisesti sidottu keskustelu on vaikea testitapaus"), ei numeroiden lähteenä.

### B5. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- **Tekijät:** Mem0-tiimi (ml. Deshraj Yadav, Taranjeet Singh ym.). **Julkaisu:** arXiv:2504.19413, huhtikuu 2025; **ECAI 2025**. **URL:** arxiv.org/abs/2504.19413 (estetty).
- **Tyyppi ja kattavuus:** Vertaisarvioitu (ECAI 2025) + avoimen lähdekoodin toteutus. **R** (GitHub `mem0ai/mem0` README luettu kokonaan, ~65 200 tähteä, Apache-2.0) + **S** (paperin luvut).
- **Keskeinen väite ja näyttö:** Kaksivaiheinen LLM-pohjainen poiminta+päivitys, vektorivarasto, valinnainen tietograafi. Väitetty LoCoMo-tulos 67,13 % (uudempi versio 92,5, +21 pistettä), LongMemEval 94,4 (+27 pistettä), p95-hakuviive 0,2 s käyttäen ~1 764 tokenia keskustelua kohti (vs. 26 031 koko kontekstin lähestymistavassa).
- **Rajoitukset ja soveltuvuus Jarvikseen:** Nämä ovat **valmistajan omia lukuja** — ks. B7, sama koskee Mem0:aa kuin Zepiä: kaupallisten toimijoiden itse raportoimia benchmark-tuloksia on syytä kohdella markkinointiväitteinä kunnes riippumaton toisto vahvistaa. Arkkitehtuurisesti vaatii LLM:n + upotusmallin + vektoritietokannan — samat operatiiviset varaukset kuin Zepillä. Ei perusteltua tarvetta Jarvikselle nykyisessä mittakaavassa (yksi käyttäjä, ei miljoonia muistoja).

### B6. CogCanvas / "Verbatim Chunks Beat Extracted Artifacts: A Controlled Ablation of Memory Representations for Long LLM Conversations"
- **Tekijät:** ei varmennettu (arXiv-tunnisteen 2601.00821 metatiedot eivät avautuneet suoraan). **Julkaisu:** arXiv:2601.00821 (v2/v3), 2026. **URL:** arxiv.org/abs/2601.00821 (estetty).
- **Tyyppi ja kattavuus:** Preprint (2026, ei vielä vertaisarvioitua venue-tietoa saatavilla). **S** — WebSearch-synteesin varassa.
- **Keskeinen väite ja näyttö:** Kontrolloitu ablaatiokoe, jossa vaihdettiin **vain** tallennettu representaatio (LLM:n poimimat jäsennellyt artefaktit vs. sanatarkat keskusteluosuudet) pitäen haku-rerank-päättely-putken muuten vakiona. Tulos: sanatarkat pätkät voittivat jäsennellyt artefaktit **15,9 pistettä** LoCoMossa (43,9 % vs. 28,0 %) ja **22,0 pistettä** LongMemEval-S:ssä (67,4 % vs. 45,4 %); 1-hop semanttinen graafi ei kuronut eroa umpeen. Mekanismi: poiminta on häviöllistä tiivistystä, joka hukkaa sanatarkkaa yksityiskohtaa, jonka raaka pätkä säilyttää ilmaiseksi.
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Erittäin relevantti löydös kysymykseen "miten estetään AI:n oman tulkinnan muuttuminen näennäiseksi faktaksi".** Tukee suoraan toimeksiannon suunnitteluperiaatetta erottaa alkuperäisaineisto ja tulkinta: säilytä alkuperäinen sanamuoto (raakateksti/lähdedokumentti) rinnalla tiivistelmän/poiminnan kanssa, älä korvaa sitä. Yksi preprint, ei toistettu riippumattomasti — käsiteltävä vahvana viitteenä, ei lopullisena totuutena.

### B7. Zep vs. Mem0 -benchmarkkiaisto (LoCoMo-tulosten luotettavuus)
- **Lähteet:** GitHub-issue `getzep/zep-papers#5` (Deshraj/Mem0, 8.5.2025) + Zepin oma vastineblogi "Is Mem0 Really SOTA in Agent Memory?" (blog.getzep.com, estetty — S). **Tyyppi:** avoin tekninen kiista/keskustelu kahden kilpailevan kaupallisen tuotteen välillä.
- **Kattavuus:** **R** (GitHub-issue luettu kokonaan sisältöineen) + **S** (Zepin vastineblogi, ei avautunut).
- **Keskeinen väite ja näyttö:** Mem0 väittää Zepin ilmoittaman 84 %:n LoCoMo-tuloksen olevan väärä laskentavirheen takia (nimittäjä sulki pois kategoria-5-kysymykset mutta osoittaja sisälsi ne); korjattu luku olisi 58,44 % ± 0,20. Zep kiistää ja väittää oman korjatun luvun olevan 75,14 %. Kumpikaan osapuoli ei ole riippumaton arvioija.
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Metodologinen opetus tälle koko tutkimukselle**: kaupallisten muistituotteiden itse julkaisemat benchmark-luvut (LoCoMo, LongMemEval) ovat systemaattisesti epäluotettavia ja kiistanalaisia toimittajien kesken. Tämä on suora perustelu toimeksiannon vaatimukselle "älä esitä suunniteltuja testejä tehtyinä tai julkaistuja benchmark-tuloksia todisteena Jarviksen suorituskyvystä" — samat varaukset koskevat myös näitä kolmannen osapuolen lukuja.

### B8. Lost in the Middle: How Language Models Use Long Contexts
- **Tekijät:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang (Stanford). **Julkaisu:** **TACL 2024**, vol. 12, s. 157–173. **URL:** aclanthology.org/2024.tacl-1.9 (estetty).
- **Tyyppi ja kattavuus:** Vertaisarvioitu (Transactions of the ACL). **S** — WebSearch-synteesin varassa, alkuperäistä ei avattu.
- **Keskeinen väite ja näyttö:** U-muotoinen suorituskykykäyrä: mallit käyttävät relevanttia tietoa parhaiten kun se on kontekstin alussa tai lopussa, heikommin keskellä — pätee myös eksplisiittisesti pitkän kontekstin malleille. Havaittu monidokumenttikysymysvastauksessa ja avain-arvo-hakutehtävässä.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Perustavanlaatuinen, laajasti siteerattu tulos (2023–2024). Vaikka malliarkkitehtuurit ovat kehittyneet, sijainnin vaikutus on toistettu tuoreemmassa Context Rot -tutkimuksessa (B9) — tukee molemmin puolin periaatetta "pienin riittävä konteksti tehtävän ratkaisemiseen", ei "kaikki mahdollisesti relevantti kontekstiin".

### B9. Context Rot: How Increasing Input Tokens Impacts LLM Performance
- **Tekijät:** Kelly Hong, Anton Troynikov, Jeff Huber (Chroma). **Julkaisu:** heinäkuu 2025 (Chroma-tekninen raportti). **URL:** research.trychroma.com/context-rot (estetty); koodirepo github.com/chroma-core/context-rot.
- **Tyyppi ja kattavuus:** Toimittajan (vektoritietokantayritys) julkaisema tekninen raportti, ei vertaisarvioitu tiedejulkaisu. **R** (GitHub-repon README luettu kokonaan) + **S** (täysi raportti estetty).
- **Keskeinen väite ja näyttö:** 18 mallia (GPT-4.1, Claude 4 -sarja, Gemini 2.5, Qwen3 ym.) testattu kontrolloiduilla kokeilla: suorituskyky heikkenee mitattavasti syötteen pituuden kasvaessa **jo kauan ennen** kontekstiraja täyttyy, ja heikkeneminen riippuu epäyhtenäisesti tarpeeton-relevantti-samankaltaisuudesta, häiriötekijöiden läsnäolosta ja "haystack"-rakenteesta. 200K-ikkunan malli voi näyttää merkittävää heikkenemistä jo ~50K tokenin kohdalla.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Toimittaja (Chroma myy vektoritietokantaa) — mahdollinen intressiristiriita raportin kehystyksessä ("konteksti-insinöörointi ja haku on tärkeämpää kuin koskaan" tukee heidän tuotettaan), mutta itse mittausmenetelmä (avoin koodi, toistettavissa) on vahva. Vahvistaa toimeksiannon periaatteen: pitkä konteksti ja häiritsevä tieto heikentävät suoritusta — tue tätä pitämällä kontekstibudjetti pienenä ja relevanttina, ei luottamalla "laita kaikki kontekstiin, malli kyllä löytää sen" -strategiaan.

---

## C. Muut merkittävät mallikehittäjät / turvallisuus

### C1. The Lethal Trifecta (Simon Willison)
- **Tekijä:** Simon Willison (riippumaton tutkija/kehittäjä, laajasti siteerattu AI-agenttiturvallisuudessa). **Julkaisu:** 16.6.2025. **URL:** simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (estetty).
- **Tyyppi ja kattavuus:** Asiantuntijablogi, ei vertaisarvioitu, mutta laajasti siteerattu toimialalla (mm. useissa turvallisuustoimittajien analyyseissa: HiddenLayer, Cyera, Promptfoo). **S** — WebSearch-synteesin varassa.
- **Keskeinen väite ja näyttö:** Kolmen ominaisuuden yhdistelmä samassa agenttisessiossa on vaarallinen: (1) pääsy yksityiseen dataan, (2) altistus luottamattomalle sisällölle, (3) kyky viestiä ulos. Kaikki kolme yhdessä mahdollistavat promptinjektiolla toteutetun tietovuodon ilman perinteistä haavoittuvuutta. Suositus: pidä vähintään yksi kolmesta poissa käytöstä samassa istunnossa.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Suoraan sovellettavissa kysymykseen D ("miten ulkoisesta aineistosta tuleva prompt injection estetään muuttumasta pysyväksi ohjeeksi tai muistiksi"). Jarvis-arkkitehtuurissa: kun agentti lukee ulkoista, luottamattomasti sisältöä (web-hakutulos, sähköposti) JA kirjoittaa pysyvään muistiin JA voi lähettää viestejä ulos — kolmikko täyttyy. Ratkaisu ei ole detektio (Willison: 99 % tunnistustarkkuus ei riitä agenttikontekstissa, koska yksi läpipäässyt hyökkäys riittää) vaan rakenteellinen erottelu: ulkoinen sisältö luokitellaan aina dataksi, ei ohjeeksi, ja pysyvään muistiin kirjoittaminen ulkoisen sisällön perusteella vaatii erillisen, rajatun hyväksymisportin.

### C2. "From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents"
- **Tekijät:** ei varmennettu nimeltä (arXiv:2606.04329). **Julkaisu:** arXiv, 2026. **URL:** arxiv.org/pdf/2606.04329 (estetty).
- **Tyyppi ja kattavuus:** Preprint. **S** — vain WebSearch-tuloslistauksen otsikko ja lyhyt kontekstilause nähty, ei sisältöä luettu.
- **Keskeinen väite ja näyttö (WebSearch-koosteen mukaan, muualla siteerattuna):** Muistin myrkyttäminen eroaa perinteisestä promptinjektiosta siinä, että haitallinen sisältö on semanttisesti erottamaton laillisesta sisällöstä — puolustus on rakennettava kirjoitusreitille (write path), ei syöttörajalle (input boundary). Pysyvät kontekstit (CLAUDE.md, muistihakemistot) ovat riskialttiita koska ne ladataan uudelleen joka käynnistyksellä.
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Merkitty osittain lukemattomaksi** — vain otsikko ja tiivistelmäkatkelma nähty, ei koko paperia. Käytä ideaa varovasti: se on linjassa C1:n kanssa ja tukee MEMORY_DESIGN.md:n validointiportin tarvetta, mutta ei ole itsenäisesti varmennettu tässä tutkimuksessa.

### C3. Claude Code — Security-dokumentti (promptinjektion suojaukset)
- **Tekijä/organisaatio:** Anthropic. **URL:** code.claude.com/docs/en/security. **Tyyppi:** virallinen dokumentaatio. **P** — luettu kokonaan.
- **Keskeinen väite ja näyttö:** Luottamattoman sisällön kanssa työskentelyn parhaat käytännöt: tarkista ehdotetut komennot, vältä luottamattoman sisällön suoraa putkittamista Claudelle, käytä VM-eristystä ulkoisten web-palveluiden kanssa. Verkkokomennot (`curl`, `wget`) eivät ole automaattisesti hyväksyttyjä. MCP-palvelimet luetteloidaan lähdekoodissa versionhallinnassa — Anthropic ei tietoturvatarkasta kolmannen osapuolen MCP-palvelimia.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Antaa konkreettisen, toteutettavan perustan Jarviksen käyttöoikeus- ja tietoturvakäytännölle (kysymys D), erityisesti MCP-integraatioiden (Copilot, muut järjestelmät) osalta.

---

## D. Käytännön toteutukset / tuotantokäytön kuvaukset

### D1. Effective harnesses for long-running agents (Anthropic) + `anthropics/cwc-long-running-agents`
- **Tekijä/organisaatio:** Anthropic (Justin Young, 26.11.2025 alkuperäinen blogi; GitHub-repo julkaistu Code with Claude 2026 -tapahtumaa varten). **URL:** anthropic.com/engineering/effective-harnesses-for-long-running-agents (estetty, S) + github.com/anthropics/cwc-long-running-agents (**R**, luettu kokonaan).
- **Tyyppi ja kattavuus:** Virallinen tekninen blogi + avoin esimerkkikoodi. Repo: **R**, täysi README-luku.
- **Keskeinen väite ja näyttö:** Kaksiosainen malli: alustaja-agentti (initializer) perustaa ominaisuuslistan (feature list, JSON), git-repositorion ja edistymistiedoston (`claude-progress.txt`/`PROGRESS.md`); koodausagentit tekevät asteittaista edistystä yksi ominaisuus kerrallaan, säilyttäen puhtaan tilan git-committeina ja rakenteisina dokumentteina. Repo lisää kolme konkreettista mekanismia: **default-FAIL-sopimus** (jokainen ominaisuus alkaa `passes: false`, `PreToolUse`-hook estää tulosten kirjoittamisen ennen kuin agentti on avannut todisteen), **tuore konteksti -arvioija** (erillinen subagentti, ei Write/Edit-työkaluja, arvioi committin puhtaalta pöydältä), ja **agentin ylläpitämä siirto** (`CLAUDE.md` + `PROGRESS.md` + commit-on-stop-hook). Periaate: "ominaisuus merkitään valmiiksi vain päästä-päähän-varmennuksen jälkeen, ei kun koodi on kirjoitettu."
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Suoraan sovellettavissa istunnon checkpoint- ja aloitusmenettelyyn** (kysymys B: "miten istunnon checkpoint ja seuraavan istunnon aloitus toteutetaan"). Malli on suunniteltu ohjelmistokehitysagenteille (git-committit tilana), mutta periaate — rakenteellinen "valmis"-tila tiedostossa + riippumaton varmennus + git historia tilan lähteenä — siirtyy suoraan Jarviksen päätösten/tehtävien elinkaareen.

### D2. Manus — "Context Engineering for AI Agents: Lessons from Building Manus"
- **Tekijä/organisaatio:** Manus (tuotantoagenttiyritys). **URL:** manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus (estetty). **Julkaisu:** 2025 (tarkkaa päivää ei varmennettu).
- **Tyyppi ja kattavuus:** Tuotantokäytön tekninen blogi. **S** — WebSearch-synteesin varassa, useiden riippumattomien tiivistelmien (Medium, dev.to, Lance Martinin blogi) yhtenevä kuvaus, joita ei myöskään voitu avata suoraan.
- **Keskeinen väite ja näyttö:** KV-cache-osumasuhde on tuotantoagentin tärkein yksittäinen mittari (Manuksen syöte:tuloste-suhde ~100:1; välimuistista löytyvä token voi olla ~10× halvempi kuin uusi). Käytännöt: pidä promptin alkuosa vakiona, älä muokkaa aiempia toimia/havaintoja jälkikäteen, peitä (mask) työkaluja logittien tasolla poistamisen sijaan (skeeman rikkoutumisen ja välimuistin hukkaamisen estämiseksi), käytä tiedostojärjestelmää rajattomana, palautettavana kontekstina (tiivistä pudottamalla sisältö mutta säilytä viite/polku, jotta se on palautettavissa), "toista" tavoite (esim. todo.md) manipuloidaksesi mallin huomiota pitkissä tehtävissä, ja säilytä virheet/epäonnistuneet yritykset kontekstissa piilottamisen sijaan, jotta malli oppii niistä.
- **Rajoitukset ja soveltuvuus Jarvikseen:** Ei alkuperäistekstiä varmennettu suoraan — käsittele suuntaa antavana. Tiedostojärjestelmä-kontekstina-periaate (palautettava tiivistys: pudota sisältö, säilytä viite) on suoraan sovellettavissa MEMORY_DESIGN.md:n compaction-käytäntöön ja tukee B6:n havaintoa (säilytä alkuperäinen, viittaa siihen).

### D3. Karpathyn "LLM wiki" -malli
- **Tekijä:** Andrej Karpathy (laajasti tunnettu ML-tutkija). **Julkaisu:** huhtikuu 2026 (X-julkaisu + GitHub Gist). **URL:** ei yksittäistä pysyvää dokumenttia — malli levinnyt useiden riippumattomien toteutusten kautta (esim. `Astro-Han/karpathy-llm-wiki`).
- **Tyyppi ja kattavuus:** Käytäntöyhteisön leviämä malli, ei virallinen julkaisu. **S** — vain WebSearch-koosteiden varassa, ei yhtä kanonista lähdettä luettu kokonaan.
- **Keskeinen väite ja näyttö:** Kolmikerroksinen rakenne: `raw/` (muuttumattomat alkuperäislähteet), `wiki/` (LLM:n ylläpitämät koostesivut), `CLAUDE.md`/skeema (säännöt). Kolme perusoperaatiota: `ingest` (uuden lähteen käsittely), `query` (kysymys viitteillä), `lint` (eheystarkistus). Periaate: "järjestelmä kumuloituu — jokainen uusi lähde tekee koko wikin älykkäämmäksi", ja se korvaa perinteisen RAG:n pysyvällä, agentin ylläpitämällä Markdown-kannalla.
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Käsitteellisesti tärkein yksittäinen löydös toimeksiannon suunnitteluperiaatteille.** `raw/` vs. `wiki/` -erottelu vastaa suoraan toimeksiannon vaatimusta erottaa alkuperäisaineisto ja tulkinta, ja `lint`-operaatio vastaa eheystarkistusta (ristiriidat, roikkuvat viitteet). Ei ole yhtä kanonista, luotettavaa alkuperäislähdettä (malli on levinnyt sekundäärisesti) — käsittele arkkitehtonisena inspiraationa, ei valmiina spesifikaationa.

### D4. OpenAI ChatGPT — Memory FAQ
- **Tekijä/organisaatio:** OpenAI. **URL:** help.openai.com/en/articles/8590148-memory-faq (estetty). **Tyyppi:** virallinen tuki-/FAQ-dokumentaatio. **S** — WebSearch-synteesin varassa.
- **Keskeinen väite ja näyttö:** Kaksi erillistä mekanismia: "saved memories" (eksplisiittisesti tallennetut/mallin päättelemät yksityiskohdat, hallittavissa erikseen) ja "chat history reference" (laajempi viittaus koko keskusteluhistoriaan). Poistettu keskustelu ei automaattisesti poista siitä syntynyttä tallennettua muistoa — se on poistettava erikseen muistinhallinnasta. Temporary Chat ei käytä eikä päivitä muistia.
- **Rajoitukset ja soveltuvuus Jarvikseen:** **Kriittinen negatiivinen löydös kysymykseen C** ("mitä voidaan siirtää järjestelmien välillä"): ChatGPT:n muisti on OpenAI:n oma, tilikohtainen palvelu — ei ole dokumentoitua vientimekanismia strukturoituun, siirrettävään muotoon (vain koko tilin data-export, ei valikoiva). Jarvis **ei voi olettaa** saavansa ChatGPT:n muistia ohjelmallisesti ulos; integraatio olisi manuaalinen (käyttäjä kopioi/liittää) tai ei-toteutettavissa nykyisillä julkisilla rajapinnoilla tämän tutkimuksen perusteella.

### D5. Microsoft 365 Copilot — Memory ja personointi
- **Tekijä/organisaatio:** Microsoft. **URL:** learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory (estetty). **Tyyppi:** virallinen dokumentaatio. **S** — WebSearch-synteesin varassa.
- **Keskeinen väite ja näyttö:** Copilot-muisti (tallennetut muistot + päätellyt yksityiskohdat + mukautetut ohjeet) tallennetaan käyttäjän **Exchange-postilaatikon piilokansioon** ja noudattaa samoja tietoturva-/compliance-käytäntöjä kuin muu postilaatikkodata (Customer Lockbox, salaus levossa). Hallinta admin- ja käyttäjätasolla, oletuksena päällä ("Enhanced personalization").
- **Rajoitukset ja soveltuvuus Jarvikseen:** Vahvistaa toimeksiannon varoituksen: **ei pidä olettaa yritysten Copilotin muistin olevan avoimesti API:n kautta siirrettävissä** — se on sidottu Microsoft 365 -tenantin postilaatikkorakenteeseen ja yrityksen compliance-kehykseen. Jarvis-integraatio Copilotiin (jos/kun toteutuu) vaatii erillisen, todennetun rajapinnan (Microsoft Graph -tason), ei tiedostopohjaista jakoa — tämä pitää varmentaa erikseen ennen kuin sitä rakennetaan.

---

## Lähteet, joita ei voitu avata / lukea (merkitty lukemattomiksi)

Seuraavat lähteet nousivat hauissa relevanteiksi mutta **egress-verkkosuodatin esti pääsyn eikä sisältöä voitu vahvistaa alkuperäisestä** — mainittu tekstissä ainoastaan WebSearch-tulosten koosteiden perusteella, ei käytetty numeerisena todisteena:
- `anthropic.com/engineering/*` (context engineering -blogi, harnesses-blogi)
- `arxiv.org/*`, `aclanthology.org/*`, `openreview.net/*`, `huggingface.co/papers/*` (kaikki alkuperäispaperit)
- `trychroma.com`, `research.trychroma.com` (Context Rot -täysraportti)
- `manus.im` (alkuperäinen Manus-blogi)
- `simonwillison.net` (alkuperäinen "lethal trifecta" -kirjoitus)
- `blog.getzep.com` (Zepin oma vastineblogi ja alkuperäinen Zep-julkistus)
- `help.openai.com`, `learn.microsoft.com` (OpenAI/Microsoft viralliset tukisivut)
- `genai.owasp.org` (OWASP LLM Top 10 -sivut promptinjektiosta ja vektoriheikkouksista)
- `web.archive.org` (ei tavoitettavissa lainkaan tässä ympäristössä)

**Varmennusaukko:** Näiden osalta suositellaan, että joku, jolla on avoimempi verkkopääsy, vahvistaa vähintään B1 (LongMemEval), B2 (Zep), B6 (CogCanvas) ja A1 (Anthropicin context engineering -blogi) suorista alkuperäislähteistä ennen kuin niiden numeroita käytetään päätöksenteon perusteena tuotantoarkkitehtuurille.
