from db import Database
db = Database()

#----------------------------------------------------------------------------------------------------------------

# Token бота
TOKEN = "Тут ваш токен"
#----------------------------------------------------------------------------------------------------------------

# ID на аккаунт админа
admins = [
	1030874842,
	745814407

]

#----------------------------------------------------------------------------------------------------------------

# Каналы на каторые нужно быть подписанными ['Имя, которое будет выводиться на кнопке', 'ID канала', 'ссылка на канал']
# Бот должен быть админом в этих каналах, чтобы проверить наличие подписки
CHANNELS = [
	# ['Канал 1', '-1001700620866', 'https://t.me/ulsksale'],
	# ['Канал 2', '-1002091818721', 'https://t.me/anonulsk_news']

	['Канал 1', '-1001734480359', 'https://t.me/Armenian_Sasha']

]

#----------------------------------------------------------------------------------------------------------------

# Сообщение которое будет выводиться если не подписал на какой-то канал
NOT_SUB_MESSAGE = 'You not subscribe channels!'


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

bot_name = 'SearchGamingFriendBot'


def generate_referral_link(user_id):
    return f"http://t.me/{bot_name}?start={user_id}"
