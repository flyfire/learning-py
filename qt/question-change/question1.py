from PyQt5.QtWidgets import QVBoxLayout

from question_1 import Ui_Question1
from base_widget import BaseWidget
from question import QuestionInfo


class Question1(Ui_Question1, QVBoxLayout, BaseWidget):
    def __init__(self, question: QuestionInfo):
        super(Question1, self).__init__()
        self.setupUi(self)
        self.label_0.setText(question.explain_1)
        self.label_1.setText(question.explain_2)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

    def process(self):
        pass
