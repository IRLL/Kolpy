"""Module to test that bycode complexity of python programs behave as expected."""

import pytest_check as check

from kolpy.bytecode import bytecode_complexity


def test_assignment():
    """An assignment should have a complexity of 1"""

    script = """
    variable = 42    
    """
    check.equal(bytecode_complexity(script), 1)
