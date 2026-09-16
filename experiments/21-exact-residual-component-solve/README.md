# Experiment 21 — exact residual component solve

Experiment 21 solves the reduced residual gateway graph component by component using memoized bitset branch-and-bound. The objective decomposes additively because disconnected components share neither frontier identities nor candidate locals.

Results:

```text
ΔF=72:    0 residual components, exact total cover = 12
ΔF=2436:  54 residual components, residual optimum = 63, exact total = 302
ΔF=2508:  53 residual components, residual optimum = 65, exact total = 309
```

All residual components completed within budget. Deterministic bipartite color-refinement signatures identify 13 repeated structural signature classes. These are grouping signatures, not isomorphism certificates.

The exact result is a minimum cover of the measured bipartite entry graph under the stated reductions and representation. It is not a claim of semantic necessity, runtime complexity, sufficiency, or universality.
