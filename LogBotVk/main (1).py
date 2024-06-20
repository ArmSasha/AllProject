from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, json


vk_session = vk_api.VkApi(token = '1496a7953a10ba99104f886a87158c03bf50f14edaddb094826252883a71f20401b801e85dc0501ea6230')
longpoll = VkLongPoll(vk_session)

class User:
	def __init__(self, id, mode):
		self.id = id
		self.mode = mode
		self.name = ''
		self.age = -1

def get_keyboard(buts):
	nb = []
	for i in range(len(buts)):
		nb.append([])
		for k in range(len(buts[i])):
			nb[i].append(None)
	for i in range(len(buts)):
		for k in range(len(buts[i])):
			text = buts[i][k][0]
			color = {'зеленый' : 'positive', 'красный' : 'negative', 'синий' : 'primary'}[buts[i][k][1]]
			nb[i][k] = {"action": {"type": "text", "payload": "{\"button\": \"" + "1" + "\"}", "label": f"{text}"}, "color": f"{color}"}
	first_keyboard = {'one_time': False, 'buttons': nb, 'inline' : False}
	first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
	first_keyboard = str(first_keyboard.decode('utf-8'))
	return first_keyboard

def sender(id, text, key):
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : key})


def save():
	login_pass_save = {}
	login_pass_save[user.name.get()] = user.age.get()
	f = open('BassData', 'wb')
	f.close()





clear_key = get_keyboard(
	[]
)

menu_key = get_keyboard([
	[('Информация', 'синий')]
])

users = []

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:

			id = event.user_id
			msg = event.text.lower()

			if msg == 'начать':
				flag = 0
				for user in users:
					if user.id == id:
						flag = 1
						break
				if flag == 0:
					users.append(User(id, 'reg1'))
					sender(id, 'Зарегистрируйтесь в боте.\nВведите своё имя:', clear_key)
				elif flag == 1:
					for user in users:
						if user.id == id:
							if not(user.moded in ['reg1', 'reg2']):
								sender(id, 'Вы уже зарегистрировались!', clear_key)

			else:
				for user in users:
					if user.id == id:

						if user.mode == 'reg1':
							user.name = msg.title()
							sender(id, 'Введите свой возраст:', clear_key)
							user.mode = 'reg2'

						elif user.mode == 'reg2':
							try:
								user.age = int(msg)
								sender(id, 'Вы успешно зарегистрировались!', menu_key)
								user.mode = 'menu'
								save()
								
							except:
								sender(id, 'Значение не подходит!', clear_key)

						elif user.mode == 'menu':
							if msg == 'информация':
								sender(id, f'Ваше имя в боте: {user.name}\nВаш возраст в боте: {user.age}', menu_key)