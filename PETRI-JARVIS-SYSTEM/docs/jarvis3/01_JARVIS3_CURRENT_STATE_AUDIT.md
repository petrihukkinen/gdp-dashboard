# 01 — JARVIS 3.0: Current State Audit (Phase 0)

**Päivämäärä:** 2026-09-28 · **Vaihe:** 0 (vain auditointi — koodia ei muutettu) · **Auditoitu revisio:** `origin/claude/jarvis-memory-context-research-0qoa07` @ `ccfb7ad`

---

## 1. Johtopäätös

**JARVIS 3.0 ei ole "upgrade" olemassa olevaan orkestrointijärjestelmään, koska orkestrointijärjestelmää ei ole olemassa** — ei ainakaan missään tämän session ulottuvilla olevassa lähteessä.

Ainoa löydetty PETRI-JARVIS-SYSTEM-koodi on **Phase 1 -muistikerros**: tiedostopohjainen tietovarasto (`RAW/INGEST/KNOWLEDGE`) + kertakäyttöinen SQLite FTS5 -hakuindeksi. 489 riviä tuotantokoodia, 380 riviä testejä, 26/26 testiä läpi. Orchestrator, planner, workers, critic, approval, hooks, permissions, logging, tool execution ja execution-persistenssi **puuttuvat kokonaan koodina**; osa niistä on *suunniteltu* tutkimusdokumenteissa.

Käytännön seuraukset:

| # | Löydös | Vaikutus JARVIS 3:een |
|---|---|---|
| F1 | Execution-kerrosta (orchestrator/planner/workers) ei ole | Moduulit 01–07 ovat **greenfield-rakennusta**, eivät muutoksia. "Älä riko toimivaa" -vaatimus koskee käytännössä vain muistikerrosta, jota JARVIS 3 ei tarvitse muuttaa lainkaan. |
| F2 | JARVIS-koodi elää **mergeämättömällä haaralla** repossa `gdp-dashboard`, joka on Streamlit-BKT-demo | Koti-repo on väärä. Oma tutkimusdokumentti (`IMPLEMENTATION_BACKLOG.md` 0.3) toteaa saman. |
| F3 | `petrihukkinen/gdp-dashboard` on **julkinen** repo | Kaikki tänne pushattu JARVIS 3 -koodi, -politiikat ja -turvamalli ovat julkisia. Riskiluokituspolitiikan julkaiseminen paljastaa hyökkääjälle, mitkä toiminnot ovat RED/AMBER. |
| F4 | Samassa repossa on haaroja, joiden nimet viittaavat Bilfingeriin | Merge-/rebase-operaatio väärältä haaralta toisi Bilfinger-sisältöä JARVIS 3 -haaraan. Vaatii eksplisiittisen haarakurin (ks. §8). |
| F5 | Ei LLM-runtime-integraatiota missään | "Model node" tarvitsee adapter-rajapinnan; testit ajetaan deterministisillä stub-workereilla. Todellinen Claude-integraatio on erillinen, myöhempi vaihe. |
| F6 | Ei baseline-mittausdataa | Onnistumiskriteeri #10 ("vähemmän babysittingiä") ei ole todennettavissa ilman ensimmäisiä JARVIS 3 -ajoja. Mittaristo (Moduuli 07) luo baselinen, ei vertaa siihen. |

---

## 2. Auditoinnin laajuus ja menetelmä

### 2.1 Tarkastettu

