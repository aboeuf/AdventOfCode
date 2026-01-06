import os


def get_parent_dirpath(path: str) -> str:
    return os.path.abspath(os.path.join(path, os.pardir))


PACKAGE_DIR = get_parent_dirpath(__file__)
ICONS_DIR = os.path.join(PACKAGE_DIR, "icons")
