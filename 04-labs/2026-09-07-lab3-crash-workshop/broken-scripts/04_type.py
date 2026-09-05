# -----------------------------------------------------------------
# 04 -- Valeur totale des flux du jeu de donnees
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                    sep=";", encoding="latin-1")

print("Valeur totale :", trade.primaryValue.sum(), "USD")
