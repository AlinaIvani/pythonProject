import sys

from PyQt5.QtWidgets import QInputDialog

from table import *
from table2 import *
from interface.auth import *
from interface.reg import *
from interface.change import *
from interface.main1 import *
from interface.test import *
from interface.admchange import *
from check_db import *
import threading



class InterfaceReg(QtWidgets.QWidget): #окно регистрации
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton_3.clicked.connect(self.change)
        self.base_line_edit = [self.ui.lineEdit_4, self.ui.lineEdit_6, self.ui.lineEdit_7,
                               self.ui.lineEdit_8, self.ui.lineEdit_3, self.ui.lineEdit,
                               self.ui.lineEdit_2]
        self.base_line_edit1 = [self.ui.lineEdit_4, self.ui.lineEdit_6, self.ui.lineEdit_7,
                               self.ui.lineEdit_8, self.ui.lineEdit_3]
        self.login = self.ui.lineEdit
        self.login1 = self.ui.lineEdit_5
        self.fio = self.ui.lineEdit_4
        self.date = self.ui.dateEdit
        self.sal = self.ui.lineEdit_6
        self.post = self.ui.lineEdit_7
        self.number = self.ui.lineEdit_8
        self.addr = self.ui.lineEdit_3
        self.passw = self.ui.lineEdit_2
        self.role = self.ui.comboBox_2
        self.sp = self.ui.comboBox
        self.push = self.ui.pushButton
        self.push1 = self.ui.pushButton_3
        self.labelpssw = self.ui.label_3
        self.label1 = self.ui.label
        self.label = self.ui.label_13


        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler1)

    def closes(self): #функция закрытия окна регистрации
        self.close()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    # проверка правильности ввода
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

    # обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def reg(self): #отправка данных для выполнения запроса к бд (регистрация)
        name = self.ui.lineEdit_4.text()
        bd = self.ui.dateEdit.text()
        sal = self.ui.lineEdit_6.text()
        post = self.ui.lineEdit_7.text()
        num = self.ui.lineEdit_8.text()
        role = self.ui.comboBox_2.currentText()
        adr = self.ui.lineEdit_3.text()
        stat = self.ui.comboBox.currentText()
        login = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, bd, sal, post, num, role, adr, stat, login, passw)

    @check_input1
    def change(self): #отправка данных для выполнения запроса к бд (изменение данных работника)
        name = self.ui.lineEdit_4.text()
        bd = self.ui.dateEdit.text()
        sal = self.ui.lineEdit_6.text()
        post = self.ui.lineEdit_7.text()
        num = self.ui.lineEdit_8.text()
        role = self.ui.comboBox_2.currentText()
        adr = self.ui.lineEdit_3.text()
        stat = self.ui.comboBox.currentText()
        login = self.ui.lineEdit_5.text()
        self.check_db.thr_changeworker(name, bd, sal, post, num, role, adr, stat, login)

    def signal_handler1(self, value): #обработчик сигналов, сигнал при изменении данных
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

class InterfaceChange(QtWidgets.QWidget): #запрос на изменение данных
    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_Form3()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.change)

        self.edit_login = self.ui.lineEdit

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def closes(self): #закрытие окна
        self.close()
        self.ui.textEdit.clear()

    def check_input(funct): #провкрка правильности ввода
        def wrapper(self):
            if len(self.ui.textEdit.toPlainText()) == 0:
                return
            funct(self)
        return wrapper

    @check_input
    def change(self): #отправка данных для внесения изменений в бд
        log = self.ui.lineEdit.text()
        req = self.ui.textEdit.toPlainText()
        self.check_db.thr_change(log, req)

    def signal_handler(self, value): #обработчик сигналов при отправке данных
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

