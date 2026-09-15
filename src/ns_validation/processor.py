"""Parse validation-idea markdown into a conservative, auditable ledger."""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Metric:
    name: str
    value: str
    context: str
    line: int


@dataclass(frozen=True)
class Claim:
    text: str
    line: int
    status: str = "unvalidated"
    falsifier: str = ""


@dataclass(frozen=True)
class ValidationLedger:
    source: str
    source_sha256: str
    claims: list[Claim]
    metrics: list[Metric]
    research_questions: list[str]
    boundaries: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


def _sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _lines(text: str) -> Iterable[tuple[int, str]]:
    yield from enumerate(text.splitlines(), start=1)


def _clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\\+|(?:text|textbf|boxed)\{", "", text)
    text = text.replace("}", "").strip()
    for separator in (". ", "? "):
        if separator in text:
            prefix, suffix = text.rsplit(separator, 1)
            if prefix.rstrip(".?") == suffix.rstrip(".?"):
                return prefix.rstrip(".?") + separator[0]
    return text


def _is_claim(line: str) -> bool:
    lower = line.lower()
    markers = ("hard global construction", "more expensive discovery", "different stages of truth production", "civilization advances")
    return any(marker in lower for marker in markers)


def parse_markdown(path: str | Path) -> ValidationLedger:
    """Extract high-signal observations without pretending they are validated."""
    source_path = Path(path).expanduser().resolve()
    text = source_path.read_text(encoding="utf-8")
    claims: list[Claim] = []
    metrics: list[Metric] = []
    questions: list[str] = []
    boundaries: list[str] = []

    for line_no, raw in _lines(text):
        # Markdown image references can contain megabytes of base64 payload.
        # They are presentation data, not validation evidence.
        if "data:image/" in raw:
            continue
        line = _clean(raw)
        if not line:
            continue
        if line.endswith("?") or line.startswith("How much information"):
            questions.append(line)
        if _is_claim(line):
            claims.append(Claim(text=line, line=line_no))
        if re.search(r"does\s+\**not|would\s+\**not|not\s+establish", line.lower()):
            boundaries.append(line)

        # Deliberately narrow extraction: only explicit number + unit statements.
        for match in re.finditer(r"(?P<value>\$?[\d,.]+(?:–[\d,.]+)?\s*(?:million|billion|hours?|agents?|messages?|tokens?|responses?|deltas?|magnitudes?|bit(?:s)?))", line, re.I):
            if match.start() and line[match.start() - 1] == ".":
                continue
            metrics.append(Metric(name="explicit_quantity", value=match.group("value"), context=line, line=line_no))

    metrics = list(dict.fromkeys(metrics))
    questions = list(dict.fromkeys(questions))

    return ValidationLedger(
        source=str(source_path),
        source_sha256=_sha256(source_path),
        claims=claims,
        metrics=metrics,
        research_questions=questions,
        boundaries=boundaries,
    )


def write_json(ledger: ValidationLedger, destination: str | Path) -> Path:
    output = Path(destination).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(ledger.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output


def render_report(ledger: ValidationLedger) -> str:
    lines = [
        "Validation ideas report",
        f"Source: {ledger.source}",
        f"Source SHA-256: {ledger.source_sha256}",
        "",
        f"Claims (unvalidated): {len(ledger.claims)}",
    ]
    lines.extend(f"- {claim.text} [line {claim.line}]" for claim in ledger.claims)
    lines.extend(["", f"Explicit quantities: {len(ledger.metrics)}"])
    lines.extend(f"- {metric.value} [line {metric.line}]" for metric in ledger.metrics)
    lines.extend(["", f"Research questions: {len(ledger.research_questions)}"])
    lines.extend(f"- {question}" for question in ledger.research_questions)
    lines.extend(["", f"Boundaries/residuals: {len(ledger.boundaries)}"])
    lines.extend(f"- {boundary}" for boundary in ledger.boundaries)
    return "\n".join(lines) + "\n"
