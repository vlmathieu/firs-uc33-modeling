# Lab 2 — Challenges

Take these if you have finished the core. Do not do them instead of it.

Every code block below is labelled **`# R`** or **`# Python`**, and every line carries a
comment saying what it does. That density of comment is for today only: in your own
scripts, comment the **why**, not the what. Here the what is the lesson.

---

## 1. The wood that floats in air — an investigation

**Where you work: in `src/02_cleaning.R` or `src/02_cleaning.py`**, at the end, after the
five decisions. This challenge adds two columns to your cleaned table, and a column that
exists only in a console is a column nobody else will ever see.

### a) Compute the apparent density

Density is weight divided by volume. The file gives you both: `netWgt` in kilograms and
`qty` in cubic metres — but only on the rows where `qtyUnitAbbr` really is `m³`.

```r
# R
volume <- ifelse(clean$qtyUnitAbbr == "m³" & clean$qty > 0,   # keep only real volumes
                 clean$qty,                                    # ... use qty there
                 NA)                                           # ... and NA elsewhere
clean$density <- clean$netWgt / volume                         # kg / m3

d <- subset(clean, !is.na(density))     # rows where a density could be computed
nrow(d)                                 # 635
median(d$density)                       # 882 kg/m3 -- plausible for green timber
summary(d$density)                      # min, quartiles, max: look at the extremes
```

```python
# Python
volume = clean.qty.where((clean.qtyUnitAbbr == "m³")      # keep only real volumes
                         & (clean.qty > 0))               # ... NaN everywhere else
clean["density"] = clean.netWgt / volume                  # kg / m3

d = clean[clean.density.notna()].copy()   # rows where a density could be computed
len(d)                                    # 635
d.density.median()                        # 882 kg/m3
d.density.describe()                      # count, mean, min, quartiles, max
```

Two things to notice in those four lines.

**`qty > 0` is not decoration.** Dividing by zero gives `Inf` in R and `inf` in Python.
Neither raises an error, and both travel through a mean and make it infinite.

**A density that cannot be computed is not an impossible one.** The rows with no volume
are dropped from the investigation, not counted as aberrant. That distinction is exactly
what the published solution got wrong on its first attempt — see the solution README.

### b) Flag the impossible ones

The lightest wood in the world, balsa, is 160 kg/m³. The heaviest, lignum vitae, is
1,250. Anything outside [200, 1300] is not wood.

**Write the guard rail first** — a line that stops the script rather than let it produce
a wrong answer:

```r
# R
stopifnot(all(d$density > 200 & d$density < 1300))   # FAILS. That is the point.
```

```python
# Python
assert d.density.between(200, 1300).all(), "physically impossible densities"   # FAILS
```

Run it. It fails. You now have a script that refuses to lie to you — and a question to
answer before you can go any further.

Then add the flag to your cleaned table, as a column:

```r
# R
DENS_MIN <- 200                                  # lighter than balsa: impossible
DENS_MAX <- 1300                                 # heavier than lignum vitae: impossible

clean$density_suspect <- !(clean$density >= DENS_MIN &     # TRUE when out of range
                           clean$density <= DENS_MAX)      # NA stays NA in R
sum(clean$density_suspect, na.rm = TRUE)                   # 86 rows
```

```python
# Python
DENS_MIN, DENS_MAX = 200, 1300

clean["density_suspect"] = (clean.density.notna()                       # computable...
                            & ~clean.density.between(DENS_MIN, DENS_MAX))  # ...and out of range
int(clean.density_suspect.sum())                                        # 86 rows
```

The `.notna()` in the Python version is the fix for the bug mentioned above:
`~series.between(a, b)` returns `True` for a missing value, which would flag 21
uncomputable rows as impossible ones.

### c) Now find out *why* — the two functions you need

About **13.5 %** of the computable densities are outside the range. Before you can
decide what to do with them, you have to know what they have in common.

