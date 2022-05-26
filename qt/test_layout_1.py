from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QMainWindow


class VideoWidget(QMainWindow):
    def __init__(self):
        super(VideoWidget, self).__init__()
        widget = QWidget()
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_widget = QWidget()
        v_layout.addStretch(1)
        v_layout.addWidget(h_widget, 18)
        v_layout.addStretch(1)
        h_layout.addStretch(1)
        video_view = QVideoWidget()
        video_view.resize(640, 360)
        h_layout.addWidget(video_view, 8)
        h_layout.setSpacing(0)
        h_layout.addStretch(1)
        v_layout.setSpacing(0)
        h_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setContentsMargins(0, 0, 0, 0)
        h_widget.setLayout(h_layout)
        widget.setLayout(v_layout)
        widget.resize(800, 400)
        self.setFixedSize(800, 400)
        self.setCentralWidget(widget)
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
    app.exec()
