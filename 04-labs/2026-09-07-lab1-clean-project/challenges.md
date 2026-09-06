# Lab 1 — Challenges

Take these if you have finished the core. Do not do them instead of it.

## 1. The Python version

Redo step 4 in Python, in `src/01_import.py`, using `pathlib`:

```python
from pathlib import Path
ROOT = Path(__file__).parent.parent
```

Compare with the R solution. What is more explicit in each of the two?

## 2. Break the project on purpose

Move `uc33-lab1` somewhere else on your disk, then run the script again. If you did the
work properly, nothing changes. If something breaks, you still had an absolute path
somewhere.

Do it again, this time by renaming the folder.

## 3. Parameters out of the code

The template already ships `config/config.yml`. Open it: it holds the two paths, the
country, and a switch. Nothing in it is code.

```yaml
input_file: data/raw/comtrade_fr_roundwood_clean.csv
output_file: data/processed/trade_france.csv

country: France
exclude_partner_aggregate: true
```

**Read it in the console first**, before touching your script, so that you can see what
you get back.

```r
# R
install.packages("yaml")   # once, on the machine
library(yaml)
library(here)

params <- read_yaml(here("config", "config.yml"))

str(params)              # a named list
params$input_file        # "data/raw/comtrade_fr_roundwood_clean.csv"
params$country           # "France"
```

```python
# Python
# needs pyyaml:  pip install pyyaml
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # in a script
# ROOT = Path.cwd()                          # in the console, at the project root

params = yaml.safe_load(open(ROOT / "config" / "config.yml"))

params                       # a dict
params["input_file"]         # 'data/raw/comtrade_fr_roundwood_clean.csv'
params["country"]            # 'France'
```

A YAML file becomes a **named list** in R and a **dict** in Python. You reach into it
the same way you would reach into anything else, and there is no third concept to learn.

Now use it. In your script, every hard-coded value is replaced by a lookup:

```r
# R
trade  <- read.csv(here(params$input_file))
france <- subset(trade, reporterDesc == params$country)
```

```python
# Python
trade  = pd.read_csv(ROOT / params["input_file"])
france = trade[trade.reporterDesc == params["country"]]
```

Then the test: change `country` to `Belgium` in the YAML file, run the script again,
and check that **you did not open a single `.R` or `.py` file to do it.** You should get
18 rows instead of 379. That is the
whole point — the person who changes the parameters is not necessarily the person who
can read the code.

This is a foretaste of 23 October.

## 4. Naming, put to the test

Create a file in `data/raw/` called `Données récoltées (final).csv`, try to read it from
your script, and explain to your partner **three distinct reasons** why that name is a
problem.

Then delete it.

## 5. Read the course repository as a project

Open [the course repository](https://github.com/vlmathieu/firs-uc33-modeling) and check
that it follows the rules it imposes on you: no accents or spaces in names, dates as
`YYYY-MM-DD`, explicit ordering, a README at the root.

**If it fails anywhere, open an issue.** This is serious: the first one found earns the
right to say so in class.
