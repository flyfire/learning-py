# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'container.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Container(object):
    def setupUi(self, Container):
        Container.setObjectName("Container")
        Container.resize(720, 1080)
        self.question_container = QtWidgets.QWidget(Container)
        self.question_container.setGeometry(QtCore.QRect(0, 324, 720, 400))
        self.question_container.setObjectName("question_container")

        self.retranslateUi(Container)
        QtCore.QMetaObject.connectSlotsByName(Container)

    def retranslateUi(self, Container):
        _translate = QtCore.QCoreApplication.translate
        Container.setWindowTitle(_translate("Container", "Form"))
