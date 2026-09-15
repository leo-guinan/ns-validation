# Experiment 06 — verification environment transfer

The project supports `lake exe cache get`. Using the pinned checkout and Lean toolchain, acquisition succeeded before target elaboration.

Receipt:

```text
acquire:    27s, 8747 files downloaded, 8475 decompressed, +5,283,278,848 bytes
elaborate:  446s, target .olean=yes, +2,046,189,568 bytes
recheck:    5s, target .olean=yes, +0 bytes
```

The target was `NavierStokesR3.coreBreakdownStatement`. Lean-level direct extraction from the elaborated `ConstantInfo` type and theorem value found exactly two constants:

```text
NavierStokesR3.candidateStatement
NavierStokesR3.ProblemStatement.coreBreakdownStatement
```

The recursive transitive walk exceeded its 300-second budget while traversing proof terms. Therefore the transitive cone remains null. The direct count is real; the cone count is not available.

This separates:

```text
E: acquired compiled environment
C_direct: elaborated constants directly referenced by d
C_transitive: not yet measured
I: not yet measured
```

No activation ratio is computed. The cold and warm conditions from Experiment 05 were both incomplete and are not compared to this successful transferred-environment run as equivalent operations.
