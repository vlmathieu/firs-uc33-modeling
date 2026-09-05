# -----------------------------------------------------------------
# 05 -- Exportations francaises de grumes de chene, 2022-2024
#
# Ce script ne plante pas. Il produit un nombre.
# Votre travail : decider si ce nombre est vrai.
# -----------------------------------------------------------------

trade <- read.csv("data/raw/comtrade_fr_roundwood_clean.csv")

oak <- subset(trade,
              cmdCode      == 440391 &
              reporterDesc == "France" &
              flowDesc     == "Export")

total <- sum(oak$primaryValue)

cat("Exportations francaises de grumes de chene, 2022-2024 :\n")
cat("  ", round(total / 1e6, 1), "millions USD\n")
cat("  ", nrow(oak), "flux declares\n")
