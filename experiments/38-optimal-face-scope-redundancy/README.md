# Experiment 38 — optimal-face scope redundancy

Under the Experiment 37 fixed current contract, each of the 14 inherited frontier identities was forced uncovered while enforcing all 2,508 delta constraints and exact width 309.

```text
feasible noncoverage: 0
proven infeasible:    14
timeouts:             0
```

The literal frontier relation is `F_delta ⊂ F_full`; the feasible-cover relation is `Feas(C_full) ⊆ Feas(C_delta)`. Every width-309 delta optimum therefore covers every inherited frontier identity. Combined with the feasible-family inclusion, this establishes equality of the two measured optimum families:

```text
Opt(C_delta) = Opt(C_full)
```

The fourteen inherited coverage constraints are syntactically additional, but proven redundant over the width-309 optimal face. Their global redundancy is not measured. This is current-contract-relative and does not transfer to the unreplayable historical contract.
