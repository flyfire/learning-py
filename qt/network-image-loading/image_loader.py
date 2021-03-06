from PyQt5 import QtNetwork
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QMainWindow, QWidget
import threading


class Glide:
    def __init__(self, label: QLabel, url: str, width=None, height=None):
        super().__init__()
        self.label = label
        self.req = QtNetwork.QNetworkRequest(QUrl(url))
        self.width = width
        self.height = height
        self.fetch_task = None

    def start(self, network_access_manager: QtNetwork.QNetworkAccessManager):
        t = threading.current_thread()
        print(f'start at {t.ident}, {t.name}')
        self.fetch_task = network_access_manager.get(self.req)
        self.fetch_task.finished.connect(self.resolve_fetch)

    def resolve_fetch(self):
        t = threading.current_thread()
        print(f'resolve at {t.ident} {t.name}')
        img_binary = self.fetch_task.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(img_binary)
        if self.width is not None and self.height is not None:
            pixmap.scaled(self.width, self.height, aspectRatioMode=Qt.KeepAspectRatio,
                          transformMode=Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.network_access_manager = QtNetwork.QNetworkAccessManager()
        widget = QWidget()
        v_layout = QVBoxLayout()
        label1 = QLabel()
        v_layout.addWidget(label1)
        Glide(label1, "https://live.staticflickr.com/65535/49251422908_591245c64a_c_d.jpg")\
            .start(self.network_access_manager)
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)


def test():
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()
