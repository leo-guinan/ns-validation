# Experiment 10 — trust resolution stack

Experiment 10 resolves the B2 frontier through the strongest available provenance layers. The `.ilean` reference records provide a declaration’s defining module field (`c.m`); local cache paths establish source-file and compiled-artifact presence. Package pins come from the acquired checkout Git heads.

Observed counts:

```text
semantic frontier declarations: 2450
module-resolved declarations:   2221
unknown declarations:           229
distinct source modules:         468
distinct source files:           413
distinct compiled artifacts:     413
package classes:                 3
```

Package pins:

```text
mathlib:    85e3a25e006c35636f0e53b0e9296caca2685bc0
Comparator: 19e111e2141cf333c7daff0f64c5f24acc91dd2e
```

The three package classes include `mathlib`, `Comparator`, and `lean-toolchain`. Root trust, artifact signatures, and independent artifact provenance remain unknown.

These are resolution counts, not compression ratios. Semantic declaration breadth and operational artifact breadth are separate measurements.
