# -----------------------------------------------------------------
# 05 -- French oak log exports, 2022-2024
#
# This script does not crash. It produces a number.
# Your job: decide whether that number is true.
# -----------------------------------------------------------------

import pandas as pd

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak = trade[(trade.cmdCode == 440391)
            & (trade.reporterDesc == "France")
            & (trade.flowDesc == "Export")]

total = oak.primaryValue.sum()

print("French oak log exports, 2022-2024:")
print(f"   {total / 1e6:.1f} million USD")
print(f"   {len(oak)} reported flows")
