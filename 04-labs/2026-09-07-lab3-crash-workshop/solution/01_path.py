# 01 -- SOLUTION: path built from the project root.
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
trade = pd.read_csv(ROOT / "data" / "raw" / "comtrade_fr_roundwood_clean.csv")
print("Rows:", len(trade))
