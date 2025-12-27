from PySide6.QtWidgets import QMessageBox


class StandardBoxes:
    def __init__(self, window_icon):
        self.window_icon = window_icon

    def ask(self, title, question):
        msg_box = QMessageBox()
        msg_box.setWindowIcon(self.window_icon)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle(title)
        msg_box.setText(question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)
        answer = msg_box.exec()
        return answer == QMessageBox.Yes

    def warn(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowIcon(self.window_icon)
        msg_box.setWindowIcon(QMessageBox.Icon.Warning)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        return msg_box.exec()
