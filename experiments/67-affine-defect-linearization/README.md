# Experiment 67 — affine defect linearization

Factor the universal full-degree monomial from each law:

```text
g_x = f_x XOR m
V = {0} ∪ {g_x}
```

The translated-linear hypothesis fails in both components:

```text
component  |V|  XOR closed  span dimension  h normal form
8            3      no             2              not claimed
11          15      no            14              not claimed
```

The exact GF(2) spans and coefficient representations are preserved. Zero is already present, and every nonzero observed mask is linearly independent of the others:

```text
component 8:  2 independent nonzero masks; span rank 2
component 11: 14 independent nonzero masks; span rank 14
```

These ranks are codimension one in the full lower-order ANF spaces, whose dimensions are 3 and 15 respectively. The observed families are therefore not translated-linear spaces, but are affine-independent sets with one shared full-degree term plus independent lower-order deviations. No storage-cost or semantic-complexity interpretation is made.