class InterfaceAdminChange(QtWidgets.QMainWindow): #окно обработки запрососв на изменение данных
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form4()
        self.ui.setupUi(self)
        self.ach = AdmChange()

        self.check_db = CheckThread()
        self.check_db.mysignal7.connect(self.signal_handler)

        self.ui.pushButton.clicked.connect(self.cell_clicked)
        self.ui.pushButton.clicked.connect(self.ach.login)
        self.ui.pushButton.clicked.connect(self.ach.changeinf)
        self.ui.pushButton_2.clicked.connect(self.closes)

        self.ui.tableWidget.setSortingEnabled(True)

    def closes(self): #закрытие окна
        self.close()

    def cell_clicked(self): #обработка нажатий в таблице
        row = self.ui.tableWidget.currentItem().row()
        log = self.ui.tableWidget.item(row, 0).text()
        inf = self.ui.tableWidget.item(row, 1).text()
        self.ach.x = log
        self.ach.y = inf
        self.ach.show()

    def admchanges(self): #вывод данных из бд
        a = 1
        self.check_db.thr_admchange(a)
        threading.Timer(15, self.admchanges).start()

    def signal_handler(self, value): #обработка сигналов, днные для вывода
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.resizeColumnsToContents()


class AdmChange(QtWidgets.QWidget): #окно для изменения данных работников
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form5()
        self.ui.setupUi(self)
        self.x = None
        self.y = None

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3,
                               self.ui.lineEdit_4]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler2)

        self.ui.pushButton_2.clicked.connect(self.closes)
        self.ui.pushButton.clicked.connect(self.changeinf2)

    def check_input(funct): #проверка правильности ввода
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    def closes(self): #закрытие окна
        self.close()

    def login(self): #внесение необходимых данных в поля
        log = self.x
        inf = self.y
        self.ui.label_3.setText('Изменение данных для ' + log)
        self.ui.label_19.setText(inf)

    def changeinf(self): #отправка данных для внесения изменений
        log = self.x
        self.check_db.thr_changeinf(log)

    @check_input
    def changeinf2(self): #данные, которые необходимо изменить
        log = self.x
        fio = self.ui.lineEdit.text()
        number = self.ui.lineEdit_2.text()
        add = self.ui.lineEdit_3.text()
        sp = self.ui.lineEdit_4.text()
        self.check_db.thr_changeinf2(log, fio, number, add, sp)


    def signal_handler2(self, value): #сигнал при изменении данных
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        self.close()

    def signal_handler(self, value): #данные для изменения
        for i in value:
            self.ui.lineEdit.setText(i[0])
            self.ui.lineEdit_2.setText(i[1])
            self.ui.lineEdit_3.setText(i[2])
            self.ui.lineEdit_4.setText(i[3])

