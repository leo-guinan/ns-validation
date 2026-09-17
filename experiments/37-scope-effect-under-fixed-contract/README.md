# Experiment 37 — scope effect under a fixed contract

The current target graph defines one shared candidate universe of 915 locals and one shared edge relation of 89,216 edges. The objective is minimum-cardinality binary set cover with at-least-one coverage constraints.

Two contracts differ only in required frontier scope:

```text
full:       2522 frontier identities, 309 minimum width
B→T delta:  2508 frontier identities, 309 minimum width
```

The candidate, objective, and constraint hashes are equal across contracts. The delta edge relation is the literal restriction of the full edge relation.

Both known width-309 witnesses are admissible and cover both scopes:

```text
I2508: full 2522/2522, delta 2508/2508
Jfull: full 2522/2522, delta 2508/2508
```

Therefore changing only required frontier scope from 2,522 to 2,508 does not restore uniqueness. The result is current-contract-relative; no historical uniqueness claim is transferred.
