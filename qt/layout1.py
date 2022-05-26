from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QSizeF, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QGraphicsScene, \
    QGraphicsView
from PyQt5.QtMultimediaWidgets import QVideoWidget, QGraphicsVideoItem


class VideoWidget(QWidget):
    def __init__(self, video_path):
        super(VideoWidget, self).__init__()
        self.init_ui()
        self.init_player(video_path)

    def init_ui(self):
        layout = self.generate_layout()
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setGeometry(300, 300, 800, 380)
        self.setFixedSize(800, 380)
        self.setStyleSheet("background-color:grey")
        self.setWindowTitle(self.__class__.__name__)

    def generate_layout(self):
        layout = QHBoxLayout()
        layout.addStretch(1)
        self.video_view = QVideoWidget()
        self.video_view.resize(640, 360)
        self.video_view.setStyleSheet("background-color:red")
        # self.video_item = QGraphicsVideoItem()
        # self.video_item.setSize(QSizeF(640, 360))
        # self.video_item.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        # scene = QGraphicsScene(self)
        # scene.addItem(self.video_item)
        # graphics_view = QGraphicsView(scene)
        # contents_rect = graphics_view.contentsRect()
        # graphics_view.setContentsMargins(0, 0, 0, 0)
        # graphics_view.setSceneRect(0, 0, contents_rect.width(), contents_rect.height())
        # graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # graphics_view.setFixedSize(640, 360)
        layout.addWidget(self.video_view)
        layout.addStretch(1)
        return layout

    def init_player(self, video_path):
        self.media_player = QMediaPlayer()
        media_content = QMediaContent(QUrl.fromLocalFile(video_path))
        self.media_player.setMedia(media_content)
        self.media_player.setVideoOutput(self.video_view)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.media_player.play()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.media_player.stop()


def test():
    app = QApplication([])
    widget = VideoWidget("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4")
    widget.show()
    app.exec()


if __name__ == '__main__':
    test()
