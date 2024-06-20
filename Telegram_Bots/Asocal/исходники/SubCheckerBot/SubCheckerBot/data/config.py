import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')

IP = os.getenv('IP')
PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{IP}/{DATABASE}'

