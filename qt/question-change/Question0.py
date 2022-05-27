from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QVBoxLayout

from question_0 import Ui_Question0
from question import QuestionInfo
from base_widget import BaseWidget


class Question0(Ui_Question0, QVBoxLayout, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(Question0, self).__init__()
        self.setupUi(self)
        self.title.setText(question.title)
        self.media_player = QMediaPlayer()
        media_content = QMediaContent(QUrl.fromLocalFile(question.video_path))
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMedia(media_content)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

    def process(self):
        self.media_player.play()
