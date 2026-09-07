# ---------------------------------------------------------------
# 03_figure.py -- SOLUTION, lab 2 step 7
#
# Input  : data/processed/trade_clean.csv   (produced by 02_cleaning.py)
# Output : output/figures/oak_destinations.png
#
# This is the script you were given, unchanged. What follows is why
# each choice was made, which is the part you were asked to work out.
# ---------------------------------------------------------------

# --- Dependencies ---
# pandas draws the chart, matplotlib does the drawing. They are two
# packages: python -m pip install matplotlib
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# --- Parameters ---
ROOT  = Path(__file__).resolve().parents[1]
OAK   = 440391    # HS code: oak logs
N_TOP = 5         # destinations shown by name; the rest become "Other"

# --- Load ---
# The output of the previous script, not the raw file.
clean = pd.read_csv(ROOT / "data" / "processed" / "trade_clean.csv")

# --- 1. Filter ---
oak = clean[(clean.cmdCode == OAK)                     # oak logs only
            & (clean.reporterDesc == "France")         # declared by France
            & (clean.flowDesc == "Export")]            # outgoing flows

# --- 2. Aggregate ---
# pivot_table gives one row per year and one column per destination, which
# is exactly the shape a stacked bar chart wants. fill_value=0 turns "this
# country bought nothing that year" into a zero rather than a hole.
by_country = oak.pivot_table(index="period", columns="partnerDesc",
                             values="primaryValue", aggfunc="sum", fill_value=0)

# Rank over the whole period, not year by year.
totals = by_country.sum().sort_values(ascending=False)
top    = list(totals.index[:N_TOP])

# Everything outside the top five is summed into one column.
graph = by_country[top].copy()
graph["Other"] = by_country.drop(columns=top).sum(axis=1)

# --- 3. Plot ---
# Stacked bars rather than lines: three years make three points.
ax = (graph / 1e6).plot(kind="bar", stacked=True, figsize=(9, 5), width=0.6)
ax.set_title("French oak log exports (HS 440391)")
ax.set_xlabel("")
ax.set_ylabel("million USD")
# The legend outside the axes: inside, it covers the tallest bar.
ax.legend(title="Destination", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()

# --- Output ---
plt.savefig(ROOT / "output" / "figures" / "oak_destinations.png", dpi=150)

print("Figure written. Top destination:", totals.index[0],
      f"({totals.iloc[0]/1e6:.1f} M$ over three years)")
