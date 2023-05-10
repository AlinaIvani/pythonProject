import pymysql
from PyQt5.QtCore import Qt

from config import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

try:
    connection = pymysql.Connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor
    )
    print("successfully connected...")

    def dbtour(inf1, inf2, inf3, inf4, inf5, inf7, inf8, inf9, inf10, inf11, a, b, c, signal):
        cursor = connection.cursor()

        if c == 1:
            cursor.execute(f'SELECT tour.tourname, tour.days, tour.pricetour, tour.burn, food.foodname, '
                           f'hotel.hotelname, tourtype.tourtypename, country.countryname '
                           f'FROM tour LEFT JOIN food ON tour.food=food.idfood '
                           f'LEFT JOIN hotel ON tour.hotel=hotel.idhotel '
                           f'LEFT JOIN tourtype ON tour.tourtype=tourtype.idtourtype '
                           f'LEFT JOIN country ON tour.country=country.idcountry '
                           f'WHERE tour.tourname LIKE "{inf1}" AND  tour.days {b} "{inf2}" AND '
                           f'tour.pricetour {a} "{inf3}" AND tour.burn LIKE "{inf4}" AND '
                           f'food.foodname LIKE "{inf5}" AND '
                           f'tourtype.tourtypename LIKE "{inf7}" AND country.countryname LIKE "{inf8}";')
            inf = cursor.fetchall()
        else:
            cursor.execute(f'SELECT tour.tourname, tour.days, tour.pricetour, tour.burn, food.foodname, '
                           f'hotel.hotelname, tourtype.tourtypename, country.countryname '
                           f'FROM tour LEFT JOIN food ON tour.food=food.idfood '
                           f'LEFT JOIN hotel ON tour.hotel=hotel.idhotel '
                           f'LEFT JOIN tourtype ON tour.tourtype=tourtype.idtourtype '
                           f'LEFT JOIN country ON tour.country=country.idcountry '
                           f'WHERE tour.tourname LIKE "{inf1}" AND  tour.days {a} "{inf2}" AND '
                           f'tour.pricetour {b} "{inf3}" AND tour.burn LIKE "{inf4}" AND '
                           f'food.foodname LIKE "{inf5}" AND '
                           f'tourtype.tourtypename LIKE "{inf7}" AND country.countryname LIKE "{inf8}" AND '
                           f'hotel.hotelname LIKE "{inf9}" AND hotel.countryhotel LIKE "{inf10}" AND '
                           f'hotel.star LIKE "{inf11}";')
            inf = cursor.fetchall()

        signal.emit(inf)

    def addchecktour(a, signal1, signal2, signal3, signal4):
        cursor = connection.cursor()

        cursor.execute(f'SELECT foodname FROM food')
        food = cursor.fetchall()
        cursor.execute(f'SELECT hotelname FROM hotel')
        hotel = cursor.fetchall()
        cursor.execute(f'SELECT tourtypename FROM tourtype')
        type = cursor.fetchall()
        cursor.execute(f'SELECT countryname FROM country')
        country = cursor.fetchall()

        signal1.emit(food)
        signal2.emit(hotel)
        signal3.emit(type)
        signal4.emit(country)

    def addtour(name, days, price, burn, food, hot, type, country, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idfood FROM food WHERE foodname="{food}"')
        inf = cursor.fetchall()
        for i in inf:
            food1 = i[0]
        cursor.execute(f'SELECT idhotel FROM hotel WHERE hotelname="{hot}"')
        inf = cursor.fetchall()
        for i in inf:
            hot1 = i[0]
        cursor.execute(f'SELECT idtourtype FROM tourtype WHERE tourtypename="{type}"')
        inf = cursor.fetchall()
        for i in inf:
            type1 = i[0]
        cursor.execute(f'SELECT idcountry FROM country WHERE countryname="{country}"')
        inf = cursor.fetchall()
        for i in inf:
            country1 = i[0]
        value = cursor.execute(f'SELECT * FROM tour WHERE tourname = "{name}"')
        if hot == "Без отеля":
            if value > 0:
                signal.emit('Тур с таким названием уже есть в базе!')
            else:
                cursor.execute(f'INSERT INTO tour (tourname, days, pricetour, burn, food, tourtype, country) '
                               f'VALUES ("{name}", "{days}", "{price}", "{burn}", "{food1}", "{type1}", "{country1}");')
                signal.emit('Успешно добавлено!')
                connection.commit()
        else:
            if value > 0:
                signal.emit('Тур с таким названием уже есть в базе!')
            else:
                cursor.execute(f'INSERT INTO tour (tourname, days, pricetour, burn, food, hotel, tourtype, country) '
                               f'VALUES ("{name}", "{days}", "{price}", "{burn}", "{food1}", "{hot1}", "{type1}", "{country1}");')
                signal.emit('Успешно добавлено!')
                connection.commit()

    def deltour(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM tour WHERE tourname = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM tour WHERE tourname = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием тура!")
        connection.commit()

    def changetour(name, days, price, burn, food, hot, type, country, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idfood FROM food WHERE foodname="{food}"')
        inf = cursor.fetchall()
        for i in inf:
            food1 = i[0]
        cursor.execute(f'SELECT idhotel FROM hotel WHERE hotelname="{hot}"')
        inf = cursor.fetchall()
        for i in inf:
            hot1 = i[0]
        cursor.execute(f'SELECT idtourtype FROM tourtype WHERE tourtypename="{type}"')
        inf = cursor.fetchall()
        for i in inf:
            type1 = i[0]
        cursor.execute(f'SELECT idcountry FROM country WHERE countryname="{country}"')
        inf = cursor.fetchall()
        for i in inf:
            country1 = i[0]
        value = cursor.execute(f'SELECT * FROM tour WHERE tourname = "{name}"')
        if hot == "Без отеля":
            cursor.execute(f'UPDATE tour SET days="{days}", pricetour="{price}",burn="{burn}", '
                           f'food="{food1}", tourtype="{type1}", country="{country1}" '
                           f'WHERE tourname="{name}"')
            signal.emit('Изменения внесены успешно!')
            connection.commit()
        else:
            cursor.execute(f'UPDATE tour SET days="{days}", pricetour="{price}",burn="{burn}", '
                           f'food="{food1}", hotel="{hot1}", '
                           f'tourtype="{type1}", country="{country1}" WHERE tourname="{name}"')
            signal.emit('Изменения внесены успешно!')
            connection.commit()

    def dbworker(inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, i, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT workname, birthdate, salary, post, telnumber, role, workadress, status, login FROM worker '
                       f'WHERE workname LIKE "{inf1}" AND birthdate LIKE "{inf2}" AND salary {i} "{inf3}" AND '
                       f'post LIKE "{inf4}" AND telnumber LIKE "{inf5}" AND role LIKE "{inf6}" AND '
                       f'status LIKE "{inf7}" AND login LIKE "{inf8}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def delworker(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM worker WHERE login = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM worker WHERE login = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием работника!")
        connection.commit()

    def register(name, bd, sal, post, num, role, adr, stat, login, passw, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM worker WHERE login="{login}";')
        if value > 0:
            signal.emit('Такой логин уже используется!')
        else:
            cursor.execute(
                f"INSERT INTO worker (workname, birthdate, salary, post, telnumber, role, password, login, workadress, status) VALUES ('{name}', '{bd}', '{sal}', '{post}', '{num}', '{role}', md5('{passw}'), '{login}', '{adr}', '{stat}');")
            signal.emit('Пользователь успешно зарегистрирован!')
            connection.commit()

    def changeworker(name, bd, sal, post, num, role, adr, stat, login, signal):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE worker SET workname = "{name}", birthdate = "{bd}", '
                       f'salary = "{sal}", post = "{post}", telnumber = "{num}", '
                       f'role = "{role}", login = "{login}", workadress = "{adr}", '
                       f'status = "{stat}" WHERE login = "{login}";')
        signal.emit('Изменения внесены успешно')
        connection.commit()

    def dbclients(inf1, inf2, inf3, inf4, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT clientsname, adress, cltelnumber, cldate, passport FROM clients '
                       f'WHERE clientsname LIKE "{inf1}" AND '
                       f'cltelnumber LIKE "{inf2}" AND cldate LIKE "{inf3}" AND '
                       f'passport LIKE "{inf4}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def addcl(name, addr, numb, date, passp, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM clients WHERE passport = "{passp}"')
        if value > 0:
            signal.emit('Такой клиент уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO clients (clientsname, adress, cltelnumber, cldate, passport) '
                           f'VALUES ("{name}", "{addr}", "{numb}", "{date}", "{passp}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def changecl(name, addr, numb, date, passp, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE clients SET clientsname = "{name}", adress = "{addr}", '
                       f'cltelnumber = "{numb}", cldate = "{date}", passport = "{passp}" '
                       f'WHERE passport = "{passp}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def delcl(passp, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM clients WHERE passport = "{passp}"')
        if value > 0:
            cursor.execute(f'DELETE FROM clients WHERE passport = "{passp}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с именем клиента!")
        connection.commit()

    def dborder(inf1, inf2, inf3, inf4, inf5, inf6, i, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT tour.tourname, ordered.orderprice, ordered.date1, ordered.paydate, '
                       f'worker.login, clients.passport, disc.discname '
                       f'FROM ordered LEFT JOIN tour ON ordered.tour=tour.idtour '
                       f'LEFT JOIN worker ON ordered.worker=worker.idworker '
                       f'LEFT JOIN clients ON ordered.client=clients.idclients '
                       f'LEFT JOIN disc ON ordered.disc=disc.iddisc '
                       f'WHERE tour.tourname LIKE "{inf1}" AND ordered.orderprice {i} "{inf2}" AND '
                       f'ordered.date1 LIKE "{inf3}" AND ordered.paydate LIKE "{inf4}" AND '
                       f'worker.workname LIKE "{inf5}" AND clients.clientsname LIKE "{inf6}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def addcheckorder(a, signal1, signal2, signal3, signal4):
        cursor = connection.cursor()

        cursor.execute(f'SELECT tourname FROM tour')
        tour = cursor.fetchall()
        cursor.execute(f'SELECT login FROM worker')
        worker = cursor.fetchall()
        cursor.execute(f'SELECT passport FROM clients')
        clients = cursor.fetchall()
        cursor.execute(f'SELECT discname FROM disc')
        disc = cursor.fetchall()

        signal1.emit(tour)
        signal2.emit(worker)
        signal3.emit(clients)
        signal4.emit(disc)

    def addorder(name, price, date1, date2, work, cl, disc, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idtour FROM tour WHERE tourname="{name}"')
        inf = cursor.fetchall()
        for i in inf:
            name1 = i[0]
        cursor.execute(f'SELECT idworker FROM worker WHERE login="{work}"')
        inf = cursor.fetchall()
        for i in inf:
            work1 = i[0]
        cursor.execute(f'SELECT idclients FROM clients WHERE passport="{cl}"')
        inf = cursor.fetchall()
        for i in inf:
            cl1 = i[0]
        cursor.execute(f'SELECT iddisc FROM disc WHERE discname="{disc}"')
        inf = cursor.fetchall()
        for i in inf:
            disc1 = i[0]
        value = cursor.execute(f'SELECT * FROM ordered WHERE tour = "{name1}" AND orderprice = "{price}" AND '
                               f'date1 = "{date1}" AND paydate = "{date2}" AND worker = "{work1}" AND '
                               f'client = "{cl1}"')
        if disc == "Без скидки":
            if value > 0:
                signal.emit('Такой заказ уже есть в базе!')
            else:
                cursor.execute(f'INSERT INTO ordered (tour, orderprice, date1, paydate, worker, client) '
                               f'VALUES ("{name1}", "{price}", "{date1}", "{date2}", "{work1}", "{cl1}");')
                signal.emit('Успешно добавлено!')
                connection.commit()
        else:
            if value > 0:
                signal.emit('Такой заказ уже есть в базе!')
            else:
                cursor.execute(f'INSERT INTO ordered (tour, orderprice, date1, paydate, worker, client, disc) '
                               f'VALUES ("{name1}", "{price}", "{date1}", "{date2}", "{work1}", "{cl1}", "{disc1}");')
                signal.emit('Успешно добавлено!')
                connection.commit()

    def delorder(name, price, date1, date2, work, cl, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idtour FROM tour WHERE tourname="{name}"')
        inf = cursor.fetchall()
        for i in inf:
            name1 = i[0]
        cursor.execute(f'SELECT idworker FROM worker WHERE login="{work}"')
        inf = cursor.fetchall()
        for i in inf:
            work1 = i[0]
        cursor.execute(f'SELECT idclients FROM clients WHERE passport="{cl}"')
        inf = cursor.fetchall()
        for i in inf:
            cl1 = i[0]

        cursor.execute(f'DELETE FROM ordered WHERE tour = "{name1}" AND orderprice = "{price}" AND '
                       f'date1 = "{date1}" AND paydate = "{date2}" AND worker = "{work1}" AND '
                       f'client = "{cl1}"')
        signal.emit("Успешно удалено!")
        connection.commit()

    def getid(name, price, date1, date2, work, cl, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idtour FROM tour WHERE tourname="{name}"')
        inf = cursor.fetchall()
        for i in inf:
            name1 = i[0]
        cursor.execute(f'SELECT idworker FROM worker WHERE login="{work}"')
        inf = cursor.fetchall()
        for i in inf:
            work1 = i[0]
        cursor.execute(f'SELECT idclients FROM clients WHERE passport="{cl}"')
        inf = cursor.fetchall()
        for i in inf:
            cl1 = i[0]

        cursor.execute(f'SELECT idorder FROM ordered WHERE tour = "{name1}" AND orderprice = "{price}" AND '
                       f'date1 = "{date1}" AND paydate = "{date2}" AND worker = "{work1}" AND '
                       f'client = "{cl1}"')
        inf = cursor.fetchall()
        for i in inf:
            inf1 = i[0]

        signal.emit(inf1)

    def changeorder(name, price, date1, date2, work, cl, disc, id, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT idtour FROM tour WHERE tourname="{name}"')
        inf = cursor.fetchall()
        for i in inf:
            name1 = i[0]
        cursor.execute(f'SELECT idworker FROM worker WHERE login="{work}"')
        inf = cursor.fetchall()
        for i in inf:
            work1 = i[0]
        cursor.execute(f'SELECT idclients FROM clients WHERE passport="{cl}"')
        inf = cursor.fetchall()
        for i in inf:
            cl1 = i[0]
        cursor.execute(f'SELECT iddisc FROM disc WHERE discname="{disc}"')
        inf = cursor.fetchall()
        for i in inf:
            disc1 = i[0]
        if disc == "Без скидки":
            cursor.execute(f'UPDATE ordered SET tour="{name1}", orderprice="{price}",date1="{date1}", '
                           f'paydate="{date2}", worker="{work1}", client="{cl1}" '
                           f'WHERE idorder="{id}"')
            signal.emit('Изменения внесены успешно!')
            connection.commit()
        else:
            cursor.execute(f'UPDATE ordered SET tour="{name1}", orderprice="{price}",date1="{date1}", '
                           f'paydate="{date2}", worker="{work1}", '
                           f'client="{cl1}", disc="{disc1}" WHERE idorder="{id}"')
            signal.emit('Изменения внесены успешно!')
            connection.commit()

    def price(price1, price2, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT pricetour FROM tour WHERE tourname = "{price1}"')
        inf1 = cursor.fetchall()
        for i in inf1:
            pr1 = i[0]
        if price2 == "Без скидки":
            pr2 = "0"
        else:
            cursor.execute(f'SELECT discamount FROM disc WHERE discname = "{price2}"')
            inf2 = cursor.fetchall()
            for i in inf2:
                pr2 = i[0]
        p1 = int(pr1)
        p2 = int(pr2)
        pr = (p1//100)*p2
        pric = p1-pr
        price = str(pric)
        signal.emit(price)


except Exception as ex:
    print("Connection refused...")
    print(ex)