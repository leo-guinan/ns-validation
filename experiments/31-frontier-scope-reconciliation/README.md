# Experiment 31 — frontier-scope reconciliation

The apparent 2508-versus-2522 discrepancy is resolved by transition-relative frontier scope.

```text
source A: theorem_1_1_with_initial_rest       |F_A| = 2450
source B: ProblemStatement.breakdownStatement |F_B| =   14
target:   theorem_1_1_with_dissipation       |F_T| = 2522
```

Literal set comparison gives:

```text
T \ A: 72
T \ B: 2508
A \ T: 0
B \ T: 0
```

Therefore both source frontiers are subsets of the same 2522-member target frontier. The 72-entry and 2508-entry objects are target-only transition deltas, not complete target-frontier sizes. The 72 delta is literally contained in the 2508 delta; the remaining difference has 2436 identities.

This reconciles frontier scope only. It does not promote delta-cover results into full-target cover results. Experiments 26–30 remain superseded until rerun against an authoritative full-target bipartite graph.
