
#IMPORTS{

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import requests
from bs4 import BeautifulSoup as BS

#}


# НАДО{

vk_session = vk_api.VkApi(token='0eba16342f679f7fad7a17fdb0758a2144651be31cf45449dfc45f46f39f6d43cd4e2fc257bb275d7e0c5')
longpoll = VkBotLongPoll(vk_session, 199029300 )

r = requests.get('https://sinoptik.ua/погода-ульяновск')
html = BS(r.content, 'html.parser')

#}


#DEF{

def sender(id, text):
    vk_session.method('messages.send',{'chat_id' : id, 'message' : text, 'random_id' : 0})

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



                elif msg[0] == 'его' and msg[1] == 'зовут' and msg[2] == 'аркаша':
                    sender(id,'Да, это я')

                elif msg[0] == 'погода':
                    for el in html.select('#content'):
                        t_min = el.select('.temperature .min')[0].text
                        t_max = el.select('.temperature .max')[0].text
                        text = el.select('.wDescription .description')[0].text

                    sender(id, "Привет, погода на сегодня:\n" +
                           t_min + ', ' + t_max + '\n' + text)
                elif msg[0] == 'онлайн':
                    sender(id,vk_api(0))
                    # elif msg[1] == 'как дела' or msg == 'как дела?':
                    #     sender(id,'Хорошо')




















