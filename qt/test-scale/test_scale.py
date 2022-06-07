from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QWidget, QApplication

from test_scale_container import Ui_test_scale_container


class TestScaleWidget(QWidget, Ui_test_scale_container):
    def __init__(self):
        super(TestScaleWidget, self).__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.do_anim)

    def do_anim(self):
        self.anim = QPropertyAnimation(self.scale_animation_container, b"geometry")
        self.anim.setDuration(5000)
        pos = self.scale_animation_container.pos()
        width = self.scale_animation_container.width()
        height = self.scale_animation_container.height()
        self.label_0.setScaledContents(True)
        self.label_1.setScaledContents(True)
        self.anim.setStartValue(QRect(pos.x(), pos.y(), width / 2, height / 2))
        self.anim.setEndValue(QRect(pos.x(), pos.y(), width, height))
        self.anim.start()
        self.anim.finished.connect(lambda: print('end'))


def test_0():
    app = QApplication([])
    widget = TestScaleWidget()
    widget.show()
    app.exec()


if __name__ == '__main__':
    test_0()