| Lähde | Tila | Menetelmä |
|---|---|---|
| `gdp-dashboard` @ `main` (`6de129b`) | Luettu kokonaan (8 tiedostoa) | Streamlit-template: `streamlit_app.py`, `data/gdp_data.csv`, README, devcontainer. Ei JARVIS-sisältöä. |
| `gdp-dashboard` @ `claude/jarvis-memory-context-research-0qoa07` (`ccfb7ad`) | Luettu, **pl. yksi tiedosto** (ks. 2.2) | Erillinen read-only worktree scratchpadissa; työhaaraan ei tuotu mitään. Testit ajettu. |
| GitHub-repolistaus (`list_repos`) | Vain nimet | 4 repoa: `gdp-dashboard`, `nordica-operating-system` (private), `control-tower-app`, `app.py` |
| Kontin `~/.claude/`, `CLAUDE.md`, `AGENTS.md` | Ei löytynyt repoista | Ei projektitason hookeja, permissioneita tai agenttimäärityksiä. |

### 2.2 Tarkoituksella poissuljettu (Bilfinger-rajoitus ja scope)

| Kohde | Syy | Toimenpide |
|---|---|---|
| Haara `claude/bilfinger-asset-performance-2030-eijndc` | Nimi viittaa Bilfingeriin | Ei fetchattu, ei avattu |
| Haara `claude/du-research-bilfinger-audit-8l1xov` | Nimi viittaa Bilfingeriin | Ei fetchattu, ei avattu |
| Haarat `claude/amor-2030-strategy-3zdqjy`, `claude/dora-gebauer-research-xg43vf` | Sisältö tuntematon; ei JARVIS-nimeä; mahdollinen Bilfinger-kytkös | Ei fetchattu, ei avattu (varovaisuusperiaate) |
| `research/2026-09-12-jarvis-context-memory/CHECKPOINT.md` | Sisältää sanan "Bilfinger" (tunnistettu `grep -l`, vain tiedostonimi tulostettu) | **Ei avattu.** Ei käytetty tässä auditoinnissa. |
| Repot `nordica-operating-system`, `control-tower-app`, `app.py` | Eivät kuulu session scopeen; sisältö tuntematon | Ei avattu. **Mahdollinen puuttuva orchestrator voi olla näissä** — vaatii Petrin vahvistuksen (§9, D1). |

Screening-menetelmä: `grep -ril bilfinger` JARVIS-haaran worktreessä ennen minkään tiedoston lukemista; vain osumattomat tiedostot luettiin.

---

## 3. Olemassa olevan JARVIS-koodin inventaario

```
PETRI-JARVIS-SYSTEM/                                  (haara jarvis-memory-context-research)
├── README.md                     221 r   Arkkitehtuuri, repo-raja, turvahuomiot, non-goals
├── docs/KNOWLEDGE_FORMAT.md       57 r   Knowledge-vaultin tiedostoformaatti
├── scripts/
│   ├── common.py                214 r   Frontmatter-parseri, ParsedDocument, is_within(), SQLite-skeema
│   ├── build_index.py           125 r   Täysi, atominen indeksin uudelleenrakennus (tmp → replace)
│   └── search.py                150 r   FTS5 AND-of-literal-tokens -haku, bm25-painotus, --json
└── EVALS/
    ├── requirements.txt                  pytest>=7 (ainoa riippuvuus, vain testeille)
    └── memory_tests/             380 r   26 testiä, 2 synteettistä fixture-korpusta
research/2026-09-12-jarvis-context-memory/   ~950 r suunnittelu- ja tutkimusdokumentteja (FI)
```

**Testiajo 2026-09-28:** `python3 -m pytest EVALS/memory_tests -q` → **26 passed in 0.34s** (Python 3.11.15).

**Turvatarkistus (grep):** ei `eval(`, `exec(`, `subprocess`, `os.system`, `pickle`, `yaml.load` hakemistossa `scripts/`. Vahvistaa READMEn väitteen.

---

## 4. Komponenttikohtainen auditointi

Legenda: **Olemassa** = koodina toteutettu · **Suunniteltu** = vain dokumentteina · **Puuttuu** = ei kumpaakaan.

