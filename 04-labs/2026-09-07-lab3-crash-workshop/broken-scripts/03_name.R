# -----------------------------------------------------------------
# 03 -- Quantite moyenne par flux exporte
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")

exports <- subset(trade, flowDesc == "Export")

cat("Quantite moyenne exportee :", mean(export$qty, na.rm = TRUE), "m3\n")
