# Experiment 43 — exact participation spectrum

Participation is computed from exact component-local optimum families. For candidate `l`, the receipt stores the integer numerator and denominator of its fraction of local optima containing `l`.

```text
backbone:                         250
optional-optimal:                200
basis-touching, never optimal:    22
basis-disconnected:              443
```

Exact checksum:

```text
sum_l p(l) = 309
backbone contribution = 250
optional-shell contribution = 59
```

The optional spectrum ranges from `1/37` to `4/5`. The exact arithmetic mean across the 200 optional declarations is `59/200 = 0.295`; this is not an assertion that every optional declaration has that individual participation. Participation is a uniform counting fraction over the finite current optimum family, not an empirical probability or semantic necessity measure.
