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

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

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

# #----------------------------------------------------------------------------------------------------------------

    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id,))


    def get_age(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                age = str(row[0])
            return age


# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

#     def set_text(self, user_id, text):
#         with self.connection:
#             return self.cursor.execute("UPDATE users SET text = ? WHERE user_id = ?", (text, user_id,))

#     def get_text(self, user_id):
#         with self.connection:
#             result = self.cursor.execute("SELECT text FROM users WHERE user_id = ?", (user_id,)).fetchall()

#             for row in result:
#                 text = str(row[0])
#             return text

# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

    def set_gender(self, user_id, gender):
        with self.connection:
            return self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id,))

    def get_gender(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                gender = str(row[0])
            return gender



# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

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


# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

#     def null_num_chats(self, user_id):
#         with self.connection:
#             #cursor.execute("INSERT INTO likes_dislikes likes = ?, dislikes = ? WHERE user_id = ? ", (0, 0, user_id,))
#             return self.cursor.execute("UPDATE users SET num_chats=? WHERE user_id=?", (0, user_id,))

#     def set_num_chats(self, user_id, num_chats):
#         with self.connection:
#             return self.cursor.execute("UPDATE users SET num_chats=? WHERE user_id = ?", (num_chats, user_id,))

#     def get_num_chats(self, user_id):
#         with self.connection:
#             num_chat = self.cursor.execute("SELECT num_chats FROM users WHERE user_id = ?", (user_id,))
#             chats = num_chat.fetchone()[0]
#             num_chats = int(chats)
#             return num_chats

#     def get_top_num_chats(self):
#         with self.connection:
#             result = self.cursor.execute("SELECT name, num_chats FROM users ORDER BY num_chats DESC").fetchmany(10)
#             #dict_result = dict(result)
#             #return dict_result
#             # output_str = ""
#             # for row in result:
#             #     output_str += "{0}: {1}\n".format(row[0], row[1])
#             #     print(output_str)
#             #     return ("{0}: {1}".format(row[0], row[1]))
#             # i=1
#             # output_list = ["{0}) {1}: {2}".format(i+1, row[0], row[1]) for row in result]
#             # output_str = "\n".join(output_list)
#             output_str = "\n".join(["{0}) {1}: {2} Диалога/ов".format(i+1, row[0], row[1]) for i, row in enumerate(result)])
#             return output_str

#             # # Создание пустых списков
#             # keys = []
#             # values = []
#             # # Извлечение ключей и значений из картежа
#             # for item in result:
#             #     key, value = item
#             #     keys.append(key)
#             #     values.append(value)
#             # return keys, values


# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

    def null_like_dislike(self, user_id):
        with self.connection:
            #cursor.execute("INSERT INTO likes_dislikes likes = ?, dislikes = ? WHERE user_id = ? ", (0, 0, user_id,))
            return self.cursor.execute("UPDATE users SET likes=?, dislikes=? WHERE user_id=?", (0, 0, user_id,))


    def set_likes(self, user_id, likes):
        with self.connection:
            return self.cursor.execute("UPDATE users SET likes=? WHERE user_id = ?", (likes, user_id,))

    def set_dislikes(self, user_id, dislikes):
        with self.connection:
            return self.cursor.execute("UPDATE users SET dislikes=? WHERE user_id = ?", (dislikes, user_id,))

    def get_like(self, partner):
        with self.connection:
            ratel = self.cursor.execute("SELECT likes FROM users WHERE user_id = ?", (partner,))
            like = ratel.fetchone()[0]
            likes = int(like)
            return likes

    def get_dislike(self, partner):
        with self.connection:
            rated = self.cursor.execute("SELECT likes, dislikes FROM users WHERE user_id = ?", (partner,))
            dislike = rated.fetchone()[1]
            dislikes = int(dislike)
            return dislikes

# #----------------------------------------------------------------------------------------------------------------

# #----------------------------------------------------------------------------------------------------------------

#     def get_users(self):
#         with self.connection:
#             result = self.cursor.execute("SELECT user_id FROM users").fetchall()
#             return result

# #----------------------------------------------------------------------------------------------------------------

#     def add_queue(self, user_id):
#         with self.connection:
#             return self.cursor.execute("INSERT INTO queue (user_id) VALUES (?)", (user_id,))

# #----------------------------------------------------------------------------------------------------------------


#     def delete_queue(self, user_id):
#         with self.connection:
#             return self.cursor.execute("DELETE FROM queue WHERE user_id = ?", (user_id,))

# #----------------------------------------------------------------------------------------------------------------


#     def get_queue(self):
#         with self.connection:
#             queue = self.cursor.execute("SELECT * FROM queue").fetchmany(1)

#             if bool(len(queue)):
#                 for row in queue:
#                     return row[1]
#             else:
#                 return False

# #----------------------------------------------------------------------------------------------------------------


#     def create_chat(self, user_id, partner_id):
#         if partner_id != 0:
#             with self.connection:
#                 self.cursor.execute("INSERT INTO chats (user, partner) VALUES (?, ?)", (user_id, partner_id))
#                 return True

#         return False

# #----------------------------------------------------------------------------------------------------------------


#     def get_chat(self, user_id):
#         with self.connection:
#             chat = self.cursor.execute("SELECT * FROM chats WHERE user = ? OR partner = ?", (user_id, user_id))

#             for i in chat:
#                 return [i[0], i[1] if i[1] != user_id else i[2]]

#             return False

# #----------------------------------------------------------------------------------------------------------------


#     def delete_chat(self, user_id):
#         with self.connection:
#             return self.cursor.execute("DELETE FROM chats WHERE user = ? OR partner = ?", (user_id, user_id))



#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def user_exists_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user_fortnite(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO fortnite (user_id) VALUES (?)", (user_id,))

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_kd_fortnite(self, user_id, kd):
        with self.connection:
            return self.cursor.execute("UPDATE fortnite SET kd = ? WHERE user_id = ?", (kd, user_id,))

    def get_kd_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT kd FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                kd = str(row[0])
            return kd

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_pr_fortnite(self, user_id, pr):
        with self.connection:
            return self.cursor.execute("UPDATE fortnite SET pr = ? WHERE user_id = ?", (pr, user_id,))

    def get_pr_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT pr FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                pr = str(row[0])
            return pr

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_role_fortnite(self, user_id, role):
        with self.connection:
            return self.cursor.execute("UPDATE fortnite SET role = ? WHERE user_id = ?", (role, user_id,))

    def get_role_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT role FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                role = str(row[0])
            return role

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_rank_fortnite(self, user_id, rank):
        with self.connection:
            return self.cursor.execute("UPDATE fortnite SET rank = ? WHERE user_id = ?", (rank, user_id,))

    def get_rank_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT rank FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                rank = str(row[0])
            return rank

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_description_fortnite(self, user_id, description):
        with self.connection:
            return self.cursor.execute("UPDATE fortnite SET description = ? WHERE user_id = ?", (description, user_id,))

    def get_description_fortnite(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT description FROM fortnite WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                description = str(row[0])
            return description

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def user_exists_valorant(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM valorant WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user_valorant(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO valorant (user_id) VALUES (?)", (user_id,))

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_kd_valorant(self, user_id, kd):
        with self.connection:
            return self.cursor.execute("UPDATE valorant SET kd = ? WHERE user_id = ?", (kd, user_id,))

    def get_kd_valorant(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT kd FROM valorant WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                kd = str(row[0])
            return kd

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_rank_valorant(self, user_id, rank):
        with self.connection:
            return self.cursor.execute("UPDATE valorant SET rank = ? WHERE user_id = ?", (rank, user_id,))

    def get_rank_valorant(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT rank FROM valorant WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                rank = str(row[0])
            return rank

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_description_valorant(self, user_id, description):
        with self.connection:
            return self.cursor.execute("UPDATE valorant SET description = ? WHERE user_id = ?", (description, user_id,))

    def get_description_valorant(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT description FROM valorant WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                description = str(row[0])
            return description

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def user_exists_csgo(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM csgo WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

#----------------------------------------------------------------------------------------------------------------

    def add_user_csgo(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO csgo (user_id) VALUES (?)", (user_id,))

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_faceit_csgo(self, user_id, faceit):
        with self.connection:
            return self.cursor.execute("UPDATE csgo SET faceit = ? WHERE user_id = ?", (faceit, user_id,))

    def get_faceit_csgo(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT faceit FROM csgo WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                faceit = str(row[0])
            return faceit

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_rank_csgo(self, user_id, rank):
        with self.connection:
            return self.cursor.execute("UPDATE csgo SET rank = ? WHERE user_id = ?", (rank, user_id,))

    def get_rank_csgo(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT rank FROM csgo WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                rank = str(row[0])
            return rank

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def set_description_csgo(self, user_id, description):
        with self.connection:
            return self.cursor.execute("UPDATE csgo SET description = ? WHERE user_id = ?", (description, user_id,))

    def get_description_csgo(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT description FROM csgo WHERE user_id = ?", (user_id,)).fetchall()

            for row in result:
                description = str(row[0])
            return description

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def get_people_fortnite(self, users_per_page, offset): #quantity
        with self.connection:

            # result = self.cursor.execute("SELECT users.name, users.age, fortnite.kd, fortnite.pr, fortnite.role, fortnite.description FROM users, fortnite ON users.user_id = fortnite.user_id").fetchall()

            result = self.cursor.execute(f"SELECT users.name, users.age, fortnite.kd, fortnite.pr, fortnite.role, fortnite.description FROM users, fortnite ON users.user_id = fortnite.user_id LIMIT {users_per_page} OFFSET {offset}").fetchall()

            return result

            # result = self.cursor.execute("SELECT users.name, users.age, fortnite.kd, fortnite.pr, fortnite.role, fortnite.description FROM users, fortnite ON users.user_id = fortnite.user_id").fetchmany(quantity)

            # # output_str = "\n\n".join(["{0}) Имя: {1} | Возраст: {2} | KD: {3} | PR: {4} | Role: {5} | Описание: {6}".format(i+1, row[0], row[1], row[2], row[3], row[4], row[5]) for i, row in enumerate(result)])
            # output_str = "\n ____________________ \n".join(["{0}) Имя: {1} \n Возраст: {2} \n KD: {3} \n PR: {4} \n Role: {5} \n Описание: {6}".format(i+1, row[0], row[1], row[2], row[3], row[4], row[5]) for i, row in enumerate(result)])
            # return output_str

