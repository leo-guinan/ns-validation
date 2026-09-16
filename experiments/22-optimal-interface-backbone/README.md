# Experiment 22 — optimal interface backbone

Experiment 22 enumerates minimum covers independently inside every reduced residual component. It classifies residual candidates as present in every optimum, some optima, or no optimum, and multiplies component cover counts because components are disconnected.

Measured result:

```text
ΔF=72:    exact total cover=12, optimal interfaces=1
ΔF=2436:  exact total cover=302, optimal interfaces=1, residual backbone=63
ΔF=2508:  exact total cover=309, optimal interfaces=1, residual backbone=65
```

All reduced residual components have exactly one optimum. Thus the residual choices are rigid in this measured representation: the 63 or 65 residual locals are all in every optimum. This does not establish semantic necessity; it establishes identity rigidity of the minimum set cover under the fixed elaborated bipartite contract.

The receipt compares repeated color-refinement signatures without treating them as graph-isomorphism certificates.
