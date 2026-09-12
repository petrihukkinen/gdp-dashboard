# Muistin suunnittelu: skeema, tietovirta ja elinkaari (Arkkitehtuuri B)

Perustuu `ARCHITECTURE_OPTIONS.md`:n suositukseen (Markdown/Git + johdettu SQLite-indeksi). Kaikki tässä esitetty on **suunnitelma**, ei toteutettu koodi — toteutus on erillinen tehtävä (ks. toimeksianto: "toteutusmuutokset tehdään erillisenä tehtävänä").

## Hakemistorakenne (ehdotus)

```
jarvis-memory/
├── SCHEMA.md                  # tämän tiedoston skeema ihmisluettavana, versionhallittu sääntö
├── profile/
│   └── user.md                 # harvoin muuttuva käyttäjäprofiili (mieltymykset, roolit)
├── projects/
│   └── <project-slug>/
│       ├── PROJECT.md           # projektin kuvaus, scope, tila
│       ├── PROGRESS.md          # istunnon checkpoint (ks. alla)
│       ├── decisions/
│       │   └── <id>.md          # yksi päätös per tiedosto
│       ├── tasks/
│       │   └── <id>.md          # yksi tehtävä per tiedosto
│       ├── facts/
│       │   └── <id>.md          # validoidut pysyvät faktat
│       └── events/
│           └── <yyyy-mm>.md     # append-only tapahtumaloki, kuukausittain rullaava
├── candidates/
│   └── <id>.md                  # validoimattomat muistiehdotukset (ks. validointiputki)
├── skills/                      # projektiriippumaton menetelmätieto (Claude Code -skillit)
└── index.sqlite                 # JOHDETTU indeksi — voidaan tuhota ja rakentaa uudelleen
```

**Periaate:** `index.sqlite` ei koskaan kanna ainutkertaista tietoa. Se rakennetaan skriptillä lukemalla kaikki `.md`-tiedostojen YAML-frontmatter. Jos indeksi ja tiedostot ovat ristiriidassa, tiedosto voittaa aina.

## Esimerkkiskeema: muistimerkintä (YAML-frontmatter jokaisessa `.md`-tiedostossa)

```yaml
---
id: dec-2026-09-12-001            # pysyvä, uudelleenkäytetty tunniste
type: decision                     # decision | task | fact | event | reference | procedure
project: yritys-x-series-a         # projekti-slug; "personal" henkilökohtaiselle
scope: personal | company:yritys-x # käyttöoikeus-/näkyvyysrajaus (kysymys D2/D3)

# Sisältö
title: "Valitaan Interactive Brokers ensisijaiseksi välittäjäksi EU-ETF-salkulle"
summary: >
  Lyhyt, ihmisen kirjoittama tai vahvistama tiivistelmä. EI koskaan ainoa
  tallennettu muoto — ks. `source_excerpt` alla.

# Lähdejäljitettävyys (kysymys B6 — estä tulkinnan muuttuminen faktaksi)
source_type: user_statement | document | agent_inference | external_content
source_ref: "keskustelu 2026-09-10, viesti #42"   # tai tiedostopolku/URL
source_excerpt: >
  Alkuperäinen sanamuoto tai dokumenttiote sellaisenaan, muokkaamatta.
  Pakollinen kenttä kun source_type = agent_inference tai external_content.

# Varmennus (kysymys B3)
verification_status: unverified | user_confirmed | superseded | retracted
verified_by: "petri.hukkinen@gmail.com"     # kuka vahvisti, jos user_confirmed
verified_at: "2026-09-12T10:00:00Z"

# Aikaleimat — kolme erillistä (kysymys B5)
recorded_at: "2026-09-10T14:32:00Z"   # milloin kirjattu järjestelmään
valid_from: "2026-09-10T00:00:00Z"    # milloin fakta/päätös tuli voimaan
valid_until: null                      # milloin lakkasi olemasta voimassa (null = edelleen voimassa)

# Korvaussuhteet (kysymys B4)
supersedes: null                       # tämän objektin id, jonka tämä korvaa
superseded_by: null                    # täytetään kun tämä korvataan

# Tehtäväspesifiset kentät (type: task)
status: open | in_progress | done | abandoned
due: null

# Käyttöoikeus (kysymys D2/D3)
access: [petri]                        # kuka/mikä saa lukea; oletuksena scope riittää yhdelle käyttäjälle

version: 3                             # optimistinen lukitus rinnakkaisille kirjoituksille (kysymys C5)
---

Vapaamuotoinen, ihmisluettava sisältö tästä eteenpäin.
```

