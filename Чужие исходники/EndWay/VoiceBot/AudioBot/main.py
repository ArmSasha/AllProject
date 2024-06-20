#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, datetime, requests, os, sqlite3, logging, aioschedule, asyncio,  gtts, secrets, string
import speech_recognition as sr
from filters import IsAdminFilter, IsOwnerFilter
import keyboard as kb
from db.db import Database
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import token, server_dir

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)
db = Database(server_dir + "/db/users.db")

dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(IsOwnerFilter)

class info(StatesGroup):
  rasst = State()
  rasst_chat = State()

async def old_db():
    users = len(await db.get_users())
    chats = len(await db.get_chats())
    voice = await db.get_voice()

    await db.set_users_old(users)
    await db.set_chat_old(chats)
    await db.set_voice_old(voice)

async def stats_day():
    chats = len(await db.get_chats())
    chats_old = await db.get_chats_old()
    chats_old = chats_old[0]

    users = len(await db.get_users())
    users_old = await db.get_users_old()
    users_old = users_old[0]

    voice = await db.get_voice()
    voice_old = await db.get_voice_old()

    return f"    <b>📊 Пользователей в боте -</b> <code>+{users - users_old}</code>\n    <b>📊 Чатов в боте -</b> <code>+{chats - chats_old}</code>\n    <b>📊 Обработано голосовых -</b> <code>+{voice - voice_old}</code>"

async def scheduler():
    aioschedule.every().day.at('00:00').do(old_db)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(message: types.Message):
    asyncio.create_task(scheduler())

async def audio_to_text(dest_name: str):
    r = sr.Recognizer()
    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="ru_RU")
    return result

