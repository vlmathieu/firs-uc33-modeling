# ---------------------------------------------------------------
# 02_cleaning_challenges.py -- SOLUTION, lab 2 core + challenge 1
#
# The brief on its own is 02_cleaning.py. This script adds the apparent
# density and the aberrant values (challenge 1), and overwrites the same
# trade_clean.csv with two extra columns. The figure is 03_figure.py.
#
# Input  : data/raw/comtrade_fr_roundwood_dirty.csv
# Output : data/processed/trade_clean.csv  (+ density, density_suspect)
# ---------------------------------------------------------------

# --- Dependencies ---
from pathlib import Path
import pandas as pd

# --- Parameters ---
ROOT     = Path(__file__).resolve().parents[1]
DENS_MIN = 200     # kg/m3 -- lighter than balsa (160): impossible
DENS_MAX = 1300    # kg/m3 -- heavier than lignum vitae (1250): impossible

# --- Load ---
# sep, decimal and encoding must be DECLARED: a CSV is not one single format.
# keep_default_na=False: without it pandas turns the literal string "N/A" in
# qtyUnitAbbr into a missing value, erasing real information (unit not
# reported is not the same thing as unit absent).
trade = pd.read_csv(ROOT / "data" / "raw" / "comtrade_fr_roundwood_dirty.csv",
                    sep=";", decimal=",", encoding="latin-1",
                    keep_default_na=False, na_values=[""])

assert trade.shape == (674, 13), f"expected (674, 13), got {trade.shape}"

# --- Diagnose ---
print("Missing values :", {k: int(v) for k, v in trade.isna().sum().items() if v})
print("qty == 0       :", int((trade.qty == 0).sum()))
print("units of qty   :", sorted(trade.qtyUnitAbbr.unique()))
print("partners       :", trade.partnerDesc.nunique(),
      "including 'World':", "World" in set(trade.partnerDesc))
print("aggrLevel      :", trade.aggrLevel.unique(), "<- constant, unusable")

# --- Clean ---
# 1. World is the all-partners aggregate: keeping it doubles every total.
#    Filter on the CODE partnerISO == "W00" rather than on the name: a name
#    gets translated and renamed, a reserved code does not.
clean = trade[trade.partnerISO != "W00"].copy()

# 2. aggrLevel equals 6 on all 674 rows: a constant column contributes
#    nothing -- no filter, no grouping, no statistic.
clean = clean.drop(columns=["aggrLevel"])

# 3. The types. qty, netWgt and primaryValue are the columns at risk: their
#    decimal mark is a comma, and undeclared they arrive as object.
assert clean[["qty", "netWgt", "primaryValue"]].dtypes.eq("float64").all(), "a value column is text"

# 4. Apparent density, only where a volume is actually reported.
#    qty == 0 would divide by zero and yield inf, which travels through a
#    mean without a sound.
volume = clean.qty.where((clean.qtyUnitAbbr == "m³") & (clean.qty > 0))
clean["density"] = clean.netWgt / volume

# 5. We KEEP the aberrant densities, but flag them.
#    Rationale: they cluster on very small flows (46 % below 10 m3, 8 % above).
#    These are rounding and reporting thresholds, not data entry errors.
#    Dropping them would bias any flow count; keeping them unflagged would
#    corrupt any density calculation.
#    Careful: ~between() returns True for NaN, which would flag as "suspect"
#    the 21 rows where the density is simply not computable. A missing density
#    is not an impossible one. Hence the notna().
clean["density_suspect"] = (clean.density.notna()
                            & ~clean.density.between(DENS_MIN, DENS_MAX))

print(f"\nRows kept        : {len(clean)} (out of {len(trade)})")
print(f"Median density   : {clean.density.median():.0f} kg/m3")
print(f"Suspect densities: {int(clean.density_suspect.sum())}")

# --- Check: the total must have been halved ---
fr = clean[clean.reporterDesc == "France"]
print(f"France total     : {fr.primaryValue.sum()/1e6:.1f} M$  (expected 778.5)")
assert abs(fr.primaryValue.sum()/1e6 - 778.5) < 0.1, "the World aggregate was not excluded"

# --- Challenge 1: WHY are the densities aberrant? ---
# The guard rail first. It fails, and that is the point.
#   assert d.density.between(DENS_MIN, DENS_MAX).all()    # fails
d = clean[clean.density.notna()].copy()

# Split the flows into volume bands and look at the share of aberrant
# densities inside each one.
d["band"] = pd.cut(d.qty, [0, 10, 100, 1000, float("inf")],
                   labels=["< 10", "10-100", "100-1000", "> 1000"])

print("\nFlows per volume band:")
print(d.band.value_counts().sort_index())
print("Share aberrant, per band (%):")
print((d.groupby("band", observed=True).density_suspect.mean() * 100).round(1))
print("Median volume, aberrant vs not:")
print(d.groupby("density_suspect").qty.median())

# CONCLUSION, in three lines.
# 1. 46 % of the flows under 10 m3 have an impossible density, against 6 to
#    12 % everywhere else. The smallest volumes go down to 0.001 m3.
# 2. That is arithmetic, not fraud: a weight rounded to the kilo divided by a
#    volume rounded to the thousandth of a cubic metre produces anything at all.
# 3. So we KEEP them and flag them. Deleting 13.5 % of the rows would bias any
#    count of flows; a test that rejects correct data is a bad test.

# --- Output ---
clean.to_csv(ROOT / "data" / "processed" / "trade_clean.csv", index=False)
