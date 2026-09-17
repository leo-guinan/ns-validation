# Experiment 40 — constraint subsumption analysis

For each frontier identity `f`, the current graph neighborhood is `N(f) = {l : (l,f) in E}`. A smaller neighborhood subsumes a larger one: `N(d) ⊆ N(h)` means the delta coverage clause for `d` implies the inherited clause for `h`.

Inherited certificates:

```text
14 inherited identities
14 subsumption witnesses
all witness checks verified
```

Across the full current graph:

```text
frontier identities:             2522
unique neighborhoods:            1662
duplicate equivalence classes:    316
inclusion-minimal constraint classes: 320
strictly subsumed identities:    1687
constraints removed by basis:    2202
```

Every frontier neighborhood contains an inclusion-minimal basis neighborhood, so the 320-class basis and full frontier define the same feasible cover family. Identity representatives are canonical labels only; the logical basis is the set of unique neighborhoods. The 2,202 removed identity constraints decompose into 1,687 strict-subsumption removals and 515 duplicate identities inside minimal classes. This is constraint compression, not semantic compression, candidate compression, or interface width.
