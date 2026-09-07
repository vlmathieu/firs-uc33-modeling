# 05 -- SOLUTION: partnerDesc == "World" is the all-partners aggregate.
import pandas as pd
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak = trade[(trade.cmdCode == 440391)
            & (trade.reporterDesc == "France")
            & (trade.flowDesc == "Export")
            & (trade.partnerISO != "W00")]

# Guard rail: makes the bug impossible instead of relying on vigilance.
assert "W00" not in set(oak.partnerISO), "the all-partners aggregate is still in the table"

print("French oak log exports, 2022-2024:")
print(f"   {oak.primaryValue.sum() / 1e6:.1f} million USD")
print(f"   {len(oak)} reported flows")
