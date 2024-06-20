import sqlite3
import time

class Database:
	def __init__(self, db_file):
		self.singup = 0
		self.nickname = ' '
		# self.money = 0
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()

		