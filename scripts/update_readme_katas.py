"""Regenerate the katas count badge and table in README.md between marker comments."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


def count_katas() -> dict[str, int]:
    counts = {}
    for kyu_dir in sorted(ROOT.glob("*-kyu"), key=lambda p: int(p.name.split("-")[0])):
        counts[kyu_dir.name] = len(list(kyu_dir.glob("*.py")))
    return counts


def render_badge(total: int) -> str:
    return f"![Katas](https://img.shields.io/badge/katas-{total}-blue)"


def render_table(counts: dict[str, int]) -> str:
    lines = ["| Nivel | Katas resueltos |", "| ----- | :-------------: |"]
    for name, count in counts.items():
        label = name.replace("-", " ")
        lines.append(f"| {label} | {count} |")
    return "\n".join(lines)


def replace_between(text: str, marker: str, replacement: str) -> str:
    pattern = re.compile(rf"(<!-- {marker} -->\n).*(\n<!-- /{marker} -->)", re.DOTALL)
    return pattern.sub(lambda m: f"{m.group(1)}{replacement}{m.group(2)}", text)


def main() -> None:
    counts = count_katas()
    total = sum(counts.values())

    text = README.read_text(encoding="utf-8")
    text = replace_between(text, "KATAS-BADGE", render_badge(total))
    text = replace_between(text, "KATAS-TABLE", render_table(counts))
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
