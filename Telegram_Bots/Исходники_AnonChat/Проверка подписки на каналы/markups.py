from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS


btnProfile = KeyboardButton('Profile')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)

def showChannels():
	keyboard = InlineKeyboardMarkup(row_width=1)

	for channel in CHANNELS:
		btn = InlineKeyboardButton(text=channel[0], url=channel[2])
		keyboard.insert(btn)

	btnDoneSub = InlineKeyboardButton(text='I subscribe', callback_data = 'subchanneldone')
	keyboard.insert(btnDoneSub)
	return keyboard