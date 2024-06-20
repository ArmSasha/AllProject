import sqlite3
import time

class Database:
	def __init__(self, db_file):
		self.singup = 0
		self.nickname = ' '
		# self.money = 0
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()


	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
			return bool(len(result))


	def add_user(self, user_id, referrer_id=None):
		with self.connection:
			if referrer_id != None:
				return self.cursor.execute("INSERT INTO users (user_id, referrer_id) VALUES (?, ?)", (user_id, referrer_id,))
			else:
				return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))


	def count_referals(self, user_id):
		with self.connection:
			return self.cursor.execute("SELECT COUNT(id) as count FROM users WHERE referrer_id = ?", (user_id,)).fetchone()[0]

	# def user_money(self, user_id):
	# 	with self.connection:
	# 		result = self.cursor.execute("SELECT money FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
	# 		return int(result[0][0])

	# def set_money(self, user_id, money):
	# 	with self.connection:
	# 		return self.cursor.execute("UPDATE users SET money = ? WHERE user_id = ?", (money, user_id,))


	def add_check(self, user_id, money, bill_id):
			with self.connection:
				return self.cursor.execute("INSERT INTO 'check' (user_id, money, bill_id ) VALUES (?, ?, ?)", (user_id, money, bill_id,))


	def get_check(self, bill_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM 'check' WHERE bill_id = ?", (bill_id,)).fetchmany(1)
			if not bool(len(result)):
				return False
			return result[0]

	def delete_check(self, bill_id):
		with self.connection:
			return self.cursor.execute("DELETE FROM 'check' WHERE bill_id = ?", (bill_id,))



	def set_nickname(self, user_id, nickname):
		with self.connection:
			return self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?", (nickname, user_id,))


	def get_signup(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				signup = str(row[0])
			return signup


	def set_signup(self, user_id, signup):
		with self.connection:
			return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id,))


	def get_nickname(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT nickname FROM users WHERE user_id = ?", (user_id,)).fetchall()
			for row in result:
				nickname = str(row[0])
			return nickname


	# def set_active(self, user_id, active):
	# 	with self.connection:
	# 		return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))


	def get_users(self):
		with self.connection:
			result = self.cursor.execute("SELECT user_id FROM users").fetchall()
			return result



	# def set_age(self, user_id, age):
	# 	with self.connection:
	# 		return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id,))

	# def get_age(self, user_id):
	# 	with self.connection:
	# 		result = self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,)).fetchall()
	# 		for row in result:
	# 			age = int(row[0])
	# 		return age



	# def set_time_sub(self, user_id, time_sub):
	# 	with self.connection:
	# 		return self.cursor.execute("UPDATE users SET time_sub = ? WHERE user_id = ?", (time_sub, user_id,))


	# def get_time_sub(self, user_id):
	# 	with self.connection:
	# 		result = self.cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
	# 		for row in result:
	# 			time_sub = int(row[0])
	# 		return time_sub

	# def get_sub_status(self, user_id):
	# 	with self.connection:
	# 		result = self.cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
	# 		for row in result:
	# 			time_sub = int(row[0])

	# 		if time_sub > int(time.time()):
	# 			return True
	# 		else:
	# 			return False