@dp.message_handler(content_types=types.ContentType.ANY, state=info.rasst)
async def rass_in_user_query(message: types.Message, state: FSMContext):
    row = await db.get_users()
    users = [user[0] for user in row] 
    if message.text == 'Отмена':
       await message.answer('Отмена! Возвращаю в главное меню.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()
    else:
       await message.answer('Начинаю рассылку...')
       for i in users:
           try:
              await message.copy_to(i)
           except:
              pass

       await message.answer('Рассылка завершена.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()

@dp.message_handler(content_types=types.ContentType.ANY, state=info.rasst_chat)
async def rass_in_chat_query(message: types.Message, state: FSMContext):
    row = await db.get_chats()
    chats = [chat[0] for chat in row] 
    if message.text == 'Отмена':
       await message.answer('Отмена! Возвращаю в главное меню.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()
    else:
       await message.answer('Начинаю рассылку...')
       for i in chats:
           try:
              await message.copy_to(i)
           except:
              pass

       await message.answer('Рассылка завершена.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()

@dp.callback_query_handler(lambda c: c.data == "rass_chat", is_owner=True)
async def rass_chat_query(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Введите фото/текст для рассылки.\n\nДля отмены нажмите кнопку ниже 👇', reply_markup=kb.back)
    await info.rasst_chat.set()

@dp.callback_query_handler(lambda c: c.data == "rass", is_owner=True)
async def rass_query(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Введите фото/текст для рассылки.\n\nДля отмены нажмите кнопку ниже 👇', reply_markup=kb.back)
    await info.rasst.set()

@dp.callback_query_handler(lambda c: c.data == "stats", is_owner=True)
async def stats_query(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'<b>🤍 Общая статистика:</b>\n    <b>📊 Пользователей в боте -</b> <code>{str(len(await db.get_users()))}</code>\n    <b>📊 Чатов в боте -</b> <code>{str(len(await db.get_chats()))}</code>\n    <b>📊 Обработано голосовых -</b> <code>{str(await db.get_voice())}</code>\n\n<b>🤍 Статистика за сутки:</b>\n{await stats_day()}', parse_mode="html")

@dp.message_handler(commands=['admin'], is_owner=True)
async def admin_handler(message: types.Message):
    await bot.send_message(message.chat.id, "🤍 Добро пожаловать в админ панель.", reply_markup=kb.apanel)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    if (not await db.user_exists(message.from_user.id)):
        await db.add_user(message.from_user.id)

    if message.chat.id < 0:
       if (not await db.chat_exists(message.chat.id)):
           await db.add_chat(message.chat.id, 1)

    file = types.InputFile(server_dir + "/" +"ava.jpg")
    await bot.send_photo(message.chat.id, photo=file, caption=f"<b>💙 Привет {message.from_user.full_name}, я бот созданный для преобразования голосовых сообщений в текст, чтобы начать работу со мной пришли мне голосовое сообщение.\n\n🤍 Ты можешь добавить меня в любой чат и голосовые сообщения в них будут автоматически преобразовываться в текст.</b>", parse_mode="html", reply_markup=kb.buttons)

@dp.message_handler(commands=['staff'])
async def staff_handler(message: types.Message):
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    owners_chat = []
    admins_chat = []
    for administrators in chat_admins:
        if administrators.user.is_bot == False:
           if administrators.status == "creator":
              if administrators.user.username == None:
                 owners_chat.append(f"  <b>•</b> <a href='tg://user?id={administrators.user.id}'>{administrators.user.first_name}</a>")
              else:
                 owners_chat.append(f"  <b>•</b> @{administrators.user.username}")

           if administrators.status == "administrator":
              if administrators.user.username == None:
                 admins_chat.append(f"  <b>•</b> <a href='tg://user?id={administrators.user.id}'>{administrators.user.first_name}</a>")
              else:
                 admins_chat.append(f"  <b>•</b> @{administrators.user.username}")
    
    owners = "\n".join(owners_chat)
    admins = "\n".join(admins_chat)
    await bot.send_message(message.chat.id, f"<b>⭐️ АДМИНИСТРАЦИЯ ЧАТА ⭐️</b>\n\n<b>👑 Владелец чата</b>\n{owners}\n\n<b>👮🏼 Админ</b>\n{admins}", parse_mode="html")

@dp.message_handler(commands=['off_welcome'], is_admin=True)
async def off_welcome_handler(message: types.Message):
    await db.set_welcome(message.chat.id, 0)
    await bot.send_message(message.chat.id, f"<b>⭐️ Приветствие в этом чате было отлючено.</b>", parse_mode="html")

@dp.message_handler(commands=['on_welcome'], is_admin=True)
async def on_welcome_handler(message: types.Message):
    await db.set_welcome(message.chat.id, 1)
    await bot.send_message(message.chat.id, f"<b>⭐️ Приветствие в этом чате было включено.</b>", parse_mode="html")

@dp.message_handler(content_types=['new_chat_members'])
async def new_members_handler(message: types.Message):
    if await db.get_welcome(message.chat.id) == 1:
       await bot.send_message(message.chat.id, f"<b>👋 Добро пожаловать <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> в чат <code>{message.chat.full_name}</code></b>", parse_mode="html")

@dp.message_handler(commands=["record"])
async def handler_record(message: types.Message):
    args = message.get_args()
    text = gtts.gTTS(args, lang="ru") 

    alphabet = string.ascii_letters + string.digits
    name = ''.join(secrets.choice(alphabet) for i in range(16))
    text.save(server_dir + f"/voice/{name}.mp3") 
    
    await bot.send_voice(message.chat.id, open(server_dir + f"/voice/{name}.mp3", "rb"))

    os.remove(server_dir + f"/voice/{name}.mp3")
    
@dp.message_handler()
async def handler(message: types.Message):
    if (not await db.user_exists(message.from_user.id)):
        await db.add_user(message.from_user.id)
    
    if message.chat.id < 0:
       if (not await db.chat_exists(message.chat.id)):
           await db.add_chat(message.chat.id, 1)

@dp.message_handler(content_types=['voice'])
async def get_audio_messages(message: types.Message):
    msg = await message.answer("🔊 Ожидайте, распознаю...")
    try:
        file_info = await bot.get_file(message.voice.file_id)
        path = file_info.file_path 
        fname = os.path.basename(path) 

        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        with open(server_dir + "/voice/" + fname + '.oga', 'wb') as f:
            f.write(doc.content)

        process = subprocess.run(['ffmpeg', '-i', server_dir + "/voice/" + fname + '.oga', "/home/senpai/VoiceBot/voice/"+fname+'.wav'])
        result = await audio_to_text(server_dir + "/voice/" + fname+'.wav')

        await db.set_voice(1)

        if message.forward_from != None:
           await msg.edit_text(f"<b>🤍 От {message.forward_from.full_name}:</b>\n" + format(result), parse_mode="html")
        else:
            await msg.edit_text(f"<b>🤍 От {message.from_user.full_name}:</b>\n" + format(result), parse_mode="html")

    except sr.UnknownValueError as e:
        if message.forward_from != None:
           await msg.edit_text(f"<b>🖤 От {message.forward_from.full_name}:</b>\nНе распознано", parse_mode="html")
        else:
           await msg.edit_text(f"<b>🖤 От {message.from_user.full_name}:</b>\nНе распознано", parse_mode="html")

    finally:
        # os.remove(server_dir+"/voice/"+fname+'.wav')
        os.remove(server_dir+"/voice/"+fname+'.oga')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)