# -----------------------------------------------------------------
# 03 -- Quantite moyenne par flux exporte
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

exports = trade[trade.flowDesc == "Export"]

print("Quantite moyenne exportee :", export.qty.mean(), "m3")
