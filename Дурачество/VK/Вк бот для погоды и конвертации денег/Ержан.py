
#IMPORTS{

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
import requests
from bs4 import BeautifulSoup as BS



#}


# НАДО{

vk_session = vk_api.VkApi(token='Тут ваш токен')
longpoll = VkBotLongPoll(vk_session, 201914526 )

upload = VkUpload(vk_session)
vk = vk_session.get_api()

r = requests.get('https://sinoptik.ua/погода-ульяновск')
html = BS(r.content, 'html.parser')


# online = vk.users.search(online=1)
# url = f"https://api.vk.com/method/users.search={online}&count=1&access_token={token}&v=5.52"
#}


#DEF{

def sender(id, text):
    vk_session.method('messages.send',{'chat_id' : id, 'message' : text, 'random_id' : 0})


def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)


def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)


url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
response = requests.get(url).json()






def send_welcome(msg):
    sender(id,'Выберите: \n'
              'Погода \n'
              'Курсы валют')
    process_select_step(msg)



def process_select_step(msg):
    try:
        if (msg == 'Курсы валют'):
            coins(msg)
        elif (msg == 'Погода'):
            weather(msg)
        else:
            send_welcome(msg)

    except Exception as e:
       print('Ошибка')



# Погода
def weather(msg):
    r = requests.get('https://sinoptik.ua/погода-харьков')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text



    sender(id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text)



# Курсы валют

def coins(msg):
    sender(id,'Выберите: \n'
              'USD \n'
              'EUR \n'
              'RUR \n'
              'BTC \n')
    sender(id,
                    "Узнать наличный курс ПриватБанка (в отделениях)")
    process_coin_step(msg)



def process_coin_step(msg):
    try:


       for coin in response:
           if (msg == coin['ccy']):
              sender(id, printCoin(coin['buy'], coin['sale']),
                               parse_mode="Markdown")

    except Exception as e:
       sender(id,'oooops')



def printCoin(buy, sale):
    '''Вывод курса пользователю'''
    return "💰 *Курс покупки:* " + str(buy) + "\n💰 *Курс продажи:* " + str(sale)














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




