### 4.1 Orchestrator
| | |
|---|---|
| Mitä on | **Puuttuu.** Ei koodia, ei suunnitelmaa. Tutkimus rajasi moniagenttirakenteen tarkoituksella pois (`ARCHITECTURE_OPTIONS.md`: "ei moniagenttirakennetta ennen dokumentoitua tarvetta"). |
| Täyttää JARVIS 3 -vaatimuksen | Ei. |
| Uudelleenkäytettävissä | Periaate "deterministinen hook > promptin varassa oleva toiminta" (`RESEARCH_REPORT.md` A5/B8). |
| Laajennettava / rakennettava | Kokonaan: `Orchestrator` = intent → planner → graph runner → approval router → receipt. |
| Riippuvuudet | Task graph -skeema, node loop engine, gate engine, risk router. |
| Muutosriski | Ei olemassa olevaa rikottavaa. **Arkkitehtuuririski:** tutkimuksen "ei moniagenttia" -linjaus. JARVIS 3 ei ole ristiriidassa sen kanssa, jos worker-solmut ovat *funktiokutsuja/adaptereita*, eivät itsenäisiä agenttiprosesseja. Suositus: pysy tässä linjassa. |

### 4.2 Planner / Splitter
| | |
|---|---|
| Mitä on | **Puuttuu.** |
| Täyttää | Ei. |
| Uudelleenkäytettävissä | Ei koodia. |
| Rakennettava | Graph planner, joka (a) tuottaa solmut + reunat, (b) vaatii jokaiselle reunalle nimetyn artefaktin ("mikä muuttuja ylittää reunan"), (c) soveltaa aktiiviset learning constraintit ennen graafin jäädyttämistä, (d) vastaanottaa return path -objektit retry-exhaustionin jälkeen ja replannaa. |
| Riippuvuudet | Task graph schema, constraint store. |
| Muutosriski | Ei olemassa olevaa. **Suunnitteluriski:** LLM-pohjainen planner on ei-deterministinen → planin *rakenne* validoidaan deterministisesti (syklittömyys, reuna-artefaktit olemassa, risk_class ≥ policy-minimi) ennen suoritusta. |

### 4.3 Workers / Agents
| | |
|---|---|
| Mitä on | **Puuttuu.** Ei agenttimäärityksiä (`.claude/agents/`), ei worker-rajapintaa. |
| Täyttää | Ei. |
| Rakennettava | `Worker`-protokolla kahdella toteutustyypillä: `CodeWorker` (deterministinen Python-funktio) ja `ModelWorker` (adapter; testeissä stub). Rinnakkaisuus: `concurrent.futures` ready-set-pohjaisesti. |
| Riippuvuudet | Node loop engine, allowed_scope-valvonta. |
| Muutosriski | Ei olemassa olevaa. |

### 4.4 Critic / Review
| | |
|---|---|
| Mitä on | **Puuttuu koodina.** Suunnitelmissa ainoa vastine on "default-FAIL"-periaate (lainattu `cwc-long-running-agents`-referenssistä, `RESEARCH_REPORT.md` B3): valmis-tila alkaa `false`, ja kirjaus estetään kunnes todiste on avattu. |
| Täyttää | Periaatteena kyllä — JARVIS 3:n "acceptance check määritelty ennen suoritusta" on sama idea. |
| Uudelleenkäytettävissä | Default-FAIL suoraan gate-rajapinnan oletukseksi: gate palauttaa `RED` ellei check eksplisiittisesti tuota `GREEN` + evidence. |
| Rakennettava | Deterministic gate engine (Moduuli 03). LLM-critic vain ei-deterministisille tarkistuksille ja aina *lisänä* deterministiselle gatelle, ei korvaajana. |
| Muutosriski | Ei. |

