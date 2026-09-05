# -----------------------------------------------------------------
# 04 -- Total value of the flows in the dataset
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                    sep=";", encoding="latin-1")

print("Total value:", trade.primaryValue.sum(), "USD")
