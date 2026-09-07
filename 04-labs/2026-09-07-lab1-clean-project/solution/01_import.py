# ---------------------------------------------------------------
# 01_import.py -- SOLUTION
# ---------------------------------------------------------------

# --- Dependencies ---
from pathlib import Path
import pandas as pd

# --- Parameters ---
ROOT    = Path(__file__).resolve().parent.parent   # project root
COUNTRY = "France"

# --- Body ---
trade = pd.read_csv(ROOT / "data" / "raw" / "comtrade_fr_roundwood_clean.csv")

# partnerDesc == "World" is the all-partners aggregate.
france = trade[(trade.reporterDesc == COUNTRY) & (trade.partnerDesc != "World")]

# --- Output ---
france.to_csv(ROOT / "data" / "processed" / "trade_france.csv", index=False)

print("Written:", len(france), "rows")
