# 05 -- SOLUTION: partnerDesc == "World" is the all-partners aggregate.
# Keeping it means counting every flow twice. Reliable marker: W00.
trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak <- subset(trade,
              cmdCode      == 440391 &
              reporterDesc == "France" &
              flowDesc     == "Export" &
              partnerISO   != "W00")

# Guard rail: makes the bug impossible instead of relying on vigilance.
stopifnot(!"W00" %in% oak$partnerISO)

cat("French oak log exports, 2022-2024:\n")
cat("  ", round(sum(oak$primaryValue) / 1e6, 1), "million USD\n")
cat("  ", nrow(oak), "reported flows\n")
