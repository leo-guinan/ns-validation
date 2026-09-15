from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from ns_validation import parse_markdown, render_report, write_json

source = Path.home() / "Downloads" / "NS Validation idea.md"
if not source.exists():
    raise SystemExit(f"required source not found: {source}")
ledger = parse_markdown(source)
json_path = write_json(ledger, Path("data") / "ledger.json")
report_path = Path("data") / "report.txt"
report_path.write_text(render_report(ledger), encoding="utf-8")
print(f"source={ledger.source}")
print(f"sha256={ledger.source_sha256}")
print(f"claims={len(ledger.claims)} metrics={len(ledger.metrics)} questions={len(ledger.research_questions)} boundaries={len(ledger.boundaries)}")
print(f"json={json_path} bytes={json_path.stat().st_size}")
print(f"report={report_path.resolve()} bytes={report_path.stat().st_size}")
