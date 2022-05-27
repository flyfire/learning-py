from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

from question import parse_questions
from question_container import QuestionContainer
from question_signals import QuestionSignals


def change_question(container, widgets, index):
    next = index + 1
    if next < len(widgets):
        QWidget().setLayout(container.question_container.layout())
        v_layout = QVBoxLayout()
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addWidget(widgets[next])
        container.question_container.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication([])
    question_signals = QuestionSignals()
    questions = parse_questions("questions.json")
    widgets = []
    for index, question in enumerate(questions):
        print(question)
        widgets.append(question.generate_widget(index, question_signals))
    index = 0
    container = QuestionContainer()
    v_layout = QVBoxLayout()
    v_layout.addWidget(widgets[index])
    v_layout.setSpacing(0)
    v_layout.setGeometry(QRect(0, 0, 720, 400))
    container.question_container.setLayout(v_layout)
    widgets[index].process()
    container.show()
    question_signals.index.connect(lambda i: change_question(container, widgets, i))
    app.exec()
