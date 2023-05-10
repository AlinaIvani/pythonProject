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


    def main(log, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT post, workname, telnumber, birthdate, status, workadress, role FROM worker WHERE login="{log}";')
        inf = cursor.fetchall()

        if value > 0:
            signal.emit(inf)

    def change(login, req, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM worker WHERE login="{login}";')
        value_1 = cursor.execute(f'SELECT * FROM req WHERE workerlog="{login}";')

        if value > 0:
            if value_1 > 0:
                signal.emit('Вы можете отправить только один запрос')
            else:
                cursor.execute(f"INSERT INTO req (reqmane, workerlog) VALUES ('{req}', '{login}');")
                signal.emit('Успешно!')
                connection.commit()


    def admchange(a, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT workerlog, reqmane FROM req;')
        inf = cursor.fetchall()

        signal.emit(inf)

    def changeinf(log, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT workname, telnumber, workadress, status FROM worker WHERE login="{log}";')
        info = cursor.fetchall()

        signal.emit(info)

    def changeinf2(log, fio, number, add, sp, signal):
        cursor = connection.cursor()

        cursor.execute(f'UPDATE worker SET workname="{fio}", telnumber = "{number}", workadress = "{add}",'
                       f'status = "{sp}" WHERE login="{log}";')
        cursor.execute(f'SELECT workname, telnumber, workadress, status FROM worker;')
        value = cursor.fetchall()
        for i in value:
            if i[0] == fio and i[1] == number and i[2] == add and i[3] == sp:
                signal.emit('Изменения внесены успешно')

        cursor.execute(f'DELETE FROM req WHERE workerlog="{log}"')
        connection.commit()


    def login(login, passw, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM worker WHERE login="{login}" AND password=md5("{passw}");')

        if value > 0:
            signal.emit('Авторизация успешна!')
        else:
            signal.emit('Проверьте правильность ввода данных!')


except Exception as ex:
    print("Connection refused...")
    print(ex)
