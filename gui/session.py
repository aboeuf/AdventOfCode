from .configuration import Configuration
from datetime import datetime, timezone, timedelta
import json
from .problem import Problem
from PySide6.QtWidgets import QApplication, QProgressDialog
from PySide6.QtCore import Qt

EST_UTC5 = timezone(timedelta(hours=-5))

STARTING_YEAR = 2015
MOUNTH = 12


def get_now() -> datetime:
    return datetime.now(EST_UTC5)


def get_nb_puzzles_per_year(year: int) -> int:
    if year < STARTING_YEAR:
        raise ValueError(f"Year {year} is too low. Starting year is {STARTING_YEAR}")
    now = get_now()
    if year > now.year:
        raise ValueError(f"Year {year} is too hight. Current year is {now.year}")
    return 12 if year > 2024 else 25


class Session(dict):
    def __init__(self, config: Configuration, cookies: dict):
        super().__init__()
        self.config = config
        self.modified = False
        self.cookies = cookies

    def clean(self) -> None:
        for year in self.keys():
            for day in self[year]:
                if self[year][day].error is not None:
                    del self[year][day]
            if len(self[year]) == 0:
                del self[year]

    def get_missing_problems(self) -> list:
        now = get_now()
        missing_problems = []
        for year in range(STARTING_YEAR, now.year + 1):
            for day in range(1, get_nb_puzzles_per_year(year) + 1):
                if year == now.year and (now.month != 12 or day > now.day):
                    continue
                if (
                    year not in self
                    or day not in self[year]
                    or self[year][day].error is not None
                ):
                    missing_problems.append((year, day))
        return missing_problems

    def download(self, main_window, problems: list) -> None:
        nb_problems = len(problems)
        if nb_problems == 0:
            return
        self.modified = True
        progress = QProgressDialog(
            "Downloading session...", "Abort", 0, nb_problems, main_window
        )
        progress.setWindowTitle("Please Wait")
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.show()
        for i in range(nb_problems):
            if progress.wasCanceled():
                break
            year = int(problems[i][0])
            day = int(problems[i][1])
            if year not in self:
                self[year] = {}
            if day not in self[year]:
                self[year][day] = Problem(year, day)
            self[year][day].download(self.cookies)
            progress.setValue(i)
            QApplication.processEvents()
        progress.setValue(nb_problems)

    def load(self, filepath: str) -> None:
        self.clear()
        with open(filepath, "r") as file:
            parsed_data = json.loads(file.read())
            file.close()
            for year_str, event in parsed_data.items():
                year = int(year_str)
                for day_str, problem_data in event.items():
                    day = int(day_str)
                    if year not in self:
                        self[year] = {}
                    self[year][day] = Problem(year, day, data=problem_data)
        self.modified = False
        self.config["session_path"] = filepath
        self.clean()

    def export(self, filepath: str) -> None:
        with open(filepath, "w") as file:
            file.write(json.dumps(self, indent=4, sort_keys=""))

    def save(self) -> None:
        self.export(self.config["session_path"])
        self.modified = False

    def save_as(self, filepath: str) -> None:
        self.config["session_path"] = filepath
        self.save()
