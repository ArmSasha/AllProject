from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

# Предположим, что у вас уже есть список пользователей из базы данных
users = [
    {'id': 1, 'name': 'Пользователь 1', 'age': 20},
    {'id': 2, 'name': 'Пользователь 2', 'age': 25},
    {'id': 3, 'name': 'Пользователь 3', 'age': 30},
    {'id': 4, 'name': 'Пользователь 4', 'age': 35},
    # Добавьте остальных пользователей из базы данных
]

# Глобальные переменные для хранения текущего диапазона поиска
min_age = 0
max_age = 100

# Обработчик команды /start
def start(update, context):
    global min_age, max_age
    keyboard = [
        [InlineKeyboardButton("Возраст", callback_data='age')],
        [InlineKeyboardButton("Плюс", callback_data='plus')],
        [InlineKeyboardButton("Минус", callback_data='minus')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)

# Обработчик нажатия на инлайн кнопку
def button(update, context):
    global min_age, max_age
    query = update.callback_query
    selected_action = query.data

    if selected_action == 'age':
        keyboard = [
            [InlineKeyboardButton("Плюс", callback_data='plus')],
            [InlineKeyboardButton("Минус", callback_data='minus')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=f"Текущий диапазон возраста: {min_age}-{max_age}\nВыберите действие:", reply_markup=reply_markup)
    elif selected_action == 'plus':
        min_age += 5
        max_age += 5
        query.edit_message_text(text=f"Текущий диапазон возраста: {min_age}-{max_age}\nВыберите действие:")
    elif selected_action == 'minus':
        min_age -= 5
        max_age -= 5
        query.edit_message_text(text=f"Текущий диапазон возраста: {min_age}-{max_age}\nВыберите действие:")

    filtered_users = [user for user in users if min_age <= user['age'] <= max_age]

    if filtered_users:
        result = '\n'.join([f"Имя: {user['name']}, Возраст: {user['age']}" for user in filtered_users])
    else:
        result = 'Пользователи с выбранным возрастом не найдены.'

    context.bot.send_message(chat_id=query.message.chat_id, text=result)

# Точка входа программы
def main():
    # Создаем экземпляр Updater и передаем ему токен вашего бота
    updater = Updater('5760615918:AAHygCHZdAnKceDwVIBzhT_L-INrrbK6HbI', use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик нажатия на инлайн кнопку
    dp.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
