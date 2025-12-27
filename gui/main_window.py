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
from .configuration import Configuration
from .dialogs import StandardBoxes
from .icons import Icons
from .paths import PACKAGE_DIR, get_parent_dirpath
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor, QKeySequence, QPalette
from PySide6.QtWidgets import QFileDialog, QMainWindow
from .session import Session
from solvers import Solvers
from traceback import print_exception
from .ui.ui_main_window import Ui_MainWindow
from .web_utils import DOMAIN_NAME, get_cookies_from_chrome, get_url


def read_css():
    with open(os.path.join(PACKAGE_DIR, "styles.css"), "r") as css_file:
        css_data = css_file.read()
        css_file.close()
        return css_data


HTML_HEADER = f"<html><style>{read_css()}</style><body>"

NO_COOKIES_ERROR_MESSAGE = [
    "Cannot recover valid cookies for the Advent of Code website.",
    "",
    "Please use the Google Chrome Browser to",
    "connect to your account and try again.",
]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.icons = Icons()
        self.setWindowIcon(self.icons["aoc"])
        self.boxes = StandardBoxes(self.icons["aoc"])

        self.config = None
        cookies = get_cookies_from_chrome()
        test_cookies = get_url(
            f"https://{DOMAIN_NAME}/2015/day/1/input", timeout=5.0, cookies=cookies
        )
        if test_cookies is None or test_cookies.status_code != 200:
            self.boxes.warn("\n".join(NO_COOKIES_ERROR_MESSAGE))
            return

        self.config = Configuration()
        self.session = Session(self.config, cookies)

        session_filepath = self.config["session_path"]
        if session_filepath is not None:
            try:
                self.session.load(session_filepath)
            except Exception as exc:
                print_exception(exc)
                self.boxes.warn(
                    f'Failed to load session file "{session_filepath}" with error {exc}'
                )
                self.config["session_path"] = None
                self.session.clear()

        self.update_title()

        self.py_solvers = Solvers()

        self.action_open.triggered.connect(self.load_session)
        self.action_save.triggered.connect(self.save_session)
        self.action_save_as.triggered.connect(self.save_session_as)
        self.year_combo_box.currentIndexChanged.connect(self.on_year_changed)
        self.day_combo_box.currentIndexChanged.connect(self.on_day_changed)

        self.action_open.setShortcut(QKeySequence("Ctrl+O"))
        self.action_save.setShortcut(QKeySequence("Ctrl+S"))

        QTimer.singleShot(0, self.ask_download_session)

    def closeEvent(self, event):
        if self.config is not None:
            ratio = self.get_splitter_ratio()
            if ratio is not None:
                self.config["splitter_ratio"] = ratio
            self.config.save()
            if self.session.modified:
                if self.boxes.ask(
                    "The session has been modified.",
                    "Do you want to save your changes?",
                ):
                    if self.config["session_path"] is None:
                        self.save_session_as()
                    else:
                        self.save_session()
        super().closeEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.set_splitter_ratio()

    def update_title(self):
        title = "Advent of Code"
        if self.session.modified or self.config["session_path"] is not None:
            title += " - {}{}".format(
                (
                    ""
                    if self.config["session_path"] is None
                    else self.config["session_path"].split("/")[-1]
                ),
                " *" if self.session.modified else "",
            )
        self.setWindowTitle(title)

    def get_splitter_ratio(self):
        sizes = self.splitter.sizes()
        total_width = sum(sizes)
        if total_width > 0:
            return sizes[0] / total_width

    def set_splitter_ratio(self):
        ratio = self.config["splitter_ratio"]
        if ratio < 0. or ratio > 1.:
            raise ValueError(f"bad ratio value {ratio}")
        total_width = self.splitter.width()
        if total_width == 0:
            raise ValueError("set_splitter_ratio called before main window is displayed")
        left_size = int(total_width * ratio)
        right_size = total_width - left_size
        self.splitter.setSizes([left_size, right_size])

    def update_year_combo_box(self):
        self.year_combo_box.blockSignals(True)
        self.year_combo_box.clear()
        for year in sorted(self.session.keys()):
            self.year_combo_box.addItem(str(year))
        if self.config["year"] not in self.session:
            self.config["year"] = min(self.session.keys())
        index = self.year_combo_box.findText(str(self.config["year"]))
        self.year_combo_box.setCurrentIndex(index)
        self.year_combo_box.blockSignals(False)
        self.on_year_changed()

    def ask_download_session(self):
        nb_missing_problems = len(self.session.get_missing_problems())
        if nb_missing_problems == 0:
            self.update_year_combo_box()
            return
        if self.boxes.ask(
            "Missing Puzzles",
            "Your session has {} missing puzzle{}.\nDo you want to download {}?".format(
                "one" if nb_missing_problems == 1 else nb_missing_problems,
                "s" if nb_missing_problems > 1 else "",
                "them" if nb_missing_problems > 1 else "it",
            ),
        ):
            self.download_session()
        else:
            self.update_year_combo_box()

    def download_session(self, clear=False):
        if clear:
            self.session.clear()
        problems = self.session.get_missing_problems()
        self.session.download(self, problems)
        self.update_title()
        self.update_year_combo_box()

    def load_session(self):
        dirpath = (
            os.getenv("HOME")
            if self.config["session_path"] is None
            else get_parent_dirpath(self.config["session_path"])
        )
        filepath = QFileDialog.getOpenFileName(
            parent=self, caption="Open AOC Session", dir=dirpath, filter="JSON (*.json)"
        )[0]
        if len(filepath) == 0:
            return
        self.session.load(filepath)
        self.update_title()
        self.update_year_combo_box()

    def save_session_as(self):
        dirpath = (
            os.getenv("HOME")
            if self.config["session_path"] is None
            else get_parent_dirpath(self.config["session_path"])
        )
        filepath = QFileDialog.getSaveFileName(
            parent=self, caption="Save AOC Session", dir=dirpath, filter="JSON (*.json)"
        )[0]
        if len(filepath) == 0:
            return
        self.session.save_as(filepath)
        self.update_title()

    def save_session(self):
        if self.config["session_path"] is None:
            self.save_session_as()
        else:
            self.session.save()
            self.update_title()

    def current_problem(self):
        return self.session[self.config["year"]][self.config["day"]]

    def on_year_changed(self):
        self.config["year"] = int(self.year_combo_box.currentText())
        self.day_combo_box.blockSignals(True)
        self.day_combo_box.clear()
        for day in sorted(self.session[self.config["year"]].keys()):
            self.day_combo_box.addItem(str(day))
        if self.config["day"] not in self.session[self.config["year"]]:
            self.config["day"] = min(self.session[self.config["year"]].keys())
        index = self.day_combo_box.findText(str(self.config["day"]))
        self.day_combo_box.setCurrentIndex(index)
        self.day_combo_box.blockSignals(False)
        self.on_day_changed()

    def on_day_changed(self):
        self.config["day"] = int(self.day_combo_box.currentText())
        problem = self.current_problem()
        self.web_engine_view.setHtml(HTML_HEADER + problem["html"] + "</body></html>")
        self.solvers_combo_box.clear()
        if aoc.has_solver(self.config["year"], self.config["day"]):
            self.solvers_combo_box.addItem("[C++]")
        if self.py_solvers.has(self.config["year"], self.config["day"]):
            self.solvers_combo_box.addItem("[Python]")
        if self.solvers_combo_box.count() == 0:
            self.solve_push_button.setEnabled(False)
            color = "red"
        else:
            self.solve_push_button.setEnabled(True)
            color = "black"
        palette = self.solver_label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(color))
        self.solver_label.setPalette(palette)
