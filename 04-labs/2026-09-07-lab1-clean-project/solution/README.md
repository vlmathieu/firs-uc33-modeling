# Lab 1 — solution

## The three problems in `src/01_import.R`

| # | Problem | Why it is a problem | Fix |
|---|---|---|---|
| 1 | `setwd("C:/Users/valentin/...")` | Declares that the script will only run on one machine, under one username, for as long as the disk is not reorganised. | Delete the line. The `.Rproj` already sets the working directory to the project root. |
| 2 | Absolute path in `read.csv()` | Same reason. Sent to your partner, put on a server, or simply moved elsewhere: it breaks. | `here("data", "raw", "...")`, or failing that the relative path `"data/raw/..."`. |
| 3 | Output written into `data/raw/` | Violates the "raw data is read-only" rule. A script-generated file sitting among the source data, and nobody can tell which is which any more. | Write to `data/processed/`. |

## Step 7 — the README they were asked to write

A model one, with the reasoning behind each line, is in
[`project-README-example.md`](project-README-example.md). Compare it with yours: the
question is not whether the words match, but whether a stranger could run your project
from what you wrote, and know afterwards whether it worked.

## Expected checks

- `getwd()` returns the project root, without any `setwd()` having been written.
- The script runs from an empty session (`Ctrl+Shift+F10` then `Ctrl+Shift+Enter`).
- It produces **361 rows** in `data/processed/trade_france.csv`.
- Move or rename the folder anywhere on the disk, and the script still runs.
- Your partner runs it without changing anything and without asking a question.

## The point that matters

The three errors share one root: **the script assumes things about its environment
instead of deducing them.** It assumes a path, a user, a working directory. A
reproducible script assumes nothing: it locates itself relative to itself.

That is the move from rung 1 to rung 3 of the reproducibility ladder, and it takes
three lines.
