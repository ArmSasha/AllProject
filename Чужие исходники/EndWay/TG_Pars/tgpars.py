import os
import time
from telethon.sync import TelegramClient
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError, SessionPasswordNeededError

# print("""\
# # Список библиотек который нужны для успешной работы
# # telethon
# Чтобы установить в cmd пропишите команду : pip install telethon
# """)

# # Приветствие
# print("""\
#          Парсер групп телеграмм от:
#  ______   _____  _________    ___   ___  ____            _____     ________  _________  
# |_   _ \ |_   _||  _   _  | .'   `.|_  ||_  _|          |_   _|   |  __   _||  _   _  | 
#   | |_) |  | |  |_/ | | \_|/  .-.  \ | |_/ /              | |     |_/  / /  |_/ | | \_| 
#   |  __'.  | |      | |    | |   | | |  __'.              | |   _    .'.' _     | |     
#  _| |__) |_| |_    _| |_   \  `-'  /_| |  \ \_  _______  _| |__/ | _/ /__/ |   _| |_    
# |_______/|_____|  |_____|   `.___.'|____||____||_______||________||________|  |_____| 
        
#          Реклама:
#          С меня парсер с вас минуточка внимания <3
#          Отработка холодных кошельков: https://zelenka.guru/threads/4787708/
#          Telegram: @bitok_moneymaker
        
# """)

# Вставляем ваш API ID и API Hash
api_id = '5681803'
api_hash = '10f02cd422cceda362b5b05a82edd0ff'

# Номер телефона телеги и пасс 2фа от вашей телеги
phone_number = '+79374517495'
password = '108989898'

# Файл с группами, которые нужно парсить
group_file_path = 'groups.txt'

# Парсинг групп
def parse_group(group_username, output_file_path):
    # Создаем новый клиент
    client = TelegramClient('session_name', api_id, api_hash)

    # Подключение к Телеграмм API
    client.connect()

    # Логинимся в своем аккаунте
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        try:
            client.sign_in(phone_number, input('Enter the code: '))
        except SessionPasswordNeededError:
            client.sign_in(password=input('Enter the 2FA password: '))
    # Выводим сообщение о начале работы парсера
    print('Парсер начал работу')
    # Получение групового объекта
    group_entity = client.get_entity(group_username)

    # Получение подписчиков с группы.
    participants = client.get_participants(group_entity, filter=ChannelParticipantsSearch(''))

    # Запись юзернеймов в файл
    def save_usernames_to_file(usernames, file_path):
        with open(file_path, 'w') as f:
            count = 0
            for username in usernames:
                f.write(username + '\n')
                count += 1
                if count % 1000 == 0:
                    print(f'Parsed {count} users - Successfully')
            print(f'Successfully saved {len(usernames)} usernames to {file_path}')

    # Извлечение юзернеймов из списка участников
    usernames = [p.username for p in participants if p.username is not None]

    # Сохранение юзернеймов в файл .txt
    save_usernames_to_file(usernames, output_file_path)

    # Оповещение об успешном завершении парсинга
    print(f'Parsing of {group_username} finished successfully. Number of users: {len(usernames)}.')

# Считываем список групп из файла и парсим каждую группу
with open(group_file_path, 'r', encoding='utf-8') as f:
    for line in f:
        group_username = line.strip()
        output_file_path = f'{group_username}.txt'
        if os.path.exists(output_file_path):
            print(f'{output_file_path} Уже существует. Пропуск парса {group_username}...')
            continue
        try:
            parse_group(group_username, output_file_path)
        except PeerFloodError as e:
            print(f'Telegram API блокирует доступ к группе {group_username} из-за слишком частых запросов. Ждем 5 минут...')
            time.sleep(300)  # sleep for 5 minutes
            parse_group(group_username, output_file_path)
        except Exception as e:
            print(f'Не удалось получить участников {group_username} {e}. Пропускаем...')


