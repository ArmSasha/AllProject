import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as con

logging.basicConfig(level=logging.INFO)

bot = Bot(token=con.TOKEN)
dp = Dispatcher(bot)

async def check_sub_channels(channels, user_id):
	for channel in channels:
		chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
		if chat_member['status'] == 'left':
			return False
	return True


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	if message.chat.type == 'private':
		if await check_sub_channels(con.CHANNELS, message.from_user.id):
			await bot.send_message(message.from_user.id, 'Hi', reply_markup = nav.profileKeyboard)
		else:
			await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

@dp.message_handler()
async def bot_message(message: types.Message):
	if message.chat.type == 'private':
		if await check_sub_channels(con.CHANNELS, message.from_user.id):
			if message.text == 'Profile':
				await bot.send_message(message.from_user.id, f'ID: {message.from_user.id}')
		else:
			await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())


@dp.callback_query_handler(text='subchanneldone')
async def subchanneldone(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if await check_sub_channels(con.CHANNELS, message.from_user.id):
		await bot.send_message(message.from_user.id, 'Hi', reply_markup = nav.profileKeyboard)
	else:
		await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)