class InterfaceMain(QtWidgets.QWidget): #главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ir = InterfaceReg()
        self.ic = InterfaceChange()
        self.ac = InterfaceAdminChange()
        self.ih = InterfaceHotel()
        self.ict = InterfaceCountry()
        self.ifood = InterfaceFood()
        self.it = InterfaceType()
        self.itour = InterfaceTour()
        self.io = InterfaceOrder()
        self.id = InterfaceDisc()
        self.iw = InterfaceWorker()
        self.icl = InterfaceClients()

        self.ui.pushButton_11.clicked.connect(self.closes)
        self.ui.pushButton_14.clicked.connect(self.reg)
        self.ui.pushButton_13.clicked.connect(self.changes)
        self.ui.pushButton_15.clicked.connect(self.admchange)
        self.ui.pushButton.clicked.connect(self.tablehotel)
        self.ui.pushButton_2.clicked.connect(self.tablecountry)
        self.ui.pushButton_3.clicked.connect(self.tablefood)
        self.ui.pushButton_4.clicked.connect(self.tabletype)
        self.ui.pushButton_5.clicked.connect(self.tabletour)
        self.ui.pushButton_6.clicked.connect(self.tableorder)
        self.ui.pushButton_9.clicked.connect(self.tabledisc)
        self.ui.pushButton_7.clicked.connect(self.tableworker)
        self.ui.pushButton_8.clicked.connect(self.tableclients)
        self.ui.pushButton_12.clicked.connect(self.touropen)
        self.ui.pushButton_10.clicked.connect(self.clopen)

        self.login = None

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.main()

    def clopen(self): #открыть работу с клиентом
        self.icl.show()
        self.icl.push6.show()
        self.icl.push7.show()
        self.icl.push8.show()
        self.icl.push2.hide()
        self.icl.push5.hide()
        self.icl.push3.setText("Новый клиент")
        self.icl.dbclients()
        self.icl.login = self.login

    def touropen(self): #открыть офрмленные туры
        self.io.show()
        name = self.login
        self.io.line.setText(name)
        self.io.check.setChecked(True)
        self.io.dborder()

    def tablehotel(self): #открыть таблицу отели
        self.ih.show()
        self.ih.dbhotel()

    def tablecountry(self): #открыть таблицу страны
        self.ict.show()
        self.ict.dbcountry()

    def tablefood(self): #открыть таблицу питание
        self.ifood.show()
        self.ifood.dbfood()

    def tabletype(self): #открыть таблицу типы туров
        self.it.show()
        self.it.dbtype()

    def tabletour(self): #открыть таблицу туры
        self.itour.show()
        self.itour.push3.show()
        self.itour.push4.show()
        self.itour.push5.show()
        self.itour.push10.hide()
        self.itour.push11.hide()
        self.itour.check13.setChecked(True)
        self.itour.dbtour()

    def tableorder(self): #открыть таблицу заказы
        self.io.show()
        self.io.dborder()

    def tabledisc(self): #открыть таблицу скидки
        self.id.show()
        self.id.dbdisc()

    def tableworker(self): #открыть таблицу сотрудники (только для администратора)
        self.iw.show()
        self.iw.dbworker()

    def tableclients(self): #открыть таблицу клиенты
        self.icl.show()
        self.icl.push6.hide()
        self.icl.push7.hide()
        self.icl.push8.hide()
        self.icl.push2.show()
        self.icl.push5.show()
        self.icl.push3.setText("Добавить данные")
        self.icl.dbclients()

    def admchange(self): #открыть окно заявок на изменение данных(администратор)
        self.ac.show()
        self.ac.admchanges()

    def changes(self): #открыть окно заявки на изменение данных
        self.ic.show()
        log = self.login
        self.ic.edit_login.setText(log)

    def reg(self): #открыть окно добавления работника(администраторы)
        self.ir.show()
        self.ir.label1.show()
        self.ir.label.hide()
        self.ir.login.show()
        self.ir.login1.hide()
        self.ir.push.show()
        self.ir.push1.hide()

    def closes(self): #закрыто программу
        self.close()

    def main(self): #отправка данных для вывода информации
        log = self.login
        self.check_db.thr_main(log)

    def signal_handler(self, value): #вывод информации
        for i in value:
            self.ui.label_2.setText(i[0])
            self.ui.label.setText(i[1])
            self.ui.label_8.setText(i[2])
            self.ui.label_9.setText(i[3])
            self.ui.label_13.setText(i[4])
            self.ui.label_19.setText(i[5])
            if i[6] == 'USER':
                self.ui.pushButton_14.hide()
                self.ui.pushButton_15.hide()
        threading.Timer(15, self.main).start()


class InterfaceAuth(QtWidgets.QWidget): #окно авторизации в системе
    def __init__(self, parent=None):
        super().__init__(parent)
        self.im = InterfaceMain()
        self.ui = Ui_Form1()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.pushButton.clicked.connect(self.im.main)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)


    # проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    # обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        name = self.ui.lineEdit.text()
        if value == "Авторизация успешна!":
            self.im.login = name
            self.im.show()
            self.close()

    @check_input
    def auth(self): #оправка данных в бд для входа в систему
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)



if __name__ == "__main__": #открытие окна
    app = QtWidgets.QApplication(sys.argv)
    mywin = InterfaceAuth()
    mywin.show()
    sys.exit(app.exec_())
