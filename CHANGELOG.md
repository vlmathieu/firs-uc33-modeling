# Changelog

All notable changes to this repository are recorded here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

If you downloaded material before one of the dates below, check what has changed since
— particularly the "Fixed" entries.

## 2026-09-05

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
