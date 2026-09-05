# -----------------------------------------------------------------
# 01 -- How many rows does the dataset contain?
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("/Users/valentin/Documents/uc33/data/raw/comtrade_fr_roundwood_clean.csv")

print("Rows:", len(trade))
