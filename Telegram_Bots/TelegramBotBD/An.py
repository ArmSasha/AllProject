import telebot
from telebot import types
import ast
import time
import datetime

import sqlite3

#bot
bot = telebot.TeleBot('1739386190:AAHFRmJbHnCcE6NK1rMqOF9vMaiklw7PBP4')





# act = {"Отправить снимок кота ": "Hello", "Отправьте скриншот": "Никита", "Написать привет": "Задание"}
# crossIcon = u"\u274C"

# def makeKeyboard():
#     markup = types.InlineKeyboardMarkup()

#     for key, value in act.items():
#         markup.add(types.InlineKeyboardButton(text=value,
#                                               callback_data="['value', '" + value + "', '" + key + "']"),
#         types.InlineKeyboardButton(text=crossIcon,
#                                    callback_data="['key', '" + key + "']"))

#     return markup



# @bot.message_handler(commands=['test'])
# def handle_command_adminwindow(message):
#     bot.send_message(chat_id=message.chat.id,
#                      text="Активные задачи",
#                      reply_markup=makeKeyboard(),
#                      parse_mode='HTML')




# @bot.callback_query_handler(func=lambda call: True)
# def handle_query(call):

#     if (call.data.startswith("['value'")):
#         print(f"call.data : {call.data} , type : {type(call.data)}")
#         print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
#         valueFromCallBack = ast.literal_eval(call.data)[1]
#         keyFromCallBack = ast.literal_eval(call.data)[2]
#         bot.answer_callback_query(callback_query_id=call.id,
#                               show_alert=True,
#                               text="Ты нажал на  " + valueFromCallBack + "\n Описание: " + keyFromCallBack)

#     if (call.data.startswith("['key'")):
#         keyFromCallBack = ast.literal_eval(call.data)[1]
#         del act[keyFromCallBack]
#         bot.edit_message_text(chat_id=call.message.chat.id,
#                               text="Активные задачи",
#                               message_id=call.message.message_id,
#                               reply_markup=makeKeyboard(),
#                               parse_mode='HTML')

# @bot.message_handler(commands = 'act')
# def act(message):
# 	rmk = types.ReplyKeyboardMarkup(resize_keyboard= True)
# 	rmk.add(types.KeyboardButton('ДА'), types.KeyboardButton('НЕТ'))
#
# 	msg = bot.send_message(message.chat.id, 'Желаете добавить активную задачу?', reply_markup = rmk)
# 	bot.register_next_step_handler(msg, user_answer)
#
# def user_answer(message):
# 	if message.text == 'ДА':
# 		msg = bot.send_message(message.chat.id, 'Впишите задачу и описание')
# 		bot.register_next_step_handler(msg, user_reg)
# 	elif message.text == 'НЕТ':
# 		bot.send_message(message.chat.id, 'Хорошо!')
# 	else:
# 		bot.send_message(message.chat.id, 'Ты что?')
#
# def user_reg(message):
# 	bot.send_message(message.chat.id, f'Задача: {message.text}')



@bot.message_handler(commands=['info'])
def get_user_info(message):



	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
	item_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')

	markup_inline.add(item_yes, item_no)
	bot.send_message(message.chat.id, 'Желаете обавить активную задачу?',
		reply_markup = markup_inline
		)


@bot.callback_query_handler(func = lambda call: True)

def answer(call):
	if call.data == 'yes':
		msg = bot.send_message(call.message.chat.id, 'Впишите задачу и описание')
		bot.register_next_step_handler(msg, user_reg)



	elif call.data == 'no':
		bot.send_message(call.message.chat.id, '- Хорошо')


		connect = sqlite3.connect('An.db')
		cursor = connect.cursor()

		cursor.execute("SELECT ACTIV FROM An")
		rows = cursor.fetchall()

		cursor = connect.cursor()

		l = [ ]
		for row in rows:
		    for x in row:
		        l.append(x)

		for task in l:
			bot.send_message(call.message.chat.id, f'{task}')



def user_reg(message):

	bot.send_message(message.chat.id, f'Задача: {message.text}')

	connect = sqlite3.connect('An.db')
	cursor = connect.cursor()

	cursor.execute("""CREATE TABLE IF NOT EXISTS An(
			ID INTEGER,
			NICK TEXT,
		    ACTIV TEXT
		)""")

	connect.commit()

	activ = (message.text)

	print(activ)

	id = message.chat.id
	nick = message.from_user.username

	cursor.execute("INSERT INTO An (id, nick, activ) VALUES (?,?,?)", (id,nick,activ,))
	connect.commit()


	connect = sqlite3.connect('An.db')
	cursor = connect.cursor()

	cursor.execute("SELECT ACTIV FROM An")
	rows = cursor.fetchall()

	cursor = connect.cursor()

	l = [ ]
	for row in rows:
	    for x in row:
	        l.append(x)

	for task in l:
		bot.send_message(message.chat.id, f'- {task}' )








@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'МОЙ ID':
		bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
	elif message.text == 'МОЙ НИК':
		bot.send_message(message.chat.id, f'Your NICK: {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    today = datetime.datetime.today()

    nas = today.strftime("%Y-%m-%d-%H.%M.%S")

    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'An/Photo/' + message.from_user.first_name + nas + '.jpeg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото добавлено")


    # print(message.from_user.id )
    # print(message.from_user.first_name)
    # print(message.from_user.last_name)
    # print(message.from_user.username)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'sticker':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECNdVggCreFQjCoRG_IK8tIXCimFi0LgACAQADwDZPExguczCrPy1RHwQ')



while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)