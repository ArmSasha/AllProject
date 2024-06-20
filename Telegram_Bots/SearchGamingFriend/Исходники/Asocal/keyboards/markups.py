from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

mainMenu = InlineKeyboardMarkup(row_width = 2) # resize_keyboard = True

btnShop = InlineKeyboardButton(text = '🎮 Магазин', callback_data = 'shop')
btnProfile = InlineKeyboardButton(text='💳 ПРОФИЛЬ', callback_data = 'profile') #
btnFAQ = InlineKeyboardButton(text='FAQ⁉️', callback_data = 'faq')

btnGuarantees = InlineKeyboardButton(text = 'Гарантии✅', callback_data = 'guarantees')
btnReviews = InlineKeyboardButton(text = '🙋‍♂️Отзывы', callback_data = 'reviews')
btnSupport = InlineKeyboardButton(text='👨‍💻Поддержка', callback_data = 'support_text')


mainMenu.add(btnShop, btnProfile, btnFAQ, btnGuarantees, btnReviews, btnSupport)

# btnList = InlineKeyboardButton(text='🧑 СПИСОК ПОЛЬЗОВАТЕЛЕЙ', callback_data = 'list_of_users') btnList
# btnSub = InlineKeyboardButton(text='❤ ПОДПИСКА', callback_data = 'subscription') # btnSub

# btnUrl = InlineKeyboardButton(text='Перейти на канал', url = 'https://t.me/Armenian_Sasha') btnUrl
# btnShare = InlineKeyboardButton(text='Поделиться!', switch_inline_query='Лучший бот в мире!') btnShare

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backMenu = InlineKeyboardMarkup(row_width = 1)
btnBack = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'back')
backMenu.add(btnBack)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

def by_menu(isUrl = True, url = '', bill = ''):
	qiwiMenu = InlineKeyboardMarkup(row_width = 1)

	if isUrl:
		btnUrlQiwi = InlineKeyboardButton(text = 'Ссылка на оплату', url=url)
		qiwiMenu.insert(btnUrlQiwi)

	btnCheckQiwi = InlineKeyboardButton(text = 'Проверить оплату', callback_data = 'check_'+bill)
	qiwiMenu.insert(btnCheckQiwi)
	return qiwiMenu

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

shopMenu = InlineKeyboardMarkup(row_width = 2)
btnDiscord = InlineKeyboardButton(text = 'Discord', callback_data = 'discord')
btnFortnite = InlineKeyboardButton(text = 'Fortnite', callback_data = 'fortnite')

