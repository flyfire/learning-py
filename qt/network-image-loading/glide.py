import requests
import threading

from PyQt5.QtCore import QThreadPool, pyqtSignal, QRunnable, Qt, QObject
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication


class Glide(QObject):
    image_loaded = pyqtSignal(tuple)

    class LabelInfo:
        def __init__(self, label, place_holder: QPixmap, error_place_holder: QPixmap):
            super().__init__()
            self.label = label
            self.place_holder = place_holder
            self.error_place_holder = error_place_holder

    class LoadImageRunnable(QRunnable):
        def __init__(self, url, width, height, image_loaded):
            super().__init__()
            self.url = url
            self.image_loaded = image_loaded
            self.width = width
            self.height = height

        def run(self) -> None:
            t = threading.current_thread()
            print(f'run at {t.ident}, {t.name}')
            try:
                response = requests.get(self.url)
            except:
                import traceback
                print(traceback.format_exc())
                self.image_loaded.emit((self.url, None))
                return
            if response.status_code == 200:
                q_image = QImage()
                q_image.loadFromData(response.content)
                if self.width is not None and self.height is not None:
                    q_image.scaled(self.width, self.height,
                                   aspectRatioMode=Qt.KeepAspectRatio,
                                   transformMode=Qt.SmoothTransformation)
                self.image_loaded.emit((self.url, q_image))
            else:
                self.image_loaded.emit((self.url, None))

    def __init__(self):
        super().__init__()
        self.label_mapping = {}
        self.thread_pool = QThreadPool.globalInstance()
        self.image_loaded.connect(self.on_image_loaded)

    def load_into(self, label: QLabel, url: str, width: int = None, height: int = None, place_holder: QPixmap = None,
                  error_place_holder: QPixmap = None):
        t = threading.current_thread()
        print(f'load into {t.ident} {t.name}')
        label_info = Glide.LabelInfo(label, place_holder, error_place_holder)
        self.label_mapping[url] = label_info
        if place_holder is not None:
            label.setPixmap(place_holder)
        runnable = Glide.LoadImageRunnable(url, width, height, self.image_loaded)
        self.thread_pool.start(runnable)

    def on_image_loaded(self, result):
        t = threading.current_thread()
        print(f'on image loaded at {t.ident}, {t.name}')
        url, q_image = result
        label_info = self.label_mapping.pop(url)
        if q_image is not None:
            pixmap = QPixmap.fromImage(q_image)
            label_info.label.setPixmap(pixmap)
            print(f'{label_info.label.width()}, {label_info.label.height()}')
        else:
            if label_info.error_place_holder is not None:
                label_info.label.setPixmap(label_info.error_place_holder)


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.glide = Glide()
        v_layout = QVBoxLayout()
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)
        label_0 = QLabel()
        label_0.setFixedSize(640, 360)
        label_0.setAlignment(Qt.AlignCenter)
        label_1 = QLabel()
        label_1.setFixedSize(640, 110)
        label_1.setStyleSheet("background-color:blue")
        v_layout.addWidget(label_0)
        v_layout.addWidget(label_1)
        self.setFixedSize(650, 480)
        self.setStyleSheet("background-color: red")
        self.setLayout(v_layout)
        place_holder = QPixmap.fromImage(QImage('loading.jpeg')).scaled(160, 90, aspectRatioMode=Qt.KeepAspectRatio,
                                                                        transformMode=Qt.SmoothTransformation)
        error_place_holder = QPixmap.fromImage(QImage('error.jpeg')).scaled(160, 90, aspectRatioMode=Qt.KeepAspectRatio,
                                                                            transformMode=Qt.SmoothTransformation)
        self.glide.load_into(label_0, "https://live.staticflickr.com/65535/49251422908_591245c64a_c_d.jpg",
                             label_0.width(),
                             label_0.height(), place_holder, error_place_holder)


def test():
    app = QApplication([])
    widget = TestWidget()
    widget.show()
    app.exec()


if __name__ == '__main__':
    test()
