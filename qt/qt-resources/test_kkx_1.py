from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QStyleOption, QStyle

import resources_rc


class Ui_KKX(object):
    def setupUi(self, container: QWidget):
        container.setFixedSize(400, 800)
        container.setStyleSheet("background-image: url(:/images/kkx.jpeg)")


class TestKKX(QWidget, Ui_KKX):
    def __init__(self):
        super(TestKKX, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("background-image: url(:/images/kkx.jpeg)")


class TestKKX1(QWidget):
    def __init__(self):
        super(TestKKX1, self).__init__()
        self.setStyleSheet("background-image: url(:/images/kkx.jpeg)")
        self.setFixedSize(400, 800)

    # https://stackoverflow.com/questions/18344135/why-do-stylesheets-not-work-when-subclassing-qwidget-and-using-q-object/32889486#32889486
    def paintEvent(self, pe):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)


def test_0():
    app = QApplication([])
    widget = TestKKX()
    widget.show()
    app.exec()


def test_1():
    app = QApplication([])
    widget = TestKKX1()
    widget.show()
    app.exec()


if __name__ == '__main__':
    # test_0()
    test_1()
