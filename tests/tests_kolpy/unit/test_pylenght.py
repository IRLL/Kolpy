"""Module to test that lenght of python programs are computed as expected."""

from pathlib import Path

import pytest_check as check

from kolpy.pylenght import pylenght


def save_as_file(program: str, filename: str, folder_path: Path) -> Path:
    filepath = folder_path / f"{filename}.py"
    filepath.write_text(program)
    return filepath


def test_pylenght(tmp_path: Path):
    """Check that programs are of expected lenghts"""
    prog = ""
    filepath = save_as_file(prog, "empty", tmp_path)
    check.equal(pylenght(filepath), 0)
