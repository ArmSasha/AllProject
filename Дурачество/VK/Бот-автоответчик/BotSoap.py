import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import datetime

vk_session = vk_api.VkApi(token='Тут ваш токен')
vk = vk_session.get_api()
# image = "C:/Users/Саша/PycharmProjects/KESHA/vuUnmRiG-Xc.jpg"
longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)

#{ <СООБЩЕНИЕ>
def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard, 'attachment': ','.join(attachments)})
#}

#{ <СТИКЕРЫ>
def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)
#}

#{ <ФОТО>
def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)
#}

def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": text
        },
        "color": color

    }


#{ <ЦВЕТА КНОПОК>
    'primary — синяя кнопка, обозначает основное действие. #5181B8\
    secondary — обычная белая кнопка. #FFFFFF\
    negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646\
    positive — согласиться, подтвердить. #4BB34B '
#}


#     #{ <КНОПКИ>
# keyboard = {
#     "one_time": False,
#     "buttons": [
#         [get_but('Привет', 'positive'), get_but('Пока', 'negative')],
#         [get_but('Как дела?', 'positive'), get_but('Как сделать заказ?', 'primary')],
#
#     ]
# }
# keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
# keyboard = str(keyboard.decode('utf-8'))
#     #}

def create_keyboard(msg):
    keyboard = VkKeyboard(one_time=False)

    if msg == 'начать':
        keyboard.add_button('Как сделать заказ?', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Как дела?', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)

    elif msg == 'привет':
        keyboard.add_button('Как сделать заказ?', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Как дела?', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)

        # keyboard.add_line()
        # keyboard.add_button('lamborghini🏎', color=VkKeyboardColor.NEGATIVE)
        # [get_but('Пока', 'negative')],
        # [get_but('Как дела?', 'positive'), get_but('Как сделать заказ?', 'primary')],

    elif msg == 'как дела?':
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Как сделать заказ?', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)

    elif msg == 'как сделать заказ?':
        keyboard.add_button('Привет', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Как дела?', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)

    elif msg == 'пока':
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Как дела?', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Как сделать заказ?', color=VkKeyboardColor.POSITIVE)

    elif msg == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()





    keyboard = keyboard.get_keyboard()
    return keyboard






#{ <ОСНОВНОЙ КОД>
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower().strip()
            id = event.user_id
            attachments = []
            # upload_image = upload.photo_messages(photos=image)[0]
            keyboard = create_keyboard(msg)
            now = datetime.datetime.now()
            #attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))

#}





#{ <ОБРАБОТКА СООБЩЕНИЙ>

            if msg == 'начать':
                sender(id,'Начинаем')
                send_stick(id,21153)
                keyboard = keyboard

            if msg == 'привет' or msg== 'дорова':
                if now.hour < 12:
                    sender(id,'Доброе утро')
                    send_stick(id, 12840)


                if now.hour > 12 and now.hour < 18 :
                    sender(id,'Добрый день')
                    send_stick(id, 21148)

                if now.hour > 18:
                    sender(id,'Добрый вечер')
                    send_stick(id, 54103)
                # send_photo(id,'photo-201186960_457239039')
                keyboard = keyboard

            elif msg == 'пока':
                sender(id,'Пока, возвращайся по скорее')
                send_stick(id,109)
                keyboard=keyboard

            elif msg == "как дела?" or msg == "как дела":
                sender(id,'Хорошо, у тебя как?')
                send_stick(id,86)
                keyboard = keyboard

            elif msg=='закрыть':
                sender(id,'Закрыть')
                keyboard = keyboard

            elif msg == "как сделать заказ?" or msg == 'как сделать заказ':
                sender(id, 'Вам надо перейти по этой ссылки и выбрать тавар https://vk.com/market-201186960 \n'
                           ' Затем нажать на кнопку "Добавить в корзину" и вабрать количество товара \n '
                           'Далее нужно перейти в корзину и оформить заказ ')
                        #   'Хит продаж:https://clck.ru/Sfbmy'
                send_stick(id, 51666)
                keyboard=keyboard


#}







