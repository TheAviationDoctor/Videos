category <- c("All aerodromes", "Scheduled service", "≥1 passenger", "Scheduled service")
a <- round(seq(from = 1, to = 75059), 0)
b <- round(seq(from = 1, to = 4247, length.out = max(a)), 0)
c <- round(seq(from = 1, to = 3400, length.out = max(a)), 0)
d <- round(seq(from = 1, to = 881,  length.out = max(a)), 0)

out <- cbind(category, rep(a, each = 4))
tail(out, 100)

# dt_apt <- rbind(
  # cbind(category, rep(a, each = 4)),
  # cbind(category, rep(b, each = 4)),
  # cbind(category, rep(c, each = 4)),
  # cbind(category, rep(d, each = 4))
# )

# tail(dt_apt, 100)