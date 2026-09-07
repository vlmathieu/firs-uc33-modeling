# 03 -- SOLUTION: the object is called `exports`, not `export`.
trade   <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")
exports <- subset(trade, flowDesc == "Export")
cat("Mean exported quantity:", mean(exports$qty, na.rm = TRUE), "m3\n")
