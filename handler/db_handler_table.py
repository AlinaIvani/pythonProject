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

    def delhotel(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM hotel WHERE hotelname = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM hotel WHERE hotelname = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием отеля!")
        connection.commit()

    def changehotel(name, city, star, note, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE hotel SET countryhotel = "{city}", star = "{star}",'
                       f'notes = "{note}" WHERE hotelname="{name}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def addhotel(name, city, star, note, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM hotel WHERE hotelname = "{name}"')
        if value > 0:
            signal.emit('Такой отель уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO hotel (hotelname, countryhotel, star, notes) '
                           f'VALUES ("{name}", "{city}", "{star}", "{note}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def dbhotel(inf1, inf2, inf3, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT hotelname, countryhotel, star, notes FROM hotel WHERE hotelname LIKE "{inf1}" AND countryhotel LIKE "{inf2}" '
                       f'AND star LIKE "{inf3}";')
        value = cursor.fetchall()
        signal.emit(value)

    def addcountry(name, visa, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM country WHERE countryname = "{name}"')
        if value > 0:
            signal.emit('Такая страна уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO country (countryname, visa) VALUES ("{name}", "{visa}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def dbcountry(inf1, inf2, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT countryname, visa FROM country WHERE countryname LIKE "{inf1}" '
                       f'AND visa LIKE "{inf2}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def changecountry(name, visa, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE country SET countryname = "{name}", visa = "{visa}" '
                       f'WHERE countryname = "{name}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def delcountry(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM country WHERE countryname = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM country WHERE countryname = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием страны!")
        connection.commit()

    def dbfood(inf1, inf2, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT foodname, descr FROM food WHERE foodname LIKE "{inf1}" '
                       f'AND descr LIKE "{inf2}";;')
        inf = cursor.fetchall()

        signal.emit(inf)

    def addfood(name, note, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM food WHERE foodname = "{name}"')
        if value > 0:
            signal.emit('Такая страна уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO food (foodname, descr) VALUES ("{name}", "{note}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def changefood(name, note, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE food SET foodname = "{name}", descr = "{note}" '
                       f'WHERE foodname = "{name}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def delfood(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM food WHERE foodname = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM food WHERE foodname = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием страны!")
        connection.commit()

    def dbtype(name, note, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT tourtypename, typedesc FROM tourtype WHERE '
                       f'tourtypename LIKE "{name}" AND typedesc LIKE "{note}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def addtype(name, note, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM tourtype WHERE tourtypename = "{name}"')
        if value > 0:
            signal.emit('Такая страна уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO tourtype (tourtypename, typedesc) VALUES ("{name}", "{note}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def changetype(name, note, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE tourtype SET tourtypename = "{name}", typedesc = "{note}" '
                       f'WHERE tourtypename = "{name}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def deltype(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM tourtype WHERE tourtypename = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM tourtype WHERE tourtypename = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием страны!")
        connection.commit()

    def dbdisc(inf1, inf2, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT discname, discamount FROM disc '
                       f'WHERE discname LIKE "{inf1}" AND discamount LIKE "{inf2}";')
        inf = cursor.fetchall()

        signal.emit(inf)

    def adddisc(name, note, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM disc WHERE discname = "{name}"')
        if value > 0:
            signal.emit('Такая скидка уже есть в базе!')
        else:
            cursor.execute(f'INSERT INTO disc (discname, discamount) VALUES ("{name}", "{note}");')
            signal.emit('Успешно добавлено!')
            connection.commit()

    def changedisc(name, note, signal1):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE disc SET discname = "{name}", discamount = "{note}" '
                       f'WHERE discname = "{name}";')
        signal1.emit('Изменения внесены успешно')
        connection.commit()

    def deldisc(name, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM disc WHERE discname = "{name}"')
        if value > 0:
            cursor.execute(f'DELETE FROM disc WHERE discname = "{name}"')
            signal.emit("Успешно удалено!")
        else:
            signal.emit("Выберете ячейку с названием страны!")
        connection.commit()


except Exception as ex:
    print("Connection refused...")
    print(ex)