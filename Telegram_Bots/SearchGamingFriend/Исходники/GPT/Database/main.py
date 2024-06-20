import aiogram
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\database.db')
# Создание подключения к базе данных
conn = sqlite3.connect(db_dir)
cursor = conn.cursor()

# Выполнение запроса на объединение таблиц и получение данных
query = """
    SELECT u.name, u.age, f.kd, f.pr, f.description
    FROM users u
    JOIN fortnite f ON u.user_id = f.user_id
"""
cursor.execute(query)
data = cursor.fetchall()

# Формирование сообщений для бота
messages = []
def people(quantity):
    for i in range(quantity):
        for row in data:
            message = f"""
            {i})
            Имя: {row[0]}
            Возраст: {row[1]}
            KD: {row[2]}
            PR: {row[3]}
            Описание: {row[4]}
            """
            i+=1
            messages.append(message)
        return messages

# Закрытие подключения к базе данных
cursor.close()
conn.close()

# Использование сообщений в телеграмм боте на aiogram
bot = aiogram.Bot(token='5760615918:AAHygCHZdAnKceDwVIBzhT_L-INrrbK6HbI')
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['get_data'])
async def send_data(message: aiogram.types.Message):
    # for msg in messages:
        # await message.answer(msg)
        # await message.answer(people(1))
    await message.answer(people(1))
if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
