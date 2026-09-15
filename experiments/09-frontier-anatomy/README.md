# Experiment 09 — frontier anatomy

Experiment 09 analyzes the B2 bounded elaborated cone for `NavierStokesR3.coreBreakdownStatement`.

The bipartite graph contains:

```text
892 local declarations
2450 external frontier declarations
85179 local→frontier edges
```

An edge means a local elaborated declaration directly references an external elaborated constant. Frontier multiplicity is the number of local declarations referencing each external declaration.

Reuse and coverage:

```text
top 10 frontier declarations: 7415 edges
top 50:                      26103 edges
50% edge coverage:           107 frontier declarations
90% edge coverage:           537
99% edge coverage:           1681
```

Defining source modules are not exposed by the extracted `ConstantInfo`, so module and namespace groupings are explicitly name-prefix proxies. They are not claims about defining modules or independently acquired artifacts.

The result does not identify a minimal, sufficient, or optimal trust interface. Declaration trust, module-proxy grouping, package-root proxy, artifact identity, and root assumptions remain separate surfaces.
