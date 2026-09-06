# Lab 3 — Challenges

## 1. The other language

Redo the five scripts in the other language. The error messages do not look alike; the
causes do.

Build the correspondence:

| Cause | R message | Python message |
|---|---|---|
| file not found | | |
| function or name not found | | |
| object not found | | |
| invalid type | | |

That table is worth more than the fixes themselves.

## 2. Write the guard rail that would have caught script 5

Script 5's problem is that it adds an aggregate together with its own components.

Write an **assertion** that makes the bug impossible — a line that fails the script
rather than letting it produce a wrong answer. Put it just after the filter, **before**
the sum.

```r
# R
stopifnot(!"W00" %in% oak$partnerISO)   # stop if the aggregate is still in the table
```

```python
# Python
assert "W00" not in set(oak.partnerISO), \
    "the all-partners aggregate is still in the table"   # same check, with your own message
```

Run it on the script **before** the fix. It must fail — that is how you know the guard
rail works. A guard rail you have never seen fail is a guard rail you have not tested.

R stops with `!"W00" %in% oak$partnerISO is not TRUE`; Python stops with the message you
wrote yourself, which is why writing one is worth the four extra words.

### Then generalise

What else must be true of this dataset, always, whatever the script does to it? Write
three more. Here are two to start you off — put them straight after the `read.csv` /
`read_csv`, so they check the file itself rather than one filtered subset.

```r
# R
stopifnot(all(trade$period >= 2022 &                    # every year is inside
              trade$period <= 2024))                    # ... the extraction window
stopifnot(all(trade$flowDesc %in%                       # every flow is one of the
              c("Import", "Export")))                   # ... two known directions
```

```python
# Python
assert trade.period.between(2022, 2024).all(), \
    "a year outside the extraction window"              # every year inside the window
assert set(trade.flowDesc) <= {"Import", "Export"}, \
    "an unexpected flow direction"                      # <= reads as "is a subset of"
```

Leads for your own three: can a value be negative? can the same
reporter–partner–year–product–flow appear twice? is every `partnerISO` three characters
long? does a quantity of zero make sense next to a non-zero value?

An assertion is not a comment. A comment saying "no duplicates here" is a hope; a line
that stops the script is a fact.

That is exactly what a **test** is, and it is the topic of 23 October.

## 3. The reprex

A **reprex** is a bug rewritten so that a stranger can run it in ten seconds. It has
four parts, always the same:

1. **hand-made data** — three rows, invented, no file to download;
2. **the code cut to the bone** — everything that is not needed to trigger the bug is
   deleted;
3. **what you expected**;
4. **what you got**.

The part that blocks everyone is the first one, because you have spent the day reading
files rather than writing tables. Here is the gesture:

```r
# R
d <- data.frame(country = c("A", "B", "C"),   # one vector per column
                value   = c(10, NA, 30))      # same length, that is all it takes
```

```python
# Python
import pandas as pd                                     # the DataFrame lives here
d = pd.DataFrame({"country": ["A", "B", "C"],           # a dict: name -> list of values
                  "value":   [10, None, 30]})           # None is Python's missing value
```

### A worked example, on a different bug

So that you see the shape before writing your own. The bug: a mean that ignores missing
values without telling you.

```r
# R — reprex
d <- data.frame(value = c(10, NA, 30))   # three rows, one of them missing
mean(d$value)                            # the whole bug, in one call

# Expected: the average of three countries.
# Got: NA. R refuses, because one value is missing.
```

```python
# Python — reprex
import pandas as pd                             # the only dependency
d = pd.DataFrame({"value": [10, None, 30]})     # three rows, one of them missing
d.value.mean()                                  # the whole bug, in one call

# Expected: the average of three countries.
# Got: 20.0 — the average of two. pandas dropped the missing one in silence.
```

Six lines each, no data file, and anyone can run them. Note in passing that the two
languages disagree again, and that the quiet one is the dangerous one.

### Now the same thing, for script 5

Here it is written out, because the point is to show you the shape, not to test you on
it. Read it before you write your own version of anything.

```r
# R — reprex for script 5
d <- data.frame(
  partnerISO   = c("CHN", "DEU", "W00"),   # two real partners, and the aggregate
  primaryValue = c(60, 40, 100)            # 60 + 40 = 100, which is what W00 holds
)

sum(d$primaryValue)                        # the buggy line, unchanged

# Expected: 100 -- the total of the flows.
# Got     : 200 -- the total counted twice, because the aggregate row is
#           summed alongside the components it is the aggregate of.
# Fix     : sum(subset(d, partnerISO != "W00")$primaryValue)   -> 100
```

```python
# Python — reprex for script 5
import pandas as pd

d = pd.DataFrame({
    "partnerISO":   ["CHN", "DEU", "W00"],   # two real partners, and the aggregate
    "primaryValue": [60, 40, 100],           # 60 + 40 = 100, which is what W00 holds
})

d.primaryValue.sum()                         # the buggy line, unchanged

# Expected: 100 -- the total of the flows.
# Got     : 200 -- the total counted twice.
# Fix     : d[d.partnerISO != "W00"].primaryValue.sum()   -> 100
```

Look at what survived the cut, and what did not.

**Gone:** the CSV file, the 674 rows, the year filter, the country filter, the product
code, `read.csv`, `here()`, the printing, the units. None of them is needed to make the
bug happen.

**Kept:** three rows, one column of codes, one column of numbers, and the line that
sums. Ten lines including the comments, no download, no setup — a stranger can run it
and see the problem in the time it takes to read it.

**And the numbers were chosen, not copied.** 60 + 40 = 100 makes the double count
obvious at a glance: nobody has to trust arithmetic they cannot do in their head. Real
data in a reprex is a distraction; the reprex only has to reproduce the *behaviour*.

Now the part that is genuinely yours: **do the same for one of the other four scripts**,
or for a bug you hit this afternoon on your own machine. That is the exercise of the
next block, and this is what it should look like when you are done.

## 4. Build a sixth script

Write, yourself, a script that produces a wrong answer without raising an error, on
this dataset. Swap it with another pair.

Three leads if you want them: units, mirror statistics, missing values that quietly
vanish from a mean.

The best one will be added to the repository for next year's cohort — with your name,
if you want it.

## 5. How could you have seen it?

Without looking at the data, estimate off the top of your head: does France export $450
million or $900 million of oak logs over three years?

Look for an external order of magnitude — French oak harvest, average price per cubic
metre, published customs statistics. You must be able to decide.

That is **the** reflex that protects against silent failure, and it is not written in
code: knowing what the result should look like before you compute it.
