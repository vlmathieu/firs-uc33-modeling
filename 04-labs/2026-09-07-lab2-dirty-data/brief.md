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

## Where you work: the console first, the script second

Two places, and the difference between them is the point of the lab.

**Steps 1 to 5 go in the console.** You are exploring — you look, you print, you throw
away. Nothing you type there is meant to survive.

**Steps 6 and 7 go in scripts.** Step 6 is `src/02_cleaning.R` or `src/02_cleaning.py`,
step 7 is `src/03_figure.R` or `src/03_figure.py`. Both are already in the project you
built in lab 1 — the template ships them. From there on you are no longer exploring, you
are recording decisions. A decision that exists only in a console is a decision nobody
can check in six months — including you.

The `01_`, `02_`, `03_` prefixes are this morning's rule doing real work: they are the
order the scripts run in, written where you cannot lose it.

### Finding the console

| | How to get there |
|---|---|
| **RStudio** | Bottom-left pane, tab **Console**. The prompt is `>`. From a script, `Ctrl+Enter` sends the current line to it. |
| **VS Code, R** | `Ctrl+Shift+P` → **R: Create R Terminal**. Then `Ctrl+Enter` from a `.R` file sends the current line. |
| **VS Code, Python** | `Ctrl+Shift+P` → **Python: Start REPL** (the prompt is `>>>`). Or select some lines and press `Shift+Enter`, which opens the interactive window. |

`Ctrl+Shift+P` is the command palette from this morning: type three letters of what you
want instead of hunting through menus.

---

## Core

### 1. Look before loading (5 min)

Download [`comtrade_fr_roundwood_dirty.csv`](../../05-data/comtrade_fr_roundwood_dirty.csv)
into `data/raw/`, next to the clean one. On the GitHub page, the download button is at
the top right of the file view.

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
import pandas as pd
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv")
```

If that `import` answers `ModuleNotFoundError: No module named 'pandas'`, the package is
not installed on this machine. `python -m pip install pandas`, **in the terminal**, then
a new Python session — lab 1, step 5.

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

The functions you need. Same job, two syntaxes:

| To do this | R | Python (pandas) |
|---|---|---|
| See the structure and the types | `str(trade)` | `trade.info()` |
| See the first rows | `head(trade)` | `trade.head()` |
| Take one column | `trade$aggrLevel` | `trade.aggrLevel` |
| Its distinct values | `unique(trade$aggrLevel)` | `trade.aggrLevel.unique()` |
| Its distinct values **with their counts** | `table(trade$aggrLevel)` | `trade.aggrLevel.value_counts()` |
| How many distinct values | `length(unique(trade$aggrLevel))` | `trade.aggrLevel.nunique()` |

`table()` and `.value_counts()` are the two most useful functions in this lab. Run one of
them on any column before you group by it, filter on it, or sum it.

Five minutes here will save you from building a grouping that groups nothing.

### 5. Diagnose (5 min)

Still in the console. Four questions, and the line that answers each.

```r
colSums(is.na(trade))            # missing values, per column
sum(trade$qty == 0)              # how many rows report a zero quantity
table(trade$qtyUnitAbbr)         # which units appear, and how often
table(trade$partnerDesc)         # every distinct partner, with its row count
```

```python
trade.isna().sum()
(trade.qty == 0).sum()
trade.qtyUnitAbbr.value_counts()
trade.partnerDesc.value_counts()
```

The last line is the most important in this lab. **Read its output in full** — all of it,
to the end. Do not skim it.

### 6. Clean (10 min)

**Open `src/02_cleaning.R`** — or `src/02_cleaning.py`. It is already in your project,
laid out with this morning's skeleton: header, dependencies, load, body, output.

The loading line it contains is the naive one from step 2, the one that fails. **Your
first job is to repair it** with what you found at step 3. Then work through the five
decisions below.

Each one gets a comment saying **why**, not what. `# filter World` is worthless.
`# W00 is the all-partners aggregate: summing it double-counts every flow` is the
exercise.

**a) The `World` aggregate.** It is the total of all partners, sitting in the table
alongside the partners it is the total of.

```r
clean <- subset(trade, partnerISO != "W00")
```
```python
clean = trade[trade.partnerISO != "W00"].copy()
```

In Python, `.copy()` is not decoration: without it pandas warns you later that you are
modifying a view of another table rather than a table of your own.

**b) The rows with `qty = 0`.** Seventeen of them. They are real flows with an
unreported quantity — but any division by that zero gives infinity, which then travels
through a mean without a sound. Decide: drop the rows, or keep them and exclude the zero
only where you divide? Whichever you choose, write down why.

```r
sum(trade$qty == 0)                          # count them first
clean <- subset(clean, qty > 0)              # if you decide to drop them
```
```python
(trade.qty == 0).sum()
clean = clean[clean.qty > 0]
```

**c) The missing net weights.** Eleven rows. Same question, same rule: a decision, and a
reason.

```r
sum(is.na(trade$netWgt))
```
```python
trade.netWgt.isna().sum()
```

**d) Columns that contribute nothing.** You found one at step 4 — `aggrLevel` holds the
same value on all 674 rows. A constant column allows no filter, no grouping and no
statistic, and left in place it invites a `group_by` that groups nothing.

```r
clean$aggrLevel <- NULL
```
```python
clean = clean.drop(columns=["aggrLevel"])
```

