import argparse
import os
import sys

PARSER_ARGS = {
    "help": "Generate specific files for QtCreator.",
}

INCLUDE_EXTENSIONS = ["h", "hpp"]
ALL_EXTENSIONS = [
    *INCLUDE_EXTENSIONS,
    "c",
    "cpp",
    "txt",
    "py",
    "gitignore",
    "ui",
    "css",
]

FILTERED_DIRECTORIES = ["build", ".git", "venv"]


THIS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
PROJECT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
PROJECT_NAME = PROJECT_DIR.split("/")[-1]


def get_paths() -> tuple:
    all_paths = []
    include_paths = [PROJECT_DIR]
    filtered = [os.path.join(PROJECT_DIR, path) for path in FILTERED_DIRECTORIES]

    def add_filepath(filepath: str) -> None:
        nonlocal all_paths, include_paths
        extension = os.path.splitext(filepath)[1][1:]
        if extension not in ALL_EXTENSIONS:
            return
        if filepath not in all_paths:
            all_paths.append(filepath)
        if extension in INCLUDE_EXTENSIONS:
            current = os.path.abspath(os.path.join(filepath, os.pardir))
            while current != PROJECT_DIR:
                if current not in include_paths:
                    include_paths.append(current)
                current = os.path.abspath(os.path.join(current, os.pardir))

    def get_paths_recursive(path: str, depth: int = 0) -> None:
        if os.path.isfile(path):
            add_filepath(path)
            return
        if not os.path.isdir(path) or path in filtered:
            return
        for name in os.listdir(path):
            if path != PROJECT_DIR or not name.startswith(PROJECT_NAME):
                get_paths_recursive(os.path.join(path, name), depth=depth + 1)

    get_paths_recursive(PROJECT_DIR)
    all_paths.sort()
    include_paths.sort()
    return (all_paths, include_paths)


def main() -> None:
    prog_name = sys.argv[0].split("/")[-1]
    parser = argparse.ArgumentParser(prog=prog_name, description=PARSER_ARGS["help"])
    parser.parse_args()
    all_paths, include_paths = get_paths()
    with open(os.path.join(PROJECT_DIR, f"{PROJECT_NAME}.files"), "w") as file:
        for path in all_paths:
            file.write(path)
            file.write("\n")
        file.close()
    with open(os.path.join(PROJECT_DIR, f"{PROJECT_NAME}.includes"), "w") as file:
        for path in include_paths:
            file.write(path)
            file.write("\n")
        file.close()


if __name__ == "__main__":
    main()
