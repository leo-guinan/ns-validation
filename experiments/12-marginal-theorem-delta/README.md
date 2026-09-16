# Experiment 12 — marginal theorem delta

For

```text
A = NavierStokesR3.theorem_1_1_with_initial_rest
B = NavierStokesR3.theorem_1_1
```

the exact bounded support comparison is:

```text
A: 3336 declarations
B: 3338 declarations
A \ B: 0
B \ A: 2
A ⊂ B: yes
```

The marginal declarations are:

```text
NavierStokesR3.ProblemStatement.breakdownStatement
NavierStokesR3.theorem_1_1
```

The final theorem directly references both `theorem_1_1_with_initial_rest` and `breakdownStatement`. The external frontier delta is zero; the observed delta is project-local.

Warm cached checks recorded zero bytes changed:

```text
module recheck:        4.312 s
initial-rest #check:  45.176 s
final theorem #check: 21.150 s
```

These are module/interface-check measurements, not isolated theorem compilation costs. The receipt does not call the two-declaration delta minimal, sufficient, or a compression ratio.

The measurement script requires an explicit Lean checkout root, for example:

```text
python3 scripts/measure_marginal_checks.py /tmp/NavierStokesAndEuler
```
