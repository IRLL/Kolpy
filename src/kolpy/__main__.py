"""Entry module of the package.

You can run this script using:
python -m kolpy

"""

import kolpy
import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser of the Kolpy package."""
    parser = argparse.ArgumentParser(
        description="Compute upper bounds of kolmogorov complexity of a python code",
    )
    return parser


def main() -> None:
    """Entry point of the package"""
    parser = build_parser()
    print(f"Hello world from {parser.prog.capitalize()} ({parser.description})")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
