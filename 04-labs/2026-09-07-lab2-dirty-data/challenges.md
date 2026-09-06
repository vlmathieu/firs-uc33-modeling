# Lab 2 — Challenges

Take these if you have finished the core. Do not do them instead of it.

Every snippet below is labelled **R** or **Python**. They assume `clean` is the table you
produced at step 6, and that `here` (R) or `ROOT` (Python) is set as in the brief.

---

## 1. The wood that floats in air — an investigation

Compute the apparent density of each flow: `netWgt / qty`, in kg/m³, on the rows where
`qtyUnitAbbr` is `m³`.

```r
d <- subset(clean, qtyUnitAbbr == "m³" & qty > 0)
d$density <- d$netWgt / d$qty

# a density that cannot be computed is not an impossible one: drop the NAs
# before counting anything. This distinction matters more than it looks —
# the published solution walked straight into it.
d <- subset(d, !is.na(density))

median(d$density)
summary(d$density)
```

```python
d = clean[(clean.qtyUnitAbbr == "m³") & (clean.qty > 0)].copy()
d["density"] = d.netWgt / d.qty

# a density that cannot be computed is not an impossible one
d = d[d.density.notna()]

d.density.median()
d.density.describe()
```

The median lands at **882 kg/m³** — plausible for green timber.

Now look at the extremes. You will find densities below 10 kg/m³ and above 40,000. The
lightest wood in the world, balsa, is 160 kg/m³; the heaviest, lignum vitae, is 1,250.
About **13 %** of rows fall outside the defensible range [200, 1300].

**Write the guard rail first** — a line that makes the script fail rather than let it
produce a wrong answer:

```r
stopifnot(all(d$density > 200 & d$density < 1300))
```

```python
assert d.density.between(200, 1300).all(), "physically impossible densities"
```

Run it. It fails. That is the point: you now have a script that refuses to lie to you.

Then investigate. The dataset contains what you need — that is the point of the
exercise, and there is no single right answer.

**Lead a — flow size.** Compare the median volume of aberrant rows with that of
plausible ones, then split by volume band.

```r
d$aberrant <- !(d$density >= 200 & d$density <= 1300)
d$band <- cut(d$qty, breaks = c(0, 10, 100, 1000, Inf),
              labels = c("< 10", "10-100", "100-1000", "> 1000"))

tapply(d$qty, d$aberrant, median)   # median volume: aberrant vs plausible
tapply(d$aberrant, d$band, mean)    # share of aberrant rows in each band
```

```python
d["aberrant"] = ~d.density.between(200, 1300)
d["band"] = pd.cut(d.qty, [0, 10, 100, 1000, float("inf")],
                   labels=["< 10", "10-100", "100-1000", "> 1000"])

d.groupby("aberrant").qty.median()
d.groupby("band", observed=True).aberrant.mean()
```

`cut()` and `pd.cut()` slice a continuous column into bands. `tapply()` and `.groupby()`
then apply a function within each band — the single most useful gesture in data analysis,
and you have just met it in both languages.

The result is clear-cut, and it is the real explanation.

**Lead b — units.** Are all the rows really in m³? What do you do with the eleven rows
where `qtyUnitAbbr` is `N/A` — does including them in a density calculation mean
anything?

```r
table(clean$qtyUnitAbbr)
```
```python
clean.qtyUnitAbbr.value_counts()
```

**Lead c — the zeros.** Seventeen rows have `qty = 0`. What does the division produce?
Does that result travel through a mean without saying anything?

```r
1 / 0            # Inf
mean(c(1, 2, Inf))
```
```python
import numpy as np
np.float64(1) / 0        # inf
np.mean([1, 2, np.inf])
```

Finish by writing **three lines of conclusion** in your script, as a comment: what
explains what, what you keep, what you discard, and why.

This is the principle of a **test**: if the model creates carbon, it is wrong, and a
test says so. But a test that rejects 13 % of correct data is a bad test. The whole
difficulty is there. We come back to it on 23 October.

---

## 2. Mirror statistics

In 2023, for oak logs (`440391`):

- what does France report exporting to China?
- what does China report importing from France?

```r
subset(clean, cmdCode == 440391 & period == 2023 & flowDesc == "Export" &
              reporterDesc == "France" & partnerDesc == "China",
       select = c(qty, netWgt, primaryValue))

subset(clean, cmdCode == 440391 & period == 2023 & flowDesc == "Import" &
              reporterDesc == "China" & partnerDesc == "France",
       select = c(qty, netWgt, primaryValue))
```

