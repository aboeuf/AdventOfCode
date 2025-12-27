#!/usr/bin/python3

import argparse
from importlib import import_module
import os
import subprocess
import sys

THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
SCRIPTS_DIR = os.path.join(THIS_DIR, "scripts")
VENV_DIR = os.path.join(THIS_DIR, "venv")
BIN_DIR = os.path.join(VENV_DIR, "bin")


def parse_commands():
    commands = {}
    for filename in os.listdir(SCRIPTS_DIR):
        filepath = os.path.join(SCRIPTS_DIR, filename)
        if os.path.isfile(filepath) and filename.endswith(".py"):
            modname = filename[:-3]
            module = import_module(f"scripts.{modname}")
            if module.__file__ != filepath:
                raise Exception(
                    f'unexpected module path "{module.__file__}" (expected "{filepath}")'
                )
            commands[modname] = module.PARSER_ARGS
            commands[modname]["filepath"] = filepath
    return commands


def main():
    prog_name = sys.argv[0].split("/")[-1]

    parser = argparse.ArgumentParser(prog=prog_name)
    subparsers = parser.add_subparsers(required=True, dest="command")
    commands = parse_commands()
    for command in sorted(commands.keys()):
        subparser = subparsers.add_parser(command, help=commands[command]["help"])
        if "args" in commands[command]:
            for name, kwargs in commands[command]["args"]:
                subparser.add_argument(name, **kwargs)

    arguments = vars(parser.parse_args())

    if arguments["command"] in ["configure", "qtfiles"]:
        py_binary = "python3"
    else:
        if not os.path.isdir(VENV_DIR) or not os.path.isdir(BIN_DIR):
            print("Cannot find virtual environment.")
            print(f'Please first run "{prog_name} configure" and try again.')
            return
        py_binary = os.path.join(BIN_DIR, "python3")

    command_list = [py_binary, commands[arguments["command"]]["filepath"]]
    command_list.extend(sys.argv[2:])

    subprocess.run(command_list)


if __name__ == "__main__":
    main()
