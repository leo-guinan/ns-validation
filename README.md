# ns-validation

A small, source-hashed processor for turning validation ideas into a falsifiable working ledger.

This repository starts with the smallest credible slice from `~/Downloads/NS Validation idea.md`:

`markdown source -> conservative extraction -> JSON ledger + text report`

It extracts only explicit quantities and high-signal candidate claims, research questions, and limitation/boundary statements. Extracted claims are not treated as facts; their initial status is `unvalidated`. The source path and SHA-256 digest make later re-runs auditable without copying the private source into this repository.

## Quickstart

From this directory:

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m ns_validation ~/Downloads/NS\ Validation\ idea.md
```

The CLI writes `data/ledger.json` and `data/report.txt`. Generated data is ignored by Git.

## Layout

- `src/ns_validation/processor.py` — pure parser, ledger model, JSON/report renderers
- `src/ns_validation/cli.py` — command-line entry point
- `tests/` — parser, hash, serialization, and report tests
- `verify.py` — one-shot real-source verification
- `data/` — ignored generated artifacts

## What this does not establish

A parsed claim is not a validated claim. This foundation does not verify the reported Navier–Stokes story, reconstruct a proof dependency graph, estimate costs, measure interface size, or establish a verification compression ratio. Those require bounded source acquisition, provenance, operational definitions, and independent readback.
