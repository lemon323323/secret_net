import sys
from mysql.connector import MySQLConnection, Error
com = input("Если вы уже зарегестрированы и хотите войти,\nвведите 'y',\nесли вы хотите зарегестрироваться,\nвведите 'n': ")
try:
    conn = MySQLConnection(user = "arseniy", host = "localhost", password = "ROBLOX323323", database = "ezhik_ru")
    cur = conn.cursor()
except Error as error:
    input(error)
    sys.exit()
def messages(uname):
    print("Введите 'mailBox' чтобы проверить почту ")
    print("Введите 'sendMail' чтобы отправить письмо ")
    print("Введите 'Exit' чтобы выйти")
    def start():
        choose = input("-> ")
        if choose == "mailBox":
            cur.execute("SELECT message,fname FROM messages WHERE uname='" + uname + "'")
            all = cur.fetchall()
            print("Вот ваши сообщения: ")
            if all:
                for j in all:
                    print(j)
                    print("\n")
            else:
                print("<пусто>")
            start()
        elif choose == "sendMail":
            touname = input("Введите имя получателя: ")
            message = input("Введите сообщение: ")
            fromname = uname
            args = (message, touname, fromname)
            query = "INSERT INTO messages(message,uname,fname) VALUES (%s,%s,%s)"
            cur.execute(query, args)
            conn.commit()
            start()
        elif choose == "Exit":
            cur.close()
            conn.close()
            sys.exit()
    start()
if com.lower() == "y":
    uname = input("Введите имя: ")
    pas = input("Введите пароль: ")
    args = (uname,pas)
    cur.execute("SELECT * FROM users")
    all = cur.fetchall()
    if args in all:
        input("5 секунд, полёт нормальный!")
        messages(uname)
    if args not in all:
        input("Такого пользователя не существует, либо пароль неверный")
elif com.lower() == "n":
    try:
        new_uname = input("Введите имя: ")
        new_pas = input("Введите пароль: ")
        new_args = (new_uname, new_pas)
        query = "INSERT INTO users(uname,pass) VALUES (%s,%s)"
        cur.execute(query, new_args)
        conn.commit()
        input("Добро пожаловать к нам в гости!")
        messages(new_uname)
    except:
        input("\nВ вашей форме регистрации присутствуют недопустимые символы\nтакие как: цифры, дефисы и т. д. ,\nлибо слишком много символов. На пароль максимум 8 символов,\nа на имя 10 символов")
