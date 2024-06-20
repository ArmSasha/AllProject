from create_bot import dp, bot, db, check_sub_channels
from keyboards import check_subscribe_btn as nav
import config as con
from aiogram import types, Dispatcher

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='subchanneldone')
async def subchanneldone(callback_query: types.CallbackQuery):
	await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
	await bot.answer_callback_query(callback_query.id)

	if await check_sub_channels(con.CHANNELS, callback_query.from_user.id):
		await callback_query.answer(" Привет, я Анонимный ЧатБот!")
		await bot.send_message(callback_query.from_user.id, 'Напишите /start')
	else:
		await bot.send_message(callback_query.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
		await bot.answer_callback_query(callback_query.id)



# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------


#Регистрируем хендлеры
def register_handlers_check_subscribe(dp: Dispatcher):
	dp.register_callback_query_handler(subchanneldone, text='subchanneldone')