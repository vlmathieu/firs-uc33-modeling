# -----------------------------------------------------------------
# 01 -- Combien de lignes le jeu de donnees contient-il ?
# -----------------------------------------------------------------

trade <- read.csv("/Users/valentin/Documents/uc33/data/raw/comtrade_fr_roundwood_clean.csv")

cat("Lignes :", nrow(trade), "\n")
