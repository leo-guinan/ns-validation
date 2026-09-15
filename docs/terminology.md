# Terminology

| Term | Operational meaning in this repository |
|---|---|
| Work | A source-labeled quantity of effort, compute, time, or cost. |
| State exported | The artifact or interface intentionally handed to the next stage. |
| Verification burden | Work required to check the exported artifact under a named procedure. |
| Trust assumptions | People, software, sources, models, or environments trusted at that boundary. |
| Interface size | Initially bytes, tokens, nodes, or explicit fields; not intrinsic information. |
| Verification compression | `rho_V = C_construct / C_reverify`. A project metric, not a universal law. |
| Interface compression | `rho_I(A->B) = size(S_A) / size(I_A->B)`. The size measure must be declared. |
| Reuse break-even | `N* = C_new_verifier / (C_old_check - C_new_check)`. Defined only when the denominator is positive. |
| Provenance label | `reported`, `derived`, `estimated`, or `modeled`; labels are not interchangeable. |
| Evidence boundary | What a source or experiment actually establishes, including known omissions. |

## Prohibited shortcuts

- Do not treat an external estimate as an official report.
- Do not infer verification success from a zero exit code or a generated file.
- Do not call synthetic fixture output empirical evidence.
- Do not call a small representation sufficient until an explicit continuation/verification test supports it.
