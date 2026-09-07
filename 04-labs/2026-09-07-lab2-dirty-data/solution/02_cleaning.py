# ---------------------------------------------------------------
# 02_cleaning.py -- SOLUTION, lab 2 core (steps 3 and 6)
#
# Input  : data/raw/comtrade_fr_roundwood_dirty.csv
# Output : data/processed/trade_clean.csv
#
# This is the brief, and nothing more. The density work and the
# investigation behind it are in 02_cleaning_challenges.py.
# ---------------------------------------------------------------

# --- Dependencies ---
from pathlib import Path
import pandas as pd

# --- Parameters ---
ROOT = Path(__file__).resolve().parents[1]

# --- Load ---
# sep, decimal and encoding must be DECLARED: a CSV is not one single format.
# keep_default_na=False: without it pandas turns the literal string "N/A" in
# qtyUnitAbbr into a missing value, erasing real information (unit not
# reported is not the same thing as unit absent).
trade = pd.read_csv(ROOT / "data" / "raw" / "comtrade_fr_roundwood_dirty.csv",
                    sep=";", decimal=",", encoding="latin-1",
                    keep_default_na=False, na_values=[""])

assert trade.shape == (674, 13), f"expected (674, 13), got {trade.shape}"

# --- Clean: five decisions, each with its reason ---

# a) World is the all-partners aggregate, sitting in the table next to the
#    partners it is the total of. Keeping it doubles every total.
#    Filter on the CODE, not the label: a label gets translated and renamed,
#    a reserved code does not.
#    .copy() is not decoration: without it pandas warns later that you are
#    modifying a view of another table rather than a table of your own.
clean = trade[trade.partnerISO != "W00"].copy()

# b) The 17 rows with qty == 0 are KEPT. They are real flows with an
#    unreported quantity, and nothing in this script divides by qty, so
#    there is no inf to produce. The decision belongs to whoever divides:
#    see 02_cleaning_challenges.py, which does, and excludes them there.
print("qty == 0 rows kept :", int((trade.qty == 0).sum()))

# c) The 11 missing netWgt are KEPT, for the same reason: no computation
#    here uses the net weight. Deleting a row costs information; leaving a
#    missing value costs nothing until something tries to average it.
print("missing netWgt kept:", int(trade.netWgt.isna().sum()))

# d) aggrLevel equals 6 on all 674 rows. A constant column allows no filter,
#    no grouping and no statistic, and left in place it invites a groupby
#    that groups nothing.
clean = clean.drop(columns=["aggrLevel"])

# e) The types. .info() before trusting anything: qty, netWgt and primaryValue
#    are the columns at risk, because their decimal mark is a comma. Declared
#    at load time they are float64; undeclared they arrive as object and
#    nothing says so. period is already an int here -- checked, not assumed.
assert clean[["qty", "netWgt", "primaryValue"]].dtypes.eq("float64").all(), "a value column is text"
assert clean.period.dtype == "int64"

# --- Check ---
# The trap of the lab, turned into a line that fails rather than lies.
fr = clean[clean.reporterDesc == "France"]
print(f"Rows kept    : {len(clean)} out of {len(trade)}")
print(f"France total : {fr.primaryValue.sum()/1e6:.1f} M$ (expected 778.5)")
assert abs(fr.primaryValue.sum()/1e6 - 778.5) < 0.1, "the World aggregate was not excluded"

# --- Output ---
clean.to_csv(ROOT / "data" / "processed" / "trade_clean.csv", index=False)
