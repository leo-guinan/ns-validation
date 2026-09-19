# Experiment 63 — compatibility defect space

Using each component's unique minimum repair set as Boolean coordinates, every exact-one reconstruction receives a defect vector with one bit per violated original coverage obligation.

Results:

```text
component  repair dimension  nonzero states  all realized  defect→violation signature
8               2                 3             yes                    yes
11              4                15             yes                    yes
```

In both components:

```text
defect vector 000...0 = exactly Opt
```

Every nonzero Boolean defect state occurs. Equal defect vectors determine equal complete original-obligation violation signatures. Exact multiplicities and literal examples are preserved.

Repair dimension is scoped to Boolean coordinates indexed by original coverage obligations. It is not a general encoding-size, semantic-complexity, or failure-probability claim.