shopMenu.add(btnDiscord, btnFortnite, btnBack)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backShopMenu = InlineKeyboardMarkup(row_width = 2)
backShopMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backShopMenu')
backShopMenu.add(backShopMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backBacksMenu = InlineKeyboardMarkup(row_width = 2)
backBacksMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backBacksMenu')
backBacksMenu.add(backBacksMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backfortniteMenu = InlineKeyboardMarkup(row_width = 2)
backfortniteMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backfortniteMenu')
backfortniteMenu.add(backfortniteMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backGiftBucksMenu = InlineKeyboardMarkup(row_width = 2)
backGiftBucksMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backGiftBucksMenu')
backGiftBucksMenu.add(backGiftBucksMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backDirectlyBucksMenu = InlineKeyboardMarkup(row_width = 2)
backDirectlyBucksMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backDirectlyBucksMenu')
backDirectlyBucksMenu.add(backDirectlyBucksMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backDiscordMenu = InlineKeyboardMarkup(row_width = 2)
backDiscordMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backDiscordMenu')
backDiscordMenu.add(backDiscordMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backNitroClassicMenu = InlineKeyboardMarkup(row_width = 2)
backNitroClassicMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backNitroClassicMenu')
backNitroClassicMenu.add(backNitroClassicMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

backNitroFullMenu = InlineKeyboardMarkup(row_width = 2)
backNitroFullMenubtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backNitroFullMenu')
backNitroFullMenu.add(backNitroFullMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________


discordMenu = InlineKeyboardMarkup(row_width = 2)
nitro_Full = InlineKeyboardButton(text = 'Nitro Full', callback_data = 'nitro_Full')
nitro_Basic = InlineKeyboardButton(text = 'Nitro Basic', callback_data = 'nitro_Basic')

discordMenu.add(nitro_Basic, nitro_Full, backShopMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

nitro_Full_Menu = InlineKeyboardMarkup(row_width=1)
nitro_Full_Month = InlineKeyboardButton(text = 'discord_nitro_full_1_month ', callback_data = 'nitro_Full_Month')
nitro_Full_Year = InlineKeyboardButton(text = 'discord_nitro_full_1_year ', callback_data = 'nitro_Full_Year')

nitro_Full_Menu.add(nitro_Full_Month, nitro_Full_Year, backDiscordMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

nitro_Classic_Menu = InlineKeyboardMarkup(row_width=1)
nitro_Classic_Month = InlineKeyboardButton(text = 'discord_nitro_full_1_month ', callback_data = 'nitro_Classic_Month')
nitro_Classic_Year = InlineKeyboardButton(text = 'discord_nitro_full_1_year ', callback_data = 'nitro_Classic_Year')

nitro_Classic_Menu.add(nitro_Classic_Month, nitro_Classic_Year, backDiscordMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

fortniteMenu = InlineKeyboardMarkup(row_width = 2)
fortnite_sets = InlineKeyboardButton(text = 'Наборы', callback_data = 'fortnite_sets')
fortnite_V_bucks = InlineKeyboardButton(text = 'V-баксы', callback_data = 'fortnite_V_bucks')


fortniteMenu.add(fortnite_sets, fortnite_V_bucks, backShopMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

V_bucsk_Menu = InlineKeyboardMarkup(row_width = 2)
bucks_gift = InlineKeyboardButton(text = 'Подарком', callback_data = 'bucks_gift')
bucks_directly = InlineKeyboardButton(text = 'Напрямую', callback_data = 'bucks_directly')


V_bucsk_Menu.add(bucks_gift, bucks_directly, backfortniteMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

gift_bucks = InlineKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
gift_500 = InlineKeyboardButton(text = '500', callback_data = 'v_500_bucks')
gift_800 = InlineKeyboardButton(text = '800', callback_data = 'v_800_bucks')
gift_1200 = InlineKeyboardButton(text = '1200', callback_data = 'v_1200_bucks')
gift_1500 = InlineKeyboardButton(text = '1500', callback_data = 'v_1500_bucks')
gift_2000 = InlineKeyboardButton(text = '2000', callback_data = 'v_2000_bucks')
battlepass_gift = InlineKeyboardButton(text = 'battlepass_gift', callback_data = 'battlepass_gift')

btnBack = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'back')

gift_bucks.add(gift_500, gift_800, gift_1200, gift_1500, gift_2000).add(battlepass_gift).add(backBacksMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________

directly_bucks = InlineKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
directly_1000 = InlineKeyboardButton(text = '1000', callback_data = 'v_1000_bucks')
directly_2800 = InlineKeyboardButton(text = '2800', callback_data = 'v_2800_bucks')
directly_5000 = InlineKeyboardButton(text = '5000', callback_data = 'v_5000_bucks')
directly_13500 = InlineKeyboardButton(text = '13500', callback_data = 'v_13500_bucks')

btnBack = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'back')

directly_bucks.add(directly_1000, directly_2800, directly_5000, directly_13500).add(backBacksMenubtn)

#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________


# sub_inline_markup = InlineKeyboardMarkup(row_width = 1)
# btnSubMonth = InlineKeyboardButton(text = 'Месяц - 150 рублей', callback_data = "submonth")
# sub_inline_markup.add(btnSubMonth, btnBack)

#_________________________________________________________________________________________________________________


topUpBacksMenu = InlineKeyboardMarkup(row_width = 1)
btnTopUp = InlineKeyboardButton(text = 'Купить💸', callback_data = 'top_up_backs')
topUpBacksMenu.add(btnTopUp, backBacksMenubtn)


#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________


topUpDicMenu = InlineKeyboardMarkup(row_width = 1)
btnTopUp = InlineKeyboardButton(text = 'Купить💸', callback_data = 'top_up_dic')
topUpDicMenu.add(btnTopUp, backDiscordMenubtn)


#_________________________________________________________________________________________________________________

#_________________________________________________________________________________________________________________
