# Experiment 61 — exact-one interface sufficiency

All distinct coordinate neighborhoods were tested for exact-one behavior across the local optimum family. The reconstructed family uses only:

```text
E z = 1
sum(z) = current optimum width
```

Results:

```text
component   exact-one rows   Opt     R_E      false positives
8                   3         48      144          96
11                  3        902    10584        9682
12                  2          1        1           0
21                  6          1        1           0
45                  2          1        1           0
```

Thus the exact-one constraints are an exactly sufficient representation of the optimum family in components 12, 21, and 45. In components 8 and 11 they are objective-value sufficient but solution-family insufficient: every optimum is reconstructed, but false positives remain. Literal false-positive witnesses and every world's membership signature are preserved.

The maximum number of pairwise-disjoint exact-one neighborhoods certifies the optimum width in all five kernel components:


```text
component 8:  3 (tight at width 3)
component 11: 3 (tight at width 3)
component 12: 1 (tight at width 1)
component 21: 2 (tight at width 2)
component 45: 1 (tight at width 1)
```

This is representation sufficiency under the fixed finite contract, not semantic compression.