### 4.5 Memory
| | |
|---|---|
| Mitä on | **Olemassa (Phase 1).** RAW/INGEST/KNOWLEDGE-kerrokset, frontmatter-metadata, FTS5-haku, `supersedes`/`superseded_by`/`status` metadatana. |
| Täyttää | "MEMORY = mitä tapahtui" -puolen osittain. Ei tallenna ajoja, solmuja eikä gate-tuloksia. |
| Uudelleenkäytettävissä | (1) **Repo-rajaperiaate** system ≠ knowledge → sama raja: `runs/` ja `constraints/` eivät kuulu system-repoon vaan vaultiin (`PETRI_JARVIS_KNOWLEDGE_ROOT`). (2) Atominen kirjoitus (`tmp → replace`). (3) `is_within()` symlink-/polkusuoja. (4) Frontmatter-malli (`supersedes`, `status`) → constraint-tiedostojen formaatti. (5) FTS5-indeksi voi myöhemmin indeksoida myös `constraints/`-tiedostot ilman koodimuutosta, jos ne ovat `.md` + frontmatter jossakin LAYERS-kansiossa. |
| Laajennettava | Ei tarvitse muuttaa JARVIS 3:n takia. Integraatio myöhemmin: learning engine voi kirjoittaa ehdotuksia `INGEST/`-kerrokseen (suunniteltu candidates-putki). |
| Riippuvuudet | Knowledge vault — **ei ole olemassa** (README: "Petrin päätös"). |
| Muutosriski | **Matala, jos ei kosketa.** Suositus: JARVIS 3 ei muokkaa `scripts/`-hakemistoa lainkaan; 26 testiä toimii regressiosuojana. |

### 4.6 Decision register
| | |
|---|---|
| Mitä on | **Osittain olemassa formaattina.** `type: decision` + `status: current/superseded` + `superseded_by` KNOWLEDGE-tiedostoissa; haku `--type decision`. Ei erillistä rekisteriä, ei kirjoituspolkua (README: "nothing in scripts/ writes to KNOWLEDGE/"). |
| Täyttää | Ei JARVIS 3:n tarvetta (ajokohtaiset päätökset: approvalit, replanit). |
| Uudelleenkäytettävissä | Supersession-malli suoraan constraint-skeemaan (`supersedes`, `active`). |
| Rakennettava | Ajokohtainen päätöskirjaus menee `runs/<run_id>/approvals/` + `receipt.json` — ei sekoiteta KNOWLEDGE-päätösrekisteriin. |
| Muutosriski | Ei. |

### 4.7 Open-loop handling
| | |
|---|---|
| Mitä on | **Suunniteltu, ei toteutettu.** `type: task` + `status: open/in_progress` -konventio; SessionStart-hook avoimien tehtävien lataukseen suunniteltu (`MEMORY_DESIGN.md`), ei rakennettu. |
| Täyttää | Ei. |
| Rakennettava | JARVIS 3:ssa open loop = ajo tilassa `AWAITING_APPROVAL` tai `ESCALATED_TO_PLANNER`. Tila persistoidaan `runs/<id>/`-puuhun → `jarvis3 runs --open` listaa ne. Ei riipu keskusteluhistoriasta. |
| Muutosriski | Ei. |

### 4.8 Security controls
| | |
|---|---|
| Mitä on | **Olemassa (rajattu):** (1) `is_within()` — indeksoija ei seuraa juuren ulkopuolelle osoittavia symlinkkejä. (2) Sisältö ≠ ohje: dokumenttisisältöä ei koskaan suoriteta (ei eval/exec/subprocess). (3) RAW immutable, testattu SHA-256-vertailulla. (4) Repo-raja: ei henkilö-/liiketoimintadataa system-repossa. (5) Ei oletusjuurta (estää vahingossa indeksoinnin väärästä paikasta). (6) `.gitignore`-suoja `*.sqlite`-tiedostoille. |
| Suunniteltu, ei toteutettu | Validointiportti ulkoiselle sisällölle; `scope`/`access`-suodatus; pakollinen ihmisen kuittaus `external_content`-lähteille. |
| Täyttää JARVIS 3 | Periaatteet kyllä; execution-tason kontrolleja (permission-rajat, risk lanes, approval) ei ole. |
| Säilytettävä | Kaikki kuusi. JARVIS 3 perii ne invariantteina: (a) mikään solmu ei suorita syötedatasta johdettua koodia, (b) kaikki tiedostopolut validoidaan `is_within(allowed_scope)`, (c) evidence-tiedostot ovat append-only. |
| Muutosriski | **Keskitaso, jos `common.py`:tä muokataan.** Suositus: kopioi ei — *importtaa* `is_within` tai toteuta identtinen, erikseen testattu funktio execution-paketissa; älä muuta `common.py`:tä. |

