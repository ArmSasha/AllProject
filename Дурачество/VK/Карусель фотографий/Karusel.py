
#IMPORTS{

import vk_api,json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
import requests
from bs4 import BeautifulSoup as BS



#}


# НАДО{

vk_session = vk_api.VkApi(token='0eba16342f679f7fad7a17fdb0758a2144651be31cf45449dfc45f46f39f6d43cd4e2fc257bb275d7e0c5')
longpoll = VkBotLongPoll(vk_session, 199029300 )

upload = VkUpload(vk_session)
vk = vk_session.get_api()

r = requests.get('https://sinoptik.ua/погода-ульяновск')
html = BS(r.content, 'html.parser')

#КАРУСЕЛЬ{
carusel = {
    	"type": "carousel",
    	"elements": [



    	{
            "photo_id": "-188446752_457239201",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "DimPy",
                    "payload": "{}"
                }
            },{
                "action": {
                    "type": "open_link",
                    "link" : "https://www.youtube.com/channel/UCP5C_Wg2rL_uAJw8qrVxtLQ",
                    "label": "Перейти",
                    "payload": "{}"
                }
            }
            ]
        },



        {
            "photo_id": "-188446752_457239202",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Хауди Хо",
                    "payload": "{}"
                }
            },{
                "action": {
                    "type": "open_link",
                    "link" : "https://www.youtube.com/channel/UC7f5bVxWsm3jlZIPDzOMcAg",
                    "label": "Перейти",
                    "payload": "{}"
                }
            }
            ]
        },



        {
            "photo_id": "-188446752_457239203",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Marmok",
                    "payload": "{}"
                }
            },{
                "action": {
                    "type": "open_link",
                    "link" : "https://www.youtube.com/channel/UCf31Gf5nCU8J6eUlr7QSU0w",
                    "label": "Перейти",
                    "payload": "{}"
                }
            }
            ]
        }



    ]
}


carusel = json.dumps(carusel, ensure_ascii = False).encode('utf-8')
carusel = str(carusel.decode('utf-8'))


#}


# online = vk.users.search(online=1)
# url = f"https://api.vk.com/method/users.search={online}&count=1&access_token={token}&v=5.52"
#}


#DEF{

def sender(id, text):
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'template' : carusel})


def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)


def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)
#}


# OPTS}
opts = {
    "name": ('аркаша','эу','эй','аркадий','арк','арка'),

    "cmds": {

        "weather": ('погода'),

     }
}

#}

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:

            id = event.chat_id
            slovo = event.object.message['text'].lower()



            try:
                dey = event.message.action['type']
                invite_id = event.message.action['member_id']
            except:
                dey = ''
                invite_id = -100

                if dey == 'chat_invite_user':
                    sender(id,f'Приветствую тебя, @id{invite_id}!')


                s2 = ' ,:@.-()/?'

                for sim in s2:
                    slovo = slovo.replace(str(sim), ',')
                msg = slovo.split(',')
                while 1:
                    try:
                        msg.remove('')
                    except ValueError:
                        break
                print(msg)

                if msg[0] == 'аркаша':

                    if msg[1] == 'привет':
                        sender(id, 'Приветствую!')

                    elif msg[1] == 'как' and msg[2] == 'дела':
                        sender(id,'Хорошо')

                    elif msg[1] == 'погода':
                        for el in html.select('#content'):
                            t_min = el.select('.temperature .min')[0].text
                            t_max = el.select('.temperature .max')[0].text
                            text = el.select('.wDescription .description')[0].text


                        sender(id,"Привет, погода на сегодня:\n" +
                              t_min + ', ' + t_max + '\n' + text)



                elif msg[0] == 'погода' and msg[1] == 'завтра':
                    for el in html.select('#content'):
                        t_min = el.select('.temperature .min')[1].text
                        t_max = el.select('.temperature .max')[1].text
                        text = el.select('.wDescription .description')[1].text

                    sender(id, "Привет, погода на завтра:\n" +
                           t_min + ', ' + t_max + '\n' + text)



                elif msg[0] == 'его' and msg[1] == 'зовут' and msg[2] == 'аркаша':
                    sender(id,'Да, это я')

                # elif msg[0] == 'погода':
                #     for el in html.select('#content'):
                #         t_min = el.select('.temperature .min')[0].text
                #         t_max = el.select('.temperature .max')[0].text
                #         text = el.select('.wDescription .description')[0].text
                #
                #     sender(id, "Привет, погода на сегодня:\n" +
                #            t_min + ', ' + t_max + '\n' + text)

                # elif msg[0] == 'online':
                #     sender(id,online)

                    # elif msg[1] == 'как дела' or msg == 'как дела?':
                    #     sender(id,'Хорошо')




















