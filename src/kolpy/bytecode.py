"""Module to compute bytecode lenght of any python file."""

import dis


def bytecode_lenght(script):
    """Compute the bytecode lenght of a given script."""
    return len(dis.Bytecode(script).dis())