**Miksi tämä skeema vastaa toimeksiannon vaatimuksiin:**
- Alkuperäisaineisto (`source_excerpt`) ja tulkinta (`summary`) ovat **eri kenttiä**, eivät sekoitu.
- `verification_status` erottaa agentin oman päätelmän (`unverified`) käyttäjän vahvistamasta faktasta (`user_confirmed`) — kysymys B6:n ydinratkaisu.
- `recorded_at` vs. `valid_from`/`valid_until` erottaa tallennusajan ja voimassaolon (kysymys B5, Zep-mallin [B2] mukaisesti, kevyempänä toteutuksena).
- `supersedes`/`superseded_by` toteuttaa korvausketjun poistamatta historiaa (kysymys B4).
- `scope`/`access` toteuttaa käyttöoikeusrajauksen haussa ja tallennuksessa (kysymys D2/D3).

## Tietovirta: alkuperäisaineistosta hyväksyttyyn muistiin

```
1. RAAKA SYÖTE
   (käyttäjän viesti / dokumentti / työkalutulos / ulkoinen sisältö)
        │
        │  Ei koskaan kirjoiteta suoraan projects/ -kansioon.
        ▼
2. EHDOTUS (candidates/<id>.md)
   Agentti kirjoittaa ehdotuksen source_type + source_excerpt -kentin.
   verification_status = unverified.
        │
        │  Haarautuu lähteen luottamustason mukaan:
        │
        ├── source_type = user_statement, agentin oma tehtävä/päätöskirjaus
        │   käyttäjän suorasta pyynnöstä
        │        │
        │        ▼  (kevyt hyväksyntä: agentti voi siirtää automaattisesti,
        │            mutta merkintä pysyy unverified kunnes käyttäjä
        │            eksplisiittisesti vahvistaa — ks. alla)
        │
        └── source_type = external_content TAI agent_inference
             ilman käyttäjän suoraa läsnäoloa (esim. web-haku, sähköposti)
                  │
                  ▼  PAKOLLINEN ihmisen kuittaus ennen siirtoa (kysymys D1,
                     lethal trifecta -periaate [C1]). Ei automaattista siirtoa.
        │
        ▼
3. VALIDOINTI
   - Onko lähde jäljitettävissä (source_ref/source_excerpt täytetty)?
   - Onko scope oikein määritelty?
   - Ristiriitatarkistus: hakee samaan projektiin/aiheeseen liittyvät
     voimassa olevat objektit (SQLite-kysely type+project+valid_until IS NULL).
     Jos ristiriita löytyy → ks. "Ristiriitojen ratkaisu" alla, ei jatketa
     automaattisesti.
        │
        ▼
4. TALLENNUS (projects/<p>/decisions|tasks|facts/<id>.md)
   Tiedosto siirretään/kirjoitetaan candidates/-kansiosta lopulliseen
   sijaintiin. Git commit. index.sqlite päivitetään (upsert).
        │
        ▼
5. TEHTÄVÄKOHTAINEN HAKU
   Seuraava istunto/tehtävä hakee vain tarvitsemansa: ensin index.sqlite
   (projekti+tyyppi+scope+aikaväli-suodatus, FTS5-avainsanahaku), sitten
   Read-työkalulla täysi sisältö vain löydetyistä osumista (progressiivinen
   lataus, ks. RESEARCH_REPORT.md A1/A6).
```

## Ristiriitojen ratkaisukäytäntö (lähteistetty)

Perustuu Zep/Graphitin bi-temporaaliseen malliin [B2] ja CogCanvas-tutkimuksen [B6] periaatteeseen (säilytä raaka, älä korvaa sitä tulkinnalla):

1. **Vanhaa ei koskaan poisteta eikä ylikirjoiteta** ristiriidan takia. Sen `valid_until` asetetaan uuden `valid_from`-hetkeen ja `superseded_by`-kenttä osoittaa uuteen objektiin.
2. **Uusi objekti** kantaa `supersedes`-kentän, joka osoittaa vanhaan.
3. Jos kaksi objektia ovat ristiriidassa **eikä ole selvää** kumpi on uudempi/oikeampi (esim. molemmat `user_statement`, eri ajankohtina, ei eksplisiittistä korvausmainintaa) — järjestelmä **ei** ratkaise automaattisesti. Se merkitsee molemmat `verification_status: unverified` (jos toistaiseksi olivat `user_confirmed`, tämä on poikkeus joka vaatii käyttäjän huomion) ja nostaa ristiriidan agentin vastaukseen eksplisiittisesti: "Löysin kaksi ristiriitaista merkintää X:stä, kumpi pätee?"
4. Poisto (todellinen tiedoston poisto, ei looginen `superseded`) on **harvinainen, eksplisiittinen** operaatio — käyttäjän suoralla pyynnöllä ("poista tämä tieto"). Poisto-operaatio: (a) tiedosto poistetaan/siirretään `archive/`-kansioon Git-historian säilyttämiseksi, (b) `index.sqlite` päivitetään poistamalla rivi samassa transaktiossa, (c) kaikki objektit, jotka viittasivat poistettuun `supersedes`/`superseded_by`-kentässä, saavat viittauksen tilalle merkinnän "lähde poistettu <pvm>".

