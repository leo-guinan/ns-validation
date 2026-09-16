# Experiment 16 — active frontier reuse

Experiment 16 separates inherited frontier persistence from active downstream reuse. For every frontier-expanding edge `e`, it defines `N_e = F_after \\ F_before`. For each reachable downstream transition it measures:

```text
P: N_e identities present in the downstream total frontier
D: N_e identities directly referenced by downstream marginal local declarations
T: N_e identities transitively required by downstream marginal local declarations
```

Observed result in the selected graph:

```text
frontier-expanding edges:          6
downstream transition observations: 5
P full-persistence observations:   5
D nonzero observations:            0
T nonzero observations:            0
```

Thus the measured frontier identities remain available in downstream closures, but the marginal declarations in the five reachable downstream transition observations do not actively reference them under the declared elaborated boundary.

This is evidence for passive inherited availability in this selected graph, not evidence that active reuse never occurs. It does not establish runtime savings, causality, necessity, minimality, or optimality.
