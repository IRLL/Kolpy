"""Module to compute bytecode lenght of any python file."""

import dis


def bytecode_lenght(script):
    """Compute the number of instructions in the bytecode of a given script."""
    return len(list(dis.get_instructions(script)))
