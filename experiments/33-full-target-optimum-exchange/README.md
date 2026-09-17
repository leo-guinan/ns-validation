# Experiment 33 — full-target optimum exchange and composition anatomy

Under the full target contract (`F_T` size 2,522), the recorded `I2508` and the independent MILP optimum `Jfull` are both width 309 and differ by one exchange:

```text
removed: ConservativeDifference.tensorDiff_divergence
added:   ConservativeDifference.weak_pressure_poisson
```

The exact-width forbidden-member sweep found 59 feasible replacements among 309 tested declarations. The remaining 250 cases are recorded as `infeasible_or_timeout`; they are not promoted to a backbone classification.

The composed transition interface has size 314. Against `Jfull`, it has 304 retained declarations, 10 composed-only declarations, and 5 full-optimum-only declarations. Its symmetric difference is 15, so the net +5 composition overhead is a 10-for-5 reoptimization rather than pure deletion.

These are graph-contract measurements. The sweep does not enumerate the optimum family, and no semantic necessity is inferred.

Contract audit: the inferred old 2,508-delta local vocabulary has 741 locals, while the target local vocabulary has 744. Both exchanged declarations are present in the inferred delta vocabulary, so the observed one-for-one exchange is not explained by the reconstructed candidate vocabulary. The old delta edge lists were not preserved, however; exact replay of `Jfull` under the old edge relation is therefore unavailable. Delta uniqueness is neither falsified nor confirmed by this audit.
