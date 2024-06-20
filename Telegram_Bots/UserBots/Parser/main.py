# from pyrogram import Client, filters

# app = Client('my_account')

# @app.on_message(filters.me)
# def echo(client, message):
#     message.reply_text(message.text)

# app.run()

import logging
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions


# Инициализируем клиент Pyrogram и логгер
app = Client("my_account")
logging.basicConfig(level=logging.INFO)

# Обработчик команды /get_users
@app.on_message(filters.command("get_users"))
def get_users(client, message):
    """Собирает все username пользователей в чате."""
    # Получаем ID пользователя, чьих друзей нужно найти
    user_id = message.from_user.id

    # Получаем список пользователей в чате
    users = client.get_chat_members(message.chat.id)

    # Создаем пустой список для хранения username пользователей
    usernames = []

    # Проходимся по всем пользователям в чате
    for user in users:
        # Проверяем, является ли пользователь обычным пользователем, а не ботом или администратором
        if not user.user.is_bot and not user.user.is_bot and user.user.id != user_id:
            # Если да, добавляем его username в список
            usernames.append(user.user.username)


    usernames_str = ['@{}'.format(str(username)) for username in usernames if username is not None]

    # Отправляем пользователю список username

    if usernames:
        client.send_message(-1001949092880, 'Вот username пользователей в чате: \n' + '\n'.join(usernames_str))
    else:
        client.send_message(-1001949092880, 'Нет username пользователей в этом чате.')

# Запускаем бота
app.run()
