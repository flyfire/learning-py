from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QApplication

from layout_1 import Ui_Container


class VideoWidget(Ui_Container, QWidget):
    def __init__(self):
        super(VideoWidget, self).__init__()
        self.setupUi(self)
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.widget)
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