from importlib import import_module
import os
import sys

THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
BINDINGS_DIR = os.path.join(PROJECT_DIR, "build/cpp_solvers")

if BINDINGS_DIR not in sys.path:
    sys.path.append(BINDINGS_DIR)


import aoc
import re


class Solvers(dict):
    def __init__(self):
        super().__init__()
        for dir_name in os.listdir(THIS_DIR):
            if not dir_name.isdigit():
                continue
            dir_path = os.path.join(THIS_DIR, dir_name)
            if not os.path.isdir(dir_path):
                continue
            year = int(dir_name)
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if not os.path.isfile(file_path):
                    continue
                m = re.fullmatch("^aoc_solver_(\\d+)_(\\d+).py$", file_name)
                if m is None:
                    continue
                if dir_name != m.group(1):
                    print(
                        f"warning: year missmatch between directory name ({dir_name}) and file name ({m.group(1)}): file '{file_name}' ignored"
                    )
                    continue
                if dir_path not in sys.path:
                    sys.path.append(dir_path)
                if year not in self:
                    self[year] = {}
                day = int(m.group(2))
                module = import_module(file_name[:-3])
                self[year][day] = module.solve

    def has(self, year, day):
        return year in self and day in self[year]

    def solve(self, year, day, input_str):
        if not self.has(year, day):
            return aoc.Result(f"Cannot find Python solver for year {year} day {day}")
        return aoc.Result(self[year][day](input_str))
