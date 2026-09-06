# Changelog

All notable changes to this repository are recorded here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

If you downloaded material before one of the dates below, check what has changed since
— particularly the "Fixed" entries.

## 2026-09-05

### Fixed

- The installation guide never asked for **pandas**, without which no Python exercise
  of 7 September runs. New section (d): `python -m pip install pandas`, plus `pyyaml`
  and `pyarrow` for the challenges, why `python -m pip` rather than `pip`, and a fourth
  line in the verification block. Sections (d) to (g) shift to (e) to (h).

### Changed

- Afternoon labs of 7 September moved to their final times: lab 1 at 13:50, lab 2 at
  14:35, lab 3 at 15:35. The session now opens with a presentation of this repository
  and of the issue channel. Lab 2 straddles the break: steps 1 to 5 before, 6 and 7
  after.
- Lab 2 now names the script it asks for (`src/02_cleaning.R` / `.py`), says where the
  console is in RStudio and VS Code, and gives the R and Python function for every step
  from 4 to 7 instead of describing them. The challenges carry runnable code too, each
  snippet labelled R or Python.
- Lab 2, step 7 asks for a stacked bar chart and recommends `ggplot2` in R, with the
  aggregation written out and a link to the one-page cheatsheet. The published R
  solution uses `ggplot2` as well, for consistency.
- Lab 3, script 4: the encoding investigation is written out. Three console lines show
  the unreadable unit, a `grepl()` that finds nothing while warning, and a `subset()`
  that finds nothing and says nothing. The instruction to work in the console rather
  than the script is now explicit.
- Lab 1, step 1 links straight to the template repository instead of naming it.
- Lab 1, challenge 1 documents the two errors that stop every VS Code user before the
  exercise starts: `ModuleNotFoundError: No module named 'pandas'`, and
  `NameError: name '__file__' is not defined` when the line is sent to the console with
  `Shift+Enter`. `__file__` in a script, `Path.cwd()` in the console, and the reason R
  needs no such distinction.
- Lab 1, step 1 links straight to the template repository instead of naming it.
- Lab 1, step 5 now installs a package in **both** languages. R installs from inside R,
  with a note on what the *Packages* pane button actually does; Python installs
  `pandas` from the terminal with `python -m pip`, with the `py -m pip` fallback for
  Windows and the reason bare `pip` can succeed and still leave the module missing. A
  table sets install (once per machine) against load (every session), which is the
  distinction lab 3's script 2 turns on.
- Lab 1, challenge 1 documents the two errors that stop every VS Code user before the
  exercise starts: `ModuleNotFoundError: No module named 'pandas'`, with the two
  `sys.executable` calls that identify a two-Python machine, and
  `NameError: name '__file__' is not defined` when the line is sent to the console with
  `Shift+Enter`. `__file__` in a script, `Path.cwd()` in the console, and the reason R
  needs no such distinction.
- Lab 2, step 2 shows the `import pandas as pd` it had left implicit, and says what to
  do if it fails.
- The challenges that need a package now give the install line: `pyyaml` in lab 1
  challenge 3, `pyarrow` in lab 2 challenge 5, both as `python -m pip install`.
- Lab 1, challenge 3 no longer asks students to create `config/config.yml`, which the
  template already ships. It shows the real file, gives the console lines that read it
  in R and in Python, and ends on a test: change the country in the YAML and re-run
  without opening a script.
- Lab 3, challenge 2 gives the guard rail in Python as well as R, both labelled, and
  asks students to run it on the broken script so they see it fail. Two worked
  assertions on the file itself replace the bare instruction to "write three".
- Lab 3, challenge 3 explains what a reprex is made of, shows how to build a
  three-row table by hand in each language, and works a complete example through on a
  different bug. The script 5 reprex is still theirs to write.
- Lab 3, script 5 solutions now assert on `partnerISO` rather than on the `World`
  label, in line with what the lab teaches about codes and labels.
- Lab 1, step 5 installs `ggplot2` alongside `here`, so that lab 2 does not stall on a
  package download.
- The project template now ships `src/02_cleaning.R` and `.py`: header, dependencies and
  a loading line. Students no longer retype the plumbing before starting lab 2. The
  loading line is the naive one that fails — repairing it is the first task of step 6.
  Lab 1's layout listing and lab 2's step 6 were adjusted to match.

### Added

- Repository layout, README, licences, `CITATION.cff`.
- Machine prerequisites installation guide (`00-admin/`), as emailed on 4 September.
- Help-request protocol and GitHub issue form (`00-admin/`, `.github/`).
- Reference sheets: R / Python / Julia equivalents, English-French glossary, terminal
  cheatsheet (`02-reference/`).
- Toy UN Comtrade dataset — French roundwood trade, 2022-2024 — in a clean and a
  degraded version (`05-data/`).
- Briefs and challenges for the three labs of 7 September, and the five broken scripts
  of lab 3 (`04-labs/`).
- PowerShell equivalent of `head -3` in lab 2, step 1 (`Get-Content -Head 3`), for
  Windows users.
- A model project README for lab 1, step 7, published with the solutions
  (`solution/project-README-example.md`): the four lines students are asked for, plus
  what each one saves the reader, and what does not belong in a README.
