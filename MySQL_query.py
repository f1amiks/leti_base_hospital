import sys

import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
)


except Exception as ex:
    print("Connection refused...")
    print(ex)

def admin_check():
    g = 0

    admin_info = []
    admin_login = []
    admin_pass = []
    admin_type = []
    user_login = input("login: ")
    user_pass = input("pass: ")
    with connection.cursor() as cursor:
        admin_info = "SELECT * FROM admin_info; "
        cursor.execute(admin_info)
        result = cursor.fetchall()

        for x in result:
            admin_login.append(x["login"])
            admin_pass.append(x["pass"])
            admin_type.append(x["type"])
    while g != 5:
        print("************")
        for i in range(0, len(admin_login), +1):  ## вход за администратора
            if user_login == admin_login[i]:
                if user_pass == admin_pass[i]:
                    print(True)
                    g = 6
                    if  admin_type[i] == 'admin':

                        print("Welcome administrator!")
                        return(True)

                    else:

                        print("welcome User!")
                        return(False)

        g += 1 
        user_login = input("неверные данные, повторите попытку\n login:")
        user_pass = input("pass: ")
def show_admin_base():

    with connection.cursor() as cursor:  # просмотр данных таблицы

        with connection.cursor() as cursor:
            select_query = "SHOW TABLES FROM " + db_name
            cursor.execute(select_query)
            result = cursor.fetchall()

            for x in result:
                print(x)

            print("done")

        name_table = input("name table:")
        show_table = "select * from " + name_table
        with connection.cursor() as cursor:
            cursor.execute(show_table)
            rows = cursor.fetchall()

        for row in rows:
            print(row)
        print('done')

def show_user_base():

    with connection.cursor() as cursor:  # просмотр данных таблицы


        show_table = "SELECT patient_name, address_street, doctor_name, diag, date_diag FROM patient_info LEFT JOIN doctor_info using(doctor_id) JOIN diagnosis using(diagnosis_id);"
        cursor.execute(show_table)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        print('done')

def show_doctor_info():

    with connection.cursor() as cursor:
        info_doctor = "SELECT doctor_name, doctor_office, doctor_date FROM leti_base.doctor_info;"
        cursor.execute(info_doctor)
        rows = cursor.fetchall()

        for row in rows:
            print("Доктор: ", row['doctor_name'], "| Кабинет:", row['doctor_office'], "| Время приема:",row['doctor_date'])

def insert_base():

    with connection.cursor() as cursor:
        select_query = "SHOW TABLES FROM " + db_name
        cursor.execute(select_query)
        result = cursor.fetchall()

        for x in result:
            print(x)

        print("done")

    admin_pass = []
    r = []
    d = []
    with connection.cursor() as cursor:

        table_name = input("table name: ")##просит ввести название таблицы
        if table_name == "patient_info":

            admin_info = "SELECT * FROM " + table_name ##выводит данные тблицы
            cursor.execute(admin_info)
            result = cursor.fetchall()

            for x in result:
                print(x)
    with connection.cursor() as cursor:

        admin_info = "DESCRIBE " + table_name         ##выводит данные таблицы
        cursor.execute(admin_info)
        result = cursor.fetchall()

        for x in result:                        ##записывает в список название столбцов
            admin_pass.append(x["Field"])
            r.append(x["Field"])
    r = list(map(str, r))       ##создаем список в формате str
    id = r[0]
    r.pop(0)  ##удаление столбца id

    for i in range(len(r)):

        d.append(input(r[i] + ":"))
    d = '", "'.join(d)
    r = ', '.join(r)           ##вывод списка без скобок через запятую
    with connection.cursor() as cursor:
        if cursor.execute("insert " + table_name + "(" + r + ") values" + ' ("' + d + '");'):
            with connection.cursor() as cursor:
                print(id)
                print(cursor.execute("SELECT " + id + " FROM " + table_name ))
            connection.commit()
            print('done')

def update_base():


    with connection.cursor() as cursor:
        ##просмотр всех таблиц
        with connection.cursor() as cursor:
            select_query = "SHOW TABLES FROM " + db_name
            cursor.execute(select_query)
            result = cursor.fetchall()

            for x in result:
                print(x)

            print("done")

        table_name = input("Enter the name of the table: ")
        ##вывод данных таблицы
        with connection.cursor() as cursor:

            admin_info = "select * from " + table_name  ##выводит данные таблицы
            cursor.execute(admin_info)
            result = cursor.fetchall()

            for x in result:
                print(x)
            ##выбор id таблицы и столбца где нужно изменить
            id_table = input("id table:")
            column_table = input("column table:")
            column_update = input("update: ")
            ##название id находти
            r = []
            with connection.cursor() as cursor:
                admin_info = "DESCRIBE " + table_name  ##выводит данные таблицы
                cursor.execute(admin_info)
                result = cursor.fetchall()

                for x in result:  ##записывает в список название столбцов
                    r.append(x["Field"])
            r = list(map(str, r))  ##делаем список в формате str
            id = r[0]
            update_table = "update `" + db_name + "`.`" + table_name + "` set `" + column_table + "` = '" + column_update + "' where (" + id + " = '" + id_table + "');"
            print(update_table)
            ##записываем значение в таблицу
            with connection.cursor() as cursor:
                cursor.execute(update_table)
                cursor.fetchall()
                print('done')

def delete_table():

    with connection.cursor() as cursor:

        table_name = input("Enter the name of the table: ")
        with connection.cursor() as cursor:

            admin_info = "select * from " + table_name  ##выводит данные таблицы
            cursor.execute(admin_info)
            result = cursor.fetchall()

            for x in result:
                print(x)

        user_id = str(input("Enter the user id of the table: "))
        delete_query = "DELETE FROM " + table_name + " WHERE id = " + user_id + ";"
        with connection.cursor() as cursor:
            cursor.execute(delete_query)
            connection.commit()
            print('done')
        user_answer = input("write the next action: ")

def certificate_base():
    with connection.cursor() as cursor:
        info_patient = "select * from patient_info"
        print("кол-во бльных:" , cursor.execute(info_patient), "\nИнформация о докторах:")

        with connection.cursor() as cursor:
            doctor_name = "SELECT  doctor_name AS 'Доктор', COUNT(*) AS 'кол-во больных' FROM patient_info INNER JOIN doctor_info ON patient_info.doctor_id = doctor_info.doctor_id GROUP BY doctor_info.doctor_name;"
            cursor.execute(doctor_name)
            rows = cursor.fetchall()

        for row in rows:
            print("Доктор: ",row['Доктор'] ,"| Кол-во больных:", row['кол-во больных'])

        print("##############\nИнформация о диагнозах:")

        with connection.cursor() as cursor:
            doctor_name = "SELECT  diag AS 'Диагноз', COUNT(*) AS 'кол-во больных' FROM patient_info INNER JOIN diagnosis ON patient_info.diagnosis_id = diagnosis.diagnosis_id GROUP BY diagnosis.diag;"
            cursor.execute(doctor_name)
            rows = cursor.fetchall()

        for row in rows:
            print("Диагноз: ", row['Диагноз'], "| Кол-во больных:", row['кол-во больных'])

        print("##############", "\nРассписание приема:")

        with connection.cursor() as cursor:
            doctor_name = "SELECT doctor_name, doctor_office, doctor_date FROM leti_base.doctor_info;"
            cursor.execute(doctor_name)
            rows = cursor.fetchall()

        for row in rows:
            print("Доктор: ", row['doctor_name'], "| Кабинет:", row['doctor_office'], "| Время приема:", row['doctor_date'])

        print('done')
