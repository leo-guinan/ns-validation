# Experiment 19 — gateway necessity

Experiment 19 starts from the frontier side of each Experiment 18 entry graph. A frontier identity with degree one forces its sole neighboring marginal local declaration into every complete local cover of that frontier.

Measured bounds:

```text
ΔF=72:    forced=12, lower=12, greedy upper=12, exact=12
ΔF=2436:  forced=239, lower=240, greedy upper=304
ΔF=2508:  forced=244, lower=245, greedy upper=310
```

The two 72-frontier cases are exact by matching lower and upper bounds. The larger cases remain bounded; no exact set-cover solve was claimed. Frontier degree distributions and iterative forced reduction are retained in the receipt.

This distinguishes observed access width from necessary cover width. It does not establish semantic necessity, runtime complexity, sufficiency, or a universal interface law.
