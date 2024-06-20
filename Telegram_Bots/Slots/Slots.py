# by GenryJr.t.me
# from endway.su
from telethon import events, TelegramClient
from telethon.tl.types import InputMediaDice

api_id = '5681803'
api_hash = 'Тут ваш токен'

client = TelegramClient('pon1', api_id, api_hash)
client.start()
print("Скрипт робит")
#.вино подкрутит 3 винограда
#.бар подкрутит 3 бара
#.лимон подкрутит 3 лимона
#.семь подкрутит 3 семерки
#.пох подкрутит 3 любые символа (одинаковые)


@client.on(events.NewMessage(pattern=r'.бар'))
async def handler3(event):
        """подкрутить слот на 3 бара"""
        val = 0
        await event.delete()
        while True:
            ms = await event.client.send_message(event.chat_id, file=InputMediaDice("🎰"))
            if ms.media.value == 1:
                break
            else:
                await ms.delete()
@client.on(events.NewMessage(pattern=r'.вино'))
async def handler4(event):
        """подкрутить слот на 3 винограда"""
        val = 0
        await event.delete()
        while True:
            ms = await event.client.send_message(event.chat_id, file=InputMediaDice("🎰"))
            if ms.media.value == 22:
                break
            else:
                await ms.delete()
@client.on(events.NewMessage(pattern=r'.лимон'))
async def handler(event):
        """подкрутить слот на 3 лимона"""
        val = 0
        await event.delete()
        while True:
            ms = await event.client.send_message(event.chat_id, file=InputMediaDice("🎰"))
            if ms.media.value == 43:
                break
            else:
                await ms.delete()
@client.on(events.NewMessage(pattern=r'.семь'))
async def handler2(event):
        """подкрутить слот на 3 семерки"""
        val = 0
        await event.delete()
        while True:
            ms = await event.client.send_message(event.chat_id, file=InputMediaDice("🎰"))
            if ms.media.value == 64:
                break
            else:
                await ms.delete()
@client.on(events.NewMessage(pattern=r'.пох'))
async def slotcmd(event):
        """подкрутить слот на похуях, главное чтобы три значения было"""
        val = 0
        await event.delete()
        while True:
            ms = await event.client.send_message(event.chat_id, file=InputMediaDice("🎰"))
            if ms.media.value == 1 or ms.media.value == 22 or ms.media.value == 43 or ms.media.value == 64:
                break
            else:
                await ms.delete()
    
client.run_until_disconnected()
