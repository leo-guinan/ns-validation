# Experiment 59 — survival/attack incidence

For every kernel world, the receipt joins exact cover participation with exact minimum-blocker incidence:

```text
p(w):       minimum-cover participation
q_tau(w):   minimum optimality-blocker incidence
q_kappa(w): minimum feasibility-blocker incidence
```

Measured strict-order result:

```text
p versus q_tau:   zero strict-order inversions in all five components
p versus q_kappa: 12 inversions in component 8
                  412 inversions in component 11
                  0 in components 12, 21, and 45
```

This does not claim identical weak-order partitions; ties are kept as a separate question for Experiment 60.

Every minimum feasibility blocker is an optimality blocker. Direct checking also verifies that every minimum-degree feasibility neighborhood is an exact-one cut of the local optimum family:

```text
|C ∩ N(x)| = 1 for every local minimum cover C
```

For each blocker, exact cover-participation mass and containment of minimum optimality blockers are preserved. These are finite combinatorial incidence fractions, not attack probabilities or real-world failure likelihoods.