The gesture is always the same: **cut a continuous column into bands, then compute
something inside each band.** Two functions, one for each half.

**`cut()` / `pd.cut()` — turn a number into a category.**

You give it the boundaries; it tells you, for each row, which interval that row falls
into. `breaks = c(0, 10, 100, 1000, Inf)` makes four bands: 0 to 10, 10 to 100, 100 to
1000, and 1000 upwards. `labels` names them, otherwise you get `(0,10]` printed
everywhere.

**`tapply()` / `.groupby()` — apply a function within each group.**

`tapply(x, g, FUN)` reads as: split `x` according to `g`, and run `FUN` on each piece.
`d.groupby("g").x.mean()` reads the same way, in the other order. This is the single
most useful gesture in data analysis, and you are meeting it in both languages at once.

One trick that does the work here: **the mean of a TRUE/FALSE column is the share of
TRUEs.** `mean(c(TRUE, FALSE, TRUE, TRUE))` is 0.75. So the mean of `density_suspect`
inside a band *is* the percentage of aberrant flows in that band.

```r
# R
d <- subset(clean, !is.na(density))                  # the computable rows again

d$band <- cut(d$qty,                                 # the column to slice
              breaks = c(0, 10, 100, 1000, Inf),     # the four boundaries
              labels = c("< 10", "10-100",           # a readable name per band
                         "100-1000", "> 1000"))

table(d$band)                                        # how many flows per band
tapply(d$density_suspect, d$band, mean)              # share aberrant, per band
tapply(d$qty, d$density_suspect, median)             # median volume: aberrant vs not
```

```python
# Python
d = clean[clean.density.notna()].copy()              # the computable rows again

d["band"] = pd.cut(d.qty,                            # the column to slice
                   [0, 10, 100, 1000, float("inf")], # the four boundaries
                   labels=["< 10", "10-100",         # a readable name per band
                           "100-1000", "> 1000"])

d.band.value_counts().sort_index()                   # how many flows per band
d.groupby("band", observed=True).density_suspect.mean()   # share aberrant, per band
d.groupby("density_suspect").qty.median()                 # median volume, aberrant vs not
```

### d) What you should be looking at

| Volume band | Flows | Aberrant |
|---|---|---|
| < 10 m³ | 89 | **46 %** |
| 10 – 100 m³ | 127 | 6 % |
| 100 – 1000 m³ | 153 | 12 % |
| > 1000 m³ | 266 | 7 % |

Median volume of an aberrant flow: **20.5 m³**. Of a plausible one: **668 m³**.

The first row is the whole answer. Look at the smallest volumes to confirm it:

```r
# R
sort(unique(d$qty))[1:10]      # 0.001, 0.013, 0.020, ... cubic metres
```
```python
# Python
sorted(d.qty.unique())[:10]    # 0.001, 0.013, 0.020, ...
```

A weight rounded to the kilogram, divided by a volume rounded to the thousandth of a
cubic metre, produces any number you like. This is **arithmetic, not fraud** — and it is
not a data entry error either, which is what most people guess first.

### e) Write the conclusion, in three lines

In your script, as a comment. What explains what, what you keep, what you discard, why.
Here is the shape of a defensible answer:

```r
# 1. 46 % of the flows under 10 m3 are aberrant, against 6-12 % everywhere else.
# 2. Cause: rounding. Tiny volumes (down to 0.001 m3) divided into weights
#    rounded to the kilo give meaningless ratios.
# 3. So: KEEP and FLAG. Deleting 13.5 % of the rows would bias any count of
#    flows, and a test that rejects correct data is a bad test.
```

That last line is the principle of a **test**: if the model creates carbon, it is wrong,
and a test says so. But a test that rejects 13 % of correct data is a bad test. The
whole difficulty is there, and we come back to it on 23 October.

### Two side questions, if you have time

