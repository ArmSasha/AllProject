from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
import datetime

#----------------------------------------------------------------------------------------------------------------

back = InlineKeyboardMarkup(row_width=1)
back.add(InlineKeyboardButton(text="Назад🔙", callback_data="back"))

#----------------------------------------------------------------------------------------------------------------

doctors_btn = InlineKeyboardMarkup(row_width=1)
doctors_btn.add(InlineKeyboardButton(text="Хирург", callback_data="surgeon"),
                InlineKeyboardButton(text="Окулист", callback_data="optometrist"),
                InlineKeyboardButton(text="Логопед", callback_data="speech_therapist"),
                InlineKeyboardButton(text="Назад🔙", callback_data="back_menu"))

#----------------------------------------------------------------------------------------------------------------

dates = InlineKeyboardMarkup(row_width=1)

start = datetime.datetime.strptime(f"{datetime.datetime.now().day}-12-2023", "%d-%m-%Y")
end = datetime.datetime.strptime(f"{datetime.datetime.now().day+6}-12-2023", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    data = date.strftime("%d-%m-%Y")
    dates.add(InlineKeyboardButton(text=data, callback_data=f"date_d{data}"))
            

#----------------------------------------------------------------------------------------------------------------

appointment = InlineKeyboardMarkup(row_width=1)
appointment_btn = InlineKeyboardButton(text='Записаться', callback_data='appointment')
back_btn = InlineKeyboardButton(text="Назад🔙", callback_data="back")
appointment.add(appointment_btn, back_btn)
#----------------------------------------------------------------------------------------------------------------

surgeon  = InlineKeyboardMarkup(row_width=1)
surgeon1 = InlineKeyboardButton(text='Беляев Матвей Петрович', callback_data='surgeon1_Беляев Матвей Петрович')
surgeon2 = InlineKeyboardButton(text='Соболев Борис Олегович', callback_data='surgeon2_Соболев Борис Олегович')
back_btn = InlineKeyboardButton(text="Назад🔙", callback_data="back")
surgeon.add(surgeon1, surgeon2, back_btn)

#----------------------------------------------------------------------------------------------------------------

optometrist  = InlineKeyboardMarkup(row_width=1)
optometrist1 = InlineKeyboardButton(text='Панова Ирина Игоревна', callback_data='optometrist1_Панова Ирина Игоревна')
optometrist2 = InlineKeyboardButton(text='Фадеева Анна Семёновна', callback_data='optometrist2_Фадеева Анна Семёновна')
back_btn = InlineKeyboardButton(text="Назад🔙", callback_data="back")
optometrist.add(optometrist1, optometrist2, back_btn)

#----------------------------------------------------------------------------------------------------------------

speech_therapist = InlineKeyboardMarkup(row_width=1)
speech_therapist1 = InlineKeyboardButton(text='Колесников Борис Ильич', callback_data='speech1_Колесников Борис Ильич')
speech_therapist2 = InlineKeyboardButton(text='Агафонов Даниил Арсениевич', callback_data='speech2_Агафонов Даниил Арсениевич')
back_btn = InlineKeyboardButton(text="Назад🔙", callback_data="back")
speech_therapist.add(speech_therapist1, speech_therapist2, back_btn)