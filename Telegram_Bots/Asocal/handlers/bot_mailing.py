from aiogram import types, Dispatcher
from create_bot import dp, bot, db
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from states import bot_mailing
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import admins

# from aiogram.dispatcher.filters import Text

# @dp.message_handler(ISPrivate(), text='/mailing', chat_id=admins)
async def start_mailing(message: types.Message):
	await message.answer(f'Введите текст рассылки:')
	await bot_mailing.text.set()

# @dp.message_handler(ISPrivate(), state=bot_mailing.text, chat_id=admins)
async def mailing_text(message: types.Message, state: FSMContext):
	answer = message.text
	markup = InlineKeyboardMarkup(row_width=2,
									inline_keyboard=[
										[
											InlineKeyboardButton(text='Добавить фотографию', callback_data='add_photo'),
											InlineKeyboardButton(text='Далее', callback_data='next'),
											InlineKeyboardButton(text='Отменить', callback_data='quit')
										]
									])
	await state.update_data(text=answer)
	await message.answer(text=answer, reply_markup=markup)
	await bot_mailing.state.set()


# @dp.calback_query_handler(text='next', state=bot_mailing.state)
async def start(call: types.CallbackQuery, state: FSMContext):
	users = db.get_users()
	data = await state.get_data()
	text = data.get('text')
	await state.finish()
	for user in users:
		try:
			await dp.bot.send_message(chat_id=user[0], text=text)
			await sleep(0.33)
		except Exception:
			pass
	await call.message.answer('Рассылка выполнена')


# @dp.calback_query_handler(text='add_photo', state=bot_mailing.state)
async def add_photo(call: types.CallbackQuery):
	await call.message.answer('Пришлите фото')
	await bot_mailing.photo.set()

# @dp.message_handler(ISPrivate(), state=bot_mailing.photo, content_types=types.ContentType.PHOTO)
async def mailing_photo(message: types.Message, state: FSMContext):
	photo_file_id = message.photo[-1].file_id
	await state.update_data(photo=photo_file_id)
	data = await state.get_data()
	text = data.get('text')
	photo = data.get('photo')
	markup = InlineKeyboardMarkup(row_width=2,
									inline_keyboard=[
										[
											InlineKeyboardButton(text='Далее', callback_data='next'),
											InlineKeyboardButton(text='Отменить', callback_data='quit')
										]
									])
	await message.answer_photo(photo=photo, caption=text, reply_markup=markup)

# @dp.calback_query_handler(text='next', state=bot_mailing.photo)
async def start_p(call: types.CallbackQuery, state: FSMContext):
	users = db.get_users()
	data = await state.get_data()
	text = data.get('text')
	photo = data.get('photo')
	await state.finish()
	for user in users:
		try:
			await dp.bot.send_photo(chat_id=user[0], photo=photo, caption=text)
			await sleep(0.33)
		except Exception:
			pass
	await call.message.answer('Рассылка выполнена')

# @dp.message_handler(ISPrivate(), state=bot_mailing.photo)
async def no_photo(message: types.Message):
	markup = InlineKeyboardMarkup(row_width=2,
									inline_keyboard=[
										[
											InlineKeyboardButton(text='Отменить', callback_data='quit')
										]
									])
	await message.answer('Пришлите фото', reply_markup=markup)

# @dp.calback_query_handler(text='quit', state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state])
async def quit(call: types.CallbackQuery, state: FSMContext):
	await state.finish()
	await call.message.answer('Рассылка отменена')


#Регистрируем хендлеры
def register_handlers_bot_mailing(dp: Dispatcher):
	dp.register_message_handler(start_mailing, text='/mailing', chat_id=admins)
	dp.register_message_handler(mailing_text, state=bot_mailing.text, chat_id=admins)
	dp.register_callback_query_handler(start, text='next', state=bot_mailing.state, chat_id=admins)
	dp.register_callback_query_handler(add_photo, text='add_photo', state=bot_mailing.state, chat_id=admins)
	dp.register_message_handler(mailing_photo,state=bot_mailing.photo, content_types=types.ContentType.PHOTO, chat_id=admins)
	dp.register_callback_query_handler(start_p, text='next', state=bot_mailing.photo, chat_id=admins)
	dp.register_message_handler(no_photo, state=bot_mailing.photo, chat_id=admins)
	dp.register_callback_query_handler(quit, text='quit', state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state], chat_id=admins)