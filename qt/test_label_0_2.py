from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLayout, QLabel, QSizePolicy, QApplication


class LabelWidget(QWidget):
    def __init__(self):
        super(LabelWidget, self).__init__()
        v_layout = QVBoxLayout()
        v_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.setLayout(v_layout)
        self.setMinimumSize(100, 500)
        self.setMaximumWidth(200)
        for i in range(5):
            label = QLabel()
            label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
            label.setWordWrap(True)
            label.setText("This is a very long text. This is a very long text. This is a very long text. "
                   "This is a very long text. This is a very long text. This is a very long text. This is a very long text. "
                   "This is a very long text. This is a very long text.")
            v_layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication([])
    widget = LabelWidget()
    widget.show()
    app.exec()