## Istunnon aloitus- ja lopetusmenettely (checkpoint)

Perustuu kolmeen yhtenevään lähteeseen: memory tool -promptimalli [A3], multisession-kuvio [A3, D1] ja `cwc-long-running-agents`-hookit [D1, A6].

**Istunnon aloitus** (toteutus: `SessionStart`-hook, matchers `startup`+`resume`, deterministinen — ei riipu siitä muistaako agentti pyytää):
1. Lue `projects/<active-project>/PROGRESS.md` (viimeisin checkpoint: mitä tehtiin viimeksi, mikä on seuraava askel, mitä jäi kesken).
2. Lue avoimien tehtävien lista (`index.sqlite` -kysely: `type=task AND status IN (open, in_progress) AND project=<active>`).
3. Injektoi tämä kontekstiin `additionalContext`-kenttänä — ei koko projektihistoriaa, vain checkpoint + avoimet tehtävät (progressiivinen lataus, RESEARCH_REPORT A1).

**Istunnon lopetus** (toteutus: `SessionEnd`-hook, varmuuskopiona `PreCompact` jos istunto tiivistetään kesken):
1. Kirjoita/päivitä `PROGRESS.md`: mitä tehtiin, mikä ratkesi, mikä on seuraava konkreettinen askel, mitä epävarmuutta jäi.
2. Kaikki tämän istunnon aikana syntyneet `candidates/`-ehdotukset, joita ei ole käsitelty, pysyvät `unverified`-tilassa — niitä **ei** korosteta valmiiksi vain koska istunto loppui.
3. Git commit (viesti: mitä muuttui, mitkä objektit).

## Lähteen muuttamisen ja poistamisen vaikutukset

| Tapahtuma | Vaikutus |
|---|---|
| Lähdedokumentti (esim. sopimus, jota `source_ref` osoittaa) muuttuu | `source_excerpt` on tallennettu ote — se **ei** muutu automaattisesti. Merkintä jää osoittamaan vanhaan otteeseen kunnes joku eksplisiittisesti luo uuden version (`supersedes`-ketju). Tämä on tarkoituksellista: estää hiljaisen, huomaamattoman tiedon muuttumisen. |
| Muistiobjekti muutetaan (esim. tehtävän tila `open`→`done`) | `version`-kenttä kasvaa, `recorded_at` ei muutu (se on alkuperäinen kirjaushetki) — lisää erillinen `updated_at`-kenttä jos tarvitaan muutoshistoria kentän tasolla; Git-historia kattaa tämän tiedostotasolla joka tapauksessa. |
| Muistiobjekti poistetaan | Ks. "Ristiriitojen ratkaisukäytäntö" kohta 4 yllä — `index.sqlite` päivittyy samassa transaktiossa, haku ei enää löydä poistettua. |
| `index.sqlite` korruptoituu/katoaa | Ei tietohäviötä — indeksi rakennetaan uudelleen kaikista `.md`-tiedostoista skriptillä. Tämä on syy, miksi indeksi ei koskaan saa kantaa ainutkertaista tietoa. |

## Vähimmäistoteutus (MVP)

1. Hakemistorakenne + `SCHEMA.md` (yllä).
2. Yksi Python-skripti: `rebuild_index.py` — lukee kaikki `.md`-tiedostojen frontmatterin, kirjoittaa `index.sqlite` (SQLite FTS5 `summary`+`title`-kentille avainsanahakuun).
3. Yksi Python-skripti: `query.py --project X --type decision --status open` — komentorivihaku indeksistä, palauttaa osumien tiedostopolut (agentti lukee sisällön itse Read-työkalulla).
4. `SessionStart`/`SessionEnd`-hookit (ks. yllä) yhteen projektiin kokeiluna.
5. Yksi skilli: "jarvis-memory" — dokumentoi agentille miten ehdotus tehdään (`candidates/`), miten validointi kysytään käyttäjältä, miten hakua käytetään.

## Selkeät ehdot myöhemmille laajennuksille

Ks. `ARCHITECTURE_OPTIONS.md`:n laukaisuehtotaulukko ja `IMPLEMENTATION_BACKLOG.md`. Ei toteuteta ennen kuin ehto on havaittu ja dokumentoitu:
- Vektorihaku `index.sqlite`:n rinnalle.
- Optimistisen lukituksen (`version`-kenttä) aktiivinen tarkistuslogiikka, jos useampi rinnakkainen kirjoittaja tulee käyttöön.
- Erillinen muistipalvelu/graafi.
