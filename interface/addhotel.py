# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addhotel.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form01(object):
    def setupUi(self, Form01):
        Form01.setObjectName("Form01")
        Form01.resize(548, 678)
        self.label_10 = QtWidgets.QLabel(Form01)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 491, 651))
        self.label_10.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(Form01)
        self.label.setGeometry(QtCore.QRect(130, 20, 301, 51))
        self.label.setStyleSheet("font: 27pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form01)
        self.label_5.setGeometry(QtCore.QRect(50, 80, 239, 16))
        self.label_5.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form01)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 461, 29))
        self.lineEdit.setToolTipDuration(-4)
        self.lineEdit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form01)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 160, 461, 29))
        self.lineEdit_2.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Form01)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 239, 21))
        self.label_6.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form01)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 239, 21))
        self.label_7.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Form01)
        self.comboBox.setGeometry(QtCore.QRect(50, 220, 461, 31))
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form01)
        self.textEdit.setGeometry(QtCore.QRect(50, 280, 461, 251))
        self.textEdit.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(Form01)
        self.label_8.setGeometry(QtCore.QRect(50, 260, 281, 21))
        self.label_8.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form01)
        self.pushButton.setGeometry(QtCore.QRect(50, 560, 461, 41))
        self.pushButton.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form01)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 610, 461, 41))
        self.pushButton_2.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(Form01)
        self.label_9.setGeometry(QtCore.QRect(50, 530, 271, 21))
        self.label_9.setStyleSheet("font: 13pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(Form01)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 560, 461, 41))
        self.pushButton_3.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form01)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 331, 51))
        self.label_2.setStyleSheet("font: 27pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form01)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 100, 461, 29))
        self.lineEdit_3.setToolTipDuration(-4)
        self.lineEdit_3.setStyleSheet("font: 15pt \"Century Gothic\";\n"
"color: rgb(75, 75, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form01)
        QtCore.QMetaObject.connectSlotsByName(Form01)

    def retranslateUi(self, Form01):
        _translate = QtCore.QCoreApplication.translate
        Form01.setWindowTitle(_translate("Form01", "Отели"))
        self.label.setText(_translate("Form01", "<html><head/><body><p align=\"center\">Добавить отель</p></body></html>"))
        self.label_5.setText(_translate("Form01", "Название:"))
        self.lineEdit.setToolTip(_translate("Form01", "<html><head/><body><p>gggg</p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Form01", "<html><head/><body><p>gggg</p></body></html>"))
        self.label_6.setText(_translate("Form01", "Город:"))
        self.label_7.setText(_translate("Form01", "Количество звезд:"))
        self.comboBox.setItemText(0, _translate("Form01", "4"))
        self.comboBox.setItemText(1, _translate("Form01", "5"))
        self.comboBox.setItemText(2, _translate("Form01", "3"))
        self.comboBox.setItemText(3, _translate("Form01", "2"))
        self.comboBox.setItemText(4, _translate("Form01", "1"))
        self.label_8.setText(_translate("Form01", "Дополнительная информация:*"))
        self.pushButton.setText(_translate("Form01", "Добавить"))
        self.pushButton_2.setText(_translate("Form01", "Закрыть"))
        self.label_9.setText(_translate("Form01", "  * - Необязательное поле"))
        self.pushButton_3.setText(_translate("Form01", "Изменить"))
        self.label_2.setText(_translate("Form01", "<html><head/><body><p align=\"center\">Изменить данные</p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Form01", "<html><head/><body><p>gggg</p></body></html>"))
