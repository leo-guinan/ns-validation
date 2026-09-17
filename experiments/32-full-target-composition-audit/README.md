# Experiment 32 — full-target composition audit

The reconciled target frontier is 2,522 declarations, with an exact nested filtration:

```text
F_B size: 14
F_A size: 2450
F_T size: 2522
B → A delta: 2436
A → T delta: 72
B → T delta: 2508
```

The two delta interfaces compose at the responsibility level:

```text
I2436 size: 302; I72 size: 12; union size: 314
I2436 ∪ I72 covers all 2522 target identities
```

The recorded 309-member `I2508` interface also covers all 2522 target identities. An independent binary MILP on the full target graph found a 309-member optimum. Thus the measured composition overhead is `314 - 309 = 5` declarations.

The full-target MILP witness differs from the recorded delta optimum by one identity, so unique-optimum status is not re-established under the full-target contract. Delta-interface uniqueness and full-target uniqueness remain separate questions.

All results are contract-specific set-cover measurements; no semantic sufficiency or cross-contract identity is inferred.
