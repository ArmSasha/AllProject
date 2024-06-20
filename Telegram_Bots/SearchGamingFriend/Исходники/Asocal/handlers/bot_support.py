from aiogram import types, Dispatcher
from create_bot import dp, bot, db
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from states import bot_support
from config import admin_chat
from keyboards import keyboard_support as kb



# @dp.callback_query_handler(text='support_text')
async def support_text(call: types.CallbackQuery):
	await bot.delete_message(call.message.chat.id, call.message.message_id)
	Logo_menu = open('Images/Logo_menu.png', 'rb')
	await bot.send_photo(call.from_user.id, caption = 'Ты можешь задать свой вопрос в поддержку создав тикет. Но перед этим рекомендуем ознакомиться с нашим <a href = "https://telegra.ph/FAQ-CHasto-zadavaemye-voprosy-02-04">FAQ</a>', photo = Logo_menu, parse_mode=types.ParseMode.HTML, reply_markup=kb.support)

# @dp.callback_query_handler(text='support')
async def support(call: types.CallbackQuery):
	await call.message.answer('Напиши мне свой вопрос и я отправлю его администрации.')



# @dp.message_handler(content_types=['text'])
async def h(message: types.Message, state: FSMContext):
	await message.answer('Сообщение доставлено.')
	await bot.send_message(admin_chat, f"<b>Получен новый вопрос!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')

# @dp.callback_query_handler(lambda call: True, state=st.item2) # Inline часть
async def cal(call: types.CallbackQuery, state: FSMContext):
	if 'ans' in call.data:
		a = call.data.index('-ans')
		ids = call.data[:a]
		await call.message.answer('Введите ответ пользователю:', reply_markup=kb.back)
		await bot_support.item.set() # админ отвечает пользователю
		await state.update_data(uid=ids)
	elif 'ignor' in call.data:
		await call.answer('Удалено')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()

# @dp.message_handler(state=st.item2)
async def proc(message: types.Message, state: FSMContext):
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.')
		await state.finish()
	else:
		await message.answer('Сообщение отправлено.')
		data = await state.get_data()
		ids = data.get("uid")
		await state.finish()
		await bot.send_message(chat_id = ids, text = 'Вам поступил ответ от администратора:\n\nТекст: {}'.format(message.text))


# #Регистрируем хендлеры
def register_handlers_bot_support(dp: Dispatcher):
	dp.register_callback_query_handler(support_text, text='support_text')
	dp.register_callback_query_handler(support, text='support')
	dp.register_message_handler(h, content_types=['text'])
	dp.register_callback_query_handler(cal, lambda call: True) #  state=st.item1
	dp.register_message_handler(proc, state=bot_support.item)