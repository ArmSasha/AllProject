import vk_api, json
from vk_api.longpoll import VkEventType, VkLongPoll


vk_session = vk_api.VkApi(token = 'Тут ваш токен')
longpoll = VkLongPoll(vk_session)

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

def sender(id, text, car):
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'template' : car})

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:

			id = event.user_id
			msg = event.text.lower()

			if msg == 'привет':
				sender(id, 'И тебе привет!', carusel)
