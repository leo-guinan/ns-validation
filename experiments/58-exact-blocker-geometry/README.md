# Experiment 58 — exact blocker geometry

Blocker cardinality and blocker-family multiplicity are separate:

```text
(tau, # minimum optimality blockers, kappa, # minimum feasibility blockers)
component 8:  (4, 3, 4, 1)
component 11: (16, 5, 21, 2)
component 12: (1, 1, 2, 2)
component 21: (1, 2, 4, 2)
component 45: (1, 1, 2, 2)
```

The receipt also preserves all inclusion-minimal coordinate-neighborhood feasibility blockers. The minimum feasibility family is exactly the distinct minimum-degree neighborhoods, verifying:

```text
kappa = min_x |N(x)|
```

Singleton minimum optimality blockers are exactly the residual cover-backbone worlds:

```text
{283, 296, 351, 354}
```

The complete blocker receipts preserve multiplicity, backbone, support, per-world incidence, literal examples, and comparisons with Experiment 55 participation. Participation remains a cover-family fraction, not a blocker probability.
