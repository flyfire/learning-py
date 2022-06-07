import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets
from multiprocessing import Process, Manager, Queue
from queue import Empty as QueueEmpty

PROCESS_TIMEOUT = 10


class App(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.img_loader = ImageManager(self)
        self.img_loader.image_loaded.connect(self.on_image_loaded)
        self.img_loader.start()

        self.img_widgets = {}

        # gui

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        img_scroll_parent = QtWidgets.QWidget()
        self.scroll_area.setWidget(img_scroll_parent)
        self.img_layout = QtWidgets.QVBoxLayout()
        img_scroll_parent.setLayout(self.img_layout)

        go_btn = QtWidgets.QPushButton('go')
        go_btn.clicked.connect(self.start_loading_images)
        self.layout.addWidget(go_btn)

    def start_loading_images(self):
        load_dir = r''  # <---- path to directory with TONS of images!
        for fn in os.listdir(load_dir):
            path = os.path.join(load_dir, fn)
            if not os.path.isdir(path):
                if os.path.splitext(fn)[1] in ['.png', '.jpg']:
                    widget = QtWidgets.QLabel('...loading...')
                    widget.setScaledContents(True)
                    widget.setFixedHeight(100)
                    self.img_layout.addWidget(widget)

                    self.img_widgets[fn] = widget
                    self.img_loader.load_image(path)

    def on_image_loaded(self, path, qimage):
        fn = os.path.split(path)[1]
        if fn in self.img_widgets:
            widget = self.img_widgets[fn]
            pixmap = QtGui.QPixmap(qimage)
            if pixmap.isNull():
                print(f'Error loading {fn}')
                return

            h = pixmap.height()
            w = pixmap.width()
            widget.setText('')
            widget.setFixedWidth(int((widget.height() * w) / h))  # this was the fastest way I could find to set an image on a label and maintain aspect ratio.
            widget.setPixmap(pixmap)

    def closeEvent(self, event):
        self.img_loader.shutdown()
        super().closeEvent(event)


class ImageManager(QtCore.QObject):
    image_loaded = QtCore.pyqtSignal(str, QtGui.QImage)

    def __init__(self, parent):
        super().__init__(parent)
        self.work_queue = Queue()
        self.done_queue = Queue()
        self.manager = Manager()
        self.img_list = self.manager.list()

        self.signal_thread = self.SignalEmitter(self, self.done_queue, self.img_list)
        self.signal_thread.imgLoaded.connect(self._emit_image)

        self.proc_count = 4
        self.bg_procs = []
        for _ in range(self.proc_count):
            bg_proc = Process(target=self._worker, args=(self.work_queue, self.done_queue, self.img_list,))
            self.bg_procs.append(bg_proc)

    def start(self):
        self.signal_thread.start()
        for p in self.bg_procs:
            p.start()

    def shutdown(self):
        # empty queues and insert poison pills
        while not self.work_queue.empty():
            self.work_queue.get()
        for _ in range(self.proc_count):
            self.work_queue.put(None)

        while not self.done_queue.empty():
            self.done_queue.get()
        self.done_queue.put(None)

        # ensure everything shuts down
        self.signal_thread.wait()
        for p in self.bg_procs:
            p.join()
        print('Image manager shutting down')

    def _emit_image(self, path, qimage):
        self.image_loaded.emit(path, qimage)

    def load_image(self, path):
        self.work_queue.put(path)
        print(f'Added {os.path.split(path)[1]} to queue.')

        dead_procs = []
        for p in self.bg_procs:
            if not p.is_alive():
                dead_procs.append(p)

        for p in dead_procs:
            self.bg_procs.remove(p)

        for _ in range(len(dead_procs)):
            bg_proc = Process(target=self._worker, args=(self.work_queue, self.done_queue, self.img_list,))
            self.bg_procs.append(bg_proc)
            bg_proc.start()

    class SignalEmitter(QtCore.QThread):
        imgLoaded = QtCore.pyqtSignal(str, QtGui.QImage)

        def __init__(self, parent, done_queue, img_list):
            super().__init__(parent)
            self.done_queue = done_queue
            self.img_list = img_list

        def run(self):
            while True:
                try:
                    img_path = self.done_queue.get(timeout=PROCESS_TIMEOUT)
                except QueueEmpty:
                    print("Queue empty, shutting down.")
                    return

                if img_path == None:
                    break

                while len(self.img_list) > 0:
                    img_data = self.img_list[0]
                    image = bytearray_to_qimage(img_data['bytes'])
                    self.imgLoaded.emit(img_data['path'], image)
                    self.img_list.pop(0)

            print('Signal emitter shutting down.')

    @staticmethod
    def _worker(work_queue, done_queue, list):
        while True:
            path = work_queue.get()
            if path == None:
                break

            qimg = QtGui.QImage(path)
            img_dict = {
                'bytes': qimage_to_bytearray(qimg),
                'path': path
            }

            list.append(img_dict)
            done_queue.put(path)

        print("BG Proc shutting down.")
        return


def qimage_to_bytearray(qimage):
    byte_array = QtCore.QByteArray()
    stream = QtCore.QDataStream(byte_array, QtCore.QIODevice.WriteOnly)
    stream << qimage
    return byte_array


def bytearray_to_qimage(byte_array):
    img = QtGui.QImage()
    stream = QtCore.QDataStream(byte_array, QtCore.QIODevice.ReadOnly)
    stream >> img
    return img
