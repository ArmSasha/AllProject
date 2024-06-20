import sqlite3
import telebot
from telebot import types

#bot
bot = telebot.TeleBot('5453482108:AAH1-2M7NzqDMPJDL59jX-fK9jmLVrJPaAw')






class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

user_dict = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Привет!
Как тебя зовут?
""")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Солько тебе лет')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Напиши возраст цифрами. Сколько тебе лет?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Мужчина', 'Женщина')
        msg = bot.reply_to(message, 'Какого ты пола?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Мужчина') or (sex == u'Женщина'):
            user.sex = sex
        else:
            raise Exception("Неверный пол")
        bot.send_message(chat_id, 'Ок ' + ' \n Имя:' + user.name + '\n Возраст:' + str(user.age) + '\n Пол:' + user.sex)



			connect = sqlite3.connect('Basse.db')
			cursor = connect.cursor()

			cursor.execute("""CREATE TABLE IF NOT EXISTS Basse(
			    id INTEGER,
			    name TEXT,
			    age INTEGER,
			    sex TEXT
			)""")

			connect.commit()

			#check
			people_id = message.chat.id
			cursor.execute(f"SELECT id FROM Basse WHERE id = {people_id}")
			data = cursor.fetchone()
			print(data)
			if data is None:
			    #add

			    users_id = [message.chat.id]
			    cursor.execute("INSERT INTO Basse VALUES(? ? ? ?);", users_id, user.name, user.age, user.sex)
			    connect.commit()

	else:
	    bot.send_message(message.chat.id, 'Такой пользовать уже существует!')

    except Exception as e:
        bot.reply_to(message, 'oooops')







#polling
bot.polling()


