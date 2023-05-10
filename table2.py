from datetime import datetime
import sys
from interface.tabletour import *
from interface.addtour import *
from table import *
from main import *
#from interface.tableorder import *
from interface.tabledisc import *
from interface.tablework import *
from interface.tablecl import *
from interface.addcl import *
from check_db import *
from interface.tableorder import *
from interface.addorder import *

import threading

class InterfaceTour(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form10()
        self.ui.setupUi(self)
        self.it = AddTour()
        self.ifood = InterfaceFood()
        self.hotel = InterfaceHotel()
        self.country = InterfaceCountry()
        self.type = InterfaceType()
        self.ao = AddOrder()
        self.clients = None
        self.worker = None

        self.ui.tableWidget.setSortingEnabled(True)
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)
        self.line = self.ui.lineEdit
        self.check = self.ui.checkBox
        self.push3 = self.ui.pushButton_3
        self.push4 = self.ui.pushButton_4
        self.push5 = self.ui.pushButton_5
        self.push10 = self.ui.pushButton_10
        self.push11 = self.ui.pushButton_11
        self.check13 = self.ui.checkBox_13

        self.ui.pushButton_3.clicked.connect(self.addopen)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.dbtour)
        self.ui.pushButton_5.clicked.connect(self.deltour)
        self.ui.pushButton_4.clicked.connect(self.cell_clicked)
        self.ui.pushButton_7.clicked.connect(self.selectfood)
        self.ui.pushButton_6.clicked.connect(self.selecthotel)
        self.ui.pushButton_8.clicked.connect(self.selecttype)
        self.ui.pushButton_9.clicked.connect(self.selectcountry)
        self.ui.pushButton_11.clicked.connect(self.orderopen)
        self.ui.pushButton_10.clicked.connect(self.choisetour)
        self.ui.pushButton_12.clicked.connect(self.print)

    def print(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.tableWidget.item(row, col).text())
                except:
                    tmp.append('Нет данных')
            data.append(tmp)

        data_for_word = []
        for i in data:
            data_for_word.append(i)

        # добавляем таблицу
        doc = docx.Document()
        table = doc.add_table(rows=len(data_for_word), cols=8)
        # применяем стиль для таблицы
        table.style = 'Table Grid'

        for row in range(len(data_for_word)):
            for col in range(8):
                # получаем ячейку таблицы
                cell = table.cell(row, col)
                # записываем в ячейку данные
                cell.text = str(data_for_word[row][col])

        doc.save('D://туры.docx')
        QtWidgets.QMessageBox.about(self, 'Оповещение', "файл сохранен на диск D")

    def orderopen(self):
        if self.ao.name.currentText() == "":
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете тур!")
        else:
            self.ao.show()
            self.ao.addcheck()
            self.ao.but2.hide()
            self.ao.but.show()
            self.ao.label2.hide()
            self.ao.label.show()
            self.ao.id.hide()
            self.ao.cl.setEditText(self.clients)
            self.ao.work.setEditText(self.worker)
            self.hide()

    def selectfood(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 4).text()
        if self.ui.tableWidget.item(row, 4).isSelected():
            self.ifood.show()
            self.ifood.line.setText(name)
            self.ifood.check.setChecked(True)
            self.ifood.dbfood()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете тип питания!")

    def selecthotel(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 5).text()
        if self.ui.tableWidget.item(row, 5).isSelected():
            self.hotel.show()
            self.hotel.line.setText(name)
            self.hotel.check.setChecked(True)
            self.hotel.dbhotel()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете отель!")

    def selecttype(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 6).text()
        if self.ui.tableWidget.item(row, 6).isSelected():
            self.type.show()
            self.type.line.setText(name)
            self.type.check.setChecked(True)
            self.type.dbtype()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете тип тура!")

    def selectcountry(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 7).text()
        if self.ui.tableWidget.item(row, 7).isSelected():
            self.country.show()
            self.country.line.setText(name)
            self.country.check.setChecked(True)
            self.country.dbcountry()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете страну!")

    def closes(self):
        self.close()

    def dbtour(self):
        threading.Timer(15, self.dbtour).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        if self.ui.checkBox_2.isChecked() == True:
            b = ">"
            inf2 = self.ui.lineEdit_2.text()
        elif self.ui.checkBox_3.isChecked() == True:
            b = "<"
            inf2 = self.ui.lineEdit_2.text()
        elif self.ui.checkBox_4.isChecked() == True:
            b = "="
            inf2 = self.ui.lineEdit_2.text()
        else:
            b = "LIKE"
            inf2 = "%"
        if self.ui.checkBox_6.isChecked() == True:
            a = ">"
            inf3 = self.ui.lineEdit_3.text()
        elif self.ui.checkBox_7.isChecked() == True:
            a = "<"
            inf3 = self.ui.lineEdit_3.text()
        elif self.ui.checkBox_5.isChecked() == True:
            a = "="
            inf3 = self.ui.lineEdit_3.text()
        else:
            a = "LIKE"
            inf3 = "%"
        if self.ui.checkBox_9.isChecked() == True:
            inf4 = "Да"
        elif self.ui.checkBox_8.isChecked() == True:
            inf4 = "Нет"
        else:
            inf4 = "%"
        if self.ui.checkBox_11.isChecked() == True:
            inf5 = self.ui.lineEdit_4.text()
        else:
            inf5 = "%"
        if self.ui.checkBox_10.isChecked() == True:
            inf7 = self.ui.lineEdit_6.text()
        else:
            inf7 = "%"
        if self.ui.checkBox_12.isChecked() == True:
            inf8 = self.ui.lineEdit_7.text()
        else:
            inf8 = "%"
        if self.ui.checkBox_13.isChecked() == True:
            c = 1
        else:
            c = 0
        if self.ui.checkBox_14.isChecked() == True:
            inf9 = self.ui.lineEdit_8.text()
        else:
            inf9 = "%"
        if self.ui.checkBox_15.isChecked() == True:
            inf10 = self.ui.lineEdit_5.text()
        else:
            inf10 = "%"
        if self.ui.checkBox_16.isChecked() == True:
            inf11 = self.ui.lineEdit_9.text()
        else:
            inf11 = "%"
        self.check_db.thr_dbtour(inf1, inf2, inf3, inf4, inf5, inf7, inf8, inf9, inf10, inf11, a, b, c)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, row[1])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, item)
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget.resizeColumnsToContents()

    def choisetour(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 0).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Выбор', 'Выбрать тур ' + a + '?',
                                 massage.Yes | massage.No)
        if value == massage.Yes:
            self.ao.name.setEditText(a)
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Тур выбран")
        else:
            massage.close()

    def deltour(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 0).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Удаление', 'Вы действительно хотите удалить тур ' + a + '?',
                                 massage.Yes | massage.No)
        if value == massage.Yes:
            self.check_db.thr_deltour(a)
        else:
            massage.close()

    def signal_handler2(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def cell_clicked(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        days = self.ui.tableWidget.item(row, 1).text()
        price = self.ui.tableWidget.item(row, 2).text()
        burn = self.ui.tableWidget.item(row, 3).text()
        food = self.ui.tableWidget.item(row, 4).text()
        hotel = self.ui.tableWidget.item(row, 5).text()
        type = self.ui.tableWidget.item(row, 6).text()
        country = self.ui.tableWidget.item(row, 7).text()
        self.it.show()
        self.it.addcheck()
        self.it.name2.setText(name)
        self.it.days.setText(days)
        self.it.price.setText(price)
        self.it.burn.setEditText(burn)
        self.it.food.setEditText(food)
        self.it.hotel.setEditText(hotel)
        self.it.type.setEditText(type)
        self.it.country.setEditText(country)
        self.it.name.hide()
        self.it.name2.show()
        self.it.but.hide()
        self.it.but2.show()
        self.it.label.hide()
        self.it.label2.show()

    def addopen(self):
        self.it.show()
        self.it.addcheck()
        self.it.name2.hide()
        self.it.name.show()
        self.it.but2.hide()
        self.it.but.show()
        self.it.label2.hide()
        self.it.label.show()

class AddTour(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form51()
        self.ui.setupUi(self)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_4]
        self.base_line_edit1 = [self.ui.lineEdit_3, self.ui.lineEdit_2, self.ui.lineEdit_4]
        self.ui.pushButton.clicked.connect(self.addtour)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton_3.clicked.connect(self.changetour)
        self.name = self.ui.lineEdit
        self.name2 = self.ui.lineEdit_3
        self.days = self.ui.lineEdit_2
        self.price = self.ui.lineEdit_4
        self.burn = self.ui.comboBox
        self.food = self.ui.comboBox_2
        self.hotel = self.ui.comboBox_3
        self.type = self.ui.comboBox_4
        self.country = self.ui.comboBox_5
        self.but = self.ui.pushButton
        self.but2 = self.ui.pushButton_3
        self.label = self.ui.label
        self.label2 = self.ui.label_2

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)
        self.check_db.mysignal2.connect(self.signal_handler3)
        self.check_db.mysignal3.connect(self.signal_handler4)
        self.check_db.mysignal7.connect(self.signal_handler5)
        self.check_db.mysignal4.connect(self.signal_handler6)

    def addcheck(self):
        a = 1
        self.check_db.thr_addchecktour(a)

    def signal_handler(self, value):
        print(len(value))
        for i, row in enumerate(value):
            self.ui.comboBox_2.addItem(row[0])

    def signal_handler2(self, value):
        self.ui.comboBox_3.addItem("Без отеля")
        for i, row in enumerate(value):
            self.ui.comboBox_3.addItem(row[0])

    def signal_handler3(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_4.addItem(row[0])

    def signal_handler4(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_5.addItem(row[0])

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    def check_input2(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit1:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    @check_input
    def addtour(self):
        name = self.ui.lineEdit.text()
        days = self.ui.lineEdit_2.text()
        price = self.ui.lineEdit_4.text()
        burn = self.ui.comboBox.currentText()
        food = self.ui.comboBox_2.currentText()
        hot = self.ui.comboBox_3.currentText()
        type = self.ui.comboBox_4.currentText()
        country = self.ui.comboBox_5.currentText()
        self.check_db.thr_addtour(name, days, price, burn, food, hot, type, country)

    def signal_handler5(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input2
    def changetour(self):
        name = self.ui.lineEdit_3.text()
        days = self.ui.lineEdit_2.text()
        price = self.ui.lineEdit_4.text()
        burn = self.ui.comboBox.currentText()
        food = self.ui.comboBox_2.currentText()
        hot = self.ui.comboBox_3.currentText()
        type = self.ui.comboBox_4.currentText()
        country = self.ui.comboBox_5.currentText()
        self.check_db.thr_changetour(name, days, price, burn, food, hot, type, country)

    def signal_handler6(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def closes(self):
        self.close()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_2.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox_5.clear()


class InterfaceWorker(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form011()
        self.ui.setupUi(self)
        self.ir = InterfaceReg()

        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.dbworker)
        self.ui.pushButton_5.clicked.connect(self.delworker)
        self.ui.pushButton_3.clicked.connect(self.openadd)
        self.ui.pushButton_4.clicked.connect(self.cell_clicked)
        self.ui.pushButton_6.clicked.connect(self.print)
        self.line = self.ui.lineEdit_8
        self.check = self.ui.checkBox_10

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)

    def print(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.tableWidget.item(row, col).text())
                except:
                    tmp.append('Нет данных')
            data.append(tmp)

        data_for_word = []
        for i in data:
            data_for_word.append(i)

        # добавляем таблицу
        doc = docx.Document()
        table = doc.add_table(rows=len(data_for_word), cols=9)
        # применяем стиль для таблицы
        table.style = 'Table Grid'

        for row in range(len(data_for_word)):
            for col in range(9):
                # получаем ячейку таблицы
                cell = table.cell(row, col)
                # записываем в ячейку данные
                cell.text = str(data_for_word[row][col])

        doc.save('D://сотрудники.docx')
        QtWidgets.QMessageBox.about(self, 'Оповещение', "файл сохранен на диск D")

    def closes(self):
        self.close()

    def dbworker(self):
        threading.Timer(15, self.dbworker).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        if self.ui.checkBox_2.isChecked() == True:
            inf2 = self.ui.lineEdit_2.text()
        else:
            inf2 = "%"
        if self.ui.checkBox_3.isChecked() == True:
            inf3 = self.ui.lineEdit_3.text()
            i = ">"
        elif self.ui.checkBox_4.isChecked() == True:
            inf3 = self.ui.lineEdit_3.text()
            i = "<"
        elif self.ui.checkBox_5.isChecked() == True:
            inf3 = self.ui.lineEdit_3.text()
            i = "="
        else:
            inf3 = "%"
            i = "LIKE"
        if self.ui.checkBox_6.isChecked() == True:
            inf4 = self.ui.lineEdit_4.text()
        else:
            inf4 = "%"
        if self.ui.checkBox_7.isChecked() == True:
            inf5 = self.ui.lineEdit_5.text()
        else:
            inf5 = "%"
        if self.ui.checkBox_8.isChecked() == True:
            inf6 = self.ui.lineEdit_6.text()
        else:
            inf6 = "%"
        if self.ui.checkBox_9.isChecked() == True:
            inf7 = self.ui.lineEdit_7.text()
        else:
            inf7 = "%"
        if self.ui.checkBox_10.isChecked() == True:
            inf8 = self.ui.lineEdit_8.text()
        else:
            inf8 = "%"
        self.check_db.thr_dbworker(inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, i)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.resizeRowsToContents()

    def delworker(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 8).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Удаление', 'Вы действительно хотите удалить работника ' + a + '?',
                                 massage.Yes | massage.No)
        if value == massage.Yes:
            self.check_db.thr_delworker(a)
        else:
            massage.close()

    def signal_handler2(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def cell_clicked(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        date = self.ui.tableWidget.item(row, 1).text()
        date1 = datetime.strptime(date, "%d.%m.%Y").date()
        sall = self.ui.tableWidget.item(row, 2).text()
        post = self.ui.tableWidget.item(row, 3).text()
        numb = self.ui.tableWidget.item(row, 4).text()
        role = self.ui.tableWidget.item(row, 5).text()
        addr = self.ui.tableWidget.item(row, 6).text()
        sp = self.ui.tableWidget.item(row, 7).text()
        login = self.ui.tableWidget.item(row, 8).text()
        self.ir.fio.setText(name)
        self.ir.date.setDate(date1)
        self.ir.sal.setText(sall)
        self.ir.post.setText(post)
        self.ir.number.setText(numb)
        self.ir.role.setEditText(role)
        self.ir.addr.setText(addr)
        self.ir.sp.setEditText(sp)
        self.ir.login1.setText(login)
        self.ir.show()
        self.ir.label.show()
        self.ir.label1.hide()
        self.ir.login1.show()
        self.ir.login.hide()
        self.ir.push1.show()
        self.ir.push.hide()
        self.ir.labelpssw.hide()
        self.ir.passw.hide()

    def openadd(self):
        self.ir.show()
        self.ir.label1.show()
        self.ir.label.hide()
        self.ir.login.show()
        self.ir.login1.hide()
        self.ir.push.show()
        self.ir.push1.hide()
        self.ir.labelpssw.show()
        self.ir.passw.show()

class InterfaceClients(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form012()
        self.ui.setupUi(self)
        self.ac = AddCl()
        self.order = AddOrder()
        self.it = InterfaceTour()
        self.login = None

        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.pushButton_3.clicked.connect(self.openadd)
        self.ui.pushButton_5.clicked.connect(self.delcl)
        self.ui.pushButton_4.clicked.connect(self.cell_clicked)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton_8.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.dbclients)
        self.ui.pushButton_6.clicked.connect(self.choicecl)
        self.ui.pushButton_7.clicked.connect(self.orderopen)
        self.ui.pushButton_10.clicked.connect(self.print)
        self.line = self.ui.lineEdit_4
        self.check = self.ui.checkBox_4
        self.push6 = self.ui.pushButton_6
        self.push7 = self.ui.pushButton_7
        self.push8 = self.ui.pushButton_8
        self.push2 = self.ui.pushButton_2
        self.push5 = self.ui.pushButton_5
        self.push3 = self.ui.pushButton_3

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)

    def print(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.tableWidget.item(row, col).text())
                except:
                    tmp.append('Нет данных')
            data.append(tmp)

        data_for_word = []
        for i in data:
            data_for_word.append(i)

        # добавляем таблицу
        doc = docx.Document()
        table = doc.add_table(rows=len(data_for_word), cols=5)
        # применяем стиль для таблицы
        table.style = 'Table Grid'

        for row in range(len(data_for_word)):
            for col in range(5):
                # получаем ячейку таблицы
                cell = table.cell(row, col)
                # записываем в ячейку данные
                cell.text = str(data_for_word[row][col])

        doc.save('D://клиенты.docx')
        QtWidgets.QMessageBox.about(self, 'Оповещение', "файл сохранен на диск D")

    def orderopen(self):
        if self.order.cl.currentText() == "":
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете клиента!")
        else:
            self.it.show()
            self.it.push3.hide()
            self.it.push4.hide()
            self.it.push5.hide()
            self.it.push10.show()
            self.it.push11.show()
            self.it.check13.setChecked(True)
            self.it.dbtour()
            self.close()

    def choicecl(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 0).text()
        b = self.ui.tableWidget.item(row, 4).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Подтверждение', 'Выбрать клиента ' + a + '?', massage.Yes | massage.No)
        if value == massage.Yes:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Клиент выбран")
            self.order.cl.setEditText(b)
            self.it.clients = b
            self.it.worker = self.login
        else:
            massage.close()

    def closes(self):
        self.close()

    def dbclients(self):
        threading.Timer(15, self.dbclients).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        if self.ui.checkBox_2.isChecked() == True:
            inf2 = self.ui.lineEdit_2.text()
        else:
            inf2 = "%"
        if self.ui.checkBox_3.isChecked() == True:
            inf3 = self.ui.lineEdit_3.text()
        else:
            inf3 = "%"
        if self.ui.checkBox_4.isChecked() == True:
            inf4 = self.ui.lineEdit_4.text()
        else:
            inf4 = "%"
        self.check_db.thr_dbclients(inf1, inf2, inf3, inf4)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.resizeColumnsToContents()

    def delcl(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 0).text()
        b = self.ui.tableWidget.item(row, 4).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Удаление', 'Вы действительно хотите удалить клиента ' + a + '?', massage.Yes | massage.No)
        if value == massage.Yes:
           self.check_db.thr_delcl(b)
        else:
           massage.close()

    def signal_handler2(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def cell_clicked(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        addr = self.ui.tableWidget.item(row, 1).text()
        numb = self.ui.tableWidget.item(row, 2).text()
        date = self.ui.tableWidget.item(row, 3).text()
        date1 = datetime.strptime(date, "%d.%m.%Y").date()
        passp = self.ui.tableWidget.item(row, 4).text()
        self.ac.nameline2.setText(passp)
        self.ac.addr.setText(addr)
        self.ac.numb.setText(numb)
        self.ac.date.setDate(date1)
        self.ac.nameline.setText(name)
        self.ac.show()
        self.ac.push.hide()
        self.ac.push2.show()
        self.ac.label.hide()
        self.ac.label2.show()
        self.ac.nameline2.show()
        self.ac.pasp.hide()

    def openadd(self):
        self.ac.show()
        self.ac.push2.hide()
        self.ac.push.show()
        self.ac.label2.hide()
        self.ac.label.show()
        self.ac.pasp.show()
        self.ac.nameline2.hide()

class AddCl(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form112()
        self.ui.setupUi(self)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler1)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_4, self.ui.lineEdit_5]
        self.base_line_edit1 = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_4, self.ui.lineEdit_3]
        self.nameline = self.ui.lineEdit
        self.nameline2 = self.ui.lineEdit_3
        self.addr = self.ui.lineEdit_2
        self.numb = self.ui.lineEdit_4
        self.pasp = self.ui.lineEdit_5
        self.date = self.ui.dateEdit
        self.push = self.ui.pushButton
        self.push2 = self.ui.pushButton_3
        self.label = self.ui.label
        self.label2 = self.ui.label_2

        self.ui.pushButton.clicked.connect(self.addcl)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton_3.clicked.connect(self.changecl)


    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    def check_input1(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit1:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    @check_input
    def addcl(self):
        name = self.ui.lineEdit.text()
        addr = self.ui.lineEdit_2.text()
        numb = self.ui.lineEdit_4.text()
        date = self.ui.dateEdit.text()
        passp = self.ui.lineEdit_5.text()
        self.check_db.thr_addcl(name, addr, numb, date, passp)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input1
    def changecl(self):
        name = self.ui.lineEdit.text()
        addr = self.ui.lineEdit_2.text()
        numb = self.ui.lineEdit_4.text()
        date = self.ui.dateEdit.text()
        passp = self.ui.lineEdit_3.text()
        self.check_db.thr_changecl(name, addr, numb, date, passp)

    def signal_handler1(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def closes(self):
        self.close()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()

class InterfaceOrder(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form014()
        self.ui.setupUi(self)
        self.ao = AddOrder()
        self.iwork = InterfaceWorker()
        self.icl = InterfaceClients()
        self.disc = InterfaceDisc()
        self.tour = InterfaceTour()

        self.ui.tableWidget.setSortingEnabled(True)
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)
        self.check_db.mysignal2.connect(self.signal_handler3)

        self.ui.pushButton_3.clicked.connect(self.addopen)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.dborder)
        self.ui.pushButton_5.clicked.connect(self.delorder)
        self.ui.pushButton_4.clicked.connect(self.cell_clicked)
        self.ui.pushButton_8.clicked.connect(self.selectwork)
        self.ui.pushButton_6.clicked.connect(self.selectcl)
        self.ui.pushButton_9.clicked.connect(self.selectdisc)
        self.ui.pushButton_7.clicked.connect(self.selecttour)
        self.ui.pushButton_10.clicked.connect(self.print)
        self.check = self.ui.checkBox_7
        self.line = self.ui.lineEdit_5

    def print(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.tableWidget.item(row, col).text())
                except:
                    tmp.append('Нет данных')
            data.append(tmp)

        data_for_word = []
        for i in data:
            data_for_word.append(i)

        # добавляем таблицу
        doc = docx.Document()
        table = doc.add_table(rows=len(data_for_word), cols=7)
        # применяем стиль для таблицы
        table.style = 'Table Grid'

        for row in range(len(data_for_word)):
            for col in range(7):
                # получаем ячейку таблицы
                cell = table.cell(row, col)
                # записываем в ячейку данные
                cell.text = str(data_for_word[row][col])

        doc.save('D://заказы.docx')
        QtWidgets.QMessageBox.about(self, 'Оповещение', "файл сохранен на диск D")

    def selectwork(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 4).text()
        if self.ui.tableWidget.item(row, 4).isSelected():
            self.iwork.show()
            self.iwork.line.setText(name)
            self.iwork.check.setChecked(True)
            self.iwork.dbworker()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете логин работника!")

    def selectcl(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 5).text()
        if self.ui.tableWidget.item(row, 5).isSelected():
            self.icl.show()
            self.icl.line.setText(name)
            self.icl.check.setChecked(True)
            self.icl.dbclients()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете данные клиента!")

    def selectdisc(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 6).text()
        if self.ui.tableWidget.item(row, 6).isSelected():
            self.disc.show()
            self.disc.line.setText(name)
            self.disc.check.setChecked(True)
            self.disc.dbdisc()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете скидку!")

    def selecttour(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        if self.ui.tableWidget.item(row, 0).isSelected():
            self.tour.show()
            self.tour.line.setText(name)
            self.tour.check.setChecked(True)
            self.tour.dbtour()
            self.tour.check13.setChecked(True)
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', "Выберете название тура!")

    def closes(self):
        self.close()

    def dborder(self):
        threading.Timer(15, self.dborder).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        if self.ui.checkBox_2.isChecked() == True:
            inf2 = self.ui.lineEdit_2.text()
            a = ">"
        elif self.ui.checkBox_3.isChecked() == True:
            inf2 = self.ui.lineEdit_2.text()
            a = "<"
        elif self.ui.checkBox_4.isChecked() == True:
            inf2 = self.ui.lineEdit_2.text()
            a = "="
        else:
            inf2 = "%"
            a = "LIKE"
        if self.ui.checkBox_5.isChecked() == True:
            inf3 = self.ui.lineEdit_3.text()
        else:
            inf3 = "%"
        if self.ui.checkBox_6.isChecked() == True:
            inf4 = self.ui.lineEdit_4.text()
        else:
            inf4 = "%"
        if self.ui.checkBox_7.isChecked() == True:
            inf5 = self.ui.lineEdit_5.text()
        else:
            inf5 = "%"
        if self.ui.checkBox_8.isChecked() == True:
            inf6 = self.ui.lineEdit_6.text()
        else:
            inf6 = "%"
        self.check_db.thr_dborder(inf1, inf2, inf3, inf4, inf5, inf6, a)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.resizeColumnsToContents()

    def delorder(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        price = self.ui.tableWidget.item(row, 1).text()
        date1 = self.ui.tableWidget.item(row, 2).text()
        date2 = self.ui.tableWidget.item(row, 3).text()
        work = self.ui.tableWidget.item(row, 4).text()
        cl = self.ui.tableWidget.item(row, 5).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, 'Удаление', 'Вы действительно хотите удалить заказ ' + name + '\n'
                                 + 'Клиента ' + cl + 'от ' + date1 + "?",
                                 massage.Yes | massage.No)
        if value == massage.Yes:
            self.check_db.thr_delorder(name, price, date1, date2, work, cl)
        else:
            massage.close()

    def signal_handler2(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def cell_clicked(self):
        row = self.ui.tableWidget.currentItem().row()
        name = self.ui.tableWidget.item(row, 0).text()
        price = self.ui.tableWidget.item(row, 1).text()
        date1 = self.ui.tableWidget.item(row, 2).text()
        date11 = datetime.strptime(date1, "%d.%m.%Y").date()
        date2 = self.ui.tableWidget.item(row, 3).text()
        date22 = datetime.strptime(date2, "%d.%m.%Y").date()
        work = self.ui.tableWidget.item(row, 4).text()
        cl = self.ui.tableWidget.item(row, 5).text()
        disc = self.ui.tableWidget.item(row, 6).text()
        self.ao.show()
        self.ao.addcheck()
        self.ao.name.setEditText(name)
        self.ao.price.setText(price)
        self.ao.date1.setDate(date11)
        self.ao.date2.setDate(date22)
        self.ao.work.setEditText(work)
        self.ao.cl.setEditText(cl)
        self.ao.disc.setEditText(disc)
        self.ao.but.hide()
        self.ao.but2.show()
        self.ao.label.hide()
        self.ao.label2.show()
        self.ao.id.hide()
        self.check_db.thr_getid(name, price, date1, date2, work, cl)

    def signal_handler3(self, value):
        value1 = str(value)
        self.ao.id.setText(value1)

    def addopen(self):
        self.ao.show()
        self.ao.addcheck()
        self.ao.but2.hide()
        self.ao.but.show()
        self.ao.label2.hide()
        self.ao.label.show()
        self.ao.id.hide()

class AddOrder(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form114()
        self.ui.setupUi(self)

        self.base_line_edit = [self.ui.lineEdit]
        self.ui.pushButton_7.clicked.connect(self.price)
        self.ui.pushButton.clicked.connect(self.addorder)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton_3.clicked.connect(self.changeorder)
        self.name = self.ui.comboBox
        self.price = self.ui.lineEdit
        self.date1 = self.ui.dateEdit
        self.date2 = self.ui.dateEdit_2
        self.work = self.ui.comboBox_2
        self.cl = self.ui.comboBox_3
        self.disc = self.ui.comboBox_4
        self.but = self.ui.pushButton
        self.but2 = self.ui.pushButton_3
        self.label = self.ui.label
        self.label2 = self.ui.label_2
        self.id = self.ui.lineEdit_2

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)
        self.check_db.mysignal2.connect(self.signal_handler3)
        self.check_db.mysignal3.connect(self.signal_handler4)
        self.check_db.mysignal7.connect(self.signal_handler5)
        self.check_db.mysignal4.connect(self.signal_handler6)
        self.check_db.mysignal5.connect(self.signal_handler7)

    def price(self):
        price1 = self.ui.comboBox.currentText()
        price2 = self.ui.comboBox_4.currentText()
        self.check_db.thr_price(price1, price2)

    def signal_handler7(self, value):
        self.ui.lineEdit.setText(value)

    def addcheck(self):
        a = 1
        self.check_db.thr_addcheckorder(a)

    def signal_handler(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox.addItem(row[0])

    def signal_handler2(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_2.addItem(row[0])

    def signal_handler3(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_3.addItem(row[0])

    def signal_handler4(self, value):
        self.ui.comboBox_4.addItem("Без скидки")
        for i, row in enumerate(value):
            self.ui.comboBox_4.addItem(row[0])

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    @check_input
    def addorder(self):
        name = self.ui.comboBox.currentText()
        price = self.ui.lineEdit.text()
        date1 = self.ui.dateEdit.text()
        date2 = self.ui.dateEdit_2.text()
        work = self.ui.comboBox_2.currentText()
        cl = self.ui.comboBox_3.currentText()
        disc = self.ui.comboBox_4.currentText()
        self.check_db.thr_addorder(name, price, date1, date2, work, cl, disc)

    def signal_handler5(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def changeorder(self):
        name = self.ui.comboBox.currentText()
        price = self.ui.lineEdit.text()
        date1 = self.ui.dateEdit.text()
        date2 = self.ui.dateEdit_2.text()
        work = self.ui.comboBox_2.currentText()
        cl = self.ui.comboBox_3.currentText()
        disc = self.ui.comboBox_4.currentText()
        id = self.ui.lineEdit_2.text()
        self.check_db.thr_changeorder(name, price, date1, date2, work, cl, disc, id)

    def signal_handler6(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def closes(self):
        self.close()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_4.clear()

