# Experiment 30 — minimum-churn 310-cover

A binary MILP minimized identity churn among exact 310-member covers of `F2508` excluding all four `A4` declarations.

```text
Dmin:                 9
removed from I*:      4
added outside I*:     5
collateral removals:  0
I72 preserved:        yes
```

The four removals are exactly `A4`; the five additions form a localized 4-for-5 realization. This proves `9 ≤ Dmin ≤ 9`, hence `Dmin = 9`. The earlier greedy `J310` remains a valid but non-minimum-churn witness with 37 removals and 38 additions.

The complete width-310 cover family remains unenumerated. All results are literal set-cover measurements, not semantic substitution or causal transfer.
