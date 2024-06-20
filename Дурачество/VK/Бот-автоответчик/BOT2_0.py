import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

vk_session = vk_api.VkApi(token='a958b1714c7aefb9bada1182ca24fb5d891ca52bfb8bb5cc29d8ec2ed0d3c0a9ce2a7168d5b12a12e4544')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

image = "C:/Users/Саша/PycharmProjects/КЕША/vuUnmRiG-Xc.jpg"
upload= VkUpload(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard, 'attachment': ','. join(attachments)})


def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)


def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": text
        },
        "color": color

    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Привет', 'positive'), get_but('Пока', 'positive')],
        [get_but('Как дела?', 'positive'), get_but('Как сделать заказ?', 'positive')],
        [get_but('Вт', 'positive'), get_but('П', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id
            attachemts= []




            if msg == 'привет':
                sender(id, 'И тебе привет!')
                send_stick(id, 13650)
                upload_image = upload.photo_messages(photo=image[0])
                attachemts.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))

            elif msg == 'пока':
                sender(id,'Пока, возвращайся по скарее')
                send_stick(id,50)

            elif msg == "как дела?" or msg == "как дела":
                sender(id,'Хорошо, у тебя как?')
                send_stick(id,86)
            elif msg == "как сделать заказ?":
                sender(id, 'Вам надо перейти по этой ссылки и выбрать тавар https://vk.com/market-190681420')
                send_stick(id, 21545)
            else:
                sender(id, 'Я вас не понимаю')
                send_stick(id,83)









