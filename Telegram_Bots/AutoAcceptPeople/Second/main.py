from aiogram import Dispatcher, Bot, types, executor
from config import data

bot = Bot(data["token"], parse_mode="html")
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def some_handler(chat_member: types.ChatJoinRequest):
	await chat_member.approve()

	await bot.send_message(chat_member.from_user.id, data["text"])

if __name__ == "__main__":
	executor.start_polling(dp)