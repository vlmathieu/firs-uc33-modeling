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

### Fixed

- Lab 2, step 6 claimed `period` was read as text and had students convert it. It is not:
  on this file `period` arrives as an integer in both languages. The columns actually at
  risk are `qty`, `netWgt` and `primaryValue`, whose decimal mark is a comma. Point (e)
  now asks for the type check that finds them, and sends anyone holding a text column
  back to step 3 rather than patching it. The two solution scripts assert the types
  instead of converting.

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
- Lab 1, step 1 links straight to the template repository instead of naming it, and its
  layout listing shows the six scripts the template now ships.
- Lab 2, step 1 links straight to the data file.
- Lab 2, step 6 gives a runnable line for every option of every decision, not only for
  the ones with a single answer: both ways of filtering the aggregate, dropping the
  zero-quantity rows against neutralising them at the division, dropping the missing
  weights against excluding them at the computation. Point (c) had no code at all. Every
  block is labelled `# R` or `# Python`, and `row.names = FALSE` / `index=False` are
  explained — including what the phantom column is called when it comes back.
- Lab 2, step 7 moves into its own script. The template ships `src/03_figure.R` / `.py`
  complete, and the exercise becomes running it a block at a time rather than typing
  twenty lines of aggregation in five minutes. The brief explains why a third script:
  each stage reads a file and writes a file, so one can be re-run, handed over or broken
  on its own. `matplotlib` is named as a separate install, and the `plt` import is shown
  where it belongs.
- Lab 1, challenge 1 documents the two errors that stop every VS Code user before the
  exercise starts: `ModuleNotFoundError: No module named 'pandas'`, and
  `NameError: name '__file__' is not defined` when the line is sent to the console with
  `Shift+Enter`. `__file__` in a script, `Path.cwd()` in the console, and the reason R
  needs no such distinction.
- Lab 1, step 1 links straight to the template repository instead of naming it.
- Lab 1, step 5 says what the RStudio *Packages* pane button actually does, and points
  at challenge 1 for the Python equivalent. The core of lab 1 stays in R.
- Lab 1, challenge 1 opens VS Code before anything else: File → Open Folder on
  `uc33-lab1`, the trust prompt, the check that the tree actually loaded, opening
  `src/01_import.py`, and a `pwd` in a fresh terminal to prove the working directory is
  the project root. Opening the folder is VS Code's `.Rproj`, and nothing warns you when
  you have skipped it. A note explains the `.Rproj.user/` folder that RStudio hides and
  VS Code does not.
- Lab 1, challenge 1 installs `pandas` before asking for anything: the terminal command
  with its Windows fallback, an install/load table against R's `install.packages()` and
  `library()`, the four things that go wrong — wrong prompt, bare `pip`, no restart,
  two Pythons — and the two `sys.executable` calls that identify the last of them. It
  then explains `NameError: name '__file__' is not defined`, which is what
  `Shift+Enter` produces on a `pathlib` line: `__file__` in a script, `Path.cwd()` in
  the console, and the reason R needs no such distinction.
- Lab 2, step 2 shows the `import pandas as pd` it had left implicit, and says what to
  do if it fails.
- The challenges that need a package now give the install line: `pyyaml` in lab 1
  challenge 3, `pyarrow` in lab 2 challenge 5, both as `python -m pip install`.
- Lab 1, challenge 3 wraps its three Python lookups in `print()`. A bare name displays
  its value in the console and displays nothing in a script, where these lines end up —
  and R, which prints a top-level name either way, gives no warning that Python will
  not.
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
- Lab 2, challenge 5 answers its own closing question. "Why is CSV still the most
  widely used format in the world" was left hanging at the end of the last challenge of
  the day, where nobody was going to come back to it. The answer ends on the point that
  transfers: choose the format by which side of the exchange you are on, which is the
  `raw/` versus `processed/` split the template already imposes.
- Lab 2's challenges are rewritten. Every code block is labelled `# R` or `# Python`
  and every line carries a comment saying what it does — for these pages only, since
  the what is the lesson here. Challenge 1 says which script to extend, explains what
  `cut()` / `pd.cut()` and `tapply()` / `.groupby()` actually do, and now walks all the
  way to the answer instead of stopping at "investigate": the volume bands, the table
  of results, the smallest volumes, and the three-line conclusion. Challenge 2 moves
  into `src/04_mirror`, which the template now ships. Challenges 3 and 5 say to work in
  the console, and 5 loads `pyarrow` rather than assuming it.
- The lab 2 solution is one script per job, like the project it teaches:
  `02_cleaning` is the brief, `03_figure` is step 7, `02_cleaning_challenges` is the
  density investigation, `04_mirror` is the mirror statistics. The figure no longer
  sits inside a cleaning script.
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
