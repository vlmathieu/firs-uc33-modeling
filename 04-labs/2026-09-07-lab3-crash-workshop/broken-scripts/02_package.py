# -----------------------------------------------------------------
# 02 -- Print the first five rows
# -----------------------------------------------------------------

trade = pd.read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

print(trade.head(5))
