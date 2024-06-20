import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = 'Тут ваш токен'  # Замените на свой токен
bot_name = 'AnonimQuections_bot'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    referral_link = generate_referral_link(message.from_user.id)
    await message.reply(f"Привет! Я анонимный вопросник. Перейди по ссылке, чтобы задать вопрос: {referral_link}")


@dp.message_handler()
async def handle_question(message: types.Message):
    question = message.text
    recipient = extract_user_id_from_referral_link(message.text)
    sender = message.from_user.id

    if recipient is not None:
        await bot.send_message(recipient, f"Анонимный вопрос: {question}")
        await message.reply("Ваш вопрос был отправлен получателю.")
    else:
        await message.reply("Неправильный формат сообщения. Пожалуйста, воспользуйтесь реферальной ссылкой для задания вопроса.")


def generate_referral_link(user_id):
    return f"http://t.me/{bot_name}?start={user_id}"


def extract_user_id_from_referral_link(referral_link):
    try:
        if referral_link and referral_link.startswith('?start='):
            user_id = referral_link.split('?start=')[1]
            return int(user_id)
    except (ValueError, TypeError):
        pass
    return None


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
