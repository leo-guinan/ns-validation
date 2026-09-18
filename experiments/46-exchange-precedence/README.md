# Experiment 46 — exchange precedence

For every ordered pair of local optima, shortest exchange paths were oriented toward the target by decreasing replacement distance. The receipt stores exact geodesic counts, immediately removable endpoint differences, and earliest removal steps.

```text
ordered local optimum pairs:          1964
pairs with precedence constraints:      34
maximum precedence depth:                3
all geodesic steps distance-decreasing: yes
```

The component-9 counterexample has direct distance 2 and one geodesic. `LocalizedFluxEstimates.weightSecondDerivativeConstant` must be removed first; `ComparisonCutoffs.baseCutoff_iteratedFDeriv_le` cannot be removed until step 2. This is precedence without exchange detour.

The receipt preserves both remove→add pairs and SHA-256 hashes for the source, intermediate, and target states. Precedence depth is defined literally as `r(S,T,x) = min{k >= 1: some S-to-T geodesic removes x at step k}`.

These are current-contract reconfiguration-order measurements, not semantic causality.
