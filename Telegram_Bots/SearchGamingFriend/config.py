from db import Database
db = Database()



#----------------------------------------------------------------------------------------------------------------

# Token бота
TOKEN = "5760615918:AAHygCHZdAnKceDwVIBzhT_L-INrrbK6HbI"
#----------------------------------------------------------------------------------------------------------------

# ID на аккаунт админа
admins = [
	1030874842,
	745814407

]

admin_chat = -1001876704240



#----------------------------------------------------------------------------------------------------------------

# Каналы на каторые нужно быть подписанными ['Имя, которое будет выводиться на кнопке', 'ID канала', 'ссылка на канал']
# Бот должен быть админом в этих каналах, чтобы проверить наличие подписки
CHANNELS = [
	['Channel 1', '-1001734480359', 'https://t.me/Armenian_Sasha']
]

#----------------------------------------------------------------------------------------------------------------

# Сообщение которое будет выводиться если не подписал на какой-то канал
NOT_SUB_MESSAGE = 'You not subscribe channels!'

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def profile(variable):
	profile_text = f"""Ваш профиль:
Имя: {db.get_name(variable)}
Возраст: {db.get_age(variable)}
Пол: {db.get_gender(variable)}
Рейтинг:
Лайки👍: {db.get_like(variable)}
Дизлайки👎: {db.get_dislike(variable)}
"""

# Количество игр:
	return profile_text

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def profileFortnite(variable):
	if(not db.user_exists_fortnite(variable)):
		profile_text = 'У вас нет анкеты в Fortnite'
	else:
		profile_text = f"""Ваш профиль:
	KD: {db.get_kd_fortnite(variable)}
	PR: {db.get_pr_fortnite(variable)}
	Роль: {db.get_role_fortnite(variable)}
	Ранг: {db.get_rank_fortnite(variable)}
	Описание: {db.get_description_fortnite(variable)}
"""
	return profile_text

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def profileValorant(variable):
	if(not db.user_exists_valorant(variable)):
		profile_text = 'У вас нет анкеты в Valorant'
	else:
		profile_text = f"""Ваш профиль:
	KD: {db.get_kd_valorant(variable)}
	Ранг: {db.get_rank_valorant(variable)}
	Описание: {db.get_description_valorant(variable)}
"""
	return profile_text

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def profileCSGO(variable):
	if(not db.user_exists_csgo(variable)):
		profile_text = 'У вас нет анкеты в CSGO'
	else:
		profile_text = f"""Ваш профиль:
	Faceit: {db.get_faceit_csgo(variable)}
	Ранг: {db.get_rank_csgo(variable)}
	Описание: {db.get_description_csgo(variable)}
"""
	return profile_text
