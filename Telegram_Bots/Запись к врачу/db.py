import sqlite3
import os.path

# Ищем путь до файла и ставим полный путь, в место относительного
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\database.db')

class Database:
    # def __init__(self, db_file):
    #     self.connection = sqlite3.connect(db_file)
    #     self.cursor = self.connection.cursor()

    def __init__(self):
        self.connection = sqlite3.connect(db_dir)
        self.cursor = self.connection.cursor()
        self.name = ' '



#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def add_column(self, data):
        with self.connection:
            return self.cursor.execute(f"""ALTER TABLE techniques ADD COLUMN VALUE (?) TEXT IF NOT EXISTS""", (data,))

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user(self, user_id, referrer_id=None):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

#----------------------------------------------------------------------------------------------------------------

    def get_info(self, fio):
        with self.connection:
            result = self.cursor.execute("SELECT info FROM doctors WHERE fio = ?", (fio,)).fetchall()

            for row in result:
                text = str(row[0])
            return text

    def get_specialization(self, fio):
        with self.connection:
            result = self.cursor.execute("SELECT direction FROM doctors WHERE fio = ?", (fio,)).fetchall()
            for row in result:
                specialization = str(row[0])
            return specialization

#----------------------------------------------------------------------------------------------------------------


    def set_surname(self, user_id, surname):
        with self.connection:
            return self.cursor.execute("UPDATE users SET surname = ? WHERE user_id = ?", (surname, user_id,))

    def get_surname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT surname FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                surname = str(row[0])
            return surname


#----------------------------------------------------------------------------------------------------------------


    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id,))


    def get_name(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                name = str(row[0])
            return name

#----------------------------------------------------------------------------------------------------------------


    def set_middlename(self, user_id, middlename):
        with self.connection:
            return self.cursor.execute("UPDATE users SET middlename = ? WHERE user_id = ?", (middlename, user_id,))

    def get_middlename(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT middlename FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                middlename = str(row[0])
            return middlename


#----------------------------------------------------------------------------------------------------------------


    def set_phone_number(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE users SET phone_number = ? WHERE user_id = ?", (phone_number, user_id,))

    def get_phone_number(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT phone_number FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                phone_number = str(row[0])
            return phone_number



#----------------------------------------------------------------------------------------------------------------


    def set_snils(self, user_id, snils):
        with self.connection:
            return self.cursor.execute("UPDATE users SET snils = ? WHERE user_id = ?", (snils, user_id,))

    def get_snils(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT snils FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                snils = str(row[0])
            return snils


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id,))


    def get_age(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                age = str(row[0])
            return age

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_gender(self, user_id, gender):
        with self.connection:
            return self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id,))

    def get_gender(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                gender = str(row[0])
            return gender
