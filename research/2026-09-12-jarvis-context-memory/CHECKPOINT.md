# Checkpoint — Jarvis context engineering & persistent memory -tutkimus

Päivitetty: 2026-09-12 (istunnon jatko mallinvaihdon jälkeen, claude-sonnet-5).

## Valmis työ

Kaikki toimeksiannon seitsemän tuotostiedostoa on kirjoitettu hakemistoon `research/2026-09-12-jarvis-context-memory/`:

- [x] `README.md` — pääsuositus, tiedostokartta, tutkimuksen rajat, loppuyhteenveto
- [x] `RESEARCH_REPORT.md` — kysymykset A–D vastattu, joka alakohdassa "lähteet osoittavat / päättelen / ehdotan / testattava vielä" -erottelu
- [x] `SOURCE_REGISTER.md` — 30 lähdettä (A1–D5) + erillinen lista lukemattomiksi merkityistä lähteistä
- [x] `ARCHITECTURE_OPTIONS.md` — A/B/C-vertailu 8 kriteerillä + laukaisuehtotaulukko
- [x] `MEMORY_DESIGN.md` — hakemistorakenne, YAML-skeema, tietovirta, ristiriitakäytäntö, checkpoint-menettely, MVP
- [x] `EVALUATION_PLAN.md` — T1–T9, baseline, ennalta määritellyt hyväksymiskriteerit
- [x] `IMPLEMENTATION_BACKLOG.md` — vaiheistettu backlog + laukaisuehdot laajennuksille

Tutkimusvaihe (verkkohaku + lukeminen) valmis: Anthropicin viralliset Claude Code/Claude-alustadokumentit (muisti, compaction, skills, security, hooks, sessiot, features-overview) luettu kokonaan. GitHub-repot (Graphiti, LongMemEval, Letta, Mem0, `cwc-long-running-agents`, context-rot, zep-papers/issues) luettu README/issue-tasolla.

## Keskeneräinen työ

Ei mitään keskeneräistä toimeksiannon vaatiman skoopin sisällä. Mahdollinen jatkotyö (ei osa tätä tehtävää):
- Varsinainen koodi/toteutus `IMPLEMENTATION_BACKLOG.md`:n Vaiheesta 1 alkaen — tarkoituksella ei toteutettu tässä tehtävässä ("toteutusmuutokset tehdään erillisenä tehtävänä").
- Käyttäjän oman `~/.claude/`-ympäristön ja mahdollisen olemassa olevan Jarvis-repon tarkistus — ei saatavilla tässä puhtaassa tutkimuskontissa.

## Luetut keskeiset lähteet (kattavuus P/R = vahva, S = hakusynteesi)

**P (täysin luettu alkuperäislähde):** Claude Code Memory-dokumentti, Memory tool -API-dokumentti, Server-side compaction -dokumentti, Skill authoring best practices, Claude Code Skills quick reference, Security-dokumentti, Hooks-tapahtumaluettelo, Sessions-dokumentti, Features overview / Extend Claude Code.

