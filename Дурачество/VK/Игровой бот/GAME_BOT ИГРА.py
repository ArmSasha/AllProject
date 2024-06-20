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

vk_session = vk_api.VkApi(token='43e04b63445d4a431dbfdb6d38e2e00a4068efdaddfa25b4e3e5e769c219b290be914d470fbf4d1fe3e49')


token ='d290c42e1a5c38a556a2ba404ab98bb1e3dcfe3ab38f39022e45659ff421a921bb9eef1b4f444adf9f43b'
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
        keyboard.add_button('Работать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Достижения', color=VkKeyboardColor.PRIMARY)

    if response == 'начать':

        keyboard.add_button('Профиль👤', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Баланс💼', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Магазин🏪', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Работать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Достижения', color=VkKeyboardColor.PRIMARY)


    elif response == 'профиль' or response == 'профиль👤':
        keyboard.add_button('Профиль👤', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Баланс💼', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Магазин🏪', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Работать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Достижения', color=VkKeyboardColor.PRIMARY)

    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response =='вернуться🔙' or response == 'вернуться' :
        keyboard.add_button('Профиль👤', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Баланс💼', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Магазин🏪', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Работать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Достижения', color=VkKeyboardColor.PRIMARY)



    elif response == 'магазин🏪' or response == 'магазин':
        keyboard.add_button('Машины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Мотоциклы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вертолёты', color=VkKeyboardColor.POSITIVE)
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



#           Вертолёты
#__________________
    elif response =='вертолёты🚁' or response =='вертолёты':
        keyboard.add_button('Robinson', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Eurocopter', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Bell', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Вернуться🔙', color=VkKeyboardColor.NEGATIVE)

#           Robinson
#__________________________________
    elif response == 'robinson':
        keyboard.add_button('Robinson R44 Raven 2', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Robinson R66', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Robinson R44 Raven 1', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Вертолёты🚁', color=VkKeyboardColor.NEGATIVE)

#           Eurocopter
#__________________________________
    elif response == 'eurocopter':
        keyboard.add_button('Eurocopter AS350', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Eurocopter AS355 NP', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Airbus Helicopters H130', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Вертолёты🚁', color=VkKeyboardColor.NEGATIVE)


#           Bell
#__________________________________
    elif response == 'bell':
        keyboard.add_button('Bell 407', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Bell 505', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Bell V-280', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Вертолёты🚁', color=VkKeyboardColor.NEGATIVE)

#           Машины
#_________________________

    elif response =='машины':
        keyboard.add_button('bmw🚗', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('mersedes🚗', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('porshe🚙', color=VkKeyboardColor.DEFAULT)

        keyboard.add_button('lamborghini🏎', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться🔙', color=VkKeyboardColor.NEGATIVE)




#           BMW
#_________________________
    elif response == 'bmw' or response== 'bmw🚗':

        keyboard.add_button('BMW 6-Series', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('BMW X6', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('BMW Z4', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('BMW X1', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Машины', color=VkKeyboardColor.NEGATIVE)



#           MERSEDES
#_________________________
    elif response == 'mersedes' or response==  'mersedes🚗':

        keyboard.add_button('Mercedes-Benz CLS-Class', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz E-Class', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz G-Class', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Mercedes-Benz SLK-Class', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Машины', color=VkKeyboardColor.NEGATIVE)



#           Porshe
#_________________________
    elif response == 'porshe' or response==  'porshe🚙':

        keyboard.add_button('Porsche 918 Spyder', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Porsche Panamera', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Porsche Cayenne', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Porsche Macan', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Машины', color=VkKeyboardColor.NEGATIVE)


#           Lamborghini
#_________________________
    elif response == 'lamborghini' or response==  'lamborghini🏎':

        keyboard.add_button('Lamborghini Urus', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Huracan', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Huracan Spyder', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()

        keyboard.add_button('Lamborghini Aventador Roadster', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()
        keyboard.add_button('Машины', color=VkKeyboardColor.NEGATIVE)



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


#                   Перименные
#_________________________________________________________
player = {"jobs": "none" }





understand=False

shop_list =[ [ [
 [{"name": "BMW 6-Series", "cost":2200000},
 {"name": "BMW X6", "cost":8500000},
 {"name": "BMW Z4", "cost":5005000 },
 {"name": "BMW X1", "cost":3000000} ],
 [
 {"name": "Mercedes-Benz CLS-Class", "cost":5900000 },{"name": "Mercedes-Benz E-Class","cost":4000000 },
 {"name": "Mercedes-Benz G-Class", "cost":17500000 },{"name": "Mercedes-Benz SLK-Class", "cost":500000} ],
 [
 {"name": "Porsche 918 Spyder", "cost":48000000}, {"name": "Porsche Panamera", "cost":9500000},
 {"name": "Porsche Cayenne", "cost":8500000}, {"name": "Porsche Macan", "cost":5500000} ],
 [{"name": "Lamborghini Urus", "cost":15200000}, {"name": "Lamborghini Huracan", "cost":17760000},
 {"name": "Lamborghini Huracan Spyder", "cost":18650000}, {"name": "Lamborghini Aventador Roadster", "cost":25500000} ] ],
 [
 [{"name": "Robinson R44 Raven 2", "cost": 47100500},{"name": "Robinson R66", "cost": 81700000},
 {"name": "Robinson R44 Raven 1", "cost":41200600}],
 [
 {"name": "Eurocopter AS350", "cost":115000000},{"name": "Eurocopter AS355 NP", "cost":105000000},
 {"name": "Airbus Helicopters H130 ", "cost":338000000}],
 [
 {"name": "Bell 407", "cost":110500000},{"name": "Bell 505", "cost":123000000},
 {"name": "Bell V-280", "cost":155000000}] ], [] ] ]



def user(id):
    MyFile = open('Users.csv', 'r')
    users=MyFile.readlines()
    for i in range(0,len(users)):
        user=users[i].split(';')
        if user[0] == str(id):
            MyFile.close()
            return user
    return 0


def user_num(id):
    MyFile = open('Users.csv', 'r')
    users=MyFile.readlines()
    for i in range(0,len(users)):
        user=users[i].split(';')
        if user[0] == id:
            MyFile.close()
            return i
    return 0


def get_money(id):
    print(user(id)[0])
    return user(id)[1]




def set_money(_money,id):
    MyFile = open('Users.csv', 'r+')
    lines=MyFile.readlines()
    lines[user_num(id)]= str(user(id)[0])+";"+str(_money)
    # for i in range(1,len(user(id))):
    #     lines[user_num(id)]+=';'+user(id)[i]
    text = ""

    for i in range(0, len(lines)):
        text += lines[i] + "\n"
    print(text)
    MyFile.write(text)
    MyFile.close()




def get_possessions():
    MyPossessions = open('Possessions.csv', 'r')
    possessions=MyPossessions.readlines()
    MyPossessions.close()

    possessionsToReturn = ""

    for i in range(0, len(possessions)):
        possessionsToReturn += possessions[i] + "\n"

    return (possessionsToReturn)


def set_possessions(_possessions):
    MyPossessions = open('Possessions.csv', 'w')
    MyPossessions.write(str(_possessions))
    MyPossessions.close()


def add_possession(_possession):
    MyPossessions = open('Possessions.csv', 'a')
    MyPossessions.write(_possession + '\n')
    MyPossessions.close()


def check(x):
	file = open('Users.csv', 'r')
	if str(x) in file.read():
		return 1
	else:
		return 0
	file.close()

def adder(x):
	file = open('Users.csv', 'a')
	file.write(str(x) + "\n")
	file.close()




for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))

        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        id = event.user_id

        if event.from_user and not event.from_me:

            achievements=0

            for i in range(0, len(shop_list)):
                for j in range(0, len(shop_list[i])):
                    for k in range(0,len(shop_list[i][j])):
                        for l in range(0, len(shop_list[i][j][k])):
                            if response == (shop_list[i][j][l][k])["name"].lower():
                                send_message(vk_session, 'user_id', event.user_id, message= shop_list[i][j][l][k]["name"])
                                send_message(vk_session, 'user_id', event.user_id, message= 'Цена ' + str(shop_list[i][j][l][k]["cost"]) + '💸' )



                                understand=True
                                if get_money(id)>= shop_list[i][j][l][k]["cost"]:
                                    send_message(vk_session, 'user_id', event.user_id, message='👱Вы успешно совершили покупку, \n спасибо приходите ещё')
                                    send_message(vk_session, 'user_id', event.user_id, message='Ваш баланс '+ str(get_money(id)) + '💸')
                                    set_money(get_money(id)- shop_list[i][j][l][k]["cost"])
                                    add_possession(shop_list[i][j][l][k]["name"])

                                    achievements+=1

                                else:
                                    send_message(vk_session, 'user_id', event.user_id, message='👱К сожалению у вас не хватает денег... ')

            if response == 'начать':
                if check(id) == 0:
                    adder(str(id)+";10000")
                send_message(vk_session, 'user_id', event.user_id, message="Профиль👤")
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money(id))
                send_message(vk_session, 'user_id', event.user_id, message="Ваши владения:")
                send_message(vk_session, 'user_id', event.user_id, get_possessions(),keyboard=keyboard)


            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)

            elif response == 'проверка':
                send_message(vk_session, 'user_id', event.user_id, message='Привет')




            elif response == "тест":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)

            elif response == "чит":
                set_money(get_money(id)+100000000)
                send_message(vk_session, 'user_id', event.user_id, get_money(id))


            elif response=='команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')


#                           Достижения
#_________________________________________________________________________________

            elif achievements==1:
                send_message(vk_session, 'user_id', event.user_id, message='🛑🛑🛑 ВНИМАНИЕ 🛑🛑🛑 \n ПОЗДРАВЛЯЕМ С ВЫПОЛНЕНИЕМ 1 ДОСТИЖЕНИЯ!!!')
                send_message(vk_session, 'user_id', event.user_id, message='В НАГРАДУ ВЫ ПОЛУЧАЕТЕ 10000 💸')
                set_money(get_money(id)+10000)

            elif response=="достижения":
                send_message(vk_session, 'user_id', event.user_id, message='1) Купить что-то в магазине \n 2) ')





#                           Закрыть
#_________________________________________________________________________________
            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)


#                           Баланс
#_________________________________________________________________________________
            elif response == 'баланс' or response == 'баланс💼':
                send_message(vk_session, 'user_id', event.user_id, get_money(id))
                send_message(vk_session, 'user_id', event.user_id, message="Это колличество ваших 💸")


#                           Профиль
#_________________________________________________________________________________
            elif response == 'профиль' or response == 'профиль👤':
                send_message(vk_session, 'user_id', event.user_id, message="Профиль👤", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money(id))
                send_message(vk_session, 'user_id', event.user_id, message="Ваши владения:")
                send_message(vk_session, 'user_id', event.user_id, get_possessions(),keyboard=keyboard)


#                           Магазин
#_________________________________________________________________________________
            elif response == 'магазин🏪' or response == 'магазин':
                send_message(vk_session, 'user_id', event.user_id, message="МАГАЗИН")
                send_message(vk_session, 'user_id', event.user_id, message="👱️Добрый день что будете брать?",keyboard=keyboard)


#                           Работать
#_________________________________________________________________________________
            elif response == 'работать':
                set_money(int(get_money(id))+1,id)
                send_message(vk_session, 'user_id', event.user_id, message="Есть")
                send_message(vk_session, 'user_id', event.user_id, get_money(id))
                send_message(vk_session, 'user_id', event.user_id, message="Это колличество ваших 💸",keyboard=keyboard)


#                           Рандом
#_________________________________________________________________________________
            elif response == 'рандом':
                send_message(vk_session, 'user_id', event.user_id,random.randint(1,10))



#                           Вернуться
#_________________________________________________________________________________
            elif response =='вернуться🔙' or response == 'вернуться':
                send_message(vk_session, 'user_id', event.user_id, message="Профиль👤",keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message="Ваша работа:")
                send_message(vk_session, 'user_id', event.user_id, player["jobs"])
                send_message(vk_session, 'user_id', event.user_id, message="Ваш баланс:")
                send_message(vk_session, 'user_id', event.user_id, get_money(id))
                send_message(vk_session, 'user_id', event.user_id, message="Ваши владения:")
                send_message(vk_session, 'user_id', event.user_id, get_possessions())



#                           Машины
#_________________________________________________________________________________
            elif response =='машины':
                send_message(vk_session, 'user_id', event.user_id, message="BMW")
                send_message(vk_session, 'user_id', event.user_id, message="MERCEDES")
                send_message(vk_session, 'user_id', event.user_id, message="PORSHE")
                send_message(vk_session, 'user_id', event.user_id, message="LAMBORGHINI",keyboard=keyboard)

            elif response == 'bmw' or response== 'bmw🚗' :
                send_message(vk_session, 'user_id', event.user_id, message="BMW 6-Series \n цена 2 200 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW X6 \n цена 8 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW Z4 \n цена 5 005 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="BMW X1 \n цена 3 000 000 💸",keyboard=keyboard)

            elif response == 'mercedes' or response== 'mersedes🚗':
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz CLS-Class \n цена 5 900 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz E-Class \n цена 4 000 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz G-Class \n цена 17 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Mercedes-Benz SLK-Class \n цена 500 000 💸",keyboard=keyboard)

            elif response == 'porsche' or response== 'porshe🚙':
                send_message(vk_session, 'user_id', event.user_id, message="Porsche 918 Spyder \n цена 48 000 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Panamera \n цена 9 500 000  💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Cayenne \n цена 8 500 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Porsche Macan \n цена 5 500 000 💸",keyboard=keyboard)

            elif response == 'lamborghini' or response== 'lamborghini🏎':
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Urus \n цена 15 200 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Huracan \n цена 17 760 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Huracan Spyder \n цена 18 650 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Lamborghini Aventador Roadster \n цена 25 500 000 💸",keyboard=keyboard)

#                   Верталёты
#___________________________________________________________
            elif response == 'вертолёты🚁' or response== 'вертолёты':
                send_message(vk_session, 'user_id', event.user_id, message="Robinson")
                send_message(vk_session, 'user_id', event.user_id, message="Eurocopter")
                send_message(vk_session, 'user_id', event.user_id, message="Bell",keyboard=keyboard)

            elif response == 'robinson🚁' or response== 'robinson':
                send_message(vk_session, 'user_id', event.user_id, message="Robinson R44 Raven 2 \n цена  47 100 500 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Robinson R66 \n цена 81 700 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Robinson R44 Raven 1 \n цена 41 200 600 💸",keyboard=keyboard)

            elif response=='eurocopter':
                send_message(vk_session,'user_id',event.user_id, message='Eurocopter AS350 \n цена 115 000 000 💸 ')
                send_message(vk_session, 'user_id', event.user_id, message="Eurocopter AS355 NP \n цена  105 000 000 💸")
                send_message(vk_session, 'user_id', event.user_id, message="Airbus Helicopters H130 \n цена 338 000 000 💸",keyboard=keyboard)

            elif response=='bell':
                send_message(vk_session,'user_id',event.user_id, message='Bell 407 \n цена 110 500 000 💸 ')
                send_message(vk_session, 'user_id', event.user_id, message="Bell 505 \n цена 123 000 000  💸")
                send_message(vk_session, 'user_id', event.user_id, message="Bell V-280 \n цена 155 000 000 💸",keyboard=keyboard)

            elif response == 'фото':
                attachment = get_pictures.get(vk_session, '130670107', session_api)
                print(attachment)
                send_message(vk_session, 'user_id', event.user_id, message="Вот",attachment=attachment)




            elif not understand:
                send_message(vk_session, 'user_id', event.user_id,message='Я вас не понимаю!')




        elif event.from_chat :
            if response == "котики":
                attachment = get_pictures.get(vk_session, -130670107, session_api)
                print(attachment)
                send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
        print('-' * 30)












