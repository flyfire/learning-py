import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
       "Nullam malesuada tellus in ex elementum, vitae rutrum enim vestibulum."


# ==============================================================================
class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        # Widgets
        self.label = QLabel(TEXT, self)
        self.label.setWordWrap(True)
        self.text = QTextEdit(self)
        self.text.setMinimumSize(480, 800)
        self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.text, 1, 0)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        self.setLayout(self.layout)

        self.setMinimumSize(self.sizeHint())
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