```python
cols = ["qty", "netWgt", "primaryValue"]

clean[(clean.cmdCode == 440391) & (clean.period == 2023)
      & (clean.flowDesc == "Export")
      & (clean.reporterDesc == "France") & (clean.partnerDesc == "China")][cols]

clean[(clean.cmdCode == 440391) & (clean.period == 2023)
      & (clean.flowDesc == "Import")
      & (clean.reporterDesc == "China") & (clean.partnerDesc == "France")][cols]
```

Compute the gap, by volume and by value.

Then generalise: build a table comparing, for each partner, what France reports and what
the partner reports. This is a **join** — two tables lined up on the columns they have in
common.

```r
exports <- subset(clean, reporterDesc == "France" & flowDesc == "Export",
                  select = c(period, cmdCode, partnerDesc, primaryValue))

mirror  <- subset(clean, partnerDesc == "France" & flowDesc == "Import",
                  select = c(period, cmdCode, reporterDesc, primaryValue))
names(mirror)[names(mirror) == "reporterDesc"] <- "partnerDesc"

comp <- merge(exports, mirror, by = c("period", "cmdCode", "partnerDesc"),
              suffixes = c("_france", "_partner"))
comp$ratio <- comp$primaryValue_partner / comp$primaryValue_france
head(comp[order(-comp$ratio), ], 10)
```

```python
exports = clean[(clean.reporterDesc == "France") & (clean.flowDesc == "Export")][
    ["period", "cmdCode", "partnerDesc", "primaryValue"]]

mirror = (clean[(clean.partnerDesc == "France") & (clean.flowDesc == "Import")]
          [["period", "cmdCode", "reporterDesc", "primaryValue"]]
          .rename(columns={"reporterDesc": "partnerDesc"}))

comp = exports.merge(mirror, on=["period", "cmdCode", "partnerDesc"],
                     suffixes=("_france", "_partner"))
comp["ratio"] = comp.primaryValue_partner / comp.primaryValue_france
comp.sort_values("ratio", ascending=False).head(10)
```

The first explanation is a valuation convention. An import is counted **CIF** — goods,
insurance and freight to the importer's border — and an export **FOB**, goods alone.
Two countries describing the same cargo therefore do not put the same things in it.

Quantify: on this dataset, what is the total of reported imports, and of exports?

```r
tapply(clean$primaryValue, clean$flowDesc, sum)
```
```python
clean.groupby("flowDesc").primaryValue.sum()
```

Is the gap enough to explain the factor observed on oak to China, or is something else
needed?

Find at least two other explanations. Leads: timber transits through foreign ports;
country of origin and country of consignment do not coincide; reporting thresholds
differ between countries.

---

## 3. France trades with France

Three rows in the file have `reporterDesc` and `partnerDesc` both equal to `France`.

```r
subset(trade, reporterDesc == partnerDesc)
```
```python
trade[trade.reporterDesc == trade.partnerDesc]
```

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

Save your cleaned table as **Parquet**, then compare.

```r
# R
install.packages("arrow")   # from inside R
library(arrow)

write_parquet(clean, here("data", "processed", "trade_clean.parquet"))

file.size(here("data", "processed", "trade_clean.csv"))
file.size(here("data", "processed", "trade_clean.parquet"))

back <- read_parquet(here("data", "processed", "trade_clean.parquet"))
str(back)      # compare the column types with what a CSV gives you back
```

For Python the package is called `pyarrow`, and it installs from the terminal:

```
python -m pip install pyarrow
```

```python
# Python
clean.to_parquet(ROOT / "data" / "processed" / "trade_clean.parquet")

(ROOT / "data" / "processed" / "trade_clean.csv").stat().st_size
(ROOT / "data" / "processed" / "trade_clean.parquet").stat().st_size

back = pd.read_parquet(ROOT / "data" / "processed" / "trade_clean.parquet")
back.dtypes
```

Compare the size, the read-back speed, and above all **the column types**: a CSV stores
everything as text and asks the reader to guess on the way back in — which is the whole
subject of this lab. Parquet stores the types alongside the data.

Why, then, is CSV still the most widely used format in the world?
