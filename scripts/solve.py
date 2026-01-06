import os
import sys

THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
BINDINGS_DIR = os.path.join(PROJECT_DIR, "build/cpp_solvers")
PY_SOLVERS_DIR = os.path.join(PROJECT_DIR, "py_solvers")

if BINDINGS_DIR not in sys.path:
    sys.path.append(BINDINGS_DIR)

if PY_SOLVERS_DIR not in sys.path:
    sys.path.append(PY_SOLVERS_DIR)

import aoc
import argparse
import shutil
from solvers import Solvers
import subprocess


PARSER_ARGS = {
    "help": "Solve a specific puzzle without running the GUI.",
    "args": [
        (
            "solver",
            {
                "choices": ["cpp", "python"],
                "help": "The solver to use (either C++ or Python)",
            },
        ),
        (
            "year",
            {
                "type": int,
                "help": "The year of the event of the puzzle to solve.",
            },
        ),
        (
            "day",
            {
                "type": int,
                "help": "The release day of the puzzle to solve.",
            },
        ),
        (
            "input",
            {
                "type": str,
                "help": "The path to the input file.",
            },
        ),
    ],
}


def solve(solver: str, year: int, day: int, input_str: str) -> None:
    if solver == "cpp":
        if aoc.has_solver(year, day):
            return aoc.solve(year, day, input_str)
        print(f"Cannot find C++ solver for year {year} day {day}")
        return

    if solver == "python":
        solvers = Solvers()
        if solvers.has(year, day):
            return solvers.solve(year, day, input_str)
        print(f"Cannot find Python solver for year {year} day {day}")
        return

    print(f"Unknown solver {solver}")


def main() -> None:
    prog_name = sys.argv[0].split("/")[-1]
    parser = argparse.ArgumentParser(prog=prog_name, description=PARSER_ARGS["help"])
    for name, kwargs in PARSER_ARGS["args"]:
        parser.add_argument(name, **kwargs)

    arguments = parser.parse_args()

    with open(arguments.input, "r") as file:
        input_str = file.read()

    result = solve(arguments.solver, arguments.year, arguments.day, input_str)

    if result is None:
        print("No result")
    else:
        print(result)
        if not result.success:
            for line in result.output():
                print(line)


if __name__ == "__main__":
    main()
