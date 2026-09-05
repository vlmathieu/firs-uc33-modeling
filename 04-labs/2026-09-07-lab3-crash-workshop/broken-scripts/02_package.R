# -----------------------------------------------------------------
# 02 -- Afficher les cinq premieres lignes
# -----------------------------------------------------------------

trade <- read_csv("data/raw/comtrade_fr_roundwood_clean.csv")

print(head(trade, 5))
