from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *
from handler.db_handler_table import *
from handler.db_handler_table2 import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(object)
    mysignal1 = QtCore.pyqtSignal(object)
    mysignal2 = QtCore.pyqtSignal(object)
    mysignal3 = QtCore.pyqtSignal(object)
    mysignal4 = QtCore.pyqtSignal(object)
    mysignal5 = QtCore.pyqtSignal(object)
    mysignal6 = QtCore.pyqtSignal(object)
    mysignal7 = QtCore.pyqtSignal(object)


    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    def thr_change(self, login, req):
        change(login, req, self.mysignal)

    def thr_admchange(self, a):
        admchange(a, self.mysignal7)

    def thr_register(self, name, bd, sal, post, num, role, adr, stat, login, passw):
       register(name, bd, sal, post, num, role, adr, stat, login, passw, self.mysignal)

    def thr_changeworker(self, name, bd, sal, post, num, role, adr, stat, login):
        changeworker(name, bd, sal, post, num, role, adr, stat, login, self.mysignal1)

    def thr_main(self, log):
        main(log, self.mysignal)

    def thr_changeinf2(self, log, fio, number, add, sp):
        changeinf2(log, fio, number, add, sp, self.mysignal1)

    def thr_changeinf(self, log):
        changeinf(log, self.mysignal)



    def thr_delhotel(self, name):
        delhotel(name, self.mysignal1)

    def thr_changehotel(self, name, city, star, note):
        changehotel(name, city, star, note, self.mysignal1)

    def thr_addhotel(self, name, city, star, note):
       addhotel(name, city, star, note, self.mysignal)

    def thr_dbhotel(self, inf1, inf2, inf3):
        dbhotel(inf1, inf2, inf3, self.mysignal)


    def thr_dbcountry(self, inf1, inf2):
        dbcountry(inf1, inf2, self.mysignal)

    def thr_addcountry(self, name, visa):
        addcountry(name, visa, self.mysignal)

    def thr_changecountry(self, name, visa):
        changecountry(name, visa, self.mysignal1)

    def thr_delcountry(self, name):
        delcountry(name, self.mysignal1)


    def thr_dbfood(self, inf1, inf2):
        dbfood(inf1, inf2, self.mysignal)

    def thr_addfood(self, name, note):
        addfood(name, note, self.mysignal)

    def thr_changefood(self, name, note):
        changefood(name, note, self.mysignal1)

    def thr_delfood(self, name):
        delfood(name, self.mysignal1)


    def thr_dbtype(self, inf1, inf2):
        dbtype(inf1, inf2, self.mysignal)

    def thr_addtype(self, name, note):
        addtype(name, note, self.mysignal)

    def thr_changetype(self, name, note):
        changetype(name, note, self.mysignal1)

    def thr_deltype(self, name):
        deltype(name, self.mysignal1)


    def thr_dbtour(self, inf1, inf2, inf3, inf4, inf5, inf7, inf8, inf9, inf10, inf11, a, b, c):
        dbtour(inf1, inf2, inf3, inf4, inf5, inf7, inf8, inf9, inf10, inf11, a, b, c, self.mysignal)

    def thr_addchecktour(self, a):
        addchecktour(a, self.mysignal, self.mysignal1, self.mysignal2, self.mysignal3)

    def thr_addtour(self, name, days, price, burn, food, hot, type, country):
        addtour(name, days, price, burn, food, hot, type, country, self.mysignal7)

    def thr_deltour(self, name):
        deltour(name, self.mysignal1)

    def thr_changetour(self, name, days, price, burn, food, hot, type, country):
        changetour(name, days, price, burn, food, hot, type, country, self.mysignal4)


    def thr_dborder(self, inf1, inf2, inf3, inf4, inf5, inf6, i):
        dborder(inf1, inf2, inf3, inf4, inf5, inf6, i, self.mysignal)

    def thr_addcheckorder(self, a):
        addcheckorder(a, self.mysignal, self.mysignal1, self.mysignal2, self.mysignal3)

    def thr_price(self, price1, price2):
        price(price1, price2, self.mysignal5)

    def thr_addorder(self, name, price, date1, date2, work, cl, disc):
        addorder(name, price, date1, date2, work, cl, disc, self.mysignal7)

    def thr_delorder(self, name, price, date1, date2, work, cl):
        delorder(name, price, date1, date2, work, cl, self.mysignal1)

    def thr_getid(self, name, price, date1, date2, work, cl):
        getid(name, price, date1, date2, work, cl, self.mysignal2)

    def thr_changeorder(self, name, price, date1, date2, work, cl, disc, id):
        changeorder(name, price, date1, date2, work, cl, disc, id, self.mysignal4)


    def thr_dbdisc(self, inf1, inf2):
        dbdisc(inf1, inf2, self.mysignal)

    def thr_adddisc(self, name, note):
        adddisc(name, note, self.mysignal)

    def thr_changedisc(self, name, note):
        changedisc(name, note, self.mysignal1)

    def thr_deldisc(self, name):
        deldisc(name, self.mysignal1)


    def thr_dbworker(self, inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, i):
        dbworker(inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, i, self.mysignal)

    def thr_delworker(self, name):
        delworker(name, self.mysignal1)


    def thr_dbclients(self, inf1, inf2, inf3, inf4):
        dbclients(inf1, inf2, inf3, inf4, self.mysignal)

    def thr_delcl(self, passp):
        delcl(passp, self.mysignal1)

    def thr_changecl(self, name, addr, numb, date, passp):
        changecl(name, addr, numb, date, passp, self.mysignal1)

    def thr_addcl(self, name, addr, numb, date, passp):
       addcl(name, addr, numb, date, passp, self.mysignal)



