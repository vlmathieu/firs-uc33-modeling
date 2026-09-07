# 02 -- SOLUTION: `import pandas as pd` was missing. The name pd did not exist.
import pandas as pd
trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")
print(trade.head(5))
