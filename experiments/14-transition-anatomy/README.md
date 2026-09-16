# Experiment 14 — transition anatomy

Experiment 14 analyzes all 12 elaborated-reachability transitions in the selected six-node graph from Experiment 13.

Distribution:

```text
frontier unchanged: 6
frontier expanding: 6
```

```text
Δlocal:    2, 4, 6, 29, 2, 4, 27, 2, 882, 884, 886, 909
Δfrontier: 0, 0, 0, 72, 0, 0, 72, 0, 2436, 2436, 2436, 2508
```

For each frontier-expanding transition, the receipt records the newly introduced external identities and their retained count in downstream selected supports. Downstream reuse is bounded to the selected six-node graph; it is not a causal runtime or sufficiency claim.

The result contains both internal capability transitions and world-expanding transitions. It does not establish a general capability-growth law, optimality, minimality, or runtime complexity relationship.
