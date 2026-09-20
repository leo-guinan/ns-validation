# Experiment 70 — minimum direct observability

This experiment restricts observation to selected raw original-obligation violation bits, rather than arbitrary XOR combinations.

```text
component  latent r  minimum raw observations  minimum sets  inverse class
8              2              3                    1          linear
11             4             15                    1          linear
```

The inverse decoder extends to a linear map on the ambient raw-observation space, and therefore is affine as well. The component-8 minimum interface is the complete three-predicate family. Component 11 requires all fifteen violation coordinates for direct injectivity, despite its four-bit latent state. Exact projection images, inverse maps, decoder classifications, support/backbone, and reversal orbits are preserved.

This is direct raw-coordinate observability under the fixed contract; it is distinct from the linear decoder using arbitrary XOR combinations of all observations and makes no semantic observability claim.
