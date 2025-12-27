import argparse
from importlib import import_module
import os
import sys

PARSER_ARGS = {
    "help": "Run the GUI.",
}

THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))

if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)


def main():
    prog_name = sys.argv[0].split("/")[-1]
    parser = argparse.ArgumentParser(prog=prog_name, description=PARSER_ARGS["help"])
    parser.parse_args()
    gui_main = import_module("gui.main")
    gui_main.main()


if __name__ == "__main__":
    main()
