# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_container(object):
    def setupUi(self, container):
        container.setObjectName("container")
        container.resize(800, 400)
        self.video_widget = QVideoWidget(container)
        self.video_widget.setGeometry(QtCore.QRect(80, 20, 640, 360))
        self.video_widget.setObjectName("video_widget")

        self.retranslateUi(container)
        QtCore.QMetaObject.connectSlotsByName(container)

    def retranslateUi(self, container):
        _translate = QtCore.QCoreApplication.translate
        container.setWindowTitle(_translate("container", "Form"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
