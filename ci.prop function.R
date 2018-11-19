ci.prop <- function(k, n, conf.level=0.95) {
  critical.value <- qnorm(1 - (1 - conf.level) / 2)
  p.hat <- k / n
  standard.error <- sqrt(p.hat * (1 - p.hat) / n)
  margin.of.error <- critical.value * standard.error
  return(p.hat + c(-margin.of.error, margin.of.error))
}
