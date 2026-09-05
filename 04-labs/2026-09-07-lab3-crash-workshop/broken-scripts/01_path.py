# -----------------------------------------------------------------
# 01 -- Combien de lignes le jeu de donnees contient-il ?
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("/Users/valentin/Documents/uc33/data/raw/comtrade_fr_roundwood_clean.csv")

print("Lignes :", len(trade))
