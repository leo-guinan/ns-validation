# Experiment 13 — marginal proof transition graph

Experiment 13 uses six theorem declarations from the source-grounded inventory in `NavierStokes/R3/Theorem.lean`. A transition is included only when the elaborated local dependency graph establishes descendant→ancestor reachability.

Boundary:

```text
recurse through NavierStokesR3; stop at external declarations
```

Observed selected transitions include:

```text
initial-rest → final theorem:       Δlocal 2,  Δfrontier 0
final theorem → candidateStatement: Δlocal 2,  Δfrontier 0
candidateStatement → coreBreakdown: Δlocal 2,  Δfrontier 0
initial-rest → dissipation theorem: Δlocal 29, Δfrontier 72
```

The full selected graph contains 6 nodes, 12 reachable transitions, and 4023 unique local dependency edges. Each transition records inherited support, marginal local declarations, marginal external frontier declarations, new direct local references, and depth change.

The two-declaration transition therefore recurs in this small chain, but larger transitions also occur. This is not the complete 892-node project DAG and does not establish a general delta law, minimality, sufficiency, or runtime complexity relationship.
