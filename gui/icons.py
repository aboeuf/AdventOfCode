import os
from .paths import ICONS_DIR
from PySide6.QtGui import QIcon


class Icons(dict):
    def __init__(self):
        super().__init__()
        for filename in os.listdir(ICONS_DIR):
            self[filename.split(".")[0]] = QIcon(os.path.join(ICONS_DIR, filename))