**e) `period` as a number.** It comes in as text. Convert it explicitly rather than
hoping.

```r
clean$period <- as.integer(clean$period)
```
```python
clean["period"] = clean.period.astype(int)
```

Then write the result out:

```r
write.csv(clean, here("data", "processed", "trade_clean.csv"), row.names = FALSE)
```
```python
clean.to_csv(ROOT / "data" / "processed" / "trade_clean.csv", index=False)
```

The toolbox, in one table:

| To do this | R | Python (pandas) |
|---|---|---|
| Keep some rows | `subset(df, cond)` | `df[cond]` |
| Drop a column | `df$col <- NULL` | `df.drop(columns=["col"])` |
| Add a column | `df$new <- ...` | `df["new"] = ...` |
| Convert a type | `as.integer(df$period)` | `df.period.astype(int)` |
| Count rows | `nrow(df)` | `len(df)` |
| Write a CSV | `write.csv(df, path, row.names = FALSE)` | `df.to_csv(path, index=False)` |

There is no single right answer to any of these five. There are decisions, and there are
undocumented decisions. Only one of the two is defensible in six months.

### 7. A figure (5 min)

**This one is written for you.** Open `src/03_figure.R` or `src/03_figure.py` — the
template ships it, filled in. Your job is not to type it: it is to **run it one block at
a time and work out what each block does.**

`Ctrl+Enter` in RStudio, `Shift+Enter` in VS Code. Send the first block, look at what
appeared. Send the second, look again. Do not run the whole file until you can say what
each of the three parts produced.

#### Why a third script, and not more of `02_cleaning`

You now have three scripts, and each does one job:

| | Reads | Writes |
|---|---|---|
| `01_import.R` | `data/raw/…clean.csv` | `data/processed/trade_france.csv` |
| `02_cleaning.R` | `data/raw/…dirty.csv` | `data/processed/trade_clean.csv` |
| `03_figure.R` | `data/processed/trade_clean.csv` | `output/figures/oak_destinations.png` |

That is a **pipeline**, and it is worth naming, because it is how every project you
build this year will be organised.

Each script starts from a file on disk, not from something left in memory by the
previous one. That has three consequences you will feel within a month:

- **You can re-run one stage without re-running the others.** Changing a colour in the
  figure does not mean re-reading and re-cleaning 674 rows.
- **You can hand one stage to someone else.** Your partner can rewrite `03_figure`
  without ever opening your cleaning code.
- **A stage that breaks tells you where.** One script, one job, one place to look.

The numeric prefixes say the order. That is this morning's naming rule doing real work:
`01`, `02`, `03` is a run order that survives you forgetting it.

#### What the figure shows

A **stacked bar chart**: one bar per year, 2022 to 2024, each bar split by destination
country, height in millions of dollars. French oak log exports only
(`cmdCode == 440391`).

Why that chart and not a line chart: you have three years. Three points make a poor
line, and six lines on three points make a poor figure. A stacked bar shows the total
*and* its composition at the same time, which is what the question actually asks.

The top five destinations are kept by name and everything else gathered into `Other` —
otherwise you get sixty legend entries and no readable figure.

#### R — `ggplot2`

It is the reason many people learn R at all, and it is worth your first contact today.
You installed it in lab 1, step 5; if you skipped that:

```r
install.packages("ggplot2")   # once, on the machine
```

The plotting block of `03_figure.R` is this:

```r
ggplot(graph, aes(x = factor(period), y = primaryValue / 1e6, fill = destination)) +
  geom_col() +
  labs(title = "French oak log exports (HS 440391)",
       x = NULL, y = "million USD", fill = "Destination")

ggsave(here("output", "figures", "oak_destinations.png"),
       width = 9, height = 5, dpi = 150)
```

Read it as a grammar rather than a function. **`aes()` maps columns onto visual
properties** — `period` onto the x axis, value onto the height, `destination` onto the
fill colour. **`geom_col()` says draw those as bars.** **`labs()` names things.** Layers
are added with `+`, and each one does one job.

→ [The ggplot2 cheatsheet](https://rstudio.github.io/cheatsheets/data-visualization.pdf)
— one page, and the only ggplot2 documentation you need this year.

#### Python — pandas and matplotlib

pandas draws the chart, but the drawing itself is done by **matplotlib**, which is a
separate package and is not installed with pandas. In the terminal:

```
python -m pip install matplotlib
```

Then the import goes at the top of the script, with the others — it is already there in
`03_figure.py`:

```python
import matplotlib.pyplot as plt
```

`plt` is to matplotlib what `pd` is to pandas: a conventional short name. If you forget
it, the failure is the one you will meet again in lab 3, script 2:
`NameError: name 'plt' is not defined`.

The plotting block is this:

```python
ax = (graph / 1e6).plot(kind="bar", stacked=True, figsize=(9, 5), width=0.6)
ax.set_title("French oak log exports (HS 440391)")
ax.set_xlabel("")
ax.set_ylabel("million USD")
ax.legend(title="Destination", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(ROOT / "output" / "figures" / "oak_destinations.png", dpi=150)
```

#### Before you move on

Open the PNG. Compare it with your partner's, who built it in the other language. Same
data, same five destinations, two different libraries: the bars should have the same
heights.

If yours are twice as tall, you know exactly which line to re-read.

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
