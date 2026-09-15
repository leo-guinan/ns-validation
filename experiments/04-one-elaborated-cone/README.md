# Experiment 04 — one elaborated dependency cone

Target: `NavierStokesR3.coreBreakdownStatement` in `NavierStokes.R3.Theorem`.

The bounded attempt was:

```text
lake build NavierStokes.R3.Theorem
```

It timed out after 600 seconds with exit code 124 and produced no target `.olean`. Lean began materializing the transitive Mathlib environment; the disposable `.lake` state reached 4,013,350,912 bytes. The attempt therefore stopped before an elaborated declaration environment existed.

This is recorded as `blocked_before_elaboration`, not as a theorem cone. Import closure, source-token inventory, and elaborated dependency cone remain separate objects. The exact blocker and smallest required source boundary are in `data/elaborated-cone.json`.

The next implementation target is a smaller compilable declaration boundary or a reusable prebuilt environment. No direct/transitive counts or axiom claims are made here.
