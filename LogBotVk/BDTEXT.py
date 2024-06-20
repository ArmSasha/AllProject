import sqlite3 as sql
from random import randint

global db
global sql



db = sql.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()

def reg():
    global user_login
    user_login = input('Login: ')
    user_password = input("Password: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print("Ok")
    else:
        print("Такая запись уже есть!")

        for value in sql.execute("SELECT * FROM users"):
            print(value)

def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()

    print('Запись удалена!')

def casino():
    global user_login
    global balance
    user_login = input('Log in:')
    number = randint(1,2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует. Зарегистрируйтесь')
        reg()



    if number == 1:
        sql.execute(f'UPDATE users SET cash = {balance + 1000} WHERE login = "{user_login}"')
        db.commit()

        print("Ура вы выйграли!")

    else:
        print("Вы проиграли")
        delete_db()

def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)

def main():
    casino()
    enter()

while True:
    main()
    db.commit()






























