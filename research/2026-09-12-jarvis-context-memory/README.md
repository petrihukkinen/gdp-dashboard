# Tutkimus: Context engineering ja persistent memory architecture Petri Jarvikselle

**Tutkimuspäivä:** 2026-09-12. **Tekijä:** Claude (agenttitutkimus). **Kohde:** arkkitehtuurisuositus PETRI JARVIS -järjestelmän pitkäkestoiselle muistille ja kontekstinhallinnalle.

## Pääsuositus tiivistetysti

Käytä **Markdown/Git-pohjaista muistia, jota täydentää kevyt, kokonaan johdettu SQLite-metadataindeksi** avainsanahaulla (Arkkitehtuuri B, ks. `ARCHITECTURE_OPTIONS.md`). **Ei** vektoritietokantaa, **ei** tietograafia, **ei** erillistä muistipalvelua, **ei** moniagenttirakennetta ennen kuin konkreettinen, dokumentoitu tarve osoittaa yksinkertaisemman ratkaisun riittämättömäksi (laukaisuehdot listattu `ARCHITECTURE_OPTIONS.md`:ssä ja `IMPLEMENTATION_BACKLOG.md`:ssä).

Perusperiaatteet, joita suositus toteuttaa:
1. **Yksi lähde per pysyvä tieto** — tiedostot ovat totuus, indeksi on aina uudelleenrakennettava johdannainen.
2. **Alkuperäisaineisto ≠ tulkinta ≠ varmennettu tieto ≠ päätös ≠ tehtävä** — erillisiä kenttiä/tiedostoja, ei sekoitettuna.
3. **Bi-temporaalinen aikakäsittely** (tapahtuma-aika / tallennusaika / voimassaolo) skeeman kenttinä, ei tietokantateknologiana.
4. **Validointiportti** ennen kuin agentin oma tulkinta tai ulkoinen sisältö voi muuttua "varmennetuksi faktaksi" — erityisesti turvallisuuskriittinen ulkoisen, luottamattoman sisällön kohdalla.
5. **Progressiivinen lataus** — istunto lataa checkpoint + avoimet tehtävät, ei koko historiaa; täysi sisältö luetaan vasta kun tehtävä nimeää sen.

## Tiedostokartta

| Tiedosto | Sisältö |
|---|---|
| `README.md` | Tämä tiedosto — pääsuositus, kartta, rajaukset |
| `RESEARCH_REPORT.md` | Tutkimuskysymykset A–D, lähteisiin viittaava synteesi, "lähteet osoittavat / päättelen / ehdotan / testattava" -erottelu jokaiselle alakysymykselle |
| `SOURCE_REGISTER.md` | 30+ arvioitua lähdettä (viitteet A1–D5), kattavuusmerkinnät (P=luettu kokonaan, R=repo/issue luettu, S=hakusynteesi), rajoitukset ja soveltuvuus |
| `ARCHITECTURE_OPTIONS.md` | Kolmen arkkitehtuurin (A/B/C) vertailu kahdeksalla kriteerillä, suositus ja laukaisuehdot laajennuksille |
| `MEMORY_DESIGN.md` | Hakemistorakenne, YAML-skeema, tietovirta, ristiriitakäytäntö, istunnon checkpoint-menettely, MVP |
| `EVALUATION_PLAN.md` | 9 synteettistä testiä (T1–T9), baseline-vertailu, ennalta määritellyt hyväksymiskriteerit |
| `IMPLEMENTATION_BACKLOG.md` | Priorisoitu, vaiheistettu toteutuslista riippuvuuksineen — ei toteutettu, vain suunniteltu |
| `CHECKPOINT.md` | Tämän tutkimustehtävän oma tila: valmis/keskeneräinen työ, esteet, seuraava askel |

## Tutkimuksen rajat (lue ennen käyttöä)

- **Ei olemassa olevaa Jarvis-toteutusta tarkistettu.** Tämä konttiympäristö oli täysin puhdas — ei löytynyt mitään olemassa olevaa Jarvis-rakennetta, `.claude/`-konfiguraatiota tai muistikansiota. Kaikki suositukset ovat siis **yleisarkkitehtuurisia**, ei olemassa olevan järjestelmän auditointia. Ennen toteutusta: tarkista käyttäjän oma ympäristö erikseen (ks. `IMPLEMENTATION_BACKLOG.md` Vaihe 0).
- **Verkkoyhteysrajoitus vaikutti lähdekattavuuteen.** Istunnon egress-välityspalvelin esti pääsyn useisiin keskeisiin alkuperäislähteisiin (`anthropic.com`, `arxiv.org`, `aclanthology.org`, `trychroma.com`, `manus.im`, `simonwillison.net`, `blog.getzep.com`, `help.openai.com`, `learn.microsoft.com`, `genai.owasp.org`, `web.archive.org`). Näiden osalta tieto perustuu hakukoneen (WebSearch) tulossynteesiin, ei suoraan alkuperäistekstin lukemiseen — merkitty selvästi **S**-kattavuudeksi `SOURCE_REGISTER.md`:ssä. Vastaavasti onnistuneesti täysin luetut lähteet (Anthropicin Claude Code- ja Claude-alustadokumentit `code.claude.com`/`platform.claude.com`, useat GitHub-READMEt) ovat vahvempi perusta kuin S-merkityt.
- **Ei suoritettuja testejä eikä julkaistuja benchmark-tuloksia esitetä Jarviksen suorituskyvyn todisteena.** `EVALUATION_PLAN.md` on suunnitelma, ei tulosraportti. Kaupallisten muistituotteiden (Zep, Mem0) omat benchmark-luvut on nimenomaisesti merkitty kiistanalaisiksi (ks. `SOURCE_REGISTER.md` B7) — niitä ei käytetä päätöksenteon perusteena.
- **Ei toteutusmuutoksia tehty.** Toimeksiannon mukaisesti tämä on tutkimus- ja suunnittelutehtävä; mitään koodia, konfiguraatiota tai olemassa olevaa järjestelmää ei ole muutettu.

## Yhteenveto

**Viisi tärkeintä löydöstä:**
1. Kolme riippumatonta lähdettä (Anthropicin memory tool -ohjeistus, multisession-kuvio, `cwc-long-running-agents`-repo) päätyy samaan istunnon checkpoint-malliin: lue tila alussa, kirjoita tila lopussa, tee tämä deterministisesti (hookilla), ei promptin varassa.
2. Mitattu tutkimus (CogCanvas-ablaatio) osoittaa sanatarkan raakatekstin voittavan LLM:n poimimat jäsennellyt artefaktit muistihaussa selvällä erolla — tue toimeksiannon periaatetta "säilytä alkuperäisaineisto, älä korvaa sitä tulkinnalla".
3. Pitkä ja häiritsevä konteksti heikentää mallin suoritusta mitattavasti, riippumatta siitä ollaanko lähellä kontekstirajaa — tue pientä, tarkkaa kontekstibudjettia, ei "lataa kaikki varmuuden vuoksi" -strategiaa.
4. Kaupallisten muistituotteiden (Zep vs. Mem0) julkiset benchmark-luvut ovat keskenään ristiriitaisia ja kiistanalaisia — kolmannen osapuolen "suorituskykyväitteitä" ei pidä ottaa arkkitehtuuripäätöksen perustaksi sellaisenaan.
5. ChatGPT:n ja Microsoft 365 Copilotin muisti ovat molemmat suljettuja, tilikohtaisia palveluita ilman dokumentoitua ohjelmallista vientirajapintaa — Jarvis ei voi olettaa saavansa niiden muistia ulos automaattisesti.

**Kolme parasta ensimmäiseksi luettavaa lähdettä** (ks. `SOURCE_REGISTER.md` täydet kuvaukset):
1. **A2/A3/A6/A7** — Claude Coden ja Claude-alustan viralliset muisti-, compaction-, skill- ja hook-dokumentit (`code.claude.com`, `platform.claude.com`) — täysin luettu, suoraan sovellettavissa, ei kiistanalainen.
2. **D1** — `github.com/anthropics/cwc-long-running-agents` — konkreettinen, toimiva referenssitoteutus istunnon checkpointille ja "default-FAIL"-validoinnille.
3. **B6** — CogCanvas-tutkimus ("Verbatim Chunks Beat Extracted Artifacts") — yksittäinen vahvin empiirinen perustelu koko muistiskeeman alkuperäisaineisto/tulkinta-erottelulle.

**Suositeltu Jarvis-arkkitehtuuri perusteluineen:** Arkkitehtuuri B (`ARCHITECTURE_OPTIONS.md`) — Markdown/Git ainoana totuuden lähteenä, kevyt johdettu SQLite-indeksi hakua varten, bi-temporaalinen ja lähdejäljitettävä skeema (`MEMORY_DESIGN.md`), validointiportti ulkoiselle/tulkinnalliselle sisällölle. Perustelu: toteuttaa kaikki toimeksiannon suunnitteluperiaatteet ilman lisäriippuvuuksia, ja mikään tutkittu lähde ei osoita raskaamman ratkaisun olevan tarpeen tässä mittakaavassa.

**Mitä ei vielä kannata rakentaa:** vektorihaku, tietograafi, erillinen muistipalvelu (Letta/Zep/Mem0-tyyppinen), rinnakkaiskirjoituksen lukitusmekanismi, automaattinen ristiriitojen ratkaisu ilman ihmisen kuittausta, ohjelmallinen integraatio ChatGPT:hen/Copilotiin. Kaikilla on eksplisiittinen laukaisuehto `ARCHITECTURE_OPTIONS.md`:ssä — rakenna vasta kun ehto on havaittu, ei etukäteen.

**Yksi konkreettinen seuraava toteutusaskel:** Toteuta `IMPLEMENTATION_BACKLOG.md`:n Vaihe 1.1–1.3: hakemistorakenne + `rebuild_index.py` + `query.py`. Tämä on pienin yksikkö, joka tekee koko arkkitehtuurista testattavan (`EVALUATION_PLAN.md` T1–T9 vaativat toimivan indeksin).

**Varmennusaukot ja tiedostojen sijainnit:** Kaikki tämän tutkimuksen tuotokset ovat hakemistossa `research/2026-09-12-jarvis-context-memory/` tässä Git-repositoriossa (branch `claude/jarvis-memory-context-research-0qoa07`). Keskeinen varmennusaukko: useat alkuperäislähteet (ks. yllä "Tutkimuksen rajat") vaativat vahvistuksen avoimemmalla verkkoyhteydellä ennen kuin niiden yksityiskohtaisia lukuja käytetään lopullisen tuotantopäätöksen perusteena — ks. `IMPLEMENTATION_BACKLOG.md` kohta 0.2 ja `SOURCE_REGISTER.md`:n loppuosan lukemattomien lähteiden lista.
