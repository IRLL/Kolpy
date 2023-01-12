"""Module to test that bycode complexity of python programs behave as expected."""

import pytest_check as check

from kolpy.bytecode import bytecode_lenght


def test_assignment():
    """A simple assignment should have expected bytecode lenght"""

    script = "variable = 42"
    check.equal(bytecode_lenght(script), 181)


def test_function():
    """A function should have the complexity of its content."""

    def myfunc(x, y):
        return (2 * x + y) == 0

    prog = "(2 * x + y) == 0"
    check.equal(bytecode_lenght(myfunc), bytecode_lenght(prog))
