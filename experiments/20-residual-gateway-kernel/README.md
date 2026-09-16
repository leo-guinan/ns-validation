# Experiment 20 — residual gateway kernel

Experiment 20 removes forced local declarations and the frontier identities they cover, then applies safe neighborhood-dominance reduction and connected-component decomposition.

Results:

```text
ΔF=72:    forced=12, β=1.000, residual=0, total bounds 12–12
ΔF=2436:  forced=239, β≈0.948, residual frontier=126, candidates=65, total bounds 293–304
ΔF=2508:  forced=244, β≈0.945, residual frontier=139, candidates=69, total bounds 297–313
```

The residual graphs split into many disconnected components. The residual lower bound counts one local per nonempty component; the upper bound retains all reduced candidates. A bitset branch-and-bound attempt on the large residual was stopped by the execution budget before an exact result was obtained, so no exact large-case minimum is claimed.

The 72-frontier cases are fully covered by forced locals and remain exact at 12. The larger cases show that forced specialized responsibilities explain most frontier identities, while a smaller residual kernel remains unresolved.
