from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        widget = QWidget()
        push_button = QPushButton('点我')
        v_layout = QVBoxLayout()
        v_layout.addWidget(push_button)
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)
        push_button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        QMessageBox.information(self, 'attention', 'hello', QMessageBox.Yes, QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()