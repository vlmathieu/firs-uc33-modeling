# 04 -- SOLUTION: decimal="," was missing.
# Without it primaryValue is a text column -- and sum() on text raises NO error
# in Python: it concatenates, and returns a 6,349-character string. R refuses.
# The more permissive language is not the safer one.
import pandas as pd
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                    sep=";", decimal=",", encoding="latin-1")
print("Total value:", trade.primaryValue.sum(), "USD")