### 4.9 Permissions
| | |
|---|---|
| Mitä on | **Puuttuu.** Ei `.claude/settings.json`, ei permission-politiikkaa, ei roolimallia. |
| Rakennettava | Governing policy layer: ihmisen omistama, versionhallittu `policy/risk_policy.json`, jonka hash kirjataan jokaiseen receiptiin. Agentti voi **nostaa** mutta ei **laskea** risk_classia; efektiivinen luokka = `max(declared, policy(action_type), policy(target))`. |
| Muutosriski | Ei olemassa olevaa. **Julkisen repon riski (F3).** |

### 4.10 Hooks
| | |
|---|---|
| Mitä on | **Suunniteltu, ei toteutettu:** SessionStart / SessionEnd / PreCompact (`MEMORY_DESIGN.md`, backlog 2.1–2.3). |
| JARVIS 3 -relevanssi | Matala Phase 1–8:ssa: JARVIS 3 -runner on itsenäinen Python-prosessi, ei Claude Code -hook. Hook-integraatio (esim. PreToolUse-esto RED-lanen työkaluille) on myöhempi vaihe. |
| Muutosriski | Ei. |

### 4.11 Tests
| | |
|---|---|
| Mitä on | **Olemassa:** pytest, 26 testiä, synteettiset fixturet, "encode observed behavior" -periaate (tunnetut rajoitteet assertoitu näkyviksi). |
| Uudelleenkäytettävissä | Testikonventiot: `conftest.py` sys.path-malli, `tmp_path`-eristys, synteettinen data, ei mockattuja tuloksia. JARVIS 3 -testit A–G samaan tyyliin, eri hakemistoon (`EVALS/execution_tests/`). |
| Muutosriski | Nolla, jos uudet testit eri hakemistossa. |

### 4.12 Logging / observability
| | |
|---|---|
| Mitä on | **Minimaalinen:** `BuildReport` (indexed/skipped/errors) + stdout. Ei strukturoitua lokia, ei trace-tiedostoja. |
| Rakennettava | `runs/<run_id>/`-trace-puu (intent, plan, graph, nodes, gates, corrections, approvals, evidence, receipt, learning, metrics). JSON, atominen kirjoitus. |
| Muutosriski | Ei. |

### 4.13 Approval mechanisms
| | |
|---|---|
| Mitä on | **Puuttuu koodina.** Suunnitelmissa: ihmisen kuittaus ennen kuin `external_content` → `user_confirmed`. |
| Rakennettava | Risk & approval router (Moduuli 04). RED → suoritus pysähtyy, `approvals/<node_id>.request.json` kirjoitetaan, ajo tilaan `AWAITING_APPROVAL`. Jatko vain ihmisen kirjoittamalla, node-sidotulla ja payload-hashiin sidotulla hyväksynnällä (estää hyväksynnän uudelleenkäytön muuttuneelle toiminnolle). |
| Muutosriski | Ei. |

### 4.14 Tool execution
| | |
|---|---|
| Mitä on | **Puuttuu.** Ainoat "työkalut" ovat kaksi CLI-skriptiä. |
| Rakennettava | Executor-rekisteri: nimetyt action-tyypit (`write_file`, `send_external` [simuloitu], …) → jokaisella policy-määritelty minimiluokka. Phase 1–8:ssa **mikään executor ei tee oikeaa ulkoista toimintoa** — RED-lanen testit käyttävät simuloitua sink-executoria. |
| Muutosriski | Ei. |

