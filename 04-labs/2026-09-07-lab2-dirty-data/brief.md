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

**Step 6 goes in a script**: `src/02_cleaning.R` or `src/02_cleaning.py`, inside the
project you built in lab 1. From there on you are no longer exploring, you are recording
decisions. A decision that exists only in a console is a decision nobody can check in six
months — including you.

The `02_` prefix is this morning's rule: it says this script runs after `01_import`.

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

**Open a script now**: `src/02_cleaning.R` or `src/02_cleaning.py`.

Start from this morning's skeleton — header, dependencies, parameters, body, output — and
paste in the loading line from step 3. Then work through the five decisions below.

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

Produce, in `output/figures/`, a **stacked bar chart**: one bar per year, 2022 to 2024,
each bar split by destination country, height in millions of dollars. French oak log
exports only (`cmdCode == 440391`).

Why that chart and not a line chart: you have three years. Three points make a poor line,
and six lines on three points make a poor figure. A stacked bar shows the total *and* its
composition at the same time, which is what the question actually asks.

Keep the top five destinations and gather everything else into `Other` — otherwise you
get sixty legend entries and no readable figure.

**In R, use `ggplot2`.** It is the reason many people learn R at all, and it is worth
your first contact today.

```r
install.packages("ggplot2")   # once, on the machine
library(ggplot2)              # every session
```

Three steps: filter, aggregate, plot.

```r
# 1. Filter: French oak log exports
oak <- subset(clean, cmdCode == 440391 &
                     reporterDesc == "France" &
                     flowDesc == "Export")

# 2. Aggregate. Read the formula as: sum primaryValue, for each
#    combination of period and partnerDesc.
by_country <- aggregate(primaryValue ~ period + partnerDesc, data = oak, FUN = sum)

#    The five biggest destinations over the whole period
totals <- aggregate(primaryValue ~ partnerDesc, data = by_country, FUN = sum)
totals <- totals[order(-totals$primaryValue), ]
top5   <- head(totals$partnerDesc, 5)

#    Everything else becomes "Other", then re-aggregate so the Others add up
by_country$destination <- ifelse(by_country$partnerDesc %in% top5,
                                 by_country$partnerDesc, "Other")
graph <- aggregate(primaryValue ~ period + destination, data = by_country, FUN = sum)

# 3. Plot
ggplot(graph, aes(x = factor(period), y = primaryValue / 1e6, fill = destination)) +
  geom_col() +
  labs(title = "French oak log exports (HS 440391)",
       x = NULL, y = "million USD", fill = "Destination")

ggsave(here("output", "figures", "oak_destinations.png"),
       width = 9, height = 5, dpi = 150)
```

How to read that `ggplot()` call, because it is a grammar rather than a function:
**`aes()` maps columns onto visual properties** — `period` onto the x axis, value onto
the height, `destination` onto the fill colour. **`geom_col()` says draw those as bars.**
**`labs()` names things.** You add layers with `+`, and each one does one job.

→ [The ggplot2 cheatsheet](https://rstudio.github.io/cheatsheets/data-visualization.pdf)
— one page, and the only ggplot2 documentation you need this year.

**In Python**, pandas plots straight from a pivot table:

```python
oak = clean[(clean.cmdCode == 440391)
            & (clean.reporterDesc == "France")
            & (clean.flowDesc == "Export")]

by_country = oak.pivot_table(index="period", columns="partnerDesc",
                             values="primaryValue", aggfunc="sum", fill_value=0)

top5  = by_country.sum().sort_values(ascending=False).index[:5]
graph = by_country[list(top5)].copy()
graph["Other"] = by_country.drop(columns=list(top5)).sum(axis=1)

ax = (graph / 1e6).plot(kind="bar", stacked=True, figsize=(9, 5))
ax.set_ylabel("million USD")
ax.set_title("French oak log exports (HS 440391)")
plt.tight_layout()
plt.savefig(ROOT / "output" / "figures" / "oak_destinations.png", dpi=150)
```

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
