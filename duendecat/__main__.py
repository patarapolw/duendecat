from duendecat import cli
import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    cli()
