# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(323, 251)
        Form.setTabletTracking(False)
        Form.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 239, 71))
        self.label.setStyleSheet("font: 27pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 241, 35))
        self.pushButton.setStyleSheet("font: 19pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 100, 241, 29))
        self.lineEdit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 140, 241, 29))
        self.lineEdit_2.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 261, 221))
        self.label_10.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.pushButton.setText(_translate("Form", "Вход"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p>gggg</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Логин.."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Пароль.."))