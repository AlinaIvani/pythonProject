# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfood.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form31(object):
    def setupUi(self, Form31):
        Form31.setObjectName("Form31")
        Form31.resize(504, 480)
        self.label_10 = QtWidgets.QLabel(Form31)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 481, 451))
        self.label_10.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(Form31)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 331, 51))
        self.label_2.setStyleSheet("font: 27pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form31)
        self.label.setGeometry(QtCore.QRect(60, 10, 401, 51))
        self.label.setStyleSheet("font: 27pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form31)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 90, 461, 29))
        self.lineEdit_3.setToolTipDuration(-4)
        self.lineEdit_3.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form31)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 239, 16))
        self.label_5.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form31)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 461, 29))
        self.lineEdit.setToolTipDuration(-4)
        self.lineEdit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(Form31)
        self.label_8.setGeometry(QtCore.QRect(20, 130, 281, 31))
        self.label_8.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(Form31)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 461, 181))
        self.textEdit.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form31)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 461, 41))
        self.pushButton_2.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form31)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 350, 461, 41))
        self.pushButton_3.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form31)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 461, 41))
        self.pushButton.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form31)
        QtCore.QMetaObject.connectSlotsByName(Form31)

    def retranslateUi(self, Form31):
        _translate = QtCore.QCoreApplication.translate
        Form31.setWindowTitle(_translate("Form31", "Питание"))
        self.label_2.setText(_translate("Form31", "<html><head/><body><p align=\"center\">Изменить данные</p></body></html>"))
        self.label.setText(_translate("Form31", "<html><head/><body><p align=\"center\">Добавить тип питания</p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Form31", "<html><head/><body><p>gggg</p></body></html>"))
        self.label_5.setText(_translate("Form31", "Тип питания:"))
        self.lineEdit.setToolTip(_translate("Form31", "<html><head/><body><p>gggg</p></body></html>"))
        self.label_8.setText(_translate("Form31", "Описание:"))
        self.pushButton_2.setText(_translate("Form31", "Закрыть"))
        self.pushButton_3.setText(_translate("Form31", "Изменить"))
        self.pushButton.setText(_translate("Form31", "Добавить"))
