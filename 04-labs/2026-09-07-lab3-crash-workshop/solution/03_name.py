# 03 -- SOLUTION: the object is called `exports`, not `export`.
import pandas as pd
trade   = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")
exports = trade[trade.flowDesc == "Export"]
print("Mean exported quantity:", exports.qty.mean(), "m3")
