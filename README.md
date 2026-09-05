# UC 3.3 Modeling — course material

**FIRS** — *Forest Information and Resource Strategies*, AgroParisTech, 2026-2027.
Course unit 3.3, part of teaching unit 3.
**Course unit leads: A. Lobianco and V. Mathieu.**

This repository holds everything you need for the course unit: slides, labs, datasets,
reference sheets, and the model cartography pack.

---

## Where to start

| If you are… | Go to |
|---|---|
| before the first session | [`00-admin/installation-guide.md`](00-admin/installation-guide.md) |
| stuck on an error | [`00-admin/how-to-ask-a-question.md`](00-admin/how-to-ask-a-question.md), then [open an issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose) |
| looking up a word | [`02-reference/glossary-en-fr.md`](02-reference/glossary-en-fr.md) |
| translating R into Python | [`02-reference/r-python-julia-equivalents.md`](02-reference/r-python-julia-equivalents.md) |
| in a lab session | [`04-labs/`](04-labs/) |
| working on the model cartography | [`06-cartography/`](06-cartography/) |

---

## Layout

```
00-admin/        installation, how to ask for help
01-handbook/     the course handbook (Quarto source + printable PDF)
02-reference/    glossary, cross-language equivalents, terminal cheatsheet
03-lectures/     lecture material, one folder per session
04-labs/         briefs, challenges and solutions
05-data/         toy datasets, with their data dictionary
06-cartography/  guidance note, analysis grid, assessment criteria
07-links.md      external resources
```

Folders are numbered and sessions are dated `YYYY-MM-DD` so that alphabetical order is
reading order. That is not decoration: it is one of the rules taught in this course
unit, and **this repository applies what it teaches**. You are invited to check — and
to report anywhere it fails to.

Nothing is ever renamed or moved: a link handed out in September still works in
January.

---

## What changes, and when

The repository evolves throughout the year. Additions and, above all, **corrections**
are recorded in [`CHANGELOG.md`](CHANGELOG.md).

If you are working from material downloaded a few weeks ago, that is the first file to
open.

---

## Asking a question

**The issues on this repository are the technical question channel for the course
unit.**

A question asked here gets an answer the whole cohort can read — and your problem is
almost never yours alone. The form asks for your operating system, your version, a
minimal example and the complete error message. That is not bureaucracy: it is exactly
the *reprex* method taught on 7 September. It is common to find the answer while
filling the form in.

[→ Open an issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose) ·
[→ The protocol, in three minutes](00-admin/how-to-ask-a-question.md)

Public repository: no names, no marks, no personal data in issues or in screenshots.

---

## Licences

- **Code** (scripts, examples, templates): [MIT](LICENSE).
- **Documents** (slides, briefs, handbook, notes):
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free reuse, including
  commercially and in modified form, provided the source is credited.
- **Data**: see [`05-data/README.md`](05-data/README.md). Extracts come from
  UN Comtrade and are redistributed for teaching purposes, with their provenance.

To cite this material, see [`CITATION.cff`](CITATION.cff).
