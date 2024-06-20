from telethon.sync import TelegramClient
from telethon.tl.types import Channel
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputMediaPhoto
import re
from urllib.parse import urlparse

api_id = 'Тут ваш айди'
api_hash = 'Тут ваш хеш'
phone_number = 'Тут ваш номер'
channel_links = ['https://t.me/+MgzDj31uAqdiYzUy', 'https://t.me/+KcwPLCwPXJ05ZTMy']
channel_id = # айди канала, куда скидывать

async def get_channel_posts():
    client = TelegramClient('session_name', api_id, api_hash)

    async with client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Введите код подтверждения: ')
            await client.sign_in(phone_number, code)

        try:
            for channel_link in channel_links:
                entity = await client.get_entity(channel_link)
                if isinstance(entity, Channel):
                    channel_entity = await client(GetFullChannelRequest(entity))
                    messages = await client.get_messages(channel_entity.full_chat.id, limit=20)
                    for message in messages:
                        if message.text:
                            post_text = message.text
                            photo = message.media.photo

                            urls = re.findall(r'(https?://\S+)', post_text)
                            u = all('gtblg.ru' not in url and 'rfnd.io' not in url and 'prfl.me' not in url for url in urls)

                            hyperlinks = re.findall(r'\[(.*?)\]\((.*?)\)', post_text)
                            h = all('gtblg.ru' not in link and 'rfnd.io' not in link and 'prfl.me' not in link for _, link in hyperlinks)

                            if u and h:
                                await client.send_file(channel_id, file=photo, caption=f"{post_text} \n\n **[🎁Ульяновск на скидках]**(https://t.me/+EQmy5NDuD001ZTdi)", parse_mode='Markdown')

        except ValueError as e:
            print("Ошибка при получении постов из канала:", e)

        await client.disconnect()

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(get_channel_posts())
