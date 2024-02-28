
import MySQL_query
## вход пользователя

type = MySQL_query.admin_check()


if type ==True:   ##если зашли за администратора

    print("select an action : show, update, delete, info from or exit")
    user_answer = input()

    while user_answer != "exit":  ## начало работы команд запросов пока пользователь не закончит

        if user_answer == "show":                                         #просмотр баз данных
            MySQL_query.show_admin_base()

            user_answer = input("write the next action: ")


        elif user_answer == "insert":
            #добавление данных таблицы
            MySQL_query.insert_base()

            user_answer = input("write the next action: ")

        elif user_answer == "update":                                 #изменение данных таблицы

            MySQL_query.update_base()

            user_answer = input("write the next action: ")

        elif user_answer == "delete":                             #удаление данных таблицы

            MySQL_query.delete_table()

            user_answer = input("write the next action: ")

        elif user_answer == "info":  # справка данных таблицы

            MySQL_query.certificate_base()

            user_answer = input("write the next action: ")
        else:
            print("error action")
            user_answer = input("write the next action: ")

if type == False:

    print("select an action : doctor info, show or exit")
    user_answer = input()
    while user_answer != "exit":
        if user_answer == "doctor info":
            MySQL_query.show_doctor_info()

            user_answer = input("write the next action: ")

        elif user_answer == "show":  # просмотр баз данных
            MySQL_query.show_user_base()

            user_answer = input("write the next action: ")
        elif user_answer == "info":  # справка данных таблицы

            MySQL_query.certificate_base()

            user_answer = input("write the next action: ")
        else:
            print("error action")
            user_answer = input("write the next action: ")