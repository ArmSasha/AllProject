import sqlite3
import telebot
from telebot import types
import os
from mg import get_map_cell


#bot
bot = telebot.TeleBot('1739386190:AAHFRmJbHnCcE6NK1rMqOF9vMaiklw7PBP4')



global price
global name


cols, rows = 8, 8

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row( telebot.types.InlineKeyboardButton('←', callback_data='left'),
              telebot.types.InlineKeyboardButton('↑', callback_data='up'),
              telebot.types.InlineKeyboardButton('↓', callback_data='down'),
              telebot.types.InlineKeyboardButton('→', callback_data='right') )

maps = {}







@bot.message_handler(commands = ['start'])
def start(message):
    connect = sqlite3.connect('Game.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Game(
        id INTEGER,
        money INTEGER,
        possession STRING,
        realty STRING
    )""")

    connect.commit()

    #check
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM Game WHERE id = {people_id}")
    data = cursor.fetchone()

    if data is None:
        #add

        id = message.chat.id
        money = 1000
        possession = 'none'
        realty = 'none'
        cursor.execute("INSERT INTO Game (id, money, possession, realty) VALUES (?,?, ?, ?);",( id, money, possession, realty))
        # cursor.execute("""INSERT INTO Game (id, money, possession, realty) VALUES (?,?,?,?)""",
        #                (id, money, possession, realty))
        connect.commit()



    else:
        bot.send_message(message.chat.id, 'Такой пользовать уже существует!')

@bot.message_handler(commands = ['chit'])
def chit(message):

    connect = sqlite3.connect('Game.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM Game WHERE id = {people_id}")
    data = cursor.fetchone()

    sql_update_query = f"""Update Game set money = money + 10000 where id = {people_id}"""
    cursor.execute(sql_update_query)
    connect.commit()

    bot.send_message(message.from_user.id, "Good")

@bot.message_handler(commands=['prof'])
def prof(message):
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Баланс💼', callback_data='bal')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Магазин🏪', callback_data='mag')
        keyboard.add(key_oven)


        bot.send_message(message.from_user.id, text='Выбирите действие', reply_markup=keyboard)





@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'mag':
        keyboard = types.InlineKeyboardMarkup()

        key_oven = types.InlineKeyboardButton(text='Машины', callback_data='avto')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Мотоциклы', callback_data='mot')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Верталёты', callback_data='vert')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Самолёты', callback_data='sam')
        keyboard.add(key_oven)

        bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)

    if call.data == 'bal':
        msg = bot.send_message(call.message.chat.id, 'Баланс💼')

        connect = sqlite3.connect('Game.db')
        cursor = connect.cursor()

        cursor.execute("SELECT money FROM Game")

        cursor = connect.cursor()

        people_id = call.message.chat.id
        ma = cursor.execute(f"SELECT money FROM Game WHERE id={people_id}")
        m = cursor.fetchone()[0]
        bot.send_message(call.message.chat.id, f"Ваш баланс: {m}")


#__________________________________
#           Автомобили
#__________________________________

    if call.data == 'avto':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Bmw🚗', callback_data='Bmw')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Mersedes🚗', callback_data='Mersedes')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Porshe🚙', callback_data='Porshe')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Lamborghini🏎', callback_data='Lamborghini')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)




#__________________________________
#__________________________________
#           BMW
#__________________________________
    if call.data == 'Bmw':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='BMW 6-Series', callback_data='Bmw1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='BMW X6', callback_data='Bmw2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='BMW Е34', callback_data='Bmw3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='BMW X1', callback_data='Bmw4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           BMW 6-Series
#__________________________________

    if call.data == 'Bmw1':
                price = '2 200 000'
                name = 'BMW 6-Series'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸")
                file = "Фото/Автомобили/BMW/BMW 6-Series"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                # bot.send_photo(chat_id=call.message.chat.id, photo="Фото/Автомобили/BMW/BMW 6-Series")


#__________________________________
#           BMW X6
#__________________________________

    if call.data == 'Bmw2':
                price = '8 500 000'
                name = 'BMW X6'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/BMW/BMW X6"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           BMW Е34
#__________________________________

    if call.data == 'Bmw3':
                price = '518 510'
                name = 'BMW Е34'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/BMW/BMW Е34"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)
#__________________________________
#           BMW X1
#__________________________________

    if call.data == 'Bmw4':
                price = '3 000 000'
                name = 'BMW X1'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/BMW/BMW X1"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)


#__________________________________
#__________________________________




#__________________________________
#__________________________________
#           Mersedes
#__________________________________
    if call.data == 'Mersedes':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Mercedes-Benz CLS-Class', callback_data='Mercedes1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Mercedes-Benz E-Class', callback_data='Mercedes2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Mercedes-Benz G-Class', callback_data='Mercedes3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Mercedes-Benz SLK-Class', callback_data='Mercedes4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Mercedes-Benz CLS-Class
#__________________________________

    if call.data == 'Mercedes1':
                price = '5 900 000'
                name = 'Mercedes-Benz CLS-Class'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Mersedes/Mercedes-Benz CLS-Class"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Mercedes-Benz E-Class
#__________________________________

    if call.data == 'Mercedes2':
                price = '4 000 000'
                name = 'Mercedes-Benz E-Class'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Mersedes/Mercedes-Benz E-Class"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Mercedes-Benz G-Class
#__________________________________

    if call.data == 'Mercedes3':
                price = '17 500 000'
                name = 'Mercedes-Benz G-Class'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Mersedes/Mercedes-Benz G-Class"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Mercedes-Benz SLK-Class
#__________________________________

    if call.data == 'Mercedes4':
                price = '500 000'
                name = 'Mercedes-Benz SLK-Class'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Mersedes/Mercedes-Benz SLK-Class"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#__________________________________




#__________________________________
#__________________________________
#           Porshe
#__________________________________
    if call.data == 'Porshe':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Porsche 918 Spyder', callback_data='Porshe1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Porsche Panamera', callback_data='Porshe2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Porsche Cayenne', callback_data='Porshe3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Porsche Macan', callback_data='Porshe4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Porsche 918 Spyder
#__________________________________

    if call.data == 'Porshe1':
                price = '5 900 000'
                name = 'Porsche 918 Spyder'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Porsche/Porsche 918 Spyder"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Porsche Panamera
#__________________________________

    if call.data == 'Porshe2':
                price = '4 000 000'
                name = 'Porsche Panamera'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Porsche/Porsche Panamera"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Porsche Cayenne
#__________________________________

    if call.data == 'Porshe3':
                price = '17 500 000'
                name = 'Porsche Cayenne'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Porsche/Porsche Cayenne"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Porsche Macan
#__________________________________

    if call.data == 'Porshe4':
                price = '500 000'
                name = 'Porsche Macan'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Porsche/Porsche Macan"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#__________________________________




#__________________________________
#__________________________________
#           Lamborghini
#__________________________________
    if call.data == 'Lamborghini':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Lamborghini Urus', callback_data='Lamborghini1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Lamborghini Huracan', callback_data='Lamborghini2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Lamborghini Huracan Spyder', callback_data='Lamborghini3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Lamborghini Aventador Roadster', callback_data='Lamborghini4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Lamborghini Urus
#__________________________________

    if call.data == 'Lamborghini1':
                price = '15 200 000'
                name = 'Lamborghini Urus'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Lamborghini/Lamborghini Urus"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Lamborghini Huracan
#__________________________________

    if call.data == 'Lamborghini2':
                price = '17 760 000'
                name = 'Lamborghini Huracan'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Lamborghini/Lamborghini Huracan"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Lamborghini Huracan Spyder
#__________________________________

    if call.data == 'Lamborghini3':
                price = '18 650 000'
                name = 'Lamborghini Huracan Spyder'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Lamborghini/Lamborghini Huracan Spyder"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)
#__________________________________
#           Lamborghini Aventador Roadster
#__________________________________

    if call.data == 'Lamborghini4':
                price = '25 500 000'
                name = 'Lamborghini Aventador Roadster'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Автомобили/Lamborghini/Lamborghini Aventador Roadster"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)
#__________________________________
#__________________________________










#__________________________________
#           Вертолёты
#__________________________________
    if call.data == 'vert':
        keyboard = types.InlineKeyboardMarkup()

        key_oven = types.InlineKeyboardButton(text='Robinson', callback_data='Robinson')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Eurocopter', callback_data='Eurocopter')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Bell', callback_data='Bell')
        keyboard.add(key_oven)

        bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)

#__________________________________
#           Robinson
#__________________________________
    if call.data == 'Robinson':
        keyboard = types.InlineKeyboardMarkup()


        key_oven = types.InlineKeyboardButton(text='Robinson R44 Raven 2', callback_data='Robinson1')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Robinson R66', callback_data='Robinson2')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Robinson R44 Raven 1', callback_data='Robinson3')
        keyboard.add(key_oven)

        bot.send_message(call.message.chat.id, text=' Выбирите верталёт ', reply_markup=keyboard)

#__________________________________
#       Robinson R44 Raven 2
#__________________________________
    if call.data == 'Robinson1':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="47 100 500💸")

#__________________________________
#       Robinson R66
#__________________________________
    if call.data == 'Robinson2':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="81 700 000💸")

#__________________________________
#       Robinson R44 Raven 1
#__________________________________
    if call.data == 'Robinson3':

            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="41 200 600💸")

#__________________________________
#   192 знака помещается туда |
#__________________________________


#__________________________________
#           Eurocopter
#__________________________________
    if call.data == 'Eurocopter':
            keyboard = types.InlineKeyboardMarkup()



            key_oven = types.InlineKeyboardButton(text='Eurocopter AS350', callback_data='Eurocopter1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Eurocopter AS355 NP', callback_data='Eurocopter2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Airbus Helicopters H130', callback_data='Eurocopter3')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите верталёт', reply_markup=keyboard)

#__________________________________
#       Eurocopter AS350
#__________________________________
    if call.data == 'Eurocopter1':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="115 000 000💸")

#__________________________________
#       Eurocopter AS355 NP
#__________________________________
    if call.data == 'Eurocopter2':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="105 000 000💸")

#__________________________________
#       Airbus Helicopters H130
#__________________________________
    if call.data == 'Eurocopter3':

            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="338 000 000💸")

#__________________________________
#   192 знака помещается туда |
#__________________________________



#__________________________________
#           Bell
#__________________________________
    if call.data == 'Bell':
            keyboard = types.InlineKeyboardMarkup()



            key_oven = types.InlineKeyboardButton(text='Bell 407', callback_data='Bell1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Bell 505', callback_data='Bell2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Bell V-280', callback_data='Bell3')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите верталёт', reply_markup=keyboard)

#__________________________________
#       Bell 407
#__________________________________
    if call.data == 'Bell1':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="110 500 000💸")

#__________________________________
#       Bell 505
#__________________________________
    if call.data == 'Bell2':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="123 000 000💸")

#__________________________________
#       Bell V-280
#__________________________________
    if call.data == 'Bell3':

            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="155 000 000💸")

#__________________________________
#   192 знака помещается туда |
#__________________________________




#__________________________________
#           Мотоциклы
#__________________________________

    if call.data == 'mot':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Honda', callback_data='Honda')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Suzuki', callback_data='Suzuki')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Kawasaki', callback_data='Kawasaki')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Yamaha', callback_data='Yamaha')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)




#__________________________________
#__________________________________
#           Honda
#__________________________________
    if call.data == 'Honda':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Honda Super Sport', callback_data='Honda1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Honda Gold Wing Tour', callback_data='Honda2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Honda CB1100RS', callback_data='Honda3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Honda Africa Twin', callback_data='Honda4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Honda Super Sport
#__________________________________

    if call.data == 'Honda1':
                price = '935 900'
                name = 'Honda Super Sport'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Honda/Honda Super Sport"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Honda Gold Wing Tour
#__________________________________

    if call.data == 'Honda2':
                price = '2 632 900'
                name = 'Honda Gold Wing Tour'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard.add)
                file = "Фото/Мотоциклы/Honda/Honda Gold Wing Tour"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Honda CB1100RS
#__________________________________

    if call.data == 'Honda3':
                price = '1 228 900'
                name = 'Honda CB1100RS'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Honda/Honda CB1100RS"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Honda Africa Twin
#__________________________________

    if call.data == 'Honda4':
                price = '1 219 900'
                name = 'Honda Africa Twin'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Honda/Honda Africa Twin"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#__________________________________


#__________________________________
#__________________________________
#           Suzuki
#__________________________________
    if call.data == 'Suzuki':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Suzuki GSX-R1000', callback_data='Suzuki1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Suzuki GSX-S1000A', callback_data='Suzuki2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Suzuki V-Strom 650 ABS', callback_data='Suzuki3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Suzuki GSX-R1000R', callback_data='Suzuki4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Suzuki GSX-R1000
#__________________________________

    if call.data == 'Suzuki1':
                price = '1 349 900'
                name = 'Suzuki GSX-R1000'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Suzuki/Suzuki GSX-R1000"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Suzuki GSX-S1000A
#__________________________________

    if call.data == 'Suzuki2':
                price = '949 900'
                name = 'Suzuki GSX-S1000A'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Suzuki/Suzuki GSX-S1000A"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Suzuki V-Strom 650 ABS
#__________________________________

    if call.data == 'Suzuki3':
                price = '669 900'
                name = 'Suzuki V-Strom 650 ABS'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Suzuki/Suzuki V-Strom 650 ABS"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#           Suzuki GSX-R1000R
#__________________________________

    if call.data == 'Suzuki4':
                price = '1 599 900'
                name = 'Suzuki GSX-R1000R'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Suzuki/Suzuki GSX-R1000R"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)


#__________________________________
#__________________________________



#__________________________________
#__________________________________
#           Kawasaki
#__________________________________
    if call.data == 'Kawasaki':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Kawasaki Ninja H2 Carbon', callback_data='Kawasaki1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Kawasaki Ninja ZX-10R', callback_data='Kawasaki2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Kawasaki W800 Cafe', callback_data='Kawasaki3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Kawasaki Ninja 1000 SX', callback_data='Kawasaki4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Kawasaki Ninja H2 Carbon
#__________________________________

    if call.data == 'Kawasaki1':
                price = '1 349 900'
                name = 'Kawasaki Ninja H2 Carbon'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Kawasaki/Kawasaki Ninja H2 Carbon"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)

#__________________________________
#           Kawasaki Ninja ZX-10R
#__________________________________

    if call.data == 'Kawasaki2':
                price = '949 900'
                name = 'Kawasaki Ninja ZX-10R'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Kawasaki/Kawasaki Ninja ZX-10R"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)

#__________________________________
#           Kawasaki W800 Cafe
#__________________________________

    if call.data == 'Kawasaki3':
                price = '669 900'
                name = 'Kawasaki W800 Cafe'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Kawasaki/Kawasaki W800 Cafe"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()

                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)

#__________________________________
#           Kawasaki Ninja 1000 SX
#__________________________________

    if call.data == 'Kawasaki4':

                price = '1 599 900'
                name = 'Kawasaki Ninja 1000 SX'

                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Kawasaki/Kawasaki Ninja 1000 SX"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='By')
                keyboard.add(key_oven)

#__________________________________
#__________________________________


#__________________________________
#__________________________________
#           Yamaha
#__________________________________
    if call.data == 'Yamaha':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Yamaha YZF-R1', callback_data='Yamaha1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Yamaha MT-03', callback_data='Yamaha2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Yamaha MT-10', callback_data='Yamaha3')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Yamaha Tracer 900', callback_data='Yamaha4')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Yamaha YZF-R1
#__________________________________

    if call.data == 'Yamaha1':

                price = '1 705 000'
                name = 'Yamaha YZF-R1'

                # bot.send_message(call.message.chat.id, text=f"{price}💸", reply_markup=keyboard)
                # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Yamaha/Yamaha YZF-R1"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo

                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='ByY1')
                keyboard.add(key_oven)
                bot.send_photo(call.message.chat.id, doc, caption, reply_markup=keyboard)



#__________________________________
#           Yamaha MT-03
#__________________________________

    if call.data == 'Yamaha2':

                price = '473 000'
                name = 'Yamaha MT-03'

                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Yamaha/Yamaha MT-03"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{nameY2} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='ByY2')
                keyboard.add(key_oven)
#__________________________________
#           Yamaha MT-10
#__________________________________

    if call.data == 'Yamaha3':

                price = '1 338 000'
                name = 'Yamaha MT-10'

                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Мотоциклы/Yamaha/Yamaha MT-10"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{nameY3} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='ByY3')
                keyboard.add(key_oven)

#__________________________________
#           Yamaha Tracer 900
#__________________________________

    if call.data == 'Yamaha4':


                price = '979 000'
                name = 'Yamaha Tracer 900'

                file = "Фото/Мотоциклы/Yamaha/Yamaha Tracer 900"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{nameY4} \nцена: {price}💸"
                #send_random_photo

                keyboard = types.InlineKeyboardMarkup()
                key_oven = types.InlineKeyboardButton(text='Купить', callback_data='ByY4')
                keyboard.add(key_oven)
                bot.send_photo(call.message.chat.id, doc, caption, reply_markup=keyboard)



#__________________________________
#__________________________________





#__________________________________
#           Самолёты
#__________________________________

    if call.data == 'sam':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Airbus', callback_data='Airbus')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Boeing', callback_data='Boeing')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Ty', callback_data='Ty')
            keyboard.add(key_oven)


            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)




#__________________________________
#__________________________________
#           Airbus
#__________________________________
    if call.data == 'Airbus':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Airbus A-319', callback_data='Airbus1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Airbus A-320', callback_data='Airbus2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Airbus-A310-300', callback_data='Airbus3')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Airbus A-319
#__________________________________

    if call.data == 'Airbus1':
                price = '3 333 402 000'
                name = 'Airbus A-319'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price}💸", reply_markup=keyboard)
                file = "Фото/Самолёты/Airbus/Airbus A-319"
                doc = open(file + '.jpg', 'rb')
                #если нужно подпись к фото
                caption = f"{name} \nцена: {price}💸"
                #send_random_photo
                bot.send_photo(call.message.chat.id, doc, caption)

#__________________________________
#           Airbus A-320
#__________________________________

    if call.data == 'Airbus2':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="3 703 780 000💸")

#__________________________________
#           Airbus-A310-300
#__________________________________

    if call.data == 'Airbus3':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="1 555 587 600💸")


#__________________________________
#__________________________________


#__________________________________
#__________________________________
#           Boeing
#__________________________________
    if call.data == 'Boeing':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Boeing-767-300ER', callback_data='Boeing1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Boeing-737-800', callback_data='Boeing2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Boeing-757-200', callback_data='Boeing3')
            keyboard.add(key_oven)

            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Boeing-767-300ER
#__________________________________

    if call.data == 'Boeing1':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="8 555 731 800💸")

#__________________________________
#           Boeing-737-800
#__________________________________

    if call.data == 'Boeing2':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="5 481 594 400💸")

#__________________________________
#           Boeing-757-200
#__________________________________

    if call.data == 'Boeing3':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="4 296 384 800💸")



#__________________________________
#__________________________________



#__________________________________
#__________________________________
#           Ty
#__________________________________
    if call.data == 'Ty':
            keyboard = types.InlineKeyboardMarkup()

            key_oven = types.InlineKeyboardButton(text='Ту-204-120', callback_data='Ty1')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Ту-214', callback_data='Ty2')
            keyboard.add(key_oven)

            key_oven = types.InlineKeyboardButton(text='Ту-204-100', callback_data='Ty3')
            keyboard.add(key_oven)


            bot.send_message(call.message.chat.id, text='Выбирите действие', reply_markup=keyboard)


#__________________________________
#           Ту-204-120
#__________________________________

    if call.data == 'Ty1':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="2 592 646 000💸")

#__________________________________
#           Ту-214
#__________________________________

    if call.data == 'Ty2':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="2 074 116 800💸")

#__________________________________
#           Ту-204-100
#__________________________________

    if call.data == 'Ty3':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="2 000 041 200💸")


#__________________________________
#__________________________________


#__________________________________
#           By
#__________________________________

    if call.data == 'ByY4':
                price = '979 000'
                # name = 'Yamaha Tracer 900'
                name = 'Tracer'
                connect = sqlite3.connect('Game.db')
                cursor = connect.cursor()

                cursor.execute("SELECT possession FROM Game")

                cursor = connect.cursor()

                people_id = call.message.chat.id
                ma = cursor.execute(f"SELECT money FROM Game WHERE id={people_id}")
                m = str(cursor.fetchone()[0])

                if price >= m:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Вы успешно купили товар")
                    sql_update_query = f"""Update Game set possession = possession + {name} where id = {people_id}"""
                    cursor.execute(sql_update_query)
                    pa = cursor.execute(f"SELECT money FROM Game WHERE id={people_id}")
                    p = str(cursor.fetchone()[0])

                    connect.commit()

                elif price < m :
                    # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас не хватает денег на баллансе")
                    bot.send_message(call.message.chat.id, f"Ваш баланс: {m}")
                    msg = bot.send_message(call.message.chat.id, '__________________________________')



# def by(price, name):




        # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"{price} {name}")

        # connect = sqlite3.connect('Game.db')
        # cursor = connect.cursor()

        # cursor.execute("SELECT possession FROM Game")

        # cursor = connect.cursor()

        # people_id = call.message.chat.id
        # ma = cursor.execute(f"SELECT money FROM Game WHERE id={people_id}")
        # m = cursor.fetchone()[0]

        # if price >= m:
        #     bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Вы успешно купили товар")
        #     sql_update_query = f"""Update Game set possession = possession + {name} where id = {people_id}"""
        #     cursor.execute(sql_update_query)
        #     connect.commit()

        # elif price < m :
        #     # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас не хватает денег на баллансе")
        #     bot.send_message(call.message.chat.id, f"Ваш баланс: {m}")




# @bot.message_handler(commands=["geophone"])
# def geophone(message):
#     # Эти параметры для клавиатуры необязательны, просто для удобства
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_phone, button_geo)
#     bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)


def get_map_str(map_cell, player):
    map_str = ""
    for y in range(rows * 2 - 1):
        for x in range(cols * 2 - 1):
            if map_cell[x + y * (cols * 2 - 1)]:
                map_str += "⬛"
            elif (x, y) == player:
                map_str += "🔴"
            else:
                map_str += "⬜"
        map_str += "\n"

    return map_str


@bot.message_handler(commands=['play'])
def play_message(message):
    map_cell = get_map_cell(cols, rows)

    user_data = {
        'map': map_cell,
        'x': 0,
        'y': 0
    }

    maps[message.chat.id] = user_data

    bot.send_message(message.from_user.id, get_map_str(map_cell, (0, 0)), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    user_data = maps[query.message.chat.id]
    new_x, new_y = user_data['x'], user_data['y']

    if query.data == 'left':
        new_x -= 1
    if query.data == 'right':
        new_x += 1
    if query.data == 'up':
        new_y -= 1
    if query.data == 'down':
        new_y += 1

    if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
        return None
    if user_data['map'][new_x + new_y * (cols * 2 - 1)]:
        return None

    user_data['x'], user_data['y'] = new_x, new_y

    if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
        bot.edit_message_text( chat_id=query.message.chat.id,
                               message_id=query.message.id,
                               text="Вы выиграли" )
        return None

    bot.edit_message_text( chat_id=query.message.chat.id,
                           message_id=query.message.id,
                           text=get_map_str(user_data['map'], (new_x, new_y)),
                           reply_markup=keyboard )


#polling
bot.polling(none_stop=False, interval=0)