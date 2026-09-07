# Lab 3 — solution

## Diagnostic table

| # | R symptom | Python symptom | Diagnosis | Prevention |
|---|---|---|---|---|
| 1 | `cannot open file '...': No such file or directory` | `FileNotFoundError` | Absolute path pointing at a machine that is not yours | Open the `.Rproj`, write relative paths, never type `setwd()` |
| 2 | `could not find function "read_csv"` | `NameError: name 'pd' is not defined` | Package installed but **not loaded** | Group every `library()` / `import` at the top of the script |
| 3 | `object 'export' not found` | `NameError ... Did you mean: 'exports'?` | Typo in an object name | Explicit names, editor autocompletion |
| 4 | `invalid 'type' (character) of argument` | **no error**: `sum()` concatenates and returns 6,349 characters | Decimal separator not declared: the column is text | Always declare `sep`, `dec`/`decimal` and the encoding. Then `str()` / `.dtypes` before computing |
| 5 | **no error** | **no error** | The `World` aggregate is summed together with its components: total exactly doubled | Look at a column's distinct values before summing. Write an assertion |

## Script 2: two causes, one message

`could not find function` has **two** possible causes, and the message does not say
which:

- the package is not installed — you would then usually get
  `there is no package called 'readr'` at the `library()` call;
- the package is installed but not loaded — that is the case here.

The test that separates them: does `library(readr)` work? If yes, loading was missing.
If no, installation was.

## Script 4: the cross-cutting lesson

Same cause, two opposite behaviours.

**R refuses** to add up a text column and raises an error. **Python accepts**,
concatenates the strings, and returns a 6,349-character "number" with no warning
whatsoever.

A more permissive language is not a safer language. R stops you; Python lets you walk
away with an absurd result — and an absurd result nobody looks at becomes a false
result somebody publishes.

Second problem, in R only: without `fileEncoding`, accented names become unreadable
bytes. The symptom is spectacular — `grepl("voire", partnerDesc)` finds **nothing**,
even though the substring is right there: the string is invalid in the current encoding
and therefore unsearchable. No error is raised.

## Script 5: the real question

Fixing it takes one line. The question that counts is the third one:
**how would you have seen it without being warned?**

Three acceptable answers, in increasing order of robustness:

1. **Order of magnitude.** $900M of oak logs exported over three years, against a
   French oak harvest of roughly 2 Mm³/year, implies an average price well above the
   market. $450M is plausible. **Knowing what the result should look like before
   computing it is the only real protection against silent failure.**
2. **The internal check.** The sum of the parts must equal the whole. Here the `World`
   row *is* the whole: it was there to serve as a check, not as a term.
3. **Inspecting the distinct values** of `partnerDesc` before any aggregation. Thirty
   seconds.

And the durable protection is the assertion, present in both solutions:

```r
stopifnot(!"World" %in% oak$partnerDesc)
```

It turns a silent failure into a loud one. That is the whole definition of a test, and
it is the topic of 23 October.

## Expected results after fixing

Both languages must give exactly the same numbers.

| Script | Result |
|---|---|
| 1 | 674 rows |
| 3 | mean exported quantity 19,944.23 m³ |
| 4 | total value 2,784,198,147 USD |
| 5 | **454.8 million USD, 101 flows** (against 909.7 and 104 before the fix) |
