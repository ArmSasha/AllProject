import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    async def user_exists(self, user_id):
        result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))
    
    async def chat_exists(self, chat_id):
        result = self.cursor.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,)).fetchall()
        return bool(len(result))

    async def add_user(self, user_id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.connection.commit()
    
    async def add_chat(self, chat_id, welcome):
        self.cursor.execute("INSERT INTO chats (chat_id, welcome) VALUES (?, ?)", (chat_id, welcome))
        self.connection.commit()

    async def set_voice(self, voice):
        result = self.cursor.execute(f"SELECT voice FROM voice").fetchone()
        get = result[0]

        self.cursor.execute(f"UPDATE voice SET voice = {get + voice}")
        self.connection.commit()
    
    async def set_welcome(self, chat_id, welcome):
        self.cursor.execute(f"UPDATE chats SET welcome = {welcome} WHERE chat_id = {chat_id}")
        self.connection.commit()
    
    async def get_welcome(self, chat_id):
        get = self.cursor.execute(f"SELECT welcome FROM chats WHERE chat_id = {chat_id}").fetchone()
        return get[0]

    async def set_voice_old(self, voice):
        result = self.cursor.execute(f"SELECT count_voice FROM old").fetchone()
        get = result[0]

        self.cursor.execute(f"UPDATE old SET count_voice = {voice}")
        self.connection.commit()

    async def set_users_old(self, users):
        result = self.cursor.execute(f"SELECT count_users FROM old").fetchone()
        get = result[0]

        self.cursor.execute(f"UPDATE old SET count_users = {users}")
        self.connection.commit()

    async def set_chat_old(self, chats):
        result = self.cursor.execute(f"SELECT count_chat FROM old").fetchone()
        get = result[0]

        self.cursor.execute(f"UPDATE old SET count_chat = {chats}")
        self.connection.commit()

    async def get_users(self):
        result = self.cursor.execute("SELECT * FROM users").fetchall()
        return result

    async def get_chats(self):
        result = self.cursor.execute("SELECT chat_id FROM chats").fetchall()
        return result

    async def get_voice(self):
        result = self.cursor.execute("SELECT voice FROM voice").fetchone()
        return result[0]

    async def get_users_old(self):
        result = self.cursor.execute("SELECT count_users FROM old").fetchall()
        return result[0]

    async def get_chats_old(self):
        result = self.cursor.execute("SELECT count_chat FROM old").fetchall()
        return result[0]

    async def get_voice_old(self):
        result = self.cursor.execute("SELECT count_voice FROM old").fetchone()
        return result[0]