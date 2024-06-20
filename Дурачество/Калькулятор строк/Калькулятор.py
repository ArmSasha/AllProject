import telebot
from telebot import types

bot = telebot.TeleBot('1739386190:AAHFRmJbHnCcE6NK1rMqOF9vMaiklw7PBP4')

user_data= {
    'name': '',
    'phone': '',
    'email': '',
    'message': ''
}

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    msg = bot.send_message(message.chat.id, 'Введите Ваше ФИО')
    bot.register_next_step_handler(msg, user_phone)


def user_phone(message):
    user_data['name'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите свой номер телефона')
    bot.register_next_step_handler(msg, user_email)

def user_email(message):
    user_data['phone'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите Вашу эл. почту')
    bot.register_next_step_handler(msg, user_message)

def user_message(message):
    user_data['email'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите ваше сообщение')
    bot.register_next_step_handler(msg, getresults)

def getresults(message):
    user_data['message'] = message.text
    bot.send_message(message.chat.id, f"ФИО: {user_data['name']} \nТел: {user_data['phone']} \nПочта: {user_data['email']} \nСообщение: {user_data['message']}")
    bot.clear_step_handler(message)

bot.polling()