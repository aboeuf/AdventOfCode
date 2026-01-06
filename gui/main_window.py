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
from .dialogs import NewInputDialog, StandardBoxes
from .icons import Icons
from .icons_delegate import IconsDelegate
from .problem import Problem
from .paths import PACKAGE_DIR, get_parent_dirpath
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import (
    QCloseEvent,
    QColor,
    QKeySequence,
    QPalette,
    QResizeEvent,
    QStandardItem,
    QStandardItemModel,
)
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QTableWidgetItem,
)
from .session import Session
from solvers import Solvers
from traceback import print_exception
from .ui.ui_main_window import Ui_MainWindow
from .web_utils import DOMAIN_NAME, get_cookies_from_chrome, get_url


def read_css() -> str:
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
        self.web_engine_view.setContextMenuPolicy(Qt.NoContextMenu)

        self.nb_examples = 0
        self.output = ""
        self.input = ""
        self.custom_input = False

        self.icons = Icons()
        self.setWindowIcon(self.icons["aoc"])
        self.boxes = StandardBoxes(self.icons["aoc"])
        self.refresh_push_button.setIcon(self.icons["refresh"])
        self.copy_part_one_push_button.setIcon(self.icons["copy"])
        self.copy_part_two_push_button.setIcon(self.icons["copy"])
        self.new_input_push_button.setIcon(self.icons["new"])
        self.delete_input_push_button.setIcon(self.icons["delete"])

        self.config = None
        self.cookies = get_cookies_from_chrome()
        test_cookies = get_url(
            f"https://{DOMAIN_NAME}/2015/day/1/input", timeout=5.0, cookies=self.cookies
        )
        if test_cookies is None or test_cookies.status_code != 200:
            self.boxes.warn("\n".join(NO_COOKIES_ERROR_MESSAGE))
            return

        self.config = Configuration()
        self.session = Session(self.config, self.cookies)

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

        self.inputs_combo_box.addItem("[AOC] perso")
        self.io_combo_box.addItem("Input")
        self.io_combo_box.addItem("Output")

        self.py_solvers = Solvers()

        self.action_open.triggered.connect(self.load_session)
        self.action_save.triggered.connect(self.save_session)
        self.action_save_as.triggered.connect(self.save_session_as)
        self.action_refresh_session.triggered.connect(
            lambda: self.download_session(clear=True)
        )
        self.year_combo_box.currentIndexChanged.connect(self.on_year_changed)
        self.day_combo_box.currentIndexChanged.connect(self.on_day_changed)
        self.io_combo_box.currentIndexChanged.connect(self.on_io_changed)
        self.inputs_combo_box.currentIndexChanged.connect(self.on_input_changed)
        self.refresh_push_button.clicked.connect(self.refresh_problem)
        self.new_input_push_button.clicked.connect(self.new_input)
        self.delete_input_push_button.clicked.connect(self.delete_input)
        self.io_plain_text_edit.textChanged.connect(self.on_custom_input_text_changed)
        self.solvers_combo_box.currentIndexChanged.connect(self.show_input)
        self.solve_push_button.clicked.connect(self.solve)
        self.copy_part_one_push_button.clicked.connect(
            lambda: QApplication.clipboard().setText(self.part_one_line_edit.text())
        )
        self.copy_part_two_push_button.clicked.connect(
            lambda: QApplication.clipboard().setText(self.part_two_line_edit.text())
        )

        self.action_open.setShortcut(QKeySequence("Ctrl+O"))
        self.action_save.setShortcut(QKeySequence("Ctrl+S"))
        self.action_refresh_session.setShortcut(QKeySequence("Ctrl+U"))

        self.overview_table_view.setItemDelegate(IconsDelegate())
        header = self.overview_table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        QTimer.singleShot(0, self.bootstrap)

    def bootstrap(self) -> None:
        self.set_splitter_ratio()
        self.ask_download_session()

    def closeEvent(self, event: QCloseEvent) -> None:
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

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.set_splitter_ratio()

    def show_status(self, message: str) -> None:
        current = self.status_bar.currentMessage()
        self.status_bar.showMessage(
            "{} | {}".format(current, message) if current else message, timeout=2000
        )

    def update_title(self) -> None:
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

    def get_splitter_ratio(self) -> float:
        sizes = self.splitter.sizes()
        total_width = sum(sizes)
        if total_width > 0:
            return sizes[0] / total_width

    def set_splitter_ratio(self) -> None:
        ratio = self.config["splitter_ratio"]
        if ratio < 0.0 or ratio > 1.0:
            raise ValueError(f"bad ratio value {ratio}")
        total_width = self.splitter.width()
        if total_width == 0:
            raise ValueError(
                "set_splitter_ratio called before main window is displayed"
            )
        left_size = int(total_width * ratio)
        right_size = total_width - left_size
        self.splitter.setSizes([left_size, right_size])

    def update_year_combo_box(self) -> None:
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

    def ask_download_session(self, nb_missed: int = None) -> None:
        nb_missing_problems = len(self.session.get_missing_problems())
        if nb_missing_problems == 0:
            self.update_year_combo_box()
            self.update_overview()
            return
        if self.boxes.ask(
            "Missing Puzzles",
            "{}our session {}has {} missing puzzle{}.\nDo you want to download {}?".format(
                "Y" if nb_missed is None else "Because of some download failures, y",
                "" if nb_missed is None else "still ",
                "one" if nb_missing_problems == 1 else nb_missing_problems,
                "s" if nb_missing_problems > 1 else "",
                "them" if nb_missing_problems > 1 else "it",
            ),
        ):
            self.download_session()
        else:
            self.update_year_combo_box()
        self.update_overview()

    def download_session(self, clear: bool = False) -> None:
        if clear:
            self.session.clear()
        problems = self.session.get_missing_problems()
        self.session.download(self, problems)
        self.update_title()
        self.update_year_combo_box()
        self.session.clean()
        nb_missed = len(problems) - len(self.session.get_missing_problems())
        if nb_missed > 0:
            self.ask_download_session(nb_missed)

    def load_session(self) -> None:
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
        self.session.clean()
        self.update_title()
        self.ask_download_session()

    def save_session_as(self) -> None:
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

    def save_session(self) -> None:
        if self.config["session_path"] is None:
            self.save_session_as()
        else:
            self.session.save()
            self.update_title()

    def touch_session(self) -> None:
        self.session.modified = True
        self.update_title()

    def current_problem(self) -> Problem:
        return self.session[self.config["year"]][self.config["day"]]

    def on_year_changed(self) -> None:
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

    def on_day_changed(self) -> None:
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
        self.show_input()
        self.update_inputs()
        self.show_status(
            "Problem ({}, {}) : ({} ex, {} cust)".format(
                self.config["year"],
                self.config["day"],
                (
                    len(problem["aoc_example_inputs"])
                    if "aoc_example_inputs" in problem
                    else 0
                ),
                len(problem["custom_inputs"]) if "custom_inputs" in problem else 0,
            )
        )

    def show_input(self) -> None:
        self.io_combo_box.blockSignals(True)
        self.io_combo_box.setCurrentIndex(0)
        self.io_combo_box.blockSignals(False)
        self.on_io_changed()

    def show_output(self) -> None:
        self.io_combo_box.blockSignals(True)
        self.io_combo_box.setCurrentIndex(1)
        self.io_combo_box.blockSignals(False)
        self.on_io_changed()

    def on_io_changed(self) -> None:
        is_input = self.io_combo_box.currentIndex() == 0
        self.inputs_combo_box.setEnabled(is_input)
        self.new_input_push_button.setEnabled(is_input)
        self.delete_input_push_button.setEnabled(is_input)
        self.io_plain_text_edit.blockSignals(True)
        self.io_plain_text_edit.clear()
        if is_input:
            self.io_plain_text_edit.appendPlainText(self.input)
            self.io_plain_text_edit.setReadOnly(not self.custom_input)
            self.delete_input_push_button.setEnabled(self.custom_input)
        else:
            self.io_plain_text_edit.appendPlainText(self.output)
            self.io_plain_text_edit.setReadOnly(True)
        self.io_plain_text_edit.blockSignals(False)

    def update_inputs(self, set_to_custom: str = None) -> None:
        problem = self.current_problem()
        self.inputs_combo_box.blockSignals(True)
        while self.inputs_combo_box.count() > 1:
            self.inputs_combo_box.removeItem(self.inputs_combo_box.count() - 1)
        self.nb_examples = len(problem["aoc_example_inputs"])
        if self.nb_examples > 1:
            for i in range(self.nb_examples):
                self.inputs_combo_box.addItem(f"[AOC] example #{i + 1}")
        elif self.nb_examples > 0:
            self.inputs_combo_box.addItem(f"[AOC] example")
        if "custom_inputs" in problem:
            for name in sorted(problem["custom_inputs"].keys()):
                self.inputs_combo_box.addItem(name)
        if set_to_custom is None:
            self.inputs_combo_box.setCurrentIndex(0)
        else:
            index = self.inputs_combo_box.findText(set_to_custom)
            if index < 0:
                self.inputs_combo_box.setCurrentIndex(0)
            else:
                self.inputs_combo_box.setCurrentIndex(index)
        self.inputs_combo_box.blockSignals(False)
        self.on_input_changed()

    def on_input_changed(self) -> None:
        self.part_one_line_edit.clear()
        self.part_two_line_edit.clear()
        self.io_plain_text_edit.blockSignals(True)
        self.io_plain_text_edit.clear()
        self.io_plain_text_edit.blockSignals(False)
        self.input = ""
        self.output = ""
        self.custom_input = self.inputs_combo_box.currentIndex() > self.nb_examples
        self.delete_input_push_button.setEnabled(self.custom_input)
        self.read_only = not self.custom_input
        problem = self.current_problem()
        if self.inputs_combo_box.currentIndex() == 0:
            self.input = problem["aoc_personal_input"]
        elif self.custom_input:
            self.input = problem["custom_inputs"][self.inputs_combo_box.currentText()]
        else:
            self.input = problem["aoc_example_inputs"][
                self.inputs_combo_box.currentIndex() - 1
            ]
        self.show_input()

    def refresh_problem(self) -> None:
        problem = self.current_problem()
        try:
            problem.download(self.cookies)
            if problem.error is not None:
                raise Exception(problem.error)
            self.show_status("Problem downloaded")
        except Exception as exc:
            print_exception(exc)
            self.boxes.warn("Failed to download problem with exception:\n" + str(exc))
            self.show_status("Download failure")
        self.on_day_changed()
        self.touch_session()
        self.update_overview()

    def update_overview(self) -> None:
        rows = 25
        years = sorted(self.session.keys())
        cols = len(years)
        model = QStandardItemModel(rows, cols)
        model.setHorizontalHeaderLabels([str(year) for year in years])
        for col in range(cols):
            year = years[col]
            for day in sorted(self.session[year].keys()):
                row = day - 1
                problem = self.session[year][day]
                nb_stars = problem.nb_stars()
                item = QStandardItem()
                icons = [
                    self.icons[
                        "{}_star".format(
                            "green"
                            if nb_stars == 2
                            else ("orange" if nb_stars == 1 else "red")
                        )
                    ],
                    self.icons[
                        "{}cpp".format("" if aoc.has_solver(year, day) else "no_")
                    ],
                    self.icons[
                        "{}python".format(
                            "" if self.py_solvers.has(year, day) else "no_"
                        )
                    ],
                ]
                item.setData(icons, Qt.UserRole)
                model.setItem(row, col, item)
        self.overview_table_view.setModel(model)

    def new_input(self) -> None:
        dialog = NewInputDialog(self.inputs_combo_box)
        if not dialog.exec():
            return
        name = dialog.get_name()
        if not dialog.valid():
            return self.boxes.warn(f'Invalid input name "{name}".')
        problem = self.current_problem()
        if problem.has_custom_input_with_name(name):
            return self.boxes.warn(f'Problem already has an input with name "{name}".')
        input = ""
        if dialog.duplicate_check_box.isChecked():
            if dialog.inputs_combo_box.currentIndex() == 0:
                input = problem.aoc_personal_input
            elif (
                "aoc_example_inputs" in problem
                and dialog.inputs_combo_box.currentIndex() - 1
                < len(problem["aoc_example_inputs"])
            ):
                input = problem["aoc_example_inputs"][
                    dialog.inputs_combo_box.currentIndex() - 1
                ]
            else:
                input = problem.get_custom_input(dialog.inputs_combo_box.currentText())
        problem.add_custom_input(name, input)
        self.update_inputs(set_to_custom=name)
        self.touch_session()

    def delete_input(self) -> None:
        problem = self.current_problem()
        index = self.inputs_combo_box.currentIndex()
        if not self.custom_input or (
            "aoc_example_inputs" in problem
            and index <= len(problem["aoc_example_inputs"])
        ):
            return self.boxes.warn("Can only delete a custom input.")
        if not self.boxes.ask("Delete current input?", "Are you sure?"):
            return
        del problem["custom_inputs"][self.inputs_combo_box.currentText()]
        self.inputs_combo_box.blockSignals(True)
        self.inputs_combo_box.removeItem(index)
        self.inputs_combo_box.blockSignals(False)
        self.update_inputs()
        self.touch_session()

    def on_custom_input_text_changed(self) -> None:
        if self.custom_input:
            problem = self.current_problem()
            self.input = self.io_plain_text_edit.toPlainText()
            problem["custom_inputs"][self.inputs_combo_box.currentText()] = self.input
            self.touch_session()

    def solve(self):
        self.part_one_line_edit.clear()
        self.part_two_line_edit.clear()
        self.output = ""

        try:
            if self.solvers_combo_box.currentText() == "[C++]":
                result = aoc.solve(self.config["year"], self.config["day"], self.input)
            elif self.solvers_combo_box.currentText() == "[Python]":
                result = self.py_solvers.solve(
                    self.config["year"], self.config["day"], self.input
                )
            elif self.solvers_combo_box.currentIndex() < 0:
                raise Exception("no solver")
            else:
                raise Exception(
                    f"unknown solver '{self.solvers_combo_box.currentText()}'"
                )
        except Exception as exc:
            self.output = str(exc)
            self.show_output()
            return

        self.part_one_line_edit.setText(result.part_one_solution)
        self.part_two_line_edit.setText(result.part_two_solution)
        self.output = "\n".join(result.output())

        problem = self.current_problem()
        widgets = [self.part_one_line_edit, self.part_two_line_edit]
        for i in range(2):
            if (
                self.inputs_combo_box.currentIndex() != 0
                or "answers" not in problem
                or i >= len(problem["answers"])
            ):
                color = "black"
            elif widgets[i].text() == problem["answers"][i]:
                color = "green"
            else:
                color = "red"
            palette = widgets[i].palette()
            palette.setColor(QPalette.ColorRole.Text, QColor(color))
            widgets[i].setPalette(palette)