**R (GitHub repo/issue luettu kokonaan):** `getzep/graphiti`, `xiaowu0162/LongMemEval`, `letta-ai/letta`, `mem0ai/mem0`, `anthropics/cwc-long-running-agents`, `chroma-core/context-rot`, `getzep/zep-papers` (+ issue #5).

**S (hakusynteesin varassa — merkitty lukemattomiksi täydellä varmuudella):** Anthropicin "Effective context engineering" ja "Effective harnesses" -blogit, kaikki arXiv/ACL-paperit suoraan (LongMemEval, Zep, MemGPT, LoCoMo, Mem0, CogCanvas, Lost in the Middle), Chroma Context Rot -täysraportti, Manus-blogi, Simon Willisonin lethal trifecta -kirjoitus, Zepin vastineblogi, OpenAI Memory FAQ, Microsoft Copilot memory -dokumentti, OWASP LLM01/LLM08.

## Todetut esteet

1. **Egress-välityspalvelimen verkkosuodatin** esti seuraavat verkkotunnukset koko istunnon ajan: `anthropic.com`, `arxiv.org`, `aclanthology.org`, `openreview.net`, `huggingface.co`, `api.semanticscholar.org`, `trychroma.com`, `manus.im`, `simonwillison.net`, `blog.getzep.com`, `help.openai.com`, `learn.microsoft.com`, `genai.owasp.org`, `web.archive.org`, `machinelearningmastery.com`, `cr0nu3.github.io`, `dev.to`, `rlancemartin.github.io`. Tarkistettu `curl $HTTPS_PROXY/__agentproxy/status` — kyseessä on organisaation politiikka, ei tilapäinen virhe; ei yritetty kiertää.
2. **Ei ollut olemassa olevaa Jarvis-toteutusta tai CLAUDE.md/AGENTS.md-tiedostoa** tarkistettavana tässä konttiympäristössä — annettu repo (`gdp-dashboard`) on tähän tutkimustehtävään osoitettu, ei Jarviksen oma.
3. **Mallinvaihto istunnon aikana** (claude-fable-5-1 → claude-sonnet-5, käyttäjän oma `/model`-komento) keskeytti alkuperäisen tutkimuksen ennen tuotostiedostojen kirjoittamista. Tuore kontti ei sisältänyt aiempaa CHECKPOINT-tiedostoa — kaikki aiemmin kerätty tutkimusaineisto oli vain keskusteluhistoriassa, ei levyllä. Tämä ratkaistiin käyttämällä keskusteluhistoriassa jo kerättyä aineistoa suoraan tuotostiedostojen kirjoittamiseen, ei aloittamalla hakuja alusta.

## Seuraava konkreettinen työvaihe

1. Commit + push branchille `claude/jarvis-memory-context-research-0qoa07`.
2. Jos käyttäjä haluaa jatkaa: vahvista `IMPLEMENTATION_BACKLOG.md`:n Vaihe 0.2 (S-merkityt lähteet avoimemmalla verkkoyhteydellä) ennen tuotantopäätöksiä, tai etene suoraan Vaiheeseen 1 (MVP-toteutus) erillisenä tehtävänä.

## Tulostiedostojen sijainnit

Kaikki: `/home/user/gdp-dashboard/research/2026-09-12-jarvis-context-memory/` (sama repositorio, branch `claude/jarvis-memory-context-research-0qoa07`):
`README.md`, `RESEARCH_REPORT.md`, `SOURCE_REGISTER.md`, `ARCHITECTURE_OPTIONS.md`, `MEMORY_DESIGN.md`, `EVALUATION_PLAN.md`, `IMPLEMENTATION_BACKLOG.md`, `CHECKPOINT.md` (tämä tiedosto).

---

## Päivitys 2026-09-12 (myöhempi istunto): Phase 1 toteutettu

`IMPLEMENTATION_BACKLOG.md`:n Vaihe 1 (vähimmäistoteutus) on toteutettu ja committoitu tälle samalle branchille, commit `64dab81`. Toteutus poikkeaa hieman tämän tutkimuksen `MEMORY_DESIGN.md`-ehdotuksesta (litteä `KNOWLEDGE/` tyyppikentällä alikansioiden sijaan, `RAW/INGEST/KNOWLEDGE/INDEX/EVALS`-nimeäminen) — jatkotehtävän oma, tarkempi kohdehakemistorakenne korvasi tämän tutkimuksen alkuperäisen ehdotuksen, periaatteet (yksi lähde, johdettu indeksi, lähdejäljitettävyys) säilyivät samoina.

Sijainti: `/home/user/gdp-dashboard/PETRI-JARVIS-SYSTEM/` (oma `README.md` selittää arkkitehtuurin, ajokomennot ja rajoitukset). Vaiheet 0.2, 2, 3, 4 (lähteiden vahvistus avoimemmalla verkkoyhteydellä, istunnon hook-kytkennät, validointiportti, evaluaatioajo oikealla datalla) ovat edelleen tekemättä — kirjattu `PETRI-JARVIS-SYSTEM/README.md`:n "Known limitations" -kohtaan.

---

## Päivitys 2026-09-12 (Phase 1.1 kovennustarkistus)

Kovennustarkistus paljasti ja korjasi rajaongelman: `PETRI-KNOWLEDGE/`-hakemisto sekoitti järjestelmän (skriptit, testit) ja kanonisen tiedon paikan (RAW/INGEST/KNOWLEDGE-kansiot) samaan puuhun, samalla nimellä kuin itse tietovarasto. `list_repos`-tarkistus vahvisti: käyttäjän GitHub-tilillä ei ole erillistä `PETRI-KNOWLEDGE`- tai `PETRI-JARVIS-SYSTEM`-repositoriota — molemmat ovat vasta suunnitelmatasolla.

Korjaus: hakemisto nimettiin uudelleen `PETRI-JARVIS-SYSTEM`:ksi, ja siitä poistettiin RAW/INGEST/KNOWLEDGE/INDEX-kansiot kokonaan (skeema siirrettiin puhtaaksi dokumentaatioksi `docs/KNOWLEDGE_FORMAT.md`:hen). Skriptit vaativat nyt eksplisiittisen `--root`-parametrin tai `PETRI_JARVIS_KNOWLEDGE_ROOT`-ympäristömuuttujan — ei enää oletusarvoa omaan hakemistoonsa. Todellista erillistä holvia ei luotu (Petrin oma päätös, ei tehty tässä tarkistuksessa).

Lisäksi: laajennettu synteettinen (ei todellinen — todellista Jarvis-tietoa ei ollut saatavilla) arviointikorpus 16 kysymyksellä, joista mitattiin suomen kielen taipumuksen käyttäytyminen suoraan (ei arvailtu) — tulokset ja rajat kirjattu `PETRI-JARVIS-SYSTEM/README.md`:n "Finnish search: measured, not assumed" -kohtaan. Kaikki 26 testiä (10 Phase 1 + 16 Phase 1.1) menivät läpi.

---

## Päivitys 2026-09-13: repositorioiden erottelu ja pysyvyystarkistus

**Valmis työ:**
- Auditoitu `gdp-dashboard`: Jarvis-työ osoittautui täysin erilliseksi alkuperäisestä dashboard-sovelluksesta (ei yhtään yhteistä tiedostoa `main`-haaran kanssa).
- Luotu paikallisesti kaksi erillistä Git-repositoriota tämän konttiympäristön levylle: `/home/user/PETRI-JARVIS-SYSTEM` (koodi, skeema, testit, tutkimus — commit `6bc6ee3`) ja `/home/user/PETRI-KNOWLEDGE` (RAW/INGEST/KNOWLEDGE/INDEX-holvi, 9 aidon mutta ei-arkaluontoisen pilottimerkinnän kanssa, commitit `b636f48` ja `2872807`).
- Vahvistettu mittauksin (`hostname`, `mount`, `df`, ympäristömuuttujat `CLAUDE_CODE_REMOTE=true` ym.), että tämä istunto ajaa pilvipohjaisessa, väliaikaisessa VM-hiekkalaatikossa, ei Petrin omalla koneella — kumpikaan uusi paikallinen repo ei säily kontin uudelleenkäynnistyksen yli, koska niillä ei ole Git-remotea.
- Loppuauditointi salaisuuksista/Bilfinger-sisällöstä molemmissa uusissa repoissa: puhdas.

**Keskeneräinen työ / esteet:**
- GitHub-repositorioiden luonti (`PETRI-JARVIS-SYSTEM`, `PETRI-KNOWLEDGE`) epäonnistui: `mcp__github__create_repository` palautti `403 Resource not accessible by integration` molemmille. Tämä on istunnon GitHub-integraation oikeusrajoitus (repositorion *luontiin*, ei push-oikeuteen olemassa oleviin repoihin — `gdp-dashboard`-push toimii edelleen normaalisti). Ei yritetty kiertää.
- Kumpaakaan uutta repoa **ei ole pushattu minnekään** — ne ovat toistaiseksi vain tämän väliaikaisen kontin levyllä.
- Petrille annettu kaksi vaihtoehtoa: (a) hän luo tyhjät yksityiset repot itse GitHubissa, jonka jälkeen push onnistuu suoraan, tai (b) GitHub-yhteys yhdistetään uudelleen laajemmin oikeuksin (claude.ai → Settings → Connectors).

**Seuraava konkreettinen työvaihe:** odotetaan Petrin päätöstä yllä olevista vaihtoehdoista (a)/(b). Kun repo(t) on luotu, push on yhden komennon toimenpide (remote lisätty, historia valmiina paikallisesti).

**Tulostiedostojen sijainnit (tässä konttiympäristössä, ei pysyviä):**
`/home/user/PETRI-JARVIS-SYSTEM/` ja `/home/user/PETRI-KNOWLEDGE/` — molemmat menetetään kontin kierrätyksessä, jos niitä ei pushata ennen sitä. `gdp-dashboard`-repositorio (tämä tiedosto mukaan lukien) on GitHubissa pysyvästi tallessa branchilla `claude/jarvis-memory-context-research-0qoa07`.
