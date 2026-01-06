import json
import os


CONFIG_FILE_PATH = os.path.join(os.path.abspath(os.getenv("HOME")), ".config/aoc.json")


class Configuration(dict):
    def __init__(self):
        super().__init__()
        if os.path.isfile(CONFIG_FILE_PATH):
            file = open(CONFIG_FILE_PATH, "r")
            for key, value in json.loads(file.read()).items():
                self[key] = value
            file.close()
        else:
            self["year"] = 2015
            self["day"] = 1
            self["session_path"] = None
        if "splitter_ratio" not in self:
            self["splitter_ratio"] = 0.75

    def save(self) -> None:
        file = open(CONFIG_FILE_PATH, "w")
        file.write(json.dumps(self, indent=4, sort_keys=True))
        file.close()
