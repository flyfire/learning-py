from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QVBoxLayout

from question import parse_questions
from question_container import QuestionContainer

if __name__ == '__main__':
    app = QApplication([])
    questions = parse_questions("questions.json")
    widgets = []
    for question in questions:
        print(question)
        widgets.append(question.generate_widget())
    index = 0
    container = QuestionContainer()
    v_layout = QVBoxLayout()
    v_layout.addWidget(widgets[index])
    v_layout.setSpacing(0)
    v_layout.setGeometry(QRect(0, 0, 720, 400))
    container.question_container.setLayout(v_layout)
    widgets[index].process()
    container.show()
    app.exec()