**Units.** Are all the rows really in cubic metres? What do you do with the eleven where
`qtyUnitAbbr` is `N/A` — does including them in a density mean anything?

```r
# R
table(clean$qtyUnitAbbr)              # counts per unit, N/A included
```
```python
# Python
clean.qtyUnitAbbr.value_counts()      # counts per unit
```

**The zeros.** Seventeen rows have `qty = 0`. Watch what the division does, and what
survives a mean:

```r
# R
1 / 0                    # Inf -- no error, no warning
mean(c(1, 2, Inf))       # Inf -- one bad row poisons the whole average
```
```python
# Python
import numpy as np
np.float64(1) / 0        # inf
np.mean([1, 2, np.inf])  # inf
```

---

## 2. Mirror statistics

**Where you work: in `src/04_mirror.R` or `src/04_mirror.py`.** The template ships it
with its header and its loading line; the rest is below.

A fourth script, and not more of `02_cleaning`, for the same reason as the figure: one
script, one job. This one reads the cleaned table and writes a comparison table. It does
not care how the cleaning was done.

### a) One case

In 2023, for oak logs (`440391`): what does France report exporting to China, and what
does China report importing from France?

```r
# R
OAK  <- 440391
YEAR <- 2023

fr_says <- subset(clean, cmdCode == OAK & period == YEAR &      # same product, same year
                         flowDesc == "Export" &                 # France's side: an export
                         reporterDesc == "France" &             # declared BY France
                         partnerDesc == "China")                # ... towards China

cn_says <- subset(clean, cmdCode == OAK & period == YEAR &      # same product, same year
                         flowDesc == "Import" &                 # China's side: an import
                         reporterDesc == "China" &              # declared BY China
                         partnerDesc == "France")               # ... from France

fr_says[, c("qty", "netWgt", "primaryValue")]     # 57.2 M$
cn_says[, c("qty", "netWgt", "primaryValue")]     # 128.4 M$
cn_says$primaryValue / fr_says$primaryValue       # 2.25 -- the same cargo, twice
```

```python
# Python
OAK, YEAR = 440391, 2023
cols = ["qty", "netWgt", "primaryValue"]

fr_says = clean[(clean.cmdCode == OAK) & (clean.period == YEAR)   # same product, same year
                & (clean.flowDesc == "Export")                    # France's side
                & (clean.reporterDesc == "France")                # declared BY France
                & (clean.partnerDesc == "China")]                 # ... towards China

cn_says = clean[(clean.cmdCode == OAK) & (clean.period == YEAR)
                & (clean.flowDesc == "Import")                    # China's side
                & (clean.reporterDesc == "China")                 # declared BY China
                & (clean.partnerDesc == "France")]                # ... from France

fr_says[cols]                                                     # 57.2 M$
cn_says[cols]                                                     # 128.4 M$
cn_says.primaryValue.iloc[0] / fr_says.primaryValue.iloc[0]       # 2.25
```

Two countries, one cargo, a factor of two. One of them is wrong, or both are, and
nothing in the file says which.

### b) Generalise: this is a join

A **join** lines up two tables on the columns they have in common. Here the two tables
are the same file read from two ends, and the catch is naming: `reporterDesc` means
"France" on one side and "the partner" on the other, so a join on that column would be
meaningless.

Fix it by naming the columns after the **roles**, not after the file. In every row of
this comparison France is the **exporter** and the other country is the **importer** —
whichever of the two happened to file the declaration.

