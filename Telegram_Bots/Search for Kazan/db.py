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



# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------
# #                PROMO CODES
# #----------------------------------------------------------------------------------------------------------------

#     def get_promo_points(self, code):
#         with self.connection:
#             result = self.cursor.execute("SELECT points FROM promo_codes WHERE code = ?", (code,)).fetchone()
#             if result:
#                 return result[0]
#             return 0  # Возвращаем 0, если промокод не найден

# #----------------------------------------------------------------------------------------------------------------

#     def add_used_promo(self, user_id, promo_code):
#         with self.connection:
#             return self.cursor.execute("INSERT INTO used_promo (user_id, promo_code) VALUES (?, ?)", (user_id, promo_code))

# #----------------------------------------------------------------------------------------------------------------

#     def check_used_promo(self, user_id, promo_code):
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM used_promo WHERE user_id = ? AND promo_code = ?", (user_id, promo_code)).fetchall()
#             return bool(result)


# #----------------------------------------------------------------------------------------------------------------


#     def minus_usage_promo(self, promo_code):
#         with self.connection:
#             return self.cursor.execute("UPDATE promo_codes SET remaining_activations = remaining_activations - 1 WHERE code = ?", (promo_code,))

# #----------------------------------------------------------------------------------------------------------------

#     def existence_promo(self, code):
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM promo_codes WHERE code = ? AND remaining_activations > 0", (code,)).fetchall()
#             return bool(result)


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    
    def add_questionnaires(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO questionnaires (user_id) VALUES (?)", (user_id,))

#----------------------------------------------------------------------------------------------------------------

    def set_date(self, user_id, date):
        with self.connection:
            return self.cursor.execute("UPDATE users SET date=? WHERE user_id = ?", (date, user_id,))

    def get_date(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT date FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                date = str(row[0])
            return date

#----------------------------------------------------------------------------------------------------------------


    def set_anonymity(self, user_id, anonymity):
        with self.connection:
            return self.cursor.execute("UPDATE questionnaires SET anonymity = ? WHERE user_id = ?", (anonymity, user_id,))


    def get_anonymity(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT anonymity FROM questionnaires WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                anonymity = str(row[0])
            return anonymity

#----------------------------------------------------------------------------------------------------------------


    def set_photo(self, user_id, photo_id):
        with self.connection:
            return self.cursor.execute("UPDATE questionnaires SET photo_id = ? WHERE user_id = ?", (photo_id, user_id,))


    def get_photo(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT photo_id FROM questionnaires WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                photo_id = str(row[0])
            return photo_id

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def null_num_questionnaires(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE users SET num_questionnaires=? WHERE user_id=?", (0, user_id,))

    def set_num_questionnaires(self, user_id, num_questionnaires):
        with self.connection:
            return self.cursor.execute("UPDATE users SET num_questionnaires = ? WHERE user_id = ?", (num_questionnaires, user_id,))

    def get_num_questionnaires(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT num_questionnaires FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                num_questionnaires = str(row[0])
            return num_questionnaires


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    # def set_age(self, user_id, age):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id,))


    # def get_age(self, user_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,)).fetchall()

    #         for row in result:
    #             age = str(row[0])
    #         return age


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

    def set_text(self, user_id, text):
        with self.connection:
            return self.cursor.execute("UPDATE questionnaires SET text = ? WHERE user_id = ?", (text, user_id,))

    def get_text(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT text FROM questionnaires WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                text = str(row[0])
            return text

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

    # def set_gender(self, user_id, gender):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id,))

    # def get_gender(self, user_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,)).fetchall()

    #         for row in result:
    #             gender = str(row[0])
    #         return gender



#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

    def null_block(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE users SET block=0 WHERE user_id=?", (user_id,))

    def set_block(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE users SET block=1 WHERE user_id =?", (user_id,))

    def get_block(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT block FROM users WHERE user_id = ?", (user_id,)).fetchone()

            return result[0]
            # return int(result[0])

            # return bool(result)

            # for row in result:
            #     global blocking
            #     blocking = int(row[0])
            # return blocking


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

    # def null_num_chats(self, user_id):
    #     with self.connection:
    #         #cursor.execute("INSERT INTO likes_dislikes likes = ?, dislikes = ? WHERE user_id = ? ", (0, 0, user_id,))
    #         return self.cursor.execute("UPDATE users SET num_chats=? WHERE user_id=?", (0, user_id,))

    # def set_num_chats(self, user_id, num_chats):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET num_chats=? WHERE user_id = ?", (num_chats, user_id,))

    # def get_num_chats(self, user_id):
    #     with self.connection:
    #         num_chat = self.cursor.execute("SELECT num_chats FROM users WHERE user_id = ?", (user_id,))
    #         chats = num_chat.fetchone()[0]
    #         num_chats = int(chats)
    #         return num_chats

    # def get_top_num_chats(self):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT name, num_chats FROM users ORDER BY num_chats DESC").fetchmany(10)

    #         #dict_result = dict(result)
    #         #return dict_result
    #         # output_str = ""
    #         # for row in result:
    #         #     output_str += "{0}: {1}\n".format(row[0], row[1])
    #         #     print(output_str)
    #         #     return ("{0}: {1}".format(row[0], row[1]))
    #         # i=1
    #         # output_list = ["{0}) {1}: {2}".format(i+1, row[0], row[1]) for row in result]
    #         # output_str = "\n".join(output_list)

    #         output_str = "\n".join(["{0}) {1}: {2} Диалога/ов".format(i+1, row[0], row[1]) for i, row in enumerate(result)])
    #         return output_str

    #         # # Создание пустых списков
    #         # keys = []
    #         # values = []
    #         # # Извлечение ключей и значений из картежа
    #         # for item in result:
    #         #     key, value = item
    #         #     keys.append(key)
    #         #     values.append(value)
    #         # return keys, values


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

    # def null_like_dislike(self, user_id):
    #     with self.connection:
    #         #cursor.execute("INSERT INTO likes_dislikes likes = ?, dislikes = ? WHERE user_id = ? ", (0, 0, user_id,))
    #         return self.cursor.execute("UPDATE users SET likes=?, dislikes=? WHERE user_id=?", (0, 0, user_id,))


    # def set_likes(self, user_id, likes):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET likes=? WHERE user_id = ?", (likes, user_id,))

    # def set_dislikes(self, user_id, dislikes):
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET dislikes=? WHERE user_id = ?", (dislikes, user_id,))

    # def get_like(self, partner):
    #     with self.connection:
    #         ratel = self.cursor.execute("SELECT likes FROM users WHERE user_id = ?", (partner,))
    #         like = ratel.fetchone()[0]
    #         likes = int(like)
    #         return likes

    # def get_dislike(self, partner):
    #     with self.connection:
    #         rated = self.cursor.execute("SELECT likes, dislikes FROM users WHERE user_id = ?", (partner,))
    #         dislike = rated.fetchone()[1]
    #         dislikes = int(dislike)
    #         return dislikes

#----------------------------------------------------------------------------------------------------------------

