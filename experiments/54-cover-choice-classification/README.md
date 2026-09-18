# Experiment 54 — cover saving versus cover choice

Cover saving and cover multiplicity are separate.

```text
positive-saving kernel components: 5
kernel cover saving:               12
residual minimum width:            130
residual cover backbone:             4 worlds
residual cover support:           1856 worlds
```

Component classification:

```text
                         M=1   M>1
no saving (s=0):           0    120
saving (s>0):              3      2
```

All five kernel components save cover width; two have multiple optima and three have unique optima. The 120 zero-saving components are width-1, one-coordinate components with multiple interchangeable candidate worlds. The complete per-component table preserves coordinate count, candidate-world count, width, saving, multiplicity, backbone, support, and the kernel label. The exact global residual multiplicity is the product of component multiplicities. Removal/addition component correspondence under path reversal is verified exactly.

The exact residual partition is:

```text
4 backbone worlds + 1852 optional-optimal worlds + 50 never-optimal worlds = 1906 residual candidates
62 full backbone worlds + 1852 optional-optimal worlds + 50 never-optimal worlds = 1964 full worlds
```

All 50 never-optimal residual worlds lie in the five-component saving kernel. The residual multiplicity factorizes as `43296` from the kernel and the preserved zero-saving substitution factor.

These are incidence/set-cover properties only.
