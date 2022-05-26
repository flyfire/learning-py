from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QSizePolicy, QApplication, QLabel, QPushButton, QListView, QWidget


class VideoWidget(QMainWindow):
    def __init__(self):
        super(VideoWidget, self).__init__()
        widget = QWidget()
        widget.resize(800, 360)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)
        video_view = QVideoWidget()
        video_view.resize(640, 360)
        # video_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(video_view, 8)
        layout.addStretch(1)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.resize(800, 360)
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(video_view)
        media_content = QMediaContent(QUrl.fromLocalFile("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4"))
        self.media_player.setMedia(media_content)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.media_player.play()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.media_player.stop()


if __name__ == '__main__':
    app = QApplication([])
    widget = VideoWidget()
    widget.show()
    label = QLabel()
    print(label.sizePolicy().horizontalPolicy(), label.sizePolicy().verticalPolicy())
    print(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum,
          QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding,
          QSizePolicy.Policy.Ignored)
    btn = QPushButton()
    print(btn.sizePolicy().horizontalPolicy(), btn.sizePolicy().verticalPolicy())
    video_view = QVideoWidget()
    print(video_view.sizePolicy().horizontalPolicy(), video_view.sizePolicy().verticalPolicy())
    list_view = QListView()
    print(list_view.sizePolicy().horizontalPolicy(), list_view.sizePolicy().verticalPolicy())
    app.exec()
