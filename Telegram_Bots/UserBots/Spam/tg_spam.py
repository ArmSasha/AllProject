from social_spam import Telegram
import time
tg = Telegram()
tg.connect_user(api_id='айди', api_hash='хеш', phone_number='номер')

# print(tg.get_chats())

while True:
	tg.start_selective_spam([айди кому, айди кому], '123')
	time.sleep(2)
