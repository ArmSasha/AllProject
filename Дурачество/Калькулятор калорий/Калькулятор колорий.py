import telebot


bot = telebot.TeleBot('1739386190:AAHFRmJbHnCcE6NK1rMqOF9vMaiklw7PBP4')



user_data= {
    'gender': '',
    'weight': '',
    'height': '',
    'age': ''
}

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    msg = bot.send_message(message.chat.id, 'Введите ваш пол: м(мужчина); д(девушка)')
    bot.register_next_step_handler(msg, user_gender)


def user_gender(message):
    user_data['gender'] = message.text
    msg = bot.send_message(message.chat.id, 'Введи свой вес(в кг)')
    bot.register_next_step_handler(msg, user_weight)

def user_weight(message):
    user_data['weight'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите ваш рос(в см)')
    bot.register_next_step_handler(msg, user_height)

def user_height(message):
    user_data['height'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите ваш возраст')
    bot.register_next_step_handler(msg, getresults)


def getresults(message):
    user_data['age'] = message.text
    user_data['message'] = message.text

    if user_data['gender'] == 'м':

        weight_r = int(10 * int(user_data['weight']))
        height_r = int(6 * int(user_data['height']))
        age_r = int(5 * int(user_data['age']))
        result_r = weight_r + height_r - age_r

        result_rb = result_r + 5

        bot.send_message(message.chat.id, f'Вам нужно употреблять по {result_rb} калорий в день')




    elif user_data['gender'] == 'д':
        weight_r = int(10 * int(user_data['weight']))
        height_r = int(6 * int(user_data['height']))
        age_r = int(5 * int(user_data['age']))
        result_r = weight_r + height_r - age_r

        result_rb = result_r - 161

        bot.send_message(message.chat.id, f'Вам нужно употреблять по {result_rb} калорий в день')

    else:
        bot.send_message(message.chat.id, 'Напишите /start для начала подсчёта')

        bot.clear_step_handler(message)

    bot.clear_step_handler(message)

bot.polling()