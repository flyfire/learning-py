from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel

from label_0 import Ui_LabelContainer


class LabelWidget(QWidget):
    def __init__(self):
        super(LabelWidget, self).__init__()
        v_layout = QVBoxLayout()
        label_1 = QLabel()
        label_1.setWordWrap(True)
        label_1.setText("Hello" * 50)
        label_1.setMaximumWidth(100)
        label_1.adjustSize()
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addWidget(label_1)
        self.setLayout(v_layout)
        self.resize(400, 600)


if __name__ == '__main__':
    app = QApplication([])
    widget = LabelWidget()
    widget.show()
    print(widget.width(), widget.height())
    app.exec()
