from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
import naruto_rc


class TestResourceWindow(QMainWindow):
    def __init__(self):
        super(TestResourceWindow, self).__init__()
        widget = QWidget()
        v_layout = QVBoxLayout()
        tmp_widget_0 = QWidget()
        tmp_widget_0.setStyleSheet("background-image: url(naruto-0.png)")
        tmp_widget_0.setFixedSize(600, 600)
        tmp_widget_1 = QWidget()
        tmp_widget_1.setStyleSheet("background-image: url(:/images/naruto-1.jpeg)")
        tmp_widget_1.setFixedSize(600, 600)
        v_layout.addWidget(tmp_widget_0)
        v_layout.addWidget(tmp_widget_1)
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)


def test_0():
    app = QApplication([])
    label = QLabel()
    label.setStyleSheet("background-image: url(naruto-0.png)")
    label.show()
    app.exec()


def test_1():
    app = QApplication([])
    window = TestResourceWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test_1()
