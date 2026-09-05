# -----------------------------------------------------------------
# 05 -- French oak log exports, 2022-2024
#
# This script does not crash. It produces a number.
# Your job: decide whether that number is true.
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak <- subset(trade,
              cmdCode      == 440391 &
              reporterDesc == "France" &
              flowDesc     == "Export")

total <- sum(oak$primaryValue)

cat("French oak log exports, 2022-2024:\n")
cat("  ", round(total / 1e6, 1), "million USD\n")
cat("  ", nrow(oak), "reported flows\n")
