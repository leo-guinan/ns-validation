# Experiment 24 — interface edit anatomy

Experiment 24 analyzes the exact non-monotone edit from the unique 302-member 2436 interface to the unique 309-member 2508 interface.

```text
removed: 9
added: 16
retained: 293
symmetric difference: 25
net width change: +7
```

The complete 12-member optimum interface for the 72-frontier case is fully contained in the 16 additions and has zero intersection with the retained 2436 interface:

```text
I72 ⊆ A
|I72 ∩ A| = 12
|I72 ∩ retained| = 0
```

The literal frontier-neighborhood edit graph contains 138 removed-to-added overlap edges, and all 9 removed gateways have at least one overlapping added gateway. These overlaps are representational frontier-identity intersections, not semantic correspondences.