### 4.15 Schemas
| | |
|---|---|
| Mitä on | SQLite-skeema (`common.SCHEMA`) + dokumentoitu frontmatter-formaatti. Ei JSON Schemaa. |
| Rakennettava | `schemas/task_graph.schema.json`, `gate_result`, `return_path`, `constraint`, `receipt`, `metrics` (JSON Schema 2020-12). |
| Päätös tarvitaan | Runtime-validointi: (a) `jsonschema`-kirjasto ajonaikaiseksi riippuvuudeksi, tai (b) stdlib-dataclass-validointi runtime + `jsonschema` vain testeissä skeema/koodi-yhdenmukaisuuden todentamiseen. **Suositus (b)** — säilyttää Phase 1:n "stdlib only runtime" -linjan. |
| Muutosriski | Ei. |

### 4.16 Persistence layer
| | |
|---|---|
| Mitä on | Tiedostot totuutena + kertakäyttöinen SQLite-indeksi. |
| Uudelleenkäytettävissä | Sama periaate: `runs/` ja `constraints/` ovat JSON/Markdown-tiedostoja (totuus); metriikka-aggregaatit lasketaan niistä, eivät ole ainutkertaista dataa. |
| Päätös tarvitaan | `runs/`-juuren sijainti. Suositus: env `PETRI_JARVIS_RUNS_ROOT`, ei oletusta repon sisällä (sama perustelu kuin knowledge rootilla). |
| Muutosriski | Ei. |

---

## 5. Gap-analyysi JARVIS 3 -moduuleittain

| Moduuli | Olemassa | Uudelleenkäyttö | Puuttuu | Arvioitu koko |
|---|---|---|---|---|
| 01 Task Graph Engine | — | — | Kaikki: skeema, graafimalli, topologinen järjestys, syklintarkistus, reuna-artefaktivalidointi, rinnakkainen ready-set-runner | M |
| 02 Node Loop Engine | Default-FAIL (periaate) | Periaate | PRODUCE→CHECK→CORRECT-silmukka, retry_limit=3, eskalaatio plannerille | M |
| 03 Deterministic Gate Engine | `sha256_of`, RAW-immutability-testi | `sha256_of`, `is_within` (logiikka) | Gate-rajapinta + perusgatet (schema, required fields, file exists, allowed-files diff, reconcile, dedupe, checksum, test exit code) | M |
| 04 Risk & Approval Engine | — | Repo-raja-ajattelu | Policy layer, lane-luokitus (GREEN/AMBER/RED), anti-downgrade, approval request/resume | M |
| 05 Return Path Engine | — | — | Return-objekti, scope-valvonta, vain epäonnistuneen solmun uudelleenajo, green-sisarten jäädytys | S–M |
| 06 Learning Constraint Engine | `supersedes`/`status`-malli | Frontmatter-/supersession-malli | Constraint-skeema, johtaminen epäonnistumisista, planner-hook joka muuttaa graafia (ei promptia) | M |
| 07 Execution Metrics | `BuildReport` (triviaali) | — | 16 mittaria, run summary, aggregointi yli ajojen | S |

S = < 300 r, M = 300–800 r (koodi + testit). Kokonaisarvio: ~3 000–4 500 riviä Python + testit, stdlib-only runtime.

---

## 6. Uudelleenkäytettävät suunnitteluperiaatteet (sitovat JARVIS 3:lle)

