from PyQt5.QtWidgets import QApplication, QWidget
import resources_rc


def test_kkx_0():
    app = QApplication([])
    widget = QWidget()
    widget.setFixedSize(400, 800)
    widget.setStyleSheet("background-image: url(:/images/kkx.jpeg)")
    widget.show()
    app.exec()


if __name__ == '__main__':
    test_kkx_0()
