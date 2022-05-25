from abc import abstractmethod

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel


class BaseWidget(QWidget):
    def __init__(self):
        super(BaseWidget, self).__init__()
        self.init_ui()

    def init_ui(self):
        layout = self.generate_layout()
        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle(self.__class__.__name__)

    @abstractmethod
    def generate_layout(self):
        pass


class Widget0(BaseWidget):
    def __init__(self):
        super(Widget0, self).__init__()

    def generate_layout(self):
        layout = QHBoxLayout()
        layout.addStretch(1)
        label1 = QLabel("Hello")
        label1.setStyleSheet("background-color:green;font-size:24px;color:blue")
        layout.addWidget(label1)
        label2 = QLabel("World")
        label2.setStyleSheet("background-color:grey;font-size:36px;color:blue")
        layout.addWidget(label2)
        layout.addStretch(1)
        return layout


def get_widget(seq):
    mapping = {"0": Widget0}
    return mapping[str(seq)]()


def test(seq):
    app = QApplication([])
    widget = get_widget(seq)
    widget.show()
    app.exec()


if __name__ == '__main__':
    test(0)
