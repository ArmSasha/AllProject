#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
from Bot import get_pictures

#login, password='',''
#vk_session = vk_api.VkApi(login, password)
#vk_session.auth()

token ='Тут ваш токен'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)



def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)


    if response == 'тест':

        keyboard.add_button('Профиль👤', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Баланс💼', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Магазин🏪', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)



    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response =='вернуться🔙' or response == 'вернуться' :
        keyboard.add_button('Профиль👤', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Баланс💼', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Магазин🏪', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif response == 'магазин🏪' or response == 'магазин':
        keyboard.add_button('Машины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Мотоциклы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Верталёты', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Самолёты', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться🔙', color=VkKeyboardColor.POSITIVE)


    elif response =='вернуться◀ ' :

        keyboard.add_button('bmw🚗', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку

        keyboard.add_button('mersedes🚗', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('porshe🚙', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('lamborghini🏎', color=VkKeyboardColor.NEGATIVE)

    elif response =='машины':
        keyboard.add_button('bmw🚗', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('mersedes🚗', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('porshe🚙', color=VkKeyboardColor.DEFAULT)

        keyboard.add_button('lamborghini🏎', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('вернуться🔙', color=VkKeyboardColor.NEGATIVE)

    elif response == 'bmw' or 'bmw🚗':

        keyboard.add_button('BMW 6-Series', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('BMW X6', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('BMW Z4', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('BMW X1', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Машины', color=VkKeyboardColor.NEGATIVE)



    elif response == 'mersedes' or 'mersedes🚗':

        keyboard.add_button('Mercedes-Benz CLS-Class', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz E-Class', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz G-Class', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz SLK-Class', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('вернуться◀ ', color=VkKeyboardColor.NEGATIVE)

    elif response == 'porshe' or 'porshe🚙':

        keyboard.add_button('Porsche 918 Spyder', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Porsche Panamera', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Porsche Cayenne', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Porsche Macan цена', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('вернуться◀ ', color=VkKeyboardColor.NEGATIVE)

    elif response == 'lamborghini' or 'lamborghini🏎':

        keyboard.add_button('Lamborghini Urus', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Huracan', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Huracan Spyder', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Aventador Roadster', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('вернуться◀ ', color=VkKeyboardColor.NEGATIVE)


    elif response == 'работать':
        keyboard.add_button('Работать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться🔙', color=VkKeyboardColor.POSITIVE)


    elif response == 'котики':
        keyboard.add_button('Котики!', color=VkKeyboardColor.POSITIVE)


    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard



def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

player = {"jobs": "none", "possessions": "none"}

def get_money():
    MyFile = open('', 'r')
    money=int(MyFile.readline())
    MyFile.close()
    return(money)

def set_money(_money):
    MyFile = open('', 'w')
    MyFile.write(str(_money))
    MyFile.close()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))

        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)



        if event.from_user and not event.from_me:





            if response == 'начать':
                send_message(vk_session, 'user_id', event.user_id, message='Привет это твой профиль! ')
                send_message(vk_session, 'user_id', event.user_id, message='И тут вы найдёте всё что надо для  игры!')
                send_message(vk_session, 'user_id', event.user_id, message="Это твой профиль!")
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money())
                send_message(vk_session, 'user_id', event.user_id, message="Ваши владения:")
                send_message(vk_session, 'user_id', event.user_id, player["possessions"])

            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
            elif response == "тест":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)
            elif response=='команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

            elif response == 'баланс' or response == 'баланс💼':
                send_message(vk_session, 'user_id', event.user_id, get_money())
                send_message(vk_session, 'user_id', event.user_id, message="Это колличество ваших 💸")

            elif response == 'профиль' or response == 'профиль👤':
                send_message(vk_session, 'user_id', event.user_id, message="Это твой профиль!")
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money())
                send_message(vk_session, 'user_id', event.user_id, message="Ваши владения:")
                send_message(vk_session, 'user_id', event.user_id, player["possessions"])

            elif response == 'магазин🏪' or response == 'магазин':
                send_message(vk_session, 'user_id', event.user_id, message="МАГАЗИН")
                send_message(vk_session, 'user_id', event.user_id, message="👱️Добрый день что будете брать?",keyboard=keyboard)

            elif response == 'работать':
                set_money(get_money()+1)
                send_message(vk_session, 'user_id', event.user_id, message="Есть")
                send_message(vk_session, 'user_id', event.user_id, get_money())
                send_message(vk_session, 'user_id', event.user_id, message="Это колличество ваших 💸",keyboard=keyboard)

            elif response == 'рандом':
                send_message(vk_session, 'user_id', event.user_id,random.randint(1,10))

            elif response =='вернуться🔙' or response == 'вернуться':
                send_message(vk_session, 'user_id', event.user_id, message="Профиль👤")
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money())

            elif response =='вернуться◀':
                send_message(vk_session, 'user_id', event.user_id, message="BMW")
                send_message(vk_session, 'user_id', event.user_id, message="MERCEDES")
                send_message(vk_session, 'user_id', event.user_id, message="PORSHE")
                send_message(vk_session, 'user_id', event.user_id, message="LAMBORGHINI",keyboard=keyboard)

            elif response =='машины':
                send_message(vk_session, 'user_id', event.user_id, message="BMW")
                send_message(vk_session, 'user_id', event.user_id, message="MERCEDES")
                send_message(vk_session, 'user_id', event.user_id, message="PORSHE")
                send_message(vk_session, 'user_id', event.user_id, message="LAMBORGHINI",keyboard=keyboard)

            elif response == 'bmw' or 'bmw🚗' :
                send_message(vk_session, 'user_id', event.user_id, message="BMW 6-Series \n цена 2 200 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW X6 \n цена 8 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW Z4 \n цена 5 005 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW X1 \n цена 3 000 000 💸",keyboard=keyboard)

            elif response == 'mercedes' or 'mersedes🚗':
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz CLS-Class \n цена 5 900 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz E-Class \n цена 4 000 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz G-Class \n цена 17 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz SLK-Class \n цена 500 000 💸",keyboard=keyboard)

            elif response == 'porsche' or 'porshe🚙':
                send_message(vk_session, 'user_id', event.user_id, message="Porsche 918 Spyder \n цена 100 000 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Panamera \n цена 9 500 000  💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Cayenne \n цена 8 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Macan \n цена 5 500 000 💸",keyboard=keyboard)

            elif response == 'lamborghini' or 'lamborghini🏎':
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Urus \n цена 15 200 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Huracan \n цена 17 760 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Huracan Spyder \n цена 18 650 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Aventador Roadster \n цена 25 500 000 💸",keyboard=keyboard)



            else:
                send_message(vk_session, 'user_id', event.user_id,message='Я вас не понимаю!' )


        elif event.from_chat :
            if response == "котики":
                attachment = get_pictures.get(vk_session, -130670107, session_api)
                print(attachment)
                send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
        print('-' * 30)












