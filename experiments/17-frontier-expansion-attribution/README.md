# Experiment 17 — frontier expansion attribution

Experiment 17 asks whether an observed frontier delta is attributable to the marginal local declarations on the same elaborated transition.

For each expanding edge:

```text
ΔL = local support(B) \\ local support(A)
ΔF = frontier(B) \\ frontier(A)
A_F(direct) = direct external dependencies of ΔL
A_F(transitive) = transitive external dependencies of ΔL
```

The receipt compares both `A_F` sets with `ΔF` and records the active-at-entry fraction.

Observed result across all six expanding edges:

```text
active-at-entry direct overlap:      |ΔF| on every edge
active-at-entry transitive overlap:  |ΔF| on every edge
active-at-entry fraction α:           1.0 on every edge
```

Under the declared elaborated dependency boundary, frontier appearance is therefore attributable to external dependencies of the marginal local declarations. This does not establish runtime causality, semantic necessity, minimality, or sufficiency. It also does not erase the Experiment 16 distinction: later marginal transitions did not actively consume these frontier identities in the five observed downstream cases.
