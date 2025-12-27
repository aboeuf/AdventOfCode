import argparse
import os
import shutil
import subprocess
import sys

ACTIONS = ["clear", "install", "cpp", "ui"]

PARSER_ARGS = {
    "help": "Bootstrap the project (install dependencies, run CMake and compile the C++ solvers).",
    "args": [
        (
            "action",
            {
                "choices": ACTIONS,
                "nargs": "?",
                "help": "The specific action to perform (all by default).",
            },
        ),
    ],
}

THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
BUILD_DIR = os.path.join(PROJECT_DIR, "build")
UI_DIR = os.path.join(PROJECT_DIR, "gui/ui")


def main():
    prog_name = sys.argv[0].split("/")[-1]
    parser = argparse.ArgumentParser(prog=prog_name, description=PARSER_ARGS["help"])
    for name, kwargs in PARSER_ARGS["args"]:
        parser.add_argument(name, **kwargs)
    arguments = vars(parser.parse_args())
    if arguments.get("action"):
        actions = [arguments["action"]]
    else:
        actions = ACTIONS

    if "clear" in actions:
        for dirpath in [VENV_DIR, BUILD_DIR]:
            if os.path.isdir(dirpath):
                shutil.rmtree(dirpath)
            os.mkdir(dirpath)
        for file_name in os.listdir(UI_DIR):
            file_path = os.path.join(UI_DIR, file_name)
            if (
                os.path.isfile(file_path)
                and file_name.startswith("ui_")
                and file_name.endswith(".py")
            ):
                os.remove(file_path)
        subprocess.run(["python3", "-m", "venv", "venv"], cwd=PROJECT_DIR)
        subprocess.run(["cmake", ".."], cwd=BUILD_DIR)

    if "install" in actions:
        subprocess.run(
            [f"{VENV_DIR}/bin/pip3", "install", "-r", "requirements.txt"],
            cwd=PROJECT_DIR,
        )

    if "cpp" in actions:
        subprocess.run(["make"], cwd=BUILD_DIR)

    if "ui" in actions:
        uic_binary = os.path.join(VENV_DIR, "bin/pyside6-uic")
        for file_name in os.listdir(UI_DIR):
            file_path = os.path.join(UI_DIR, file_name)
            if not os.path.isfile(file_path) or not file_name.endswith(".ui"):
                continue
            ui_name = file_name[:-3]
            print(f"Compiling {file_name} to ui_{ui_name}.py")
            subprocess.run(
                [uic_binary, file_name, "-o", f"ui_{ui_name}.py"], cwd=UI_DIR
            )


if __name__ == "__main__":
    main()
