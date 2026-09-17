# Experiment 28 — A4 forbidden-subset lattice

All 16 forbidden subsets of the four `A4` additions were evaluated.

```text
subsets evaluated: 16
feasible:          16
infeasible:         0
exact constrained results: 15
minimal infeasible subsets: none
```

For every nonempty forbidden subset, the unique 309-member baseline gives a lower bound of 310. The recorded 310-member witness for the all-A4 case excludes every nonempty subset, so it is a universal feasible witness for all fifteen constrained cases. Therefore, with `c(S) = W*_(-S) - 309`:

```text
c(empty) = 0
c(S)     = 1 for every nonempty S
```

The empty subset retains the known unconstrained optimum 309.

Thus `A4` is not collectively feasibility-essential. Its four members are individually replaceable and jointly replaceable, although excluding any nonempty subset imposes a uniform +1 minimum-cover-width penalty in this measured candidate universe. This is a cover-size result, not a claim that exactly one declaration substitutes for each excluded declaration.

All claims are bounded to the literal elaborated set-cover representation.
