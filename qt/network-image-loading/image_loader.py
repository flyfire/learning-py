from PyQt5 import QtNetwork
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class Glide:
    def __init__(self, label: QLabel, url: str, width=None, height=None):
        super().__init__()
        self.label = label
        self.req = QtNetwork.QNetworkRequest(QUrl(url))
        self.width = width
        self.height = height
        self.fetch_task = None

    def start(self, network_access_manager: QtNetwork.QNetworkAccessManager):
        self.fetch_task = network_access_manager.get(self.req)
        self.fetch_task.finished.connect(self.resolve_fetch)

    def resolve_fetch(self):
        img_binary = self.fetch_task.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(img_binary)
        if self.width is not None and self.height is not None:
            pixmap.scaled(self.width, self.height, aspectRatioMode=Qt.KeepAspectRatio,
                          transformMode=Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)
