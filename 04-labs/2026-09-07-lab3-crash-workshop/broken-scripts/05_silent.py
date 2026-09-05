# -----------------------------------------------------------------
# 05 -- Exportations francaises de grumes de chene, 2022-2024
#
# Ce script ne plante pas. Il produit un nombre.
# Votre travail : decider si ce nombre est vrai.
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak = trade[(trade.cmdCode == 440391)
            & (trade.reporterDesc == "France")
            & (trade.flowDesc == "Export")]

total = oak.primaryValue.sum()

print("Exportations francaises de grumes de chene, 2022-2024 :")
print(f"   {total / 1e6:.1f} millions USD")
print(f"   {len(oak)} flux declares")
