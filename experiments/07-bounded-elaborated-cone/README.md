# Experiment 07 — bounded elaborated dependency cone

Target: `NavierStokesR3.coreBreakdownStatement`.

The extractor traverses elaborated declaration types and theorem values, memoizing visited declarations. The local traversal boundary is the `NavierStokesR3` namespace. Mathlib and all other external declarations are recorded as a trust frontier and are not recursively opened.

Observed receipt:

```text
direct elaborated references: 2
project-local declarations:    892
external frontier declarations: 2450
maximum local depth:           25
r_immediate = 892 / 2:         446.0
```

`r_immediate` is descriptive only. It is not a compression ratio and does not establish minimality or sufficiency. The unbounded transitive cone remains unknown.

This boundary makes the graph modular:

```text
target → NavierStokesR3 local cone → external trust frontier
```

The source-level import graph and syntax inventory remain separate artifacts.
