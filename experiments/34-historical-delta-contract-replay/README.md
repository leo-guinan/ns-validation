# Experiment 34 — historical delta contract replay

The historical extractor from commit `b6f089b` was run against the pinned Lean checkout. It timed out after 330 seconds, emitting only 2 of the 6 requested node sections. The resulting partial stream is preserved by hash but is not treated as the historical optimization contract.

```text
historical_contract_replay = unavailable_under_current_budget
nodes emitted: 2/6
external edges emitted: 170254
```

The exact candidate, frontier, edge, objective, and constraint hashes are therefore null. This is not a claim of irrecoverability: the contract was not reproduced under the current budget. No replay of `Jfull` and no falsification or confirmation of historical delta uniqueness is claimed.

The reusable `ns_validation.optimization_contract.contract_fingerprint` utility hashes canonicalized `L`, `F`, `E`, `O`, and `K` components and combines them into `H_contract` for future optimization receipts.
