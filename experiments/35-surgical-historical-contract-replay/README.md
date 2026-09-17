# Experiment 35 — surgical historical contract replay

The unchanged historical extractor from `b6f089b` was run separately for the source-B and target declarations. Both completed successfully. The target produced 915 local declarations, 2,522 frontier identities, and 89,216 external edges; the source produced 6 locals, 14 frontier identities, and 17 edges. Their literal target-only frontier delta is exactly 2,508 with no source-only identities.

An independent-node falsifier also passed: `theorem_1_1_with_initial_rest` extracted in isolation matched its six-node-prefix local, frontier, and edge sets exactly.

The historical optimization contract remains unavailable. Three counts are kept separate: 909 raw regenerated target-minus-source locals; 882 historically reported optimization candidates; and 741 later reconstructed/inferred delta locals from Experiment 33. Their equality is not assumed. The 909→882 gap is 27, while the 882→741 gap is 141; the filtering/reduction stages, objective, and constraint configuration were not preserved sufficiently for exact reconstruction. `Jfull` was therefore not replayed against an inferred contract.

This establishes exact node extraction, not historical delta uniqueness or its falsification.
