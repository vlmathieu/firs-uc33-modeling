# Lab 2 — solution

One script per job, the same way your own project should be organised.

| File | What it answers |
|---|---|
| `02_cleaning.R` / `.py` | **The brief**, steps 3 and 6. Five decisions, nothing else. |
| `03_figure.R` / `.py` | **The brief**, step 7. The script you were given, with the reasoning behind each choice added. |
| `02_cleaning_challenges.R` / `.py` | **Challenge 1** — apparent density, the aberrant values, the investigation, and the flag rather than the deletion. |
| `04_mirror.R` / `.py` | **Challenge 2** — the join, the CIF/FOB arithmetic, and what it fails to explain. |

Take the short pair first. If your own cleaning script is longer than `02_cleaning.R`,
you were probably answering a challenge without being asked to.

All of them are commented line by line: the *why* of each decision, not the *what*.

## Expected results

| Check | Value |
|---|---|
| Correct load | 674 rows × 13 columns |
| After excluding the `World` aggregate | **656 rows** |
| France total, with `World` | $1,557.0M |
| France total, without `World` | **$778.5M** |
| Median apparent density (challenge script) | 882 kg/m³ |
| Densities outside [200, 1300] kg/m³ (challenge script) | 86 |
| `aggrLevel` | constant at 6 — dropped |
| Top destination for oak logs | China, $217.4M over three years |

## The decisions, and their justification

**Declare `sep`, `decimal` and `encoding`.** Without them the load fails — and not in
the same way in the two languages. R complains about the column count
(`more columns than column names`, because the `cmdDesc` labels contain commas), Python
about the encoding (`UnicodeDecodeError`). Each reports the first obstacle it hits, not
the full list of problems.

**Keep `N/A` as a string, in Python.** By default pandas turns the literal `N/A` in
`qtyUnitAbbr` into a missing value. But "unit not reported" is information, distinct
from "data absent". Hence `keep_default_na=False, na_values=[""]`. It is arguable — but
the decision must be written down.

**Filter on `partnerISO == "W00"`, not on `partnerDesc == "World"`.** Both work today.
But a label gets translated, renamed and spelled several ways, whereas a reserved code
is stable. A reflex to acquire for every classification.

**Check the types rather than convert them.** The earlier version of this brief said
`period` came in as text and had it converted. It does not: on this file `period`
arrives as an integer in R and in Python. The columns genuinely at risk are `qty`,
`netWgt` and `primaryValue`, whose decimal mark is a comma — declared at load time they
are numeric, undeclared they are text, and nothing announces it. So the scripts assert
the types instead of patching them: a column read wrongly and repaired afterwards is a
column you have to remember about forever.

**Drop `aggrLevel`.** It equals 6 on all 674 rows. A constant column allows no filter,
no grouping and no statistic — and left in place, it invites a `group_by` that groups
nothing.

**Keep the `qty == 0` rows and the missing `netWgt` rows, in the core script.** They
are real flows, and nothing in `02_cleaning` divides or averages, so nothing can go
wrong with them there. The decision belongs to whoever computes: which is
`02_cleaning_challenges`, and it makes it there. Deciding "keep" is still a decision,
and it is still written down.

**Exclude `qty == 0` from the density calculation, explicitly** — in the challenge
script, where the division actually happens. A division by zero
yields `Inf`, which travels through a mean without a sound and makes it infinite. We
exclude it at the point of calculation rather than dropping the rows, which are real
flows.

**Flag aberrant densities rather than delete them.** They cluster overwhelmingly on
very small flows — 46 % below 10 m³, 8 % above — pointing at rounding and reporting
thresholds, not at data entry errors. Deleting them would bias any flow count; keeping
them unflagged would corrupt any density calculation. So a `density_suspect` column is
added.

## A trap the solution itself walked into

The first version of the Python script flagged **107** suspect densities, against 86 in
R. Cause: `~series.between(a, b)` returns `True` for a `NaN`, so the 21 rows where the
density is simply *not computable* were counted as *aberrant*.

A missing density is not an impossible one. Fix:

```python
clean["density_suspect"] = (clean.density.notna()
                            & ~clean.density.between(DENS_MIN, DENS_MAX))
```

No error was raised. Both scripts ran. They just did not say the same thing — and it
was comparing them that revealed it.

That is exactly the subject of lab 3, and it happened while preparing this solution.
Nobody is exempt.

## The assertion that locks it down

Both scripts end with a numeric check:

```python
assert abs(fr.primaryValue.sum() / 1e6 - 778.5) < 0.1
```

If the `World` aggregate ever comes back into the file or into the filter, the script
stops. It does not produce a figure that is twice too tall.
