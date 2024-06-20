"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Файл для работы с клавиатурами телеграма

"""

from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def buy_logs(categories):
    keyboard = InlineKeyboardMarkup()
    for category in categories:
        keyboard.add(InlineKeyboardButton(category[0], callback_data="buy_logs_" + category[1]))
    return keyboard


def admin():
    admin_button_1 = InlineKeyboardButton('👤Просмотреть пользователя👤', callback_data='profile_check')
    admin_button_2 = InlineKeyboardButton('✉️Рассылка ✉️', callback_data='sends')
    admin_button_3 = InlineKeyboardButton('📤Скачать базу📤', callback_data='download')
    admin_button_4 = InlineKeyboardButton('⚙️Настройки⚙️', callback_data='settings')
    admin_button_5 = InlineKeyboardButton('💰Баланс💰', callback_data='balance')
    return InlineKeyboardMarkup().add(admin_button_1).add(admin_button_2).add(admin_button_3)\
        .add(admin_button_4).add(admin_button_5)


def categories_edit():
    categories_edit_button_1 = InlineKeyboardButton('Создать категорию', callback_data='add_category')
    categories_edit_button_2 = InlineKeyboardButton('Удалить категорию', callback_data='del_category')
    categories_edit_button_3 = InlineKeyboardButton('Поменять категорию загрузки', callback_data='set_category')
    return InlineKeyboardMarkup().add(categories_edit_button_1).add(categories_edit_button_2).add(categories_edit_button_3)


def categories_set(categories):
    keyboard = InlineKeyboardMarkup()
    for category in categories:
        keyboard.add(InlineKeyboardButton(category[0], callback_data=f"upload_to_{category[1]}"))
    keyboard.add(InlineKeyboardButton('Скрыть', callback_data='cancel'))
    return keyboard


def category_delete(categories):
    keyboard = InlineKeyboardMarkup()
    for category in categories:
        keyboard.add(InlineKeyboardButton(category[0], callback_data=f'delete_category_{category[1]}'))
    keyboard.add(InlineKeyboardButton('Скрыть', callback_data='cancel'))
    return keyboard


def profile(user_id):
    profile_button_1 = InlineKeyboardButton('Выдать баланс', callback_data=f'user_give_{user_id}')
    profile_button_2 = InlineKeyboardButton('Удалить баланс', callback_data=f'user_delete_{user_id}')
    profile_button_3 = InlineKeyboardButton('Стереть баланс', callback_data=f'user_clear_{user_id}')
    profile_button_4 = InlineKeyboardButton('Скрыть', callback_data=f'cancel')
    return InlineKeyboardMarkup().add(profile_button_1).add(profile_button_2).add(profile_button_3).add(profile_button_4)


def cancel():
    cancel_button_1 = InlineKeyboardButton('Скрыть', callback_data=f'cancel')
    return InlineKeyboardMarkup().add(cancel_button_1)


def main():
    main_button_1 = KeyboardButton('🛒Купить логи🛒')
    main_button_2 = KeyboardButton('💳Пополнить💳')
    main_button_3 = KeyboardButton('📜Правила📜')
    return ReplyKeyboardMarkup(resize_keyboard=True).add(main_button_1).add(main_button_2).add(main_button_3)


def check_payment_lolz(payment_id, link, amount):
    check_payment_lolz_button_link = InlineKeyboardButton('🔗Ссылка на платеж🔗', url=link)
    check_payment_lolz_button = InlineKeyboardButton('Проверить платеж', callback_data=f"check_lolz_{payment_id}_{amount}")
    return InlineKeyboardMarkup().add(check_payment_lolz_button_link).add(check_payment_lolz_button)


def check_payment_qiwi(payment_id, link):
    check_payment_qiwi_button_link = InlineKeyboardButton('🔗Ссылка на платеж🔗', url=link)
    check_payment_qiwi_button = InlineKeyboardButton('Проверить платеж', callback_data=f"check_qiwi_{payment_id}")
    return InlineKeyboardMarkup().add(check_payment_qiwi_button_link).add(check_payment_qiwi_button)


def check_payment_lava(payment_id, link):
    check_payment_lava_button_link = InlineKeyboardButton('🔗Ссылка на платеж🔗', url=link)
    check_payment_lava_button = InlineKeyboardButton('Проверить платеж', callback_data=f"check_lava_{payment_id}")
    return InlineKeyboardMarkup().add(check_payment_lava_button_link).add(check_payment_lava_button)


def check_payment_crystal_pay(payment_id, link):
    check_payment_crystal_pay_button_link = InlineKeyboardButton('🔗Ссылка на платеж🔗', url=link)
    check_payment_crystal_pay_button = InlineKeyboardButton('Проверить платеж', callback_data=f"check_crystalpay_{payment_id}")
    return InlineKeyboardMarkup().add(check_payment_crystal_pay_button_link).add(check_payment_crystal_pay_button)


def deposit():
    deposit_button_1 = InlineKeyboardButton('Qiwi', callback_data="qiwi_pay")
    deposit_button_2 = InlineKeyboardButton('Lolz', callback_data="lolz_pay")
    deposit_button_3 = InlineKeyboardButton('Crystal Pay', callback_data="crystal_pay")
    deposit_button_4 = InlineKeyboardButton('Lava', callback_data="lava_pay")
    return InlineKeyboardMarkup().add(deposit_button_1).add(deposit_button_2)\
    .add(deposit_button_3).add(deposit_button_4)
