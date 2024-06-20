from telethon import TelegramClient, functions, sync
import config

client = TelegramClient("Get Chats", config.api_id, config.api_hash)

with open("C:/Users/Саша/PycharmProjects/KESHA/EndWay/Chat_Parser/endings.txt", "r") as file:
	ends = file.read().split("\n")

with open("C:/Users/Саша/PycharmProjects/KESHA/EndWay/Chat_Parser/names.txt", "r") as file:
	names = file.read().split("\n")

client.start()

old = []
with open("output.txt", "w", encoding="utf-8") as file:
	print("Запуск скрипта...")
	for title in names:
		for end in ends:
			name = title + end
			print("Подбираются чаты найденные по имени: ", name)
			name = name.lower()
			request = client(functions.contacts.SearchRequest(q=name,limit=10))
			for channel in request.chats:
				if channel.megagroup:
					username = channel.username.lower() if channel.username is not None else ""
					if username not in old:
						if channel.title not in old:
							print(f"Найден чат: t.me/{channel.username}")
							file.write(f"t.me/{channel.username}\n")
							old.append(channel.username)
							print("Найден чат с подобранным именем: ", channel.title)
print("Скрипт завершил свою работу...")

