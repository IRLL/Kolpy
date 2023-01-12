"""Module to compute simple lenght of any python file."""

from pathlib import Path


def number_of_characters(path: Path) -> int:
    path = Path(path)
    return len(path.read_text(encoding="utf-8"))
