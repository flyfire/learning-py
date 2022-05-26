from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QApplication


class LabelWidget(QMainWindow):
    def __init__(self):
        super(LabelWidget, self).__init__()
        self.resize(290, 201)
        label = QLabel()
        label.resize(290, 201)
        self.setCentralWidget(label)
        image = QImage("kkx.jpeg")
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(290, 201, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication([])
    widget = LabelWidget()
    widget.show()
    app.exec()