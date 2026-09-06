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
│   ├── 02_cleaning.R     <- lab 2. Leave them alone for now.
│   ├── 02_cleaning.py
│   ├── 03_figure.R
│   ├── 03_figure.py
│   ├── 04_mirror.R
│   └── 04_mirror.py
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

```r
install.packages("here")   # once, on the machine
library(here)              # every session, at the top of the script
```

There is also a button: the **Packages** pane, bottom right of RStudio, *Install*, type
the name, *Install*. Watch the console while you click it — it writes
`install.packages(...)` for you. There is only one mechanism; the button types it.

While you are at it, install `ggplot2` too — you will need it in lab 2 and a package
download in the middle of an exercise wastes everyone's time:

```r
install.packages("ggplot2")
```

Replace your relative path with a call to `here()`:

```r
read.csv(here("data", "raw", "comtrade_fr_roundwood_clean.csv"))
```

Understand the difference between those two lines: the first downloads, the second
declares a need. They do not go in the same place and they do not happen at the same
rhythm. Install once per machine; load every session.

Python works the same way and says it differently — `pip install` and `import`. The
commands, and the one trap in them, are in
[`challenges.md`](challenges.md), challenge 1.

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
