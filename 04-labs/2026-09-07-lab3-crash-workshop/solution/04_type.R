# 04 -- SOLUTION: sep, dec AND fileEncoding. All three must be declared.
#   without dec=","       -> primaryValue read as text, sum() refuses
#   without fileEncoding  -> accents unreadable, and no error raised at all
trade <- read.csv("data/raw/comtrade_fr_roundwood_dirty.csv",
                  sep = ";", dec = ",", fileEncoding = "latin1")
cat("Total value:", sum(trade$primaryValue, na.rm = TRUE), "USD\n")
