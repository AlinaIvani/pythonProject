# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form4(object):
    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.resize(664, 555)
        self.tableWidget = QtWidgets.QTableWidget(Form4)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 581, 311))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.label_20 = QtWidgets.QLabel(Form4)
        self.label_20.setGeometry(QtCore.QRect(20, 10, 621, 521))
        self.label_20.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_4 = QtWidgets.QLabel(Form4)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 551, 51))
        self.label_4.setStyleSheet("font: 25pt \"Century Gothic\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 158, 88);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form4)
        self.pushButton.setGeometry(QtCore.QRect(130, 410, 411, 51))
        self.pushButton.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form4)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 470, 411, 51))
        self.pushButton_2.setStyleSheet("font: 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 50px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 158, 88);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_20.raise_()
        self.tableWidget.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form4", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form4", "Логин работника"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form4", "Запрос"))
        self.label_4.setText(_translate("Form4", "Запросы на изменение данных"))
        self.pushButton.setText(_translate("Form4", "Выполнить запрос"))
        self.pushButton_2.setText(_translate("Form4", "Закрыть"))
