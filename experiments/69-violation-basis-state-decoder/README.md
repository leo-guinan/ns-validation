# Experiment 69 — violation basis and exact state decoder

The original-obligation violation predicates form a basis of the Boolean functions on the repair cube that vanish at zero defect:

```text
component  basis rank  repair-bit decoder  one-hot state decoders
8               3              yes                  yes
11             15              yes                  yes
```

The nonzero-state evaluation matrices are square and invertible over GF(2). Their exact matrices, inverses, repair-coordinate expansions, and one-hot state expansions are preserved.

The finite representation therefore has nonlinear forward encoding from defect state to violation predicates, and fixed linear XOR decoding back to repair coordinates or exact nonzero-state identity. This is scoped to the fixed Boolean/coverage contract and is not a storage-cost, semantic-complexity, or causal claim.
