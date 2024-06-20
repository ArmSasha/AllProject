'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from environs import Env

env = Env()

env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
CRYPTO_PAY_TOKEN = env.str('CRYPTO_PAY_TOKEN')

ADMINS_ID = [1537002204]
