# Experiment 18 — entry-interface anatomy

Experiment 18 builds a bipartite graph for each of the six frontier-expanding transitions:

```text
marginal local declaration l → new frontier declaration f
```

An edge exists only when the elaborated direct references contain that pair. Local access width is the number of marginal local declarations with at least one edge into `ΔF`; it is kept distinct from `|ΔF|`.

Observed access widths:

```text
72-frontier expansions:     14 / 14 active local declarations
2436-frontier expansions:   875–876 active local declarations
2508-frontier expansion:    902 active local declarations
```

Degree-ranked coverage is descriptive. The 72-frontier graphs reach 90% coverage with 6 active local declarations. The 2436-frontier graphs require 312 active declarations for 90%; the 2508-frontier graph requires 325. The 100% prefixes are not exact set-cover minima.

The result is mixed: medium expansions have narrow access width, while the large expansions are broadly distributed across marginal local declarations. This does not establish interface complexity, runtime complexity, minimality, or sufficiency.
