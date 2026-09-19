# Experiment 62 — minimum compatibility repair

Components 8 and 11 are repaired by restoring the smallest subsets of original coverage obligations to the exact-one interface.

```text
component 8:  minimum repair size 2; one minimum repair set
component 11: minimum repair size 4; one minimum repair set
```

The repaired reconstructed families equal the true optimum families. False-positive violation signatures, repair backbones/supports, all minimum repair sets, and literal same-membership-signature substitution witnesses are preserved.

A same-signature witness has the form:

```text
same exact-one membership signature
+ valid optimum with world a
+ invalid replacement with world b
```

Repairs restore original finite coverage obligations. This is a contract-sufficiency result, not a semantic compression claim.
