# Experiment 27 — member-wise feasibility and replacement

Experiment 27 forbids each member of the embedded 12-member I72 block and each of the four A4 additions individually.

Results:

```text
I72: 12/12 individually infeasible
A4:  0/4 individually infeasible; valid feasible witnesses have sizes 310, 311, 310, 311
```

Every I72 member has at least one original degree-1 frontier witness, and excluding any one leaves the frontier uncoverable. The A4 members have no original degree-1 witness individually; each can be excluded while retaining a feasible cover, but no 309-member witness exists because the unconstrained 309-cover is unique and contains every A4 member. Thus the 310-member witnesses are exact optima; the 311-member witnesses retain bounds of 310–311.

This distinguishes individual feasibility necessity from minimum-cover necessity. Results are limited to the literal elaborated set-cover candidate universe.
