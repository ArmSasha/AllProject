from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton as ib
from logging import basicConfig
import sqlite3

basicConfig()

bot = Bot(token="", parse_mode="HTML")
dp = Dispatcher(bot)

conn = sqlite3.connect("./database.db")
cursor = conn.cursor()

def writeNewUser(
		user_id: int,
		username: str):
	status = False

	info = cursor.execute(
        "SELECT * FROM users WHERE user_id = ?", [user_id]
	).fetchall()

	if len(info) == 0:
		cursor.execute(
                "INSERT INTO users VALUES (?,?)", [user_id, username]
		)
		conn.commit()
		status = True

		return status


@dp.chat_join_request_handler()
async def join(request: ChatJoinRequest):
	await request.approve()
	status = writeNewUser(user_id=request.from_user.id, username=request.from_user.username)
	if status:
		await bot.send_message(
			text="<b>🏳️‍🌈 Оставь тут ссыль на @end_soft</b>",
		)
	else:
		await bot.send_message(
			text="Ты уже был в боте"
		)


@dp.message_handler(commands="start")
async def start(m: Message):
	status = writeNewUser(user_id=m.from_user.id, username=m.from_user.username)
	if status:
		await m.answer(f"Привет, {m.from_user.get_mention()}")
	else:
		await m.answer(f"Привет, {m.from_user.get_mention()}")

if __name__ == "__main__":
	executor.start_polling(dp)