1. **Tiedosto on totuus, johdannainen on kertakäyttöinen** → run-trace on totuus; metrics.json on johdettu ja uudelleenlaskettavissa.
2. **System ≠ Knowledge** → execution-koodi system-repoon, `runs/` + `constraints/` vaultiin.
3. **Default-FAIL** → gate = RED ellei todisteellista GREENiä.
4. **Sisältö on dataa, ei ohjetta** → solmun output ei voi muuttaa graafia, politiikkaa eikä omaa risk_classiaan; vain planner (constraintien kautta) ja policy (ihminen) voivat.
5. **Stdlib-only runtime** → ei LangGraph/Prefect/Airflow/Celery; `concurrent.futures` + `graphlib.TopologicalSorter` (stdlib, Python ≥ 3.9) riittävät.
6. **Havaittu, ei oletettu** → testit assertoivat todellisen käyttäytymisen, myös rajoitteet.
7. **Laukaisuehto ennen laajennusta** → ei hajautettua suoritusta, ei tietokantaa, ei agenttiframeworkia ennen dokumentoitua tarvetta.

---

## 7. Riskit

| # | Riski | Tod.näk. | Vaikutus | Mitigaatio |
|---|---|---|---|---|
| R1 | JARVIS 3 -turvapolitiikka julkaistaan julkisessa repossa (F3) | Varma, jos jatketaan tässä repossa | Keskitaso: paljastaa gating-logiikan | Siirto private-repoon ennen Phase 5:tä (§9 D2) |
| R2 | Bilfinger-sisältö vuotaa haaroja yhdistettäessä (F4) | Matala, jos kuri pidetään | Korkea (ehdoton rajoite) | JARVIS 3 -haara perustuu `main`iin; muistikerros tuodaan vain `git checkout <ref> -- PETRI-JARVIS-SYSTEM/` -polkurajatusti, **ei** koko haaran mergellä (joka toisi `CHECKPOINT.md`:n) |
| R3 | "Upgrade"-kehys johtaa ylimitoitettuun rakenteeseen, koska korvattavaa ei ole | Keskitaso | Keskitaso | Pidä runner kirjastona + CLI:nä, ei palveluna |
| R4 | ModelWorker-adapteri ilman oikeaa LLM:ää → testit todentavat vain kontrollilogiikan, eivät mallin laatua | Varma | Keskitaso | Eksplisiittinen rajaus build reportissa; oikea integraatio erillisenä vaiheena |
| R5 | Planner luokittelee oman toimintonsa alempaan laneen | Keskitaso ilman kontrollia | Korkea | Anti-downgrade: efektiivinen luokka = max(declared, policy); testi E + erillinen negatiivitesti |
| R6 | Muistikerroksen regressio | Matala | Matala | `scripts/`-hakemistoon ei kosketa; 26 testiä ajetaan joka vaiheessa |
| R7 | Puuttuva orchestrator on olemassa toisessa repossa (`nordica-operating-system`?) | Tuntematon | Korkea (tuplatoteutus) | §9 D1 — vahvistus ennen Phase 1:tä |

---

## 8. Ehdotettu toteutusjärjestys

**Sijainti:** `PETRI-JARVIS-SYSTEM/execution/` (uusi paketti), `PETRI-JARVIS-SYSTEM/schemas/`, `PETRI-JARVIS-SYSTEM/policy/`, `PETRI-JARVIS-SYSTEM/EVALS/execution_tests/`. Olemassa oleviin tiedostoihin ei kosketa.

