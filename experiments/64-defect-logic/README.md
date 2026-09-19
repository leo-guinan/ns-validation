# Experiment 64 — defect logic

Each original coverage obligation is represented by its exact Boolean violation function over the fully realized repair-defect cube.

Results:

```text
component  monotone violation map  dependency orders
8          no                       all 2
11         no                       all 4
```

Every original violation function has minimal dependency support equal to the full repair dimension: 2 in component 8 and 4 in component 11. This does not measure algebraic interaction degree; that is deferred to Experiment 65.

The map is not monotone: literal counterexamples are preserved. Thus adding a repair defect can change which original obligation is violated rather than merely accumulate violations.

Component 11's four-bit reversal preserves both defect-state multiplicities and the multiset of literal violation functions. This is not yet claimed as a full automorphism: Experiment 65 tests whether one fixed permutation of original obligations works across every defect state. Component 8 has no corresponding multiplicity swap symmetry.

Full-suite status is environment-bounded: targeted Experiment 63/64 tests pass, but the full suite requires the existing `/tmp/NavierStokesAndEuler/NavierStokes/R3/Theorem.lean` fixture, which may be absent.

Component 8 fails the exact 2×2 multiplicity-factorization test, so complete support does not imply independent state counts. Exact truth tables, minimal dependency supports, algebraic normal forms, and automorphism mappings are preserved.
