from PyQt5.QtWidgets import QWidget

from container import Ui_Container


class QuestionContainer(Ui_Container, QWidget):
    def __init__(self):
        super(QuestionContainer, self).__init__()
        self.setupUi(self)