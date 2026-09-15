# Experiment 02 — proof-interface graph

Status: outline-only. Experiment 01 remains frozen.

This graph changes levels. The lifecycle graph describes how a result was produced; this graph describes how a reported mathematical construction is said to compose.

The current graph is transcribed from the OpenAI public announcement and a public proof-outline discussion. It is not a reconstruction of the complete proof: the complete 166-page artifact was not available to this run. Two identical local PDFs were checked and rejected as unrelated 2-page “Chronoflux” documents.

Each node records `P_i = (assumptions, internal construction, exported object, validation condition)`. Each edge records the literal interface described by the outline. No edge is labeled minimal or sufficient. Interface compression is deliberately not calculated.

Run:

```text
python3 verify.py
python3 -m unittest discover -s tests -v
```

Next gate: acquire the complete proof and formalization, pin versions/hashes, then replace outline references with section/page/theorem spans. Only after that should candidate sufficient interfaces be proposed.
