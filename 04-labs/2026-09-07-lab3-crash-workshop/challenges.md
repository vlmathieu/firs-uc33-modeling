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
rather than letting it produce a wrong answer:

```r
stopifnot(!"World" %in% oak$partnerDesc)
```

Then generalise: what other assertions would you put on this dataset from the start?
Write three.

That is exactly what a **test** is, and it is the topic of 23 October.

## 3. The reprex

Take script 5 **before the fix** and turn it into a minimal reproducible example aimed
at someone who does not have the data file: three rows of hand-made data, the code cut
to the bone, and a statement of expected versus observed behaviour.

You should get under ten lines.

That is the exercise of the next block. Get ahead.

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
