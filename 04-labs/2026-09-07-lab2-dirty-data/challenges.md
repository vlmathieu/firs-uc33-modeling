# Lab 2 — Challenges

## 1. The wood that floats in air — an investigation

Compute the apparent density of each flow: `netWgt / qty`, in kg/m³, on the rows where
`qtyUnitAbbr` is `m³`.

The median lands around **884 kg/m³** — plausible for green timber.

Now look at the extremes. You will find densities below 10 kg/m³ and above 40,000. The
lightest wood in the world, balsa, is 160 kg/m³; the heaviest, lignum vitae, is 1,250.
About **13 %** of rows fall outside the defensible range [200, 1300].

**Write the guard rail first** — a line that makes the script fail rather than let it
produce a wrong answer:

```r
stopifnot(all(d$dens > 200 & d$dens < 1300, na.rm = TRUE))
```

Then investigate. The dataset contains what you need — that is the point of the
exercise, and there is no single right answer.

**Lead a — flow size.** Compare the median volume of aberrant rows with that of
plausible ones. Then split by volume band: under 10 m³, 10 to 100, 100 to 1,000, over
1,000. The result is clear-cut, and it is the real explanation.

**Lead b — units.** Are all the rows really in m³? What do you do with the eleven rows
where `qtyUnitAbbr` is `N/A` — does including them in a density calculation mean
anything?

**Lead c — the zeros.** Seventeen rows have `qty = 0`. What does the division produce?
Does that result travel through a mean without saying anything?

Finish by writing **three lines of conclusion** in your script, as a comment: what
explains what, what you keep, what you discard, and why.

This is the principle of a **test**: if the model creates carbon, it is wrong, and a
test says so. But a test that rejects 13 % of correct data is a bad test. The whole
difficulty is there. We come back to it on 23 October.

## 2. Mirror statistics

In 2023, for oak logs (`440391`):

- what does France report exporting to China?
- what does China report importing from France?

Compute the gap, by volume and by value.

Then generalise: build a table comparing, for each partner, what France reports and
what the partner reports.

The first explanation is a valuation convention. An import is counted **CIF** — goods,
insurance and freight to the importer's border — and an export **FOB**, goods alone.
Two countries describing the same cargo therefore do not put the same things in it.

Quantify: on this dataset, what is the total of reported imports, and of exports? Is
the gap enough to explain the factor observed on oak to China, or is something else
needed?

Find at least two other explanations. Leads: timber transits through foreign ports;
country of origin and country of consignment do not coincide; reporting thresholds
differ between countries.

## 3. France trades with France

Three rows in the file have `reporterDesc` and `partnerDesc` both equal to `France`.

This is not a data entry error. Find out what it is, and decide whether those rows
belong in your cleaned dataset.

## 4. A genuinely hostile CSV

Open `comtrade_fr_roundwood_dirty.csv` in Excel, **without saving anything**. Look at
what happens to the accented country names and to the large numeric values.

Then close without saving.

Write three lines explaining to a colleague why "just having a quick look in Excel" is
a dangerous move on raw data.

## 5. The format that has none of these problems

Save your cleaned table as **Parquet** (`arrow::write_parquet()` in R, `d.to_parquet()`
in Python). Compare the size, the read-back speed, and ask yourself what happens to the
column types.

Why is CSV still the most widely used format in the world?
