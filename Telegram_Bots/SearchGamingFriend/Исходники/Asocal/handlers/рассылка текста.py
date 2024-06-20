from aiogram.utils import executor
from aiogram import types, Dispatcher
from create_bot import dp, bot, db


# @dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
	if message.chat.type == 'private':
		if message.from_user.id == 1030874842 or message.from_user.id == 745814407:
			text = message.text[9:]
			users = db.get_users()
			for row in users:
				try:
					await bot.send_message(row[0], text)
					if int(row[1]) != 1:
						db.set_active(row[0], 1)
				except:
					db.set_active(row[0], 0)
			await bot.send_message(message.from_user.id, 'Рассылка успешно окончена!')


#Регистрируем хендлеры
def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(sendall, commands = ['sendall'])