from PyQt5.QtWidgets import QWidget, QApplication
from container import Ui_container


class TestContainer(QWidget, Ui_container):
    def __init__(self):
        super(TestContainer, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    widget = TestContainer()
    widget.show()
    app.exec()
