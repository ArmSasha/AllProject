from social_spam import Telegram
import time
tg = Telegram()
tg.connect_user(api_id='24299549', api_hash='71dd49045fd731a379e84238a9e49b44', phone_number='89951039893')

# print(tg.get_chats())

while True:
	tg.start_selective_spam([-4068993362, 1030874842], '123')
	time.sleep(2)