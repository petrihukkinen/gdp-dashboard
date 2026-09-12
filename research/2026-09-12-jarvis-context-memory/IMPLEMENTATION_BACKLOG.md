# Toteutuslista: Jarviksen muistiarkkitehtuuri (priorisoitu)

Tämä on **backlog tulevaa, erillistä toteutustehtävää varten** — mitään näistä ei ole toteutettu tässä tutkimustehtävässä. Riippuvuudet merkitty eksplisiittisesti.

## Vaihe 0 — Ennakkoehdot (ennen mitä tahansa koodia)

| # | Tehtävä | Riippuvuus | Perustelu |
|---|---|---|---|
| 0.1 | Tarkista käyttäjän oma `~/.claude/`-asetusrakenne ja mahdollinen olemassa oleva Jarvis-repo/kansio oikeassa ympäristössä (ei tässä tutkimuskontissa saatavilla) | — | RESEARCH_REPORT.md:n "Tausta"-luku — tämä tutkimus tehtiin puhtaassa kontissa, ei käyttäjän omassa ympäristössä |
| 0.2 | Vahvista/kumoa S-merkityt lähteet (ks. SOURCE_REGISTER.md), erityisesti A1 (Anthropic context engineering -blogi) ja B6 (CogCanvas), avoimemmalla verkkoyhteydellä | — | Nykyiset väitteet perustuvat hakusynteesiin, ei alkuperäistekstiin |
| 0.3 | Päätä konkreettinen tallennuspaikka (esim. oma Git-repo `jarvis-memory`, ei osa tätä `gdp-dashboard`-repoa, joka on tähän tutkimustehtävään osoitettu, ei Jarviksen oma) | 0.1 | Toimeksianto: "projektikohtainen tieto kuuluu projektiin" |

## Vaihe 1 — MVP-perusta (ks. MEMORY_DESIGN.md "Vähimmäistoteutus")

| # | Tehtävä | Riippuvuus | Koko (arvio) |
|---|---|---|---|
| 1.1 | Luo hakemistorakenne + `SCHEMA.md` | 0.3 | Pieni |
| 1.2 | Kirjoita `rebuild_index.py` (SQLite FTS5 -indeksin rakennus frontmatterista) | 1.1 | Pieni-keskisuuri |
| 1.3 | Kirjoita `query.py` (komentorivihaku: projekti/tyyppi/scope/aikaväli/avainsana) | 1.2 | Pieni |
| 1.4 | Kirjoita validointiputken minimitoteutus: `candidates/`-kansio + skripti, joka siirtää `user_confirmed`-tilaan merkityn ehdotuksen lopulliseen sijaintiin | 1.1 | Keskisuuri |
| 1.5 | Yksi Claude Code -skilli ("jarvis-memory"), joka dokumentoi agentille koko työnkulun (ehdotus → validointi → tallennus → haku) | 1.1–1.4 | Pieni-keskisuuri |

## Vaihe 2 — Istunnon jatkuvuus

| # | Tehtävä | Riippuvuus | Koko |
|---|---|---|---|
| 2.1 | `SessionStart`-hook: lukee aktiivisen projektin `PROGRESS.md` + avoimet tehtävät, injektoi `additionalContext`-kenttään | 1.1–1.3 | Pieni |
| 2.2 | `SessionEnd`-hook (+ `PreCompact`-varmuuskopio): kirjoittaa `PROGRESS.md`-päivityksen deterministisesti | 1.1 | Pieni-keskisuuri |
| 2.3 | Git-automaatio: commit checkpoint-päivityksen yhteydessä (ei joka pienestä muutoksesta — kynnysarvo esim. istunnon loppu) | 2.2 | Pieni |

## Vaihe 3 — Turvallisuus ja rajaus (ei siirrettävissä myöhemmäksi — ks. perustelut alla)

| # | Tehtävä | Riippuvuus | Koko |
|---|---|---|---|
| 3.1 | Pakota `source_type: external_content`/`agent_inference` -ehdotuksille eksplisiittinen ihmisen kuittaus ennen `verification_status: user_confirmed` (ei koskaan automaattinen) | 1.4 | Keskisuuri |
| 3.2 | `scope`-kentän pakollisuus + haun oletussuodatus nykyiseen scopeen | 1.2, 1.3 | Pieni-keskisuuri |
| 3.3 | Testaa EVALUATION_PLAN.md T8/T9 manuaalisesti ennen tuotantokäyttöä | 3.1, 3.2 | Pieni |

**Perustelu vaiheen 3 priorisoinnille korkealle:** Lethal trifecta [C1] ja muistin myrkytys -tutkimus [C2] osoittavat, että kirjoitusreitin suojaus on rakenteellinen, ei lisättävä jälkikäteen "kun on aikaa" — jos Jarvis alkaa käyttää ulkoisia lähteitä (web-haku, sähköposti) ilman 3.1:tä, jokainen sellainen käyttö on riski jo ennen kuin suojaus on olemassa.

## Vaihe 4 — Arviointi

| # | Tehtävä | Riippuvuus | Koko |
|---|---|---|---|
| 4.1 | Rakenna EVALUATION_PLAN.md:n synteettinen testiaineisto | Vaihe 1–3 valmis | Pieni-keskisuuri |
| 4.2 | Aja T1–T9 manuaalisesti, kirjaa `EVALUATION_RESULTS.md` | 4.1 | Keskisuuri |
| 4.3 | Aja samat testit Arkkitehtuuri A -baselinella vertailuksi | 4.1 | Pieni-keskisuuri |

## Myöhemmät laajennukset — EI toteuteta ennen laukaisuehtoa

Ks. `ARCHITECTURE_OPTIONS.md`:n laukaisuehtotaulukko täydellisenä. Tiivistetty:

| Laajennus | Laukaiseva ehto (pitää olla havaittu ja dokumentoitu ennen toteutusta) |
|---|---|
| Vektorihaku | Dokumentoitu, toistuva avainsanahaun epäonnistuminen semanttisen sanastoeron takia |
| Tietograafi | Toistuva tarve moniportaiseen suhdepäättelyyn ajassa (ei kertaluonteinen) |
| Erillinen muistipalvelu (Letta/Zep/Mem0-tyyppinen) | SQLite-mittakaava ylittyy havaittavasti TAI useita samanaikaisia kirjoittajia tarvitaan reaaliajassa |
| Rinnakkaiskirjoituksen lukitus (`version`-kentän aktiivinen tarkistus) | Useampi samanaikainen istunto/kirjoittaja havaittu käytännössä |
| Moniagenttirakenne muistin hallintaan | Havaittu tarve ajaa useita rinnakkaisia validointi-/hakuprosesseja suurella kuormalla |
| Automaattinen ristiriitojen ratkaisu (ei ihmisen kuittausta) | Ei toteuteta koskaan oletuksena — tämä on tarkoituksellinen, pysyvä rajoitus, ei väliaikainen (ks. RESEARCH_REPORT B4 ja MEMORY_DESIGN "ristiriitojen ratkaisukäytäntö" kohta 3) |

## Ei sisälly tähän backlogiin

- Integraatio ChatGPT:hen tai Copilotiin ohjelmallisesti — RESEARCH_REPORT.md C4 osoittaa, ettei tällaista vientirajapintaa ole dokumentoidusti olemassa. Jos tarve tulee, se on **erillinen selvitystehtävä** (varmista Microsoft Graph -tason API Copilotille), ei suoraan toteutettava kohta.
- Minkään olemassa olevan järjestelmän (Claude Code -asetukset, muut projektit) muuttaminen — toimeksianto rajaa tämän tutkimustehtävän ulkopuolelle.
