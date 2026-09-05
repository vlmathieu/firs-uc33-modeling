# Lab 2 — Reading dirty data

**Monday 7 September · 14:35 – 15:35 · 45 minutes of work, split by the break · in pairs**

## Goal

Load a real file, diagnose what is wrong with it, clean it with a script, and produce a
figure.

This is not an artificial exercise. `comtrade_fr_roundwood_dirty.csv` was not rigged to
trap you: it is what an export from a French-configured Excel produces. You will be
handed files in that shape for your entire career.

**Work as mirrors, R and Python**: one of you in R, the other in Python, then compare.
You will find the problems are the same and the solutions look alike.

**The break falls inside this lab**, at 15:00. Steps 1 to 5 come before it, steps 6 and 7
after. That is deliberate: you diagnose first, you act second.

---

## Core

### 1. Look before loading (5 min)

Download `comtrade_fr_roundwood_dirty.csv` into `data/raw/`.

**Do not open it in Excel.** Look at its first lines from the terminal:

```
head -3 data/raw/comtrade_fr_roundwood_dirty.csv
```

On **Windows PowerShell** — the default terminal in VS Code on Windows — `head` does not
exist. Use:

```powershell
Get-Content -Head 3 data\raw\comtrade_fr_roundwood_dirty.csv
```

Worth noticing in passing: the terminal is not one thing, and its commands are not
universal. That is one more difference between your machines that your work has to
survive.

Answer these four questions before writing a single line of code:

- what is the column separator?
- what is the decimal separator?
- why are some fields quoted?
- how many columns are there?

### 2. Load naively, and read the error (5 min)

```r
trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv")
```

```python
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv")
```

**Both fail.** You do not get a wonky table: you get an error, and it is not the same
one in the two languages.

| | Message |
|---|---|
| R | `more columns than column names` |
| Python | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb3` |

Before fixing anything, answer three questions:

- what exactly is R complaining about? How does it relate to what you saw at step 1?
- what is Python complaining about? It is not the same problem. Which one does it hit
  first?
- why do two languages reading **the same file** not report the same thing?

This is the first error-reading exercise of the day. An error message names the problem
the tool hit **first**, not the list of everything that is wrong.

### 3. Load correctly (10 min)

Three things to declare: the separator, the decimal mark, the encoding.

```r
trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                  sep = ";", dec = ",", fileEncoding = "latin1")
```

```python
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                    sep=";", decimal=",", encoding="latin-1")
```

Check three things:

- `Côte d'Ivoire` and `Türkiye` display correctly;
- `qty`, `netWgt` and `primaryValue` are numeric;
- you have **674 rows and 13 columns**.

> **A trap you will hit in Python.** The `qtyUnitAbbr` column contains the literal
> string `N/A`, meaning "unit not reported". pandas converts it to a missing value
> automatically. Is that what you want? Argue it, then decide — and write your decision
> in a comment.

### 4. Read the columns before using them (5 min)

Open the [data dictionary](../../05-data/README.md) and answer without computing
anything:

- which column gives a **volume**, and in what unit?
- which column gives a **weight**, and in what unit?
- what do you get by dividing one by the other?
- what is in `aggrLevel`? Look at its distribution before answering — `table()` in R,
  `.nunique()` in Python. What can you do with it?
- do `partnerISO` and `partnerDesc` say the same thing? Which of the two would you
  filter on, and why?

Five minutes here will save you from building a grouping that groups nothing.

### 5. Diagnose (5 min)

Write a short check block answering these questions:

- how many missing values, and in which columns?
- how many rows have `qty = 0`?
- which units appear in `qtyUnitAbbr`?
- what distinct values does `partnerDesc` take? **Look at that list carefully.**

The last question is the most important in this lab.

### 6. Clean (10 min)

Produce `data/processed/trade_clean.csv` from the raw version, with a script,
documenting every decision in a comment — the *why*, not the *what*.

At minimum:

- handle the `World` aggregate;
- decide what to do with the `qty = 0` rows;
- decide what to do with the missing net weights;
- decide what to do with columns that contribute nothing;
- convert `period` to a number if you need it as one.

There is no single right answer. There are decisions, and they must be written down.

### 7. A figure (5 min)

Produce, in `output/figures/`, a figure showing the **2022-2024 trend in French oak log
exports (`440391`) by destination country**, by value.

Keep the top five partners, aggregate the rest.

---

## The trap you must not miss

`World` is not a country. It is the aggregate of all partners.

If you sum `primaryValue` without excluding those rows, **your total is exactly twice
the true one**. No error will be raised. Your figure will look fine. Your numbers will
be wrong.

Check your cleaning: on the rows where France is the reporter, the total with `World`
is $1,557.0M and without `World` $778.5M.

If you get 1,557, re-read your filter.

One last point on *how* to filter. `partnerDesc != "World"` works, and so does
`partnerISO != "W00"`. Prefer the second: a name gets translated, renamed and spelled
several ways; a reserved code does not. It is a reflex that will serve you on every
classification you meet this year.

---

## What you should have understood by the end

- A CSV is not a format, it is a family of formats. Separator, decimal mark and
  encoding are declared, not guessed.
- A numeric column read as text does not always crash: sometimes it gives a wrong
  answer.
- A missing value can be encoded five different ways in the same file.
- **Looking at the distinct values of a column before summing it** is the single
  gesture that will save you the most errors this year.
- A column whose name looks clear can be redundant, constant, or mean something other
  than you assume. Read the dictionary before computing.

Challenges, if you have finished: [`challenges.md`](challenges.md).
