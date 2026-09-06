# Lab 3 — Crash workshop

**Monday 7 September · 15:35 – 16:35 · 60 minutes · in pairs**

## Goal

Five scripts. None of them does what it claims. Repair them.

This is not a speed exercise. **The goal is the method**, not the number of scripts
fixed. A pair that handles three scripts while explaining each diagnosis has done
better work than a pair that fixes five by guessing.

The scripts are in [`broken-scripts/`](broken-scripts/), in an R and a Python version.
Take whichever you like; challenge 1 is to do the other one.

---

## Getting the scripts into your project

**Where they go: a new folder, `src/broken-scripts/`.**

```
uc33-lab1/
├── data/
│   └── raw/           <- BOTH csv files must be here: clean and dirty
├── src/
│   ├── 01_import.R        your pipeline
│   ├── 02_cleaning.R      ...
│   ├── 03_figure.R        ...
│   ├── 04_mirror.R        ...
│   └── broken-scripts/    <- the ten files of this lab go here
│       ├── 01_path.R
│       ├── 01_path.py
│       └── ...
```

Not loose in `src/`. Your `01_`, `02_`, `03_`, `04_` are a pipeline that runs in that
order; these ten are ten unrelated exercises that happen to be numbered too. Mixing them
would make the numbering mean two different things in one folder, which is exactly the
mistake this morning's naming rule exists to prevent.

**How to download them.** GitHub does not let you download a folder on its own, so
there are two ways in and the first is faster:

**Either** take the whole course repository at once — on
[its front page](https://github.com/vlmathieu/firs-uc33-modeling), green *Code* button →
*Download ZIP*. Unzip it anywhere (your Downloads folder is fine — this is a delivery,
not a project). Inside, go to
`04-labs/2026-09-07-lab3-crash-workshop/broken-scripts/` and copy that whole folder into
your `src/`.

**Or** open each file on GitHub and use the **Download raw file** button, top right of
the file view. Ten files, ten clicks. Do this only if the ZIP fails.

**If the network is against you**, ask: the files are on a USB stick at the front of the
room.

### Check before you start

Three things, and it takes twenty seconds:

```r
# R
list.files("src/broken-scripts")     # ten files
list.files("data/raw")               # two csv files
getwd()                              # must end in uc33-lab1
```

```python
# Python
import os
os.listdir("src/broken-scripts")     # ten files
os.listdir("data/raw")               # two csv files
os.getcwd()                          # must end in uc33-lab1
```

That last line is not a formality. **These scripts read their data with paths relative
to the project root** — `data/raw/comtrade_fr_roundwood_clean.csv` — not relative to
themselves. Run them from anywhere else and every single one fails with the same
message, which would make script 1 unreadable and the other four indistinguishable from
it.

In RStudio, opening the `.Rproj` guarantees it. In VS Code, opening the *folder*
`uc33-lab1` does.

**How to run one of these scripts.** Two routes, and they must agree:

| | |
|---|---|
| **RStudio** | Open the file, then `Ctrl+Shift+Enter` (*Source*). Better: `Session > Restart R` first, so a leftover object from the previous script cannot mask the fault. |
| **VS Code, Python** | Open the file, then the ▷ button — or, in the terminal, `python src/broken-scripts/01_path.py` |
| **Any terminal** | `Rscript src/broken-scripts/01_path.R` — **from the project root**, never from inside `src/broken-scripts/` |

That last warning is not pedantry. `cd src/broken-scripts` then `python 01_path.py`
makes all five scripts fail with the same file-not-found, and you will spend twenty
minutes debugging your own terminal instead of my bugs.

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

Prerequisite: the ten scripts in `src/broken-scripts/`, both files from
[`05-data/`](../../05-data/) in `data/raw/`, and a properly opened project — the three
checks above.

**How to spend the hour.** Scripts 1 to 3 recycle this morning and lab 1; they should
take about five minutes each. Script 4 is worth fifteen, and **script 5 is worth
twenty** — it is the one the whole afternoon has been building towards. If you are still
on script 2 at four o'clock, skip to script 5. Finishing three scripts with a diagnosis
you can defend beats finishing five by guessing, and this is not a race.

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
and at the `qtyUnitAbbr` column.

**Run these lines in the console**, not in the script — you are investigating, not
producing a result yet.

```r
unique(trade$qtyUnitAbbr)          # "m\xb3", not "m³"

# look for Côte d'Ivoire, which is definitely in the file
sum(grepl("voire", trade$partnerDesc))               # 0, plus a warning
nrow(subset(trade, partnerDesc == "Côte d'Ivoire"))  # 0, and no warning at all
```

Zero matches, on a substring that is right there in the file. The `grepl()` at least
warns you, and the warning hands you the answer:
`unable to translate 'C<f4>te d'Ivoire' to a wide string`. The `subset()` returns an
empty table and says nothing at all — the same silent failure as script 5, in a
different disguise.

Explain why, then fix it, then run the same three lines again. Nothing crashes at any
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
