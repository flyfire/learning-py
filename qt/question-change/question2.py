from PyQt5.QtWidgets import QVBoxLayout

from question_2 import Ui_Question2
from base_widget import BaseWidget
from question import QuestionInfo


class Question2(Ui_Question2, QVBoxLayout, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(Question2, self).__init__()
        self.setupUi(self)
        self.label_result.setText("恭喜Solarex答对 + 20分")

    def process(self):
        pass
