# Lab 3 — Crash workshop

**Monday 7 September · 15:15 – 16:05 · 50 minutes · in pairs**

## Goal

Five scripts. None of them does what it claims. Repair them.

This is not a speed exercise. **The goal is the method**, not the number of scripts
fixed. A pair that handles three scripts while explaining each diagnosis has done
better work than a pair that fixes five by guessing.

The scripts are in [`broken-scripts/`](broken-scripts/), in an R and a Python version.
Take whichever you like; challenge 1 is to do the other one.

---

## The four-step method

Apply it to each script, in order, skipping nothing.

1. **Read the error.** In full, down to the last line. An error message is
   *information*, not punishment. It almost always contains the offending object's name
   and a line number.
2. **Read the documentation** for the function involved. `?read.csv`,
   `help(pd.read_csv)`.
3. **Search** for the message, stripping out what is specific to you.
4. **Ask** — your partner first, then the instructor.

For each script, write down on paper:

| | |
|---|---|
| **Symptom** | what the machine prints |
| **Diagnosis** | what is wrong, in one sentence |
| **Fix** | what you changed |
| **Prevention** | what would have avoided this bug at writing time |

The *Prevention* column is the one that will serve you all year.

---

## The five scripts

Prerequisite: both files from [`05-data/`](../../05-data/) must be in `data/raw/`, and
you are working from a properly opened project (lab 1).

### 1. `01_path`
Counts the rows in the dataset. **Expected message:** the file does not exist.

### 2. `02_package`
Prints the first five rows. **Expected message:** something cannot be found — a
*function* in R (`could not find function "read_csv"`), a *name* in Python
(`NameError: name 'pd' is not defined`).

Careful: there are **two possible causes** for that kind of message. Work out which one
applies here, and say how you would have told them apart.

### 3. `03_name`
Computes a mean quantity. **Expected message:** an object cannot be found. The shortest
of the five to fix, and the most frequent in real life.

Worth noticing in passing: Python hands you the answer
(`Did you mean: 'exports'?`), R just says `object 'export' not found`. Error messages
are not equally good across languages. Note it.

### 4. `04_type`
Computes a total value, from the **dirty** file. The problem is a **type** problem, and
it does not surface the same way in the two languages. That is the whole point of this
script.

**In R**, an error is raised: `invalid 'type' (character) of argument`. The language
refuses to add up text.

**In Python**, nothing crashes. `sum()` on a text column **concatenates the strings**
and hands you a 6,349-character "number". The program finishes normally.

Diagnose the common cause, fix both, then answer: which of the two behaviours do you
prefer, and why?

**Second problem, in R only.** Once the type error is fixed, look at the country names
and at the `qtyUnitAbbr` column. You will see `m\xb3` and unreadable strings. Try to
find "Côte d'Ivoire" with a `grepl()`: you will find **nothing**, even though the
substring `voire` is right there. Explain why, then fix it. Nothing crashes at any
point.

### 5. `05_silent` — the most important of the five

This script **does not crash**. It runs cleanly and prints:

```
French oak log exports, 2022-2024:
   909.7 million USD
   104 reported flows
```

The number is wrong. It is exactly **twice** the right answer.

Your task:

1. find out why, without being told where to look;
2. fix it;
3. **answer the question that matters: how would you have noticed if I had not warned
   you?**

Three rows out of a hundred and four are enough to double the result. No message, no
warning, nothing in red. A perfectly presentable figure, and a false conclusion.

Both languages give the same result, to the cent. So they are wrong in the same way —
which should already tell you something about the value of "it gives the same in both".

This is the kind of error that survives a viva, ends up in a report, and steers a
decision. The first four scripts cost you ten minutes. The fifth costs you your
credibility.

---

## What you should have understood by the end

- An error message is a gift: it tells you where to look. The absence of a message does
  not mean everything is fine.
- The four messages of today — file not found, function or name not found, object not
  found, invalid type — cover the overwhelming majority of what you will meet this
  year.
- **A more permissive language is not a safer language.** R refuses to add up text;
  Python does it without blinking. Script 4 shows it in one line.
- **The only protection against silent failure is knowing what the result should look
  like before you compute it.**

Solutions are published on this repository **after the session**.

Challenges, if you have finished: [`challenges.md`](challenges.md).
