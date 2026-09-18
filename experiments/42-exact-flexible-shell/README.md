# Experiment 42 — exact flexible shell

Under the current Experiment 41 basis graph, componentwise optimum unions and intersections classify all 915 candidates exactly.

```text
candidates:                         915
basis-touching:                    472
basis-disconnected:                443
basis-touching but never optimal:   22
backbone:                          250
optimum support U*:                450
optional-optimal shell:            200
non-backbone slots per optimum:     59
```

The global optimum count factors as:

```text
1,852,694,344,344,010,752,000,000
= 2,470,259,125,792,014,336,000 × 750
```

The first factor comes from zero-slack substitution components; the second from positive-slack components. Component categories are recorded separately for rigid local obligations, pure substitution, shared realization with rigid implementation, and shared realization with substitution.

All claims are current-contract graph claims, not semantic necessity or historical-contract claims.
