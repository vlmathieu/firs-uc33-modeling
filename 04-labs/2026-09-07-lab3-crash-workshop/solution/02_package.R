# 02 -- SOLUTION: read_csv() comes from readr, which was not loaded.
# Two fixes are possible; this one avoids adding a dependency.
trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")
print(head(trade, 5))
