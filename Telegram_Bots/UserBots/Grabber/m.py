from telethon.sync import TelegramClient
from telethon.tl.types import Channel
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputMediaPhoto
import re
from urllib.parse import urlparse

api_id = '5681803'
api_hash = '10f02cd422cceda362b5b05a82edd0ff'
phone_number = '89374517495'
channel_link = 'https://t.me/+MgzDj31uAqdiYzUy'
channel_id = -1001949092880



async def get_channel_posts():
    client = TelegramClient('session_name', api_id, api_hash)
    u = False
    h = False

    async with client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Введите код подтверждения: ')
            await client.sign_in(phone_number, code)


        try:
            entity = await client.get_entity(channel_link)
            if isinstance(entity, Channel):
                channel_entity = await client(GetFullChannelRequest(entity))
                messages = await client.get_messages(channel_entity.full_chat.id, limit=20)
                for message in messages:
                    if message.text:
                        post_text = message.text
                        photo = message.media.photo
                        # await client.send_message(channel_id, f"Текст поста: {post_text}")
                        # await client.send_file(channel_id, file=photo, caption=f"Текст поста: {post_text} \n\n **[🎁Ульяновск на скидках]**(https://t.me/+EQmy5NDuD001ZTdi)", parse_mode='Markdown')
                        urls = re.findall(r'(https?://\S+)', post_text)
                        for url in urls:
                            parsed_url = urlparse(url)
                            if parsed_url.netloc:
                                if 'gtblg.ru' in url:
                                    u = False
                                elif 'rfnd.io' in url:
                                    u = False
                                elif 'prfl.me' in url:
                                    u = False
                                else:
                                    u = True

                        hyperlinks = re.findall(r'\[(.*?)\]\((.*?)\)', post_text)
                        # for text, link in hyperlinks:
                        #     await client.send_message(channel_id, f"Гиперссылка - Текст: {text}")
                        #     await client.send_message(channel_id, f"Гиперссылка - Ссылка: {link}")
                        for text, link in hyperlinks:
                            if 'gtblg.ru' in link:
                                h = False
                            elif 'rfnd.io' in link:
                                h = False
                            elif 'prfl.me' in link:
                                h = False
                            else:
                                h = True
                        if u and h == True:
                            await client.send_file(channel_id, file=photo, caption=f"{post_text} \n\n **[🎁Ульяновск на скидках]**(https://t.me/+EQmy5NDuD001ZTdi)", parse_mode='Markdown')
                        else:
                            pass



        except ValueError as e:
            print("Ошибка при получении постов из канала:", e)

        await client.disconnect()

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(get_channel_posts())