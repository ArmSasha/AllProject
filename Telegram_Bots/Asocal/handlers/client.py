from aiogram.utils import executor
from aiogram import types, Dispatcher
from keyboards import markups as nav
from create_bot import dp, bot, db, p2p
import random
import config as conf

lot_money = 0

# @dp.callback_query_handler(text="profile")
async def profile(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	user_nickname = 'Ваш ник: ' + db.get_nickname(message.from_user.id)
	us_id = str(message.from_user.id)
	user_id_prof = (f'\nВаш ID: <code> {us_id} </code> ')
	referral_link = (f'\nВаша реферальная ссылка: https://t.me/{conf.bot_NICKNAME}?start={message.from_user.id}')
	referral_quantity = (f'\nКол-во рефералов: {db.count_referals(message.from_user.id)}')
	# money_user = f'\nНа вашем счету: {db.user_money(message.from_user.id)} руб.'
	# user_age = f'\nВаш возраст: {db.get_age(message.from_user.id)}'
	await bot.send_message(message.from_user.id, user_nickname + user_id_prof + referral_link + referral_quantity, parse_mode=types.ParseMode.HTML, reply_markup = nav.backMenu)


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backShopMenu')
async def backShopMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.shopMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backShopMenu')
async def backBacksMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.V_bucsk_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backShopMenu')
async def backfortniteMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.fortniteMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backGiftBucksMenu')
async def backGiftBucksMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.gift_bucks)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backDirectlyBucksMenu')
async def backDirectlyBucksMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.directly_bucks)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backDiscordMenu')
async def backDiscordMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.discordMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backNitroClassicMenu')
async def backNitroClassicMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.nitro_Classic_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backNitroFullMenu')
async def backNitroFullMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.nitro_Classic_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text="back")
async def back(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Главное меню', photo = Logo_menu, reply_markup=nav.mainMenu)


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='faq')
async def faq(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Вопросы имеют место повторяться, составили для вашего удобства ответы на: \n<a href = "https://telegra.ph/FAQ-CHasto-zadavaemye-voprosy-02-04">Часто задаваемые вопросы</a> ', photo = Logo_menu, parse_mode=types.ParseMode.HTML, reply_markup=nav.backMenu)


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='shop')
async def shop(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.shopMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite')
async def fortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.fortniteMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite_sets')
async def fortnite_sets(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'fortnite_sets', photo = Logo_menu, reply_markup=nav.backShopMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite_V_bucks')
async def fortnite_V_bucks(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'fortnite_V_bucks', photo = Logo_menu, reply_markup=nav.V_bucsk_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='bucks_gift')
async def bucks_gift(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'bucks_gift', photo = Logo_menu, reply_markup=nav.gift_bucks)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='bucks_directly')
async def bucks_directly(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'bucks_directly', photo = Logo_menu, reply_markup=nav.directly_bucks)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------


# @dp.message_handler(commands=['v_500_bucks'])
async def v_500_bucks(message: types.Message):
	global lot_money
	lot_money = 139
	global com
	com = 'v_500_bucks'
	description = "Товар: 500 В-баксов\n\
Цена: 139₽\n\n\
Описание: 500 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks200_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)
	await bot.send_message(message.from_user.id, text = 'Назад', reply_markup=backBacksMenu)

# @dp.message_handler(commands=['v_800_bucks'])
async def v_800_bucks(message: types.Message):
	global lot_money
	lot_money = 229
	global com
	com = 'v_800_bucks'
	description = "Товар: 800 В-баксов\n\
Цена: 229₽\n\n\
Описание: 800 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks800_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_1000_bucks'])
async def v_1000_bucks(message: types.Message):
	global lot_money
	lot_money = 275
	global com
	com = 'v_1000_bucks'
	description = "Товар: 1000 В-баксов\n\
Цена: 275₽\n\n\
Описание: 1 000 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks1k.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_1200_bucks'])
async def v_1200_bucks(message: types.Message):
	global lot_money
	lot_money = 339
	global com
	com = 'v_1200_bucks'
	description = "Товар: 1200 В-баксов\n\
Цена: 339₽\n\n\
Описание: 1 200 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"

	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks1_2k_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_1600_bucks'])
async def v_1500_bucks(message: types.Message):
	global lot_money
	lot_money = 419
	global com
	com = 'v_1500_bucks'
	description = "Товар: 1500 В-баксов\n\
Цена: 419₽\n\n\
Описание: 1 500 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"

	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks1_5k_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_2000_bucks'])
async def v_2000_bucks(message: types.Message):
	global lot_money
	lot_money = 559
	global com
	com = 'v_2000_bucks'
	description = "Товар: 2000 В-баксов\n\
Цена: 559₽\n\n\
Описание: 2 000 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks2k_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_2800_bucks'])
async def v_2800_bucks(message: types.Message):
	global lot_money
	lot_money = 749
	global com
	com = 'v_2800_bucks'
	description = "Товар: 2800 В-баксов\n\
Цена: 749₽\n\n\
Описание: 2 800 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks2_8k.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_5000_bucks'])
async def v_5000_bucks(message: types.Message):
	global lot_money
	lot_money = 1149
	global com
	com = 'v_5000_bucks'
	description = "Товар: 5000 В-баксов\n\
Цена: 1149₽\n\n\
Описание: 1 149 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks5k.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['v_13500_bucks'])
async def v_13500_bucks(message: types.Message):
	global lot_money
	lot_money = 2799
	global com
	com = 'v_13500_bucks'
	description = "Товар: 13500 В-баксов\n\
Цена: 2799₽\n\
Описание: 13 500 В-баксов, которые можно потратить в «Королевской битве» и творческом режиме, чтобы купить экипировки, дельтапланы, кирки, эмоции, обёртки и боевой пропуск текущего сезона! Дельтапланы и воздушные следы недоступны в режиме «Сражение с Бурей».\n\
В-баксы на ваш аккаунт Fortnite в Epic Games.\n\
В-баксы доступны на все платформы, кроме Nintendo"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/vbucks13_5k.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = description, photo = Logo_menu, reply_markup = nav.topUpBacksMenu)

# @dp.message_handler(commands=['battlepass_gift'])
async def battlepass_gift(message: types.Message):
	global lot_money
	lot_money = 275
	global com
	com = 'v_1000_bucks'
	description = "Товар: Боевой пропуст\n\
Цена: 275₽\n\n\
Описание: Боевой пропуск"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/battlepass_gift.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'battlepass_gift', photo = Logo_menu, reply_markup = nav.topUpBacksMenu)


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='discord')
async def discord(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = Logo_menu, reply_markup=nav.discordMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='nitro_Full')
async def nitro_Full(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'nitro_Full', photo = Logo_menu, reply_markup = nav.nitro_Full_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands=['nitro_Full_Month'])
async def nitro_Full_Month(message: types.Message):
	global lot_money
	lot_money = 229
	global com
	com = 'nitro_Full_Month'
	description = "Товар: Discord Full на месяц\n\
Цена: 229₽\n\
Описание: Discord Full на месяц"
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/discord_nitro_full_1_month.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'discord_nitro_full_1_month', photo = Logo_menu, reply_markup = nav.topUpDicMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands=['nitro_Full_Year'])
async def nitro_Full_Year(message: types.Message):
	global lot_money
	lot_money = 2299
	global com
	com = 'nitro_Full_Year'
	description = "Товар: Discord Full на год\n\
Цена: 2299₽\n\
Описание: Discord Full на год"

	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/discord_nitro_full_1_year.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'discord_nitro_full_1_year', photo = Logo_menu, reply_markup = nav.topUpDicMenu)


#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------


# @dp.callback_query_handler(text='nitro_Basic')
async def nitro_Basic(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'nitro_Basic', photo = Logo_menu, reply_markup = nav.nitro_Classic_Menu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands=['nitro_Classic_Month'])
async def nitro_Classic_Month(message: types.Message):
	global lot_money
	lot_money = 129
	global com
	com = 'nitro_Classic_Month'
	description = "Товар: Discord Classic на год\n\
Цена: 129₽\n\
Описание: Discord Classic на год"

	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/discord_nitro_classic_1_month.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'discord_nitro_classic_1_month', photo = Logo_menu, reply_markup = nav.topUpDicMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands=['nitro_Classic_Year'])
