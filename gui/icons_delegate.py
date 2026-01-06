from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QWidget
from PySide6.QtCore import Qt, QModelIndex, QSize
from PySide6.QtGui import QIcon, QPainter


class IconsDelegate(QStyledItemDelegate):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.icon_size = 20
        self.spacing = 5

    def paint(
        self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex
    ) -> None:
        icons = index.data(Qt.UserRole)
        if not icons or not isinstance(icons, list):
            return
        painter.save()
        rect = option.rect
        y_pos = rect.y() + (rect.height() - self.icon_size) / 2
        current_x = rect.x() + self.spacing
        for icon in icons:
            if isinstance(icon, QIcon):
                pixmap = icon.pixmap(self.icon_size, self.icon_size)
                painter.drawPixmap(int(current_x), int(y_pos), pixmap)
                current_x += self.icon_size + self.spacing
        painter.restore()

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        width = (self.icon_size * 3) + (self.spacing * 4)
        return QSize(width, 30)
