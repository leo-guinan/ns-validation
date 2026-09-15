# Experiment 05 — verification activation amortization

Target: `NavierStokes.R3.Theorem`.

The same target was run under two declared conditions:

- `cold`: `.lake` removed before the run.
- `warm_preserved_after_cold`: the partial environment from the cold run was retained.

Both runs received a 180-second budget. Neither produced `Theorem.olean`; the warm condition therefore was not a usable compiled environment. It continued materializing Mathlib rather than checking the target theorem.

Observed receipt:

```text
cold: 180.637s, lake +2,601,805,024 bytes, target .olean=no
warm: 180.763s, lake +1,134,811,480 bytes, target .olean=no
```

`activation_ratio` is intentionally null. These are incomplete activation runs, not comparable cold/warm theorem-check times. No declaration cone or recheck cost is reported.

Re-run with:

```text
python3 scripts/measure_activation.py /path/to/NavierStokesAndEuler data/activation-experiment.json
```

The script preserves the source checkout and deletes only `.lake` before the cold condition.
