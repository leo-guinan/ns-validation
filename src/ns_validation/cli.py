from __future__ import annotations

import argparse
from pathlib import Path

from .processor import parse_markdown, render_report, write_json


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Process a validation-idea markdown file")
    parser.add_argument("source", type=Path)
    parser.add_argument("--json", type=Path, default=Path("data/ledger.json"))
    parser.add_argument("--report", type=Path, default=Path("data/report.txt"))
    args = parser.parse_args(argv)

    ledger = parse_markdown(args.source)
    json_path = write_json(ledger, args.json)
    report_path = args.report.expanduser().resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(ledger), encoding="utf-8")
    print(f"claims={len(ledger.claims)} metrics={len(ledger.metrics)} questions={len(ledger.research_questions)}")
    print(f"wrote {json_path}")
    print(f"wrote {report_path}")


if __name__ == "__main__":
    main()
