# -----------------------------------------------------------------
# 03 -- Mean quantity per exported flow
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")

exports <- subset(trade, flowDesc == "Export")

cat("Mean exported quantity:", mean(export$qty, na.rm = TRUE), "m3\n")
