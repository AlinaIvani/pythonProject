# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(467, 468)
        self.label_16 = QtWidgets.QLabel(Form3)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 411, 441))
        self.label_16.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(Form3)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 391, 41))
        self.pushButton.setStyleSheet("font: 18pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form3)
        self.textEdit.setGeometry(QtCore.QRect(40, 110, 391, 221))
        self.textEdit.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form3)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 391, 29))
        self.lineEdit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form3)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 239, 16))
        self.label_5.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form3)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 239, 20))
        self.label_6.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form3)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 390, 391, 41))
        self.pushButton_2.setStyleSheet("font: 18pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Смена данных"))
        self.pushButton.setText(_translate("Form3", "Отправить"))
        self.lineEdit.setToolTip(_translate("Form3", "<html><head/><body><p>gggg</p></body></html>"))
        self.label_5.setText(_translate("Form3", "Логин:"))
        self.label_6.setText(_translate("Form3", "Запрос:"))
        self.pushButton_2.setText(_translate("Form3", "Закрыть"))