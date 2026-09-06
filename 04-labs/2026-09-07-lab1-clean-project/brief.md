# Lab 1 — Building a clean project

**Monday 7 September · 13:50 – 14:35 · 45 minutes · in pairs**

## Goal

By the end of this lab your working folder runs **on your partner's machine, with
nothing for them to change**. That is rung 3 of the reproducibility ladder, and it will
be checked by someone other than you.

You each work on your own machine. The cross-check comes at the end.

---

## Core

### 1. Get the template (5 min)

Go to [`uc33-project-template`](https://github.com/vlmathieu/uc33-project-template),
green *Code* button → *Download ZIP*. Unzip it, rename the folder `uc33-lab1`.

**Put it outside any synced folder** — not in OneDrive, iCloud, Google Drive or
Dropbox. Those services move files while you are standing on them. If you have no
choice, note it: we will come back to it if something breaks.

Check that you get this layout:

```
uc33-lab1/
├── data/
│   ├── raw/          <- empty for now
│   └── processed/
├── src/
│   ├── 01_import.R
│   ├── 01_import.py
│   ├── 02_cleaning.R     <- lab 2. Leave it alone for now.
│   └── 02_cleaning.py
├── output/
│   ├── figures/
│   └── tables/
├── config/
│   └── config.yml
├── doc/
├── README.md
└── uc33-project.Rproj
```

Rename `uc33-project.Rproj` to `uc33-lab1.Rproj`: an `.Rproj` file normally carries the
project's name.

### 2. Install the data (2 min)

Download `comtrade_fr_roundwood_clean.csv` from [`05-data/`](../../05-data/) and put it
in **`data/raw/`**.

From now on that file is read-only. You do not open it in Excel, you do not overwrite
it, you do not rename it.

### 3. Open the project, both ways (5 min)

**In RStudio**: double-click `uc33-lab1.Rproj`. Check that the project name appears in
the top right corner, then type in the console:

```r
getwd()
```

The result must be the project root. That is what the `.Rproj` file does, and it is why
you will never write `setwd()`.

**In VS Code**: *File* → *Open Folder* → select `uc33-lab1`. You must see the whole
tree in the explorer on the left, not a single file.

### 4. Fix a script (15 min)

Open `src/01_import.R`. It contains three problems. Fix them.

1. An **absolute path**. Replace it with a path relative to the project root.
2. A **`setwd()`**. Delete it. It should break nothing: if the project is opened
   properly, it is useless.
3. An **output written in the wrong place**. Processed data goes in
   `data/processed/`, never next to the raw data.

The script must produce `data/processed/trade_france.csv` and nothing else.

### 5. Install and load a package (5 min)

**Do both languages, whichever one you are working in.** You need `pandas` this
afternoon whether or not you write Python today: lab 2 and lab 3 both use it.

#### R — from inside R

```r
install.packages("here")     # once, on the machine
install.packages("ggplot2")  # you need it in lab 2. Get the download over with now.

library(here)                # every session, at the top of the script
```

There is also a button: the **Packages** pane, bottom right of RStudio, *Install*, type
the name, *Install*. Watch the console while you click it — it writes
`install.packages(...)` for you. There is only one mechanism; the button types it.

#### Python — from the terminal, not from Python

In VS Code, open a terminal: **Terminal → New Terminal**, or ``Ctrl+` ``.

```
python -m pip install pandas
```

Then, in your script or console:

```python
import pandas as pd     # every session, at the top of the script
```

Three things about that command, because it is the one that goes wrong.

- It runs **in the terminal**, at the ordinary shell prompt. Not at the `>>>` Python
  prompt, and not in a `.py` file.
- Write `python -m pip`, not `pip`. Your machine has more than one Python. Bare `pip`
  may install into one of them while VS Code runs another, and the package is then
  missing even though the install said it succeeded. `python -m pip` installs into the
  interpreter that runs the command.
- **Windows**: if `python` is not recognised, use `py -m pip install pandas`.

After installing, **start a new Python session**. A package installed while a session is
open is not visible to that session.

#### The distinction that matters, in both languages

| | Install | Load |
|---|---|---|
| R | `install.packages("here")` | `library(here)` |
| Python | `python -m pip install pandas` | `import pandas as pd` |
| How often | **Once per machine** | **Every session**, at the top of the script |

The first downloads. The second declares a need. They do not go in the same place and
they do not happen at the same rhythm — and confusing them is the cause of the error you
will meet in lab 3, script 2.

Note where each one lives, because the two languages disagree: R installs its packages
**from inside R**, Python installs its packages **from outside Python**. That is why
RStudio can offer a button and VS Code cannot.

#### Finally, use `here()`

Replace your relative path with a call to `here()`:

```r
read.csv(here("data", "raw", "comtrade_fr_roundwood_clean.csv"))
```

### 6. Restart and run all (5 min)

In RStudio: `Session > Restart R` (or `Ctrl+Shift+F10`), then `Ctrl+Shift+Enter`.

Your script must run **top to bottom, from an empty session, with no intervention**.
If it breaks, you have just found a bug now rather than tonight.

Repeat until it is clean.

### 7. Write the README (3 min)

Four lines is enough, but they must answer three questions:

- what is this folder for?
- what has to be installed to run it?
- in what order do the scripts run?

That document is what moves your project from rung 2 to rung 3.

### 8. Cross-check (5 min)

Swap folders with your partner — USB stick, or a zip archive by email. Each of you
opens the other's project and runs their script.

**Rule: you may not change anything, and you may not ask a question.** If it does not
run, write down why and hand the folder back.

That is the only test that counts.

---

## What you should have understood by the end

- An open `.Rproj` fixes the working directory. That solves the whole problem.
- An absolute path is a declaration: "this script will only ever work on my machine".
- Installing and loading a package are two distinct actions.
- A script that does not survive a session restart is not finished.

Challenges, if you have finished: [`challenges.md`](challenges.md).