| Vaihe | Sisältö | Tuotokset | Portti seuraavaan |
|---|---|---|---|
| **0.5** | Repo-/haarapäätös (§9) + muistikerroksen polkurajattu tuonti tälle haaralle (valinnainen) | Päätös kirjattu | Petrin hyväksyntä |
| **1** | Skeemat + rajapinnat: `task_graph`, `node`, `gate_result`, `return_path`, `constraint`, `receipt`, `metrics`; Python-dataclassit + validointi | `schemas/*.json`, `execution/models.py`, docs 02 + 05 | Skeema/dataclass-yhdenmukaisuustesti vihreä |
| **2** | Task graph engine: rakentaminen, syklintarkistus, reuna-artefaktisääntö, topologinen rinnakkainen runner (ready-set) | `execution/graph.py`, `runner.py`; **Testi A** | A vihreä + muistitestit 26/26 |
| **3** | Node loops + gates: PRODUCE→CHECK→CORRECT, retry_limit 3, gate-kirjasto, CodeWorker vs. ModelWorker(stub) | `execution/loop.py`, `gates.py`, `workers.py`; **Testit C, D** | C, D vihreä |
| **4** | Return paths + replanning: vain epäonnistunut yksikkö, scope-valvonta, planner-eskalaatio | `execution/return_path.py`, `planner.py`; **Testit B, G** | B, G vihreä |
| **5** | Risk & approval: policy layer, lanet, anti-downgrade, approval request/resume, simuloitu RED-executor | `execution/risk.py`, `approval.py`, `policy/risk_policy.json`; doc 04; **Testi E** + downgrade-negatiivitesti | E vihreä; **R1 ratkaistu** |
| **6** | Learning constraints: johtaminen, store, planner-integraatio (muuttaa graafia, ei promptia) | `execution/learning.py`; **Testi F** | F vihreä |
| **7** | Metrics + observability: `runs/<id>/`-trace, 16 mittaria, run summary, CLI | `execution/trace.py`, `metrics.py`, `cli.py`; doc 06 | Jokainen testiajo tuottaa validin receiptin + metricsin |
| **8** | Integraatiotestit A–G end-to-end, docs 03 + 07, `JARVIS3_BUILD_REPORT.md` | Kaikki deliverablet | Koko suite vihreä |

Jokaisen vaiheen jälkeen: testiajo, muutetut tiedostot, tunnetut rajoitteet, backwards-compat-tarkistus (= muistitestit 26/26), commit + push.

---

## 9. Päätökset, jotka tarvitaan Petriltä ennen Phase 1:tä

| # | Päätös | Vaihtoehdot | Suositus |
|---|---|---|---|
| **D1** | Onko olemassa JARVIS-orchestrator/planner-koodia jossain muualla (esim. `nordica-operating-system`, `control-tower-app`, paikallinen kone)? | Kyllä → anna repo, auditoin sen (Bilfinger-screening ensin) · Ei → greenfield | Vahvista. Jos kyllä, tämä auditointi on puutteellinen. |
| **D2** | Missä JARVIS 3 rakennetaan? | (a) Tässä julkisessa repossa, tällä haaralla · (b) Uusi private-repo (esim. `petri-jarvis-system`) · (c) Olemassa oleva private-repo | **(b)**. Phase 1–4 voidaan tehdä tässä, mutta siirto ennen Phase 5:tä (risk policy). Uuden repon luonti on sinun toimenpiteesi / hyväksyntäsi. |
| **D3** | Tuodaanko Phase 1 -muistikerros tälle haaralle? | (a) Polkurajattu tuonti `PETRI-JARVIS-SYSTEM/` (ilman `research/`-kansiota → `CHECKPOINT.md` ei tule mukaan) · (b) Ei tuoda; JARVIS 3 itsenäinen paketti, integraatio myöhemmin | **(a)** — mahdollistaa regressioajon samassa puussa. `research/`-kansio jätetään pois. |
| **D4** | Runtime-riippuvuudet | stdlib-only · `jsonschema` sallittu | **stdlib-only runtime**, `jsonschema` vain testeissä |
| **D5** | Oikea LLM-integraatio Phase 1–8:n aikana? | Ei (stub-workerit) · Kyllä (Claude API, vaatii API-avaimen ja kustannukset) | **Ei.** Kontrollilogiikka ensin; mallintegraatio erillisenä vaiheena. |

---

## 10. Tiedostot, joita tämä vaihe muutti

- **Lisätty:** `PETRI-JARVIS-SYSTEM/docs/jarvis3/01_JARVIS3_CURRENT_STATE_AUDIT.md` (tämä dokumentti).
- **Muutettu:** ei mitään.
- **Koodi:** ei muutoksia.
