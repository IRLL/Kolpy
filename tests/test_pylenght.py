"""Module to test that lenght of python programs are computed as expected."""

from pathlib import Path

import pytest_check as check

from kolpy.pylenght import number_of_characters


def save_as_file(program: str, filename: str, folder_path: Path) -> Path:
    filepath = folder_path / f"{filename}.py"
    filepath.write_text(program)
    return filepath


class TestPylenght:

    """Check that programs are of expected lenghts"""

    def test_empty(self, tmp_path: Path):
        """empty program should be of lenght 0."""
        prog = ""
        filepath = save_as_file(prog, "empty", tmp_path)
        check.equal(number_of_characters(filepath), 0)

    def test_assignment(self, tmp_path: Path):
        """assignment should be of lenght of line."""
        prog = "variable = 42"
        filepath = save_as_file(prog, "assignment", tmp_path)
        check.equal(number_of_characters(filepath), len(prog))
