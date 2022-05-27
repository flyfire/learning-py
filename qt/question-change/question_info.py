from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from question_0 import Ui_Question0
from question_1 import Ui_Question1
from question_2 import Ui_Question2
from base_widget import BaseWidget


class QuestionInfo:
    def __init__(self, t="", title="", subtitle="", video_path="", explain_1="", explain_2="", count_down=10):
        super(QuestionInfo, self).__init__()
        self.t = t
        self.title = title
        self.subtitle = subtitle
        self.video_path = video_path
        self.explain_1 = explain_1
        self.explain_2 = explain_2
        self.count_down = count_down

    def generate_widget(self):
        mapping = {
            "intro_1": QuestionInfo0,
            "countdown": QuestionInfo1,
            "result": QuestionInfo2
        }
        return mapping[self.t](self)

    def __repr__(self):
        return f"t={self.t}, title={self.title}, subtitle={self.subtitle}, video_path={self.video_path}, explain_1={self.explain_1}, explain_2={self.explain_2}, count_down={self.count_down}"


class QuestionInfo0(Ui_Question0, QWidget, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(QuestionInfo0, self).__init__()
        self.setupUi(self)
        self.title.setText(question.title)
        self.media_player = QMediaPlayer()
        media_content = QMediaContent(QUrl.fromLocalFile(question.video_path))
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMedia(media_content)

    def process(self):
        self.media_player.play()


class QuestionInfo1(Ui_Question1, QWidget, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(QuestionInfo1, self).__init__()
        self.setupUi(self)
        self.label_0.setText(question.explain_1)
        self.label_1.setText(question.explain_2)

    def process(self):
        pass


class QuestionInfo2(Ui_Question2, QWidget, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(QuestionInfo2, self).__init__()
        self.setupUi(self)
        self.label_result.setText("恭喜Solarex答对 + 20分")

    def process(self):
        pass