```r
# R
exports <- subset(clean,
                  reporterDesc == "France" & flowDesc == "Export",      # France's own account
                  select = c(period, cmdCode, partnerDesc, primaryValue))
names(exports)[names(exports) == "partnerDesc"]  <- "importer"          # the buyer
names(exports)[names(exports) == "primaryValue"] <- "value_exporter"    # what FRANCE says

mirror  <- subset(clean,
                  partnerDesc == "France" & flowDesc == "Import",       # the partners' account
                  select = c(period, cmdCode, reporterDesc, primaryValue))
names(mirror)[names(mirror) == "reporterDesc"]  <- "importer"           # same buyer, other side
names(mirror)[names(mirror) == "primaryValue"]  <- "value_importer"     # what THEY say

comp <- merge(exports, mirror,                             # line the two accounts up
              by = c("period", "cmdCode", "importer"))     # same year, product, buyer

comp$ratio <- comp$value_importer / comp$value_exporter    # >1: the buyer declares more

nrow(comp)                                          # 128 pairs comparable
median(comp$ratio)                                  # 1.15
head(comp[order(-comp$ratio), ], 10)                # the worst disagreements first
```

```python
# Python
exports = (clean[(clean.reporterDesc == "France")                 # France's own account
                 & (clean.flowDesc == "Export")]
           [["period", "cmdCode", "partnerDesc", "primaryValue"]]
           .rename(columns={"partnerDesc": "importer",            # the buyer
                            "primaryValue": "value_exporter"}))   # what FRANCE says

mirror = (clean[(clean.partnerDesc == "France")                   # the partners' account
                & (clean.flowDesc == "Import")]
          [["period", "cmdCode", "reporterDesc", "primaryValue"]]
          .rename(columns={"reporterDesc": "importer",            # same buyer, other side
                           "primaryValue": "value_importer"}))    # what THEY say

comp = exports.merge(mirror,                                      # line the two accounts up
                     on=["period", "cmdCode", "importer"])        # same year, product, buyer

comp["ratio"] = comp.value_importer / comp.value_exporter         # >1: the buyer declares more

len(comp)                                           # 128 pairs comparable
comp.ratio.median()                                 # 1.15
comp.sort_values("ratio", ascending=False).head(10) # the worst disagreements first
```

Naming the columns `value_exporter` and `value_importer` rather than `primaryValue_x`
and `primaryValue_y` is not tidiness. Three weeks from now, `ratio > 1` means nothing
and *the importer declares more than the exporter* means everything — and the second one
is readable straight off the column names, by someone who never saw this code.

Note what `merge` silently does: it keeps only the rows present on **both** sides. A
flow one country reported and the other did not has no mirror, and disappears from the
comparison without a word. Count what you started with and what you ended with.

### c) How much of it is a valuation convention?

An import is counted **CIF** — goods, insurance and freight to the importer's border.
An export is counted **FOB** — goods alone. Two countries describing the same cargo do
not put the same things in the price.

```r
# R
tapply(clean$primaryValue, clean$flowDesc, sum)     # 752.1 M$ exported, 1253.6 M$ imported
```
```python
# Python
clean.groupby("flowDesc").primaryValue.sum()        # 752.1 M$ / 1253.6 M$
```

A ratio of **1.67** across the whole file, and a median ratio of **1.15** pair by pair.
CIF/FOB is worth 10 to 20 %. It is real, and it is nowhere near enough.

Find at least two other explanations. Leads: timber transits through foreign ports;
country of origin and country of consignment do not coincide; reporting thresholds
differ between countries.

Then write the conclusion in your script. The line worth arriving at: **mirror
statistics are a diagnostic, not a correction.** They tell you two figures disagree.
They never tell you which one is right.

---

## 3. France trades with France

**In the console.** Three lines, nothing to record.

Three rows in the file have `reporterDesc` and `partnerDesc` both equal to `France`.

```r
# R
subset(trade, reporterDesc == partnerDesc)      # 3 rows -- on the RAW table
```
```python
# Python
trade[trade.reporterDesc == trade.partnerDesc]  # 3 rows -- on the RAW table
```

Note that this one runs on `trade`, the table as loaded, not on `clean`: depending on
what you filtered at step 6 they may already be gone, and you want to see them.

This is not a data entry error. Find out what it is, and decide whether those rows
belong in your cleaned dataset.

---

## 4. A genuinely hostile CSV

**No code for this one, deliberately.**

Open `comtrade_fr_roundwood_dirty.csv` in Excel, **without saving anything**. Look at
what happens to the accented country names and to the large numeric values.

Then close without saving.

Write three lines explaining to a colleague why "just having a quick look in Excel" is
a dangerous move on raw data.

---

## 5. The format that has none of these problems

**In the console.** You are comparing two files, not producing a result.

Save your cleaned table as **Parquet**, then compare.

```r
# R
install.packages("arrow")     # once on the machine, from inside R
library(arrow)                # every session -- without it, write_parquet is not found

write_parquet(clean, here("data", "processed", "trade_clean.parquet"))   # same table, other format

file.size(here("data", "processed", "trade_clean.csv"))       # bytes, CSV
file.size(here("data", "processed", "trade_clean.parquet"))   # bytes, Parquet

back <- read_parquet(here("data", "processed", "trade_clean.parquet"))   # read it back
str(back)     # compare the column types with what read.csv hands you back
```

For Python the package is called `pyarrow`, and it installs from the terminal:

```
python -m pip install pyarrow
```

```python
# Python
import pyarrow                 # pandas does the calling, but the engine must be there:
                               # without it, to_parquet raises ImportError

clean.to_parquet(ROOT / "data" / "processed" / "trade_clean.parquet")    # same table, other format

(ROOT / "data" / "processed" / "trade_clean.csv").stat().st_size         # bytes, CSV
(ROOT / "data" / "processed" / "trade_clean.parquet").stat().st_size     # bytes, Parquet

back = pd.read_parquet(ROOT / "data" / "processed" / "trade_clean.parquet")   # read it back
back.dtypes                    # compare with what read_csv hands you back
```

Compare the size, the read-back speed, and above all **the column types**: a CSV stores
everything as text and asks the reader to guess on the way back in — which is the whole
subject of this lab. Parquet stores the types alongside the data, so `period` comes back
as an integer without anyone declaring anything.

Why, then, is CSV still the most widely used format in the world?

### The answer

Answer it with your partner first. Then read this.

**Because everything reads it, without being asked.** A CSV opens in a text editor, in
Excel, in R, in Python, in a terminal, on a machine from 2005 and on one you have never
seen. Parquet needs a library: without `arrow` or `pyarrow` installed, the file you just
wrote is unreadable bytes. A format that requires an installation is a format that loses
an exchange.

**Because it has no version.** There is no Parquet-1.0-versus-2.0 problem in a CSV,
because there is nothing in it to version. The absence of a specification — the very
thing that cost you twenty minutes at step 3 — is also why nothing about it can ever
break.

**Because a human can read it.** You looked at three lines of this file in the terminal
before writing a single line of code, and you diagnosed the separator, the decimal mark
and the quoting from that alone. Try that on a Parquet file. Being inspectable by eye is
worth more than it sounds when something goes wrong at eleven at night.

**Because it is append-only friendly.** A sensor can add a line to a CSV every second
with no more machinery than an open file. Parquet is a columnar block format: adding one
row means rewriting a file.

**And, honestly: because the person who exports it does not pay for it.** Whoever
clicked *Save as CSV* in a French-configured Excel had no problem at all. The cost lands
on you, three weeks later, in another country, in another language. A format whose costs
fall on somebody else spreads very well.

That last point is the one to keep. The lesson of this lab is not "CSV bad, Parquet
good" — it is **choose by which side of the exchange you are on**:

| | Format | Why |
|---|---|---|
| `data/raw/` | Whatever you were given | You do not choose it, and you do not touch it |
| Handing data to someone unknown | **CSV** | It will be readable by them, and in ten years |
| `data/processed/`, your own pipeline | **Parquet** | You are the only reader, types are worth keeping, and the file is a third of the size |

Which is exactly the split the project template already imposes on you. Now you know
why the two folders are not the same thing.
