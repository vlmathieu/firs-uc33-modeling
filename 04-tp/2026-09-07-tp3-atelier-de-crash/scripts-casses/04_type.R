# -----------------------------------------------------------------
# 04 -- Valeur totale des flux du jeu de donnees
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv", sep = ";")

cat("Valeur totale :", sum(trade$primaryValue, na.rm = TRUE), "USD\n")
