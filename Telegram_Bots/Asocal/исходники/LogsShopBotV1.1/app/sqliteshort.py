"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Файл для упрощенной работы с sqlite

"""

import sqlite3


class SQLite:

    cur = None
    conn = None

    @staticmethod
    def create_base():
        """Создаем базу blyat."""

        SQLite.conn = sqlite3.connect("base.db", check_same_thread=False)
        SQLite.cur = SQLite.conn.cursor()

        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INT, balance INT, want TEXT, pay TEXT)""")
        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS txnids_qiwi(id TEXT)""")
        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS txnids_lava(id TEXT)""")
        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS txnids_lolz(id TEXT)""")
        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS txnids_crystalpay(id TEXT)""")
        SQLite.cur.execute("""CREATE TABLE IF NOT EXISTS categories(name TEXT, data TEXT, amount INT)""")

        return True

    @staticmethod
    def check_payment(type : str,id : str):
        """Чекаем находится ли айди счета в списке базы."""

        data = SQLite.cur.execute(f'SELECT id FROM txnids_{type} WHERE id = "{id}"').fetchall()
        if data:
            return True

        return False

    @staticmethod
    def add_payment(type : str,id : str):
        """Добавить транзакцию в базу чтобы баланс не пополнялся второй раз."""

        SQLite.cur.execute(f"INSERT INTO txnids_{type} VALUES('{id}')")
        SQLite.conn.commit()

        return True

    @staticmethod
    def add_user(user_id : int):
        """Добавить пользователя."""

        SQLite.cur.execute(f"INSERT INTO users VALUES({user_id}, 0, '', '')")
        SQLite.conn.commit()

        return True

    @staticmethod
    def get_users():
        """Получить пользователей."""

        data = SQLite.cur.execute(f'SELECT * FROM users').fetchall()

        return data


    @staticmethod
    def get_user(user_id : int):
        """Получить пользователя."""

        data = SQLite.cur.execute(f'SELECT * FROM users WHERE user_id = {user_id}').fetchall()

        if not data:
            SQLite.add_user(user_id)
            return SQLite.get_user(user_id)

        return data[0]

    @staticmethod
    def add_balance(user_id : int, money : int):
        """Выдать баланс ползователю."""

        data = SQLite.get_user(user_id)
        new_balance = money + data[1]
        SQLite.cur.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {user_id}').fetchall()
        SQLite.conn.commit()
        return True

    @staticmethod
    def want_log(user_id : int, category : str):
        """Ставим флажок на то, какие логи хочет купить пользователь. (Сделал
        чтобы не ебаться с списками)
        """

        SQLite.cur.execute(f'UPDATE users SET want = "{category}"WHERE user_id = {user_id}').fetchall()
        SQLite.conn.commit()
        return True

    @staticmethod
    def want_pay(user_id : int, pay : str):
        """Ставим флажок на то, какой способ оплаты у нас будет. (Сделал
        чтобы не ебаться с списками)
        """

        SQLite.cur.execute(f'UPDATE users SET pay = "{pay}" WHERE user_id = {user_id}').fetchall()
        SQLite.conn.commit()
        return True

    @staticmethod
    def del_balance(user_id : int, money : int):
        """Удаляем некоторые средства с баланса пользователя."""

        data = SQLite.get_user(user_id)
        new_balance = data[1] - money
        SQLite.cur.execute(f'UPDATE users SET balance = {new_balance} WHERE user_id = {user_id}').fetchall()
        SQLite.conn.commit()
        return True

    @staticmethod
    def get_logs(type : str):
        """Получаем все логги."""

        data = SQLite.cur.execute(f'SELECT * FROM "{type}"').fetchall()

        return data

    @staticmethod
    def del_log(type : str, name : str):
        """Удаляем лог из базы"""

        SQLite.cur.execute(f"DELETE FROM '{type}' WHERE logs = '{name}'")
        SQLite.conn.commit()
        return True

    @staticmethod
    def clear_balance(user_id : int):
        """Полностью очищаем баланс ползователю."""

        SQLite.cur.execute(f'UPDATE users SET balance = 0 WHERE user_id = {user_id}').fetchall()
        SQLite.conn.commit()
        return True


    @staticmethod
    def add_log(type, name):
        """Добавляем лог в базу."""

        SQLite.cur.execute(f"INSERT INTO '{type}' VALUES('{name}')")
        SQLite.conn.commit()
        return True

    @staticmethod
    def create_category(name : str, data : str, amount : int):
        """Создаем категорию."""

        SQLite.cur.execute(f"INSERT INTO categories VALUES('{name}', '{data}', {amount})")
        SQLite.cur.execute(f"""CREATE TABLE IF NOT EXISTS '{data}'(logs TEXT)""")
        SQLite.conn.commit()
        return True

    @staticmethod
    def get_categories():
        """Получаем все категории"""

        data = SQLite.cur.execute(f'SELECT * FROM categories').fetchall()

        return data


    @staticmethod
    def get_category(data):
        """Получаем все категории"""

        data = SQLite.cur.execute(f'SELECT * FROM categories WHERE data = "{data}"').fetchall()

        return data

    @staticmethod
    def del_category(data : str):
        """Удаляем категорию."""

        SQLite.cur.execute(f"DROP TABLE '{data}'")
        SQLite.cur.execute(f"""DELETE FROM categories WHERE data = '{data}'""")
        SQLite.conn.commit()
        return True
