"""Module to test that bycode complexity of python programs behave as expected."""

import pytest_check as check

from kolpy.bytecode import bytecode_lenght


def test_assignment():
    """An assignment should have a bytecode lenght of 4 = 2 LOAD + 1 STORE + 1 RETURN"""

    script = "variable = 42"
    check.equal(bytecode_lenght(script), 4)
