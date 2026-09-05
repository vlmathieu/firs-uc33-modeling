# -----------------------------------------------------------------
# 03 -- Mean quantity per exported flow
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

exports = trade[trade.flowDesc == "Export"]

print("Mean exported quantity:", export.qty.mean(), "m3")
