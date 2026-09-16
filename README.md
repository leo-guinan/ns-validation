# ns-validation

A validation-architecture project for turning expensive mathematical work into progressively cheaper, more durable objects of trust.

The first case study originated in `~/Downloads/NS Validation idea.md`. That raw note is not repository-controlled and is not required for current verification; the checked-in derived ledger preserves its source hash and evidence status. This is not another attempt to solve Navier–Stokes. The initial executable slice is:

`markdown source -> conservative extraction -> JSON ledger + text report`

It extracts only explicit quantities and high-signal candidate claims, research questions, and limitation/boundary statements. It also validates a machine-readable stage graph with explicit work, exported state, verification burden, and trust assumptions. Extracted claims are not treated as facts; their initial status is `unvalidated`. The source path and SHA-256 digest make later re-runs auditable without copying the private source into this repository.

## Quickstart

From this directory:

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m ns_validation ~/Downloads/NS\ Validation\ idea.md
```

The CLI writes `data/ledger.json` and `data/report.txt`. Generated data is ignored by Git.

The committed case-study artifacts are deliberately different: `data/source-ledger.json` preserves provenance-labeled evidence records, `data/cost-estimates.json` isolates an unverified external estimate, and `data/proof-stages.json` is the explicit stage/interface hypothesis.

## Layout

- `src/ns_validation/processor.py` — pure parser, ledger model, JSON/report renderers
- `src/ns_validation/stages.py` — stage model and graph validation
- `src/ns_validation/cli.py` — command-line entry point
- `tests/` — parser, hash, serialization, and report tests
- `docs/` — research question, terminology, claims, and boundaries
- `schemas/` — machine-readable stage and evidence contracts
- `experiments/` — staged experiment specifications
- `verify.py` — one-shot real-source verification
- `data/` — ignored generated artifacts

## What this does not establish

A parsed claim is not a validated claim. This foundation does not verify the reported Navier–Stokes story, reconstruct a proof dependency graph, estimate costs, measure interface size, or establish a verification compression ratio. Those require bounded source acquisition, provenance, operational definitions, and independent readback.
