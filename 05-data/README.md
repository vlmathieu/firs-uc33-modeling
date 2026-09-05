# Datasets

## `comtrade_fr_roundwood_clean.csv` and `comtrade_fr_roundwood_dirty.csv`

**French external trade in roundwood**, 2022-2024, from UN Comtrade.

Two files, **the same content**. Only the format differs.

| File | Encoding | Separator | Decimals |
|---|---|---|---|
| `..._clean.csv` | UTF-8 | `,` | `.` |
| `..._dirty.csv` | Latin-1 | `;` | `,` |

The second was not rigged for the exercise: it is what an export from a
French-configured Excel produces. You will be handed files in that shape for your
entire career.

---

## Scope

| Dimension | Selection |
|---|---|
| Source | UN Comtrade, HS classification, annual data |
| Period | 2022, 2023, 2024 |
| Filter | every row where **France is either reporter or partner** |
| Products | 3 six-digit headings, all **roundwood** (logs) |
| Flows | imports and exports |
| Size | **674 rows, 13 columns** |

### The three products

| HS code | Product |
|---|---|
| `440323` | Fir (*Abies* spp.) and spruce (*Picea* spp.), in the rough, smallest cross-sectional dimension ≥ 15 cm |
| `440349` | Tropical wood in the rough, other than dark red meranti, light red meranti and meranti bakau |
| `440391` | Oak (*Quercus* spp.), in the rough |

All three are **roundwood**: unprocessed timber. That is deliberate — the export of
French oak logs is a live forest policy issue, and the data shows it.

---

## Data dictionary

### Identifying the flow

| Column | Type | Description |
|---|---|---|
| `period` | text | Reference year. **Stored as text**, not as a number. |
| `reporterISO` | text | ISO3 code of the reporting country |
| `reporterDesc` | text | Name of the reporting country |
| `flowDesc` | text | `Import` or `Export`, **from the reporter's point of view** |
| `partnerISO` | text | ISO3 code of the partner. **`W00` = the "all partners" aggregate.** |
| `partnerDesc` | text | Name of the partner; `World` for the aggregate |
| `cmdCode` | text | Six-digit HS heading |
| `cmdDesc` | text | Official product label. Contains semicolons and commas. |

### Product and quantities

| Column | Type | Description |
|---|---|---|
| `aggrLevel` | integer | Aggregation level of the HS heading. **Equals 6 on all 674 rows** of this extract. |
| `qtyUnitAbbr` | text | Unit of `qty`: `m³`, or `N/A` if not reported |
| `qty` | number | Quantity in the unit above |
| `netWgt` | number | Net weight, **in kilograms** |
| `primaryValue` | number | Value of the flow, **in US dollars** |

> Two magnitude columns, two different units: `qty` is a **volume** in m³, `netWgt` a
> **weight** in kg. Their ratio is a density, and that is where the work of lab 2
> begins.

---

## What this data actually contains

Nothing below was added. It all comes from the source.

| Feature | Extent |
|---|---|
| Rows where the partner is the `World` aggregate | 18 |
| Zero quantities (`qty = 0`) | 17 |
| Missing net weight | 11 |
| Unit of `qty` not reported (`N/A`) | 11 |
| `aggrLevel` | **equals 6 on all 674 rows** |
| Countries with accented names | Côte d'Ivoire, Türkiye, Saint Barthélemy |
| Rows where France trades with France | 3 |
| Distinct reporting countries | 63 |
| Distinct partners | 68 |

---

## Four things to know before you compute anything

### 1. `World` is not a country

It is the aggregate of all partners. Summing `primaryValue` without excluding those
rows **doubles the total exactly** — and nothing will warn you. On the rows where
France is the reporter: **1,557.0 M$ with `World`, 778.5 M$ without. Factor 2.00.**

The reliable marker is `partnerISO == "W00"` — the code reserved for the aggregate.
Filtering on the name `partnerDesc != "World"` also works, but a name gets translated
and renamed; a code does not.

### 2. A constant column is not data

`aggrLevel` equals **6 on all 674 rows**. That is expected — the extract only keeps
six-digit HS headings — but it means no filter, no grouping and no statistic on that
column tells you anything.

Look at the distribution of your columns before using them. A constant column is
spotted in one line (`table()` in R, `.nunique()` in Python) and saves you building a
grouping that groups nothing.

### 3. `netWgt / qty` gives a density, and it deserves investigation

The median is **884 kg/m³**, perfectly plausible for green timber. But **13 %** of the
rows fall outside the physically defensible range of [200, 1300] kg/m³, with values at
1 kg/m³ and above 40,000.

This is not inexplicable, and the dataset holds what you need to investigate: **the
anomalies cluster overwhelmingly on small flows.** Among rows below 10 m³, **46 %** are
aberrant; above 10 m³, only **8 %**. The median volume of an aberrant row is 20 m³,
against 742 m³ for a plausible one.

The honest conclusion, and the one you should be able to write yourself: most of the
absurd densities come from rounding and reporting thresholds on tiny flows. It is
neither a bug in your code nor a reason to throw everything away — it is a reason to
filter explicitly, and to write down why.

### 4. Two countries do not report the same thing

In 2023 France reports exporting 147,158 m³ of oak logs to China for $57.2M. China
reports importing 283,521 m³ for $128.4M from France. A factor of 1.9 by volume.

These are **mirror statistics**. Part of the gap is structural: an import is valued
**CIF** — goods, insurance and freight to the importer's border — while an export is
valued **FOB**, goods alone. Both countries describe the same cargo and do not put the
same things in it. On this dataset, reported imports total $1,253.6M and exports
$752.1M.

The rest — transit through foreign ports, country of origin versus country of
consignment, reporting thresholds — is a research topic in its own right.

---

## Provenance and licence

- **Source**: United Nations Comtrade Database, <https://comtradeplus.un.org/>
- **Extraction**: HS chapter 44, annual data, carried out by V. Mathieu.
- **Processing**: row and column selection only. **No value has been modified,
  corrected or invented.** The "dirty" file differs from the "clean" one only in its
  encoding, separator and decimal mark.
- **Reuse**: small derived extract, redistributed for teaching purposes. Any reuse
  must credit UN Comtrade as the source.

The full source file (2 million rows) is not versioned in this repository.
