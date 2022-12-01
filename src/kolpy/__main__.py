"""Entry module of the package.

You can run this script using:
python -m kolpy

"""

import kolpy
import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser of the Kolpy package."""
    parser = argparse.ArgumentParser(
        prog=kolpy.__name__,
        description=kolpy.__doc__,
    )
    return parser


def main() -> None:
    """Entry point of the package"""
    print(f"Hello world from {kolpy.__name__.capitalize()} ({kolpy.__doc__})")
    parser = build_parser()
    args = parser.parse_args()


if __name__ == "__main__":
    main()
