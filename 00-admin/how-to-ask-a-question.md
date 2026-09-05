# How to ask a technical question

*Three minutes to read. The highest-return skill of the year.*

---

## Why it matters

You will be asking technical questions for your entire career: of a forum, a
colleague, an AI, an instructor. The quality of the answer is almost entirely
determined by the quality of the question.

"It doesn't work" has no answer. Not because the person on the other side is
unwilling, but because there is **nothing there to answer**.

And there is a side benefit, which is really the main one: **you very often find the
answer while formulating the question.** Reducing a problem to a minimal example is
already debugging.

---

## The reprex

A *reprex* — **repr**oducible **ex**ample — is the smallest complete program that
reproduces your problem. It has four properties.

**Minimal.** Strip out everything not needed to trigger the error. Your 300 lines
almost always reduce to 5. Do the reduction: that is where the cause shows up.

**Complete.** Someone must be able to copy and paste your code and get the same error.
That means the `library()` / `import` lines at the top, and the data included.

**Reproducible.** No absolute paths, no file only you possess. If the problem comes
from your data, build three rows of toy data that reproduce it:

```r
# instead of: read.csv("C:/Users/me/Documents/my_data.csv")
d <- data.frame(qty = c(12.5, 0, 3.1), netWgt = c(9800, 450, NA))
```

**With the COMPLETE error message.** As text, never as a screenshot, and in full. The
line you judge irrelevant is often the one holding the cause.

---

## The four-step method, before asking

1. **Read the error.** In full, to the end. An error message is *information*, not
   punishment. It almost always contains the name of the offending object and a line
   number.
2. **Read the documentation.** `?read.csv` in R, `help(pd.read_csv)` in Python.
3. **Search.** Paste the error message into a search engine, stripping out what is
   specific to you — your file names, your variable names.
4. **Ask.** With a reprex.

The fourth step is legitimate. It comes after the other three.

---

## Where to ask

**The issues on this repository** are the official channel for the course unit.

[→ Open an issue](https://github.com/vlmathieu/firs-uc33-modeling/issues/new/choose)

The form asks for exactly the elements above. That is not administration: it is the
reprex, enforced by the tool.

Advantage over email: the answer is readable by the whole cohort, and it stays
available. Your problem is almost never yours alone.

Public repository: no names, no personal data, no screenshot containing an identifier.

---

## What about AI?

The same rules apply, for the same reason: an AI given the context, the version and
the complete error message answers far better than one given "it doesn't work".

Two differences to keep in mind. An AI always answers, including when it is wrong, and
with exactly the same confident tone. And it will not tell you it did not understand.
Ask it for an **explanation** rather than a block of code to paste — then you can tell
whether the answer holds.

The rules on declaring AI use in your submitted work are covered by the dedicated
course in the programme and restated in §9 of the syllabus.
