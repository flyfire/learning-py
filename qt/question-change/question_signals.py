from PyQt5.QtCore import QObject, pyqtSignal


class QuestionSignals(QObject):
    index = pyqtSignal(int)