from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QApplication


class LabelWidget(QWidget):
    def __init__(self):
        super(LabelWidget, self).__init__()
        self.resize(100, 500)
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        label = QLabel()
        label.setWordWrap(True)
        label.setMaximumWidth(50)
        label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        label.setText("Hello" * 50)
        label.adjustSize()
        h_layout.addWidget(label, 2)
        h_layout.addStretch(1)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    widget = LabelWidget()
    widget.show()
    app.exec()