async def nitro_Classic_Year(message: types.Message):
	global lot_money
	lot_money = 229
	global com
	com = 'nitro_Classic_Year'
	description = "Товар: Discord Classic на год\n\
Цена: 1290₽\n\
Описание: Discord Classic на год"

	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/discord_nitro_classic_1_year.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'discord_nitro_classic_1_year', photo = Logo_menu, reply_markup = nav.topUpDicMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='guarantees')
async def guarantees(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Тык по ссылки ниже чтобы \n<a href = "https://telegra.ph/FAQ-CHasto-zadavaemye-voprosy-02-04">Ознакомиться с гарантиями</a> ', photo = Logo_menu, parse_mode=types.ParseMode.HTML, reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='reviews')
async def reviews(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Создали отдельный чат с отзывами, только учти, что писать в чат могут только те, кто хоть раз что-то купил. \n<a href = "https://telegra.ph/FAQ-CHasto-zadavaemye-voprosy-02-04">Чатик с отзывами </a> ', photo = Logo_menu, parse_mode=types.ParseMode.HTML, reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# # @dp.callback_query_handler(text='support')
# async def support(call: types.CallbackQuery):
# 	await bot.delete_message(call.from_user.id, call.message.message_id)
# 	Logo_menu = open('Images/Logo_menu.png', 'rb')
# 	await bot.send_photo(call.from_user.id, caption = f'Для подачи заявки, перейдите в данного бота: \n<a href = "https://t.me/Asocal_Support_bot">Подержка</a>', photo = Logo_menu, parse_mode=types.ParseMode.HTML, reply_markup=nav.backMenu)



#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

# PAY
# @dp.callback_query_handler(text = 'top_up_backs')
async def pay(message: types.Message):
	message_money = lot_money  # ЦЕНА
	comment = str(message.from_user.id) + "_" + str(com) + "_" + str(random.randint(1000, 9999))
	bill = p2p.bill(amount=message_money, lifetime = 15, comment=comment)

	db.add_check(message.from_user.id, message_money, bill.bill_id)

	await bot.send_message(message.from_user.id, f"Вам нужно отправить {message_money} руб. на наш счёт QIWI\nСсылка: {bill.pay_url}\nУказав комментарий к оплате: {comment}", reply_markup=nav.by_menu(url=bill.pay_url, bill=bill.bill_id))


# @dp.callback_query_handler(text_contains='check_')
async def check(callback: types.CallbackQuery):
	bill = str(callback.data[6:])
	info = db.get_check(bill)
	if info != False:
		if str(p2p.check(bill_id=bill).status) == "PAID":
			user_money = db.user_money(callback.from_user.id)
			money = int(info[2])
			db.set_money(callback.from_user.id, user_money+money)
			delete_check()
			await bot.send_message(callback.from_user.id, 'Ваш счёт пополнен!')
			await bot.send_message(-1001630751716, f'ЭЭЭЭЭЭ, ТАМ ПОПОЛНЕНИЕ!\n{com}')
		else:
			await bot.send_message(callback.from_user.id, 'Вы не отплатили счёт!', reply_markup = nav.by_menu(False, bill=bill))

	else:
		await bot.send_message(callback.from_user.id, 'Счёт не найден')
	# await bot.delete_message(call.from_user.id, call.message.message_id)
	# Logo_menu = open('Images/Logo_menu.png', 'rb')
	# await bot.send_photo(callback.from_user.id, caption = f'Cancel', photo = Logo_menu, reply_markup=nav.backMenu)



#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------


# PAY
# @dp.callback_query_handler(text = 'top_up_dic')
async def pay(message: types.Message):
	message_money = lot_money  # ЦЕНА
	comment = str(message.from_user.id) + "_" + str(com) + "_" + str(random.randint(1000, 9999))
	bill = p2p.bill(amount=message_money, lifetime = 15, comment=comment)

	db.add_check(message.from_user.id, message_money, bill.bill_id)

	await bot.send_message(message.from_user.id, f"Вам нужно отправить {message_money} руб. на наш счёт QIWI\nСсылка: {bill.pay_url}\nУказав комментарий к оплате: {comment}", reply_markup=nav.by_menu(url=bill.pay_url, bill=bill.bill_id))


# @dp.callback_query_handler(text_contains='check_')
async def check(callback: types.CallbackQuery):
	bill = str(callback.data[6:])
	info = db.get_check(bill)
	if info != False:
		if str(p2p.check(bill_id=bill).status) == "PAID":
			user_money = db.user_money(callback.from_user.id)
			money = int(info[2])
			db.set_money(callback.from_user.id, user_money+money)
			delete_check()
			await bot.send_message(callback.from_user.id, 'Ваш счёт пополнен!')
			await bot.send_message(-1001630751716, f'ЭЭЭЭЭЭ, ТАМ ПОПОЛНЕНИЕ!\n{com}')
		else:
			await bot.send_message(callback.from_user.id, 'Вы не отплатили счёт!', reply_markup = nav.by_menu(False, bill=bill))

	else:
		await bot.send_message(callback.from_user.id, 'Счёт не найден')
	# await bot.delete_message(call.from_user.id, call.message.message_id)
	# Logo_menu = open('Images/Logo_menu.png', 'rb')
	# await bot.send_photo(callback.from_user.id, caption = f'Cancel', photo = Logo_menu, reply_markup=nav.backMenu)



#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------


# #Регистрируем хендлеры
def register_handlers_client(dp: Dispatcher):
	dp.register_callback_query_handler(profile, text='profile')
	dp.register_callback_query_handler(back, text="back")
	dp.register_callback_query_handler(backShopMenu, text='backShopMenu')
	dp.register_callback_query_handler(backBacksMenu, text='backBacksMenu')
	dp.register_callback_query_handler(backfortniteMenu, text='backfortniteMenu')
	dp.register_callback_query_handler(backGiftBucksMenu, text='backGiftBucksMenu')
	dp.register_callback_query_handler(backDirectlyBucksMenu, text='backDirectlyBucksMenu')
	dp.register_callback_query_handler(backDiscordMenu, text='backDiscordMenu')
	dp.register_callback_query_handler(backNitroClassicMenu, text='backNitroClassicMenu')
	dp.register_callback_query_handler(backNitroFullMenu, text='backNitroFullMenu')
	dp.register_callback_query_handler(faq, text='faq')
	dp.register_callback_query_handler(shop, text='shop')
	dp.register_callback_query_handler(discord, text='discord')
	dp.register_callback_query_handler(nitro_Full, text='nitro_Full')
	dp.register_callback_query_handler(nitro_Basic, text='nitro_Basic')
	dp.register_callback_query_handler(fortnite, text='fortnite')
	dp.register_callback_query_handler(fortnite_sets, text='fortnite_sets')
	dp.register_callback_query_handler(fortnite_V_bucks, text='fortnite_V_bucks')
	dp.register_callback_query_handler(bucks_gift, text='bucks_gift')
	dp.register_callback_query_handler(bucks_directly, text='bucks_directly')
	dp.register_callback_query_handler(v_500_bucks, text='v_500_bucks')
	dp.register_callback_query_handler(v_800_bucks, text='v_800_bucks')
	dp.register_callback_query_handler(v_1000_bucks, text='v_1000_bucks')
	dp.register_callback_query_handler(v_1200_bucks, text='v_1200_bucks')
	dp.register_callback_query_handler(v_1500_bucks, text='v_1500_bucks')
	dp.register_callback_query_handler(v_2000_bucks, text='v_2000_bucks')
	dp.register_callback_query_handler(v_2800_bucks, text='v_2800_bucks')
	dp.register_callback_query_handler(v_5000_bucks, text='v_5000_bucks')
	dp.register_callback_query_handler(v_13500_bucks, text='v_13500_bucks')
	dp.register_callback_query_handler(battlepass_gift, text='battlepass_gift')
	dp.register_callback_query_handler(nitro_Full_Month, text='nitro_Full_Month')
	dp.register_callback_query_handler(nitro_Full_Year, text='nitro_Full_Year')
	dp.register_callback_query_handler(nitro_Classic_Month, text='nitro_Classic_Month')
	dp.register_callback_query_handler(nitro_Classic_Year, text='nitro_Classic_Year')
	dp.register_callback_query_handler(guarantees, text='guarantees')
	dp.register_callback_query_handler(reviews, text='reviews')
	# dp.register_callback_query_handler(support, text='support')
	dp.register_callback_query_handler(pay, text = 'top_up_backs')
	dp.register_callback_query_handler(pay, text = 'top_up_dic')
	dp.register_callback_query_handler(check, text_contains='check_')

