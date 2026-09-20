# Experiment 65 — Boolean defect structure

Canonical ANF analysis separates algebraic degree from the full minimal dependency-support result of Experiment 64.

```text
component  degree histogram  pure-add edges  pure-remove edges  replacement edges
8          degree 2: 3              2                 0                 2
11         degree 4: 15             4                 0                28
```

Every original violation function has full repair-coordinate dependency, but its canonical algebraic degree is reported separately. Complete one-bit transition edges, added/removed obligation sets, ANF monomial supports, and degree histograms are preserved.

A single fixed permutation of original obligations verifies the unweighted logical defect-map automorphism for both components. The certificate is literal:

```text
rho(phi(reverse(d))) = phi(d)
```

for every defect state in the relevant cube. Multiplicity preservation is a separate property: it holds for component 11 and fails for component 8. This is not a semantic or path-reversal claim.
