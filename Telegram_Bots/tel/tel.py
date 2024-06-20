import telebot, ctypes, requests, urllib.request
from os import system as s
from pyautogui import screenshot as scr
from os.path import abspath as pat
from time import time



bot = telebot.TeleBot('Тут ваш токен')
need_format = False

def sender(id, text):
	bot.send_message(id, text)

def send_photo(id, img):
	bot.send_photo(id, img)


@bot.message_handler(commands = ['start'])
def starter(message):
	sender( message.chat.id, 'Выберите одну из следующих команд:\n/wallpaper\n/ping\n/photo\n/autoformat\n/my_id\n/photo' )


@bot.message_handler(commands = ['ping'])
def pinger(message):
	st = message.date.real
	sender( message.chat.id, f'Ваш пинг: {round(time()-st, 2)}')


@bot.message_handler(commands = ['my_id'])
def ider(message):
	sender( message.chat.id, message.chat.id)


@bot.message_handler(commands = ['autoformat'])
def to_format(message):
	need_format = True
	msg = bot.send_message(message.chat.id, 'Пришли мне .py документ и я сделаю из него шедевр')
	bot.register_next_step_handler(msg, formater)


@bot.message_handler(commands = ['photo'])
def screen(message):
	try:
		scr('screenshot.jpeg')
		file = open('screenshot.jpeg', 'rb')
		send_photo(message.chat.id, file)
		file.close()
		s('del screenshot.jpeg')
	except:
		sender(message.chat.id, 'Error!')


@bot.message_handler(commands = ['wallpaper'])
def desk(message):
	msg = bot.send_message(message.chat.id, 'Пришли мне фото или ссылку на фото')
	bot.register_next_step_handler(msg, loader)


@bot.message_handler(content_types = ['photo', 'text'], func = lambda message: ((message.photo) or (message.text and ('http' in message.text.lower()))))
def loader(message):
	if message.photo:
		img = bot.get_file(message.photo[-1].file_id)
		path = bot.download_file(img.file_path)
		with open('wall.jpeg', 'wb') as file:
			file.write(path)
		file.close()
		ctypes.windll.user32.SystemParametersInfoW(20, 0, pat('wall.jpeg'), 0)
		sender(message.chat.id, 'Обои успешно установлены!')

	elif 'http' in message.text.lower():
		img = urllib.request.urlopen(message.text).read()
		with open('wall.jpeg', 'wb') as file:
			file.write(img)
		file.close()
		ctypes.windll.user32.SystemParametersInfoW(20, 0, pat('wall.jpeg'), 0)
		sender(message.chat.id, 'Обои успешно установлены!')

	else:
		sender(message.chat.id, 'Что-то пошло не так...')


@bot.message_handler(content_types = ['document'], func = lambda need_format: ((need_format == True) and (message.document)))
def formater(message):
	if message.document:
		if message.document.file_name.endswith('.py'):
			doc = bot.get_file(message.document.file_id)
			path = bot.download_file(doc.file_path)

			with open(f'loaded{message.chat.id}.py', 'wb') as file:
				file.write(path)
			file.close()
			sender(message.chat.id, 'Файл загружен, идёт обработка файла...')

			s(f'yapf -i loaded{message.chat.id}.py')
			sender(message.chat.id, 'Файл обработан!')

			file = open(f'loaded{message.chat.id}.py', 'rb')
			bot.send_document(message.chat.id, file)
			file.close()
			s(f'del loaded{message.chat.id}.py')
		else:
			sender(message.chat.id, 'Я форматирую только .py файлы')
		need_format = False
	else:
		sender(message.chat.id, 'Что-то пошло не так...')
	need_format = False


bot.polling(none_stop = True, interval = 0)
