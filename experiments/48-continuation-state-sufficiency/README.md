# Experiment 48 — continuation-state sufficiency

Exact suffix-language signatures were computed for every reachable geodesic state in every ordered local-optimum pair.

Cross-tab:

```text
precedence pairs:              34
partial-retention pairs:       76
non-poset pairs:               12
precedence ∩ partial:           34
partial without precedence:     42
non-poset ∩ precedence:          6
non-poset ∩ partial:            12
all three:                       6
```

Continuation sufficiency:

```text
depth-only collisions:          54 pairs
removal-set collisions:           0
addition-set collisions:           0
full (R,A) collisions:             0
```

The exact continuation-state count is `K_continuation = 4104`; all 4,104 measured continuation states had distinct exact signatures. An arbitrary index therefore needs a 13-bit information-theoretic lower bound (`2^12 < 4104 <= 2^13`), not a claim about literal representation size. Pair-scoped `(endpoint pair, R)` and `(endpoint pair, A)` projection universes each contain 4,104 distinct entries, with canonical hashes recorded in the receipt, so either projection uniquely identifies the measured state. Depth alone is insufficient; removal-only and addition-only descriptions were sufficient for this finite measured family.

A collision proves a representation insufficient for exact current-contract future-route prediction. It is not a semantic causality claim.
