# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_scale_container.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test_scale_container(object):
    def setupUi(self, test_scale_container):
        test_scale_container.setObjectName("test_scale_container")
        test_scale_container.resize(722, 746)
        self.scale_animation_container = QtWidgets.QWidget(test_scale_container)
        self.scale_animation_container.setGeometry(QtCore.QRect(130, 210, 411, 301))
        self.scale_animation_container.setObjectName("scale_animation_container")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scale_animation_container)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setSpacing(0)
        self.v_layout.setObjectName("v_layout")
        self.label_0 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_0.setStyleSheet("background-color: rgb(199, 255, 108);")
        self.label_0.setObjectName("label_0")
        self.v_layout.addWidget(self.label_0)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setStyleSheet("background-color: rgb(90, 73, 255);")
        self.label_1.setObjectName("label_1")
        self.v_layout.addWidget(self.label_1)
        self.start = QtWidgets.QPushButton(test_scale_container)
        self.start.setGeometry(QtCore.QRect(240, 60, 100, 32))
        self.start.setObjectName("start")

        self.retranslateUi(test_scale_container)
        QtCore.QMetaObject.connectSlotsByName(test_scale_container)

    def retranslateUi(self, test_scale_container):
        _translate = QtCore.QCoreApplication.translate
        test_scale_container.setWindowTitle(_translate("test_scale_container", "test_scale_container"))
        self.label_0.setText(_translate("test_scale_container", "TextLabel"))
        self.label_1.setText(_translate("test_scale_container", "TextLabel"))
        self.start.setText(_translate("test_scale_container", "start"))