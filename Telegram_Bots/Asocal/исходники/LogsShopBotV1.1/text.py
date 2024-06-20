"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

А теперь немного про этот файлик, тут находятся все сообщения которые отправляет бот пользователю, если вы
что-то поменяли в этом файле и сообщение перестало приходить -  вы неправильно настроили форматирование текста,
например: Чтобы текст был жирным нужно указывать его так: *Привет*, Но если вам нужен текст который можно скопировать
то указывайте его вот так: *Ваш ID:* `{userid}` - Что это такое в фигурных скобках? Все просто, это переменные.
Они используются для того чтобы заменить этот текст на нужный параметр, например: вот это *У вас {balance} ₽.*
при отправке будет выглядеть так: У вас 21.00 ₽. и кстати, в тексте нельзя указывать новые переменные, если в
конкретном тексте есть конкретные переменные, вы имеете право просто перенести их только в этом тексте не
перенося в другие сообщения. Если что, весь текст должен быть в тройных ковычках иначе бот не стартанет!
"""

START_TEXT = """
➖➖➖➖➖
*{userfirstname} Привет!*
*Хочешь приобрести логи? Тебе к нам!
    - Лучшие цены
    - Свежайшие заливы
    - Большое количество товара
    - Бот который обслужит вас по высшему классу
*
➖➖➖➖➖
"""

LOGS_MENU = """
➖➖➖➖➖
*{userfirstname} А вот и логи!*
*Ваш ID:* `{userid}`
*Ваш баланс:* `{balance}` *₽*
*На данный момент у нас такая информация:*
{logsinformation}
*Выберите тип логов.*
➖➖➖➖➖
"""

NO_LOG_FILE_TEXT = """
➖➖➖➖➖
*🤬Вы отправили не лог!*
➖➖➖➖➖
"""

#Эта переменная которая указывается в LOGS_MENU, тут вы можете настроить отображение логов при покупке.
logsinformation = "*{category}* `{amount}` *₽ В наличии:* `{count}` *шт.*"

NO_SPAM_TEXT = """
➖➖➖➖➖
*🤬Пожалуйста, прекратите спамить!*
➖➖➖➖➖
"""

NO_CATEGORY_TEXT = """
➖➖➖➖➖
*❌Данной категории не существует
Нажмите на кнопку покупки логов снова.*
➖➖➖➖➖
"""

BALANCE_ADD_TEXT = """
➖➖➖➖➖
*Введите сумму пополнения: (без копеек)*
➖➖➖➖➖
"""

BALANCE_DEL_TEXT = """
➖➖➖➖➖
*Введите сумму удаления: (без копеек)*
➖➖➖➖➖
"""

ADMIN_TEXT = """
➖➖➖➖➖
*Нагрузка процессора: {cpu}%
Нагрузка оперативной памяти: {ram}%
Внизу находятся кнопки для выбора действий.*
➖➖➖➖➖
"""

CATEGORY_CHOICE_DELETE_TEXT = """
➖➖➖➖➖
*Выберите категорию для удаления.*
➖➖➖➖➖
"""

LOG_ADDED_TEXT = """
➖➖➖➖➖
✅*Лог добавлен!*
➖➖➖➖➖
"""

SET_CATEGORY_TEXT = """
➖➖➖➖➖
*Выберите новую категорию для загрузки.*
➖➖➖➖➖
"""

LOG_ADDED_ERROR_TEXT = """
➖➖➖➖➖
❌*Лог недобавлен, проверьте место загрузки логов в настройках.*
➖➖➖➖➖
"""

CATEGORY_NOT_DELETE_TEXT = """
➖➖➖➖➖
❌*Удалять нечего.*
➖➖➖➖➖
"""

NO_LOGS_TEXT = """
➖➖➖➖➖
❌*Логов этой категории пока что нет в наличии.*
➖➖➖➖➖
"""


CATEGORY_NOT_SET_TEXT = """
➖➖➖➖➖
❌*Нету категории которую можно использовать для загрузки*
➖➖➖➖➖
"""

LOGS_COUNT_TEXT = """
➖➖➖➖➖
*Категория: *`{category}`
*В наличии: *`{count}` *шт.*
*Цена за шт: *`{amount}` *₽*
*Укажите количество логов для покупки:*
➖➖➖➖➖
"""

LOGS_CATEGORY_AMOUNT_TEXT = """
➖➖➖➖➖
*Введите цену за 1 лог: (без копеек)*
➖➖➖➖➖
"""


NO_MONEY_TEXT = """
➖➖➖➖➖
❌*Вам не хватает:* `{need}` *₽ Для покупки.*
➖➖➖➖➖
"""

SUCCESS_PURCHASE_TEXT = """
➖➖➖➖➖
✅*Вы успешно купили* `{count}` *шт.
С вашего баланса списано:* `{spend}` *₽*
➖➖➖➖➖
"""

RULES_TEXT = """
➖➖➖➖➖
*{userfirstname} Правила!
1. Не курить
2. Не пить...*
➖➖➖➖➖
"""

NO_LOGS_COUNT_TEXT = """
➖➖➖➖➖
*❌На данный момент этих логов нет в продаже.*
➖➖➖➖➖
"""

ERROR_LOGS_COUNT_TEXT = """
➖➖➖➖➖
*❌Вы указали не правильное количество при покупке логов.*
➖➖➖➖➖
"""

PAYMENT_TEXT = """
➖➖➖➖➖
*{userfirstname} Оплата.
Для пополнения баланса вы можете 
написать нашему администратору: 
@example
Или же воспользоваться автоматической оплатой ниже.*
➖➖➖➖➖
"""

ERROR_PAYMENT_TEXT = """
➖➖➖➖➖
*❌На данный момент эта система пополнения не доступна.*
➖➖➖➖➖
"""

NO_PAYMENT_TEXT = """
➖➖➖➖➖
*❌Платеж не найден.*
➖➖➖➖➖
"""

PAYMENT_COUNT_TEXT = """
➖➖➖➖➖
*Введите сумму для пополнения (без копеек)
Минимальная сумма пополнения:* `{minimal}` *₽*
➖➖➖➖➖
"""

CATEGORY_CREATED_TEXT = """
➖➖➖➖➖
*✅Данная категория успешно создана*
➖➖➖➖➖
"""

CATEGORY_DELETED_TEXT = """
➖➖➖➖➖
*✅Данная категория успешно удалена*
➖➖➖➖➖
"""

CREATE_CATEGORY_TEXT = """
➖➖➖➖➖
*Дайте название новой категории:*
➖➖➖➖➖
"""

SETUP_CATEGORY_TEXT = """
➖➖➖➖➖
*✅Данная категория выбрана для загрузки*
➖➖➖➖➖
"""

SETTINGS_TEXT = """
➖➖➖➖➖
*Категория для загрузки:* `{category}`
➖➖➖➖➖
"""

ADD_PAYMENT_TEXT = """
➖➖➖➖➖
*✅Платеж найден, на ваш счёт начислено:* `{added}` *₽*
➖➖➖➖➖
"""

UPLOAD_CATEGORY_ERROR_TEXT = """
➖➖➖➖➖
*❌Мы не можем добавить в эту категорию логи по причине ее отсутствия.*
➖➖➖➖➖
"""

CHANNEL_TEXT = """
➖➖➖➖➖
*❌Перед тем как пользоваться ботом вам следует вступить в наш канал: @example.*
➖➖➖➖➖
"""

PROFILE_CHECK_TEXT = """
➖➖➖➖➖
*ID:* `{userid}`
*Username:* `{username}`
*Баланс:* `{balance}` *₽*
➖➖➖➖➖
"""

GIVE_PROFILE_CHECK_TEXT = """
➖➖➖➖➖
*Введите id для проверки пользователя:*
➖➖➖➖➖
"""

NO_PROFILE_CHECK_TEXT = """
➖➖➖➖➖
*❌Такого аккаунта не существует или же вы не правильно указали пользователя, пример: 432433*
➖➖➖➖➖
"""

OLD_PAYMENT_TEXT = """
➖➖➖➖➖
*❌Этот счет уже задействован.*
➖➖➖➖➖
"""

MINIMAL_AMOUNT_ERROR_TEXT = """
➖➖➖➖➖
*❌Данная сумма меньше минимальной.
Минимальная сумма:* `{minimal}` *₽*
➖➖➖➖➖
"""

BALANCE_ADDED_CHECK_TEXT = """
➖➖➖➖➖
*✅Баланс успешно добален пользователю* `{username}`
*Баланс:* `{balance}` *₽*
➖➖➖➖➖
"""

NEW_PAYMENT_TEXT = """
➖➖➖➖➖
*✅Оплата прошла успешно!
Добавлено на баланс:* `{balance}` *₽*
➖➖➖➖➖
"""

BALANCE_DELETED_CHECK_TEXT = """
➖➖➖➖➖
*✅Баланс успешно удален у пользователя {username}
Баланс:* `{balance}` *₽*
➖➖➖➖➖
"""

SENDS_END_TEXT = """
➖➖➖➖➖
*✅Рассылка успешно закончена.*
➖➖➖➖➖
"""

BALANCE_CLEAR_CHECK_TEXT = """
➖➖➖➖➖
*✅Баланс успешно очищен.*
➖➖➖➖➖
"""

SENDS_TEXT = """
➖➖➖➖➖
*Введите текст для рассылки:*
➖➖➖➖➖
"""

LOLZ_PAY_TEXT = """
➖➖➖➖➖
*Для оплаты с помощью Lolz вам нужно перейти по ссылке ниже и отправить ровно* `{amount}` *₽*
➖➖➖➖➖
"""

QIWI_PAY_TEXT = """
➖➖➖➖➖
*Для оплаты по Qiwi вам нужно перейти по ссылке ниже оплатить счёт.*
*Сумма:* `{amount}` *₽*
*Счёт действителен 60 минут.*
➖➖➖➖➖
"""

CRYSTAL_PAY_TEXT = """
➖➖➖➖➖
*Для оплаты по Crystal Pay вам нужно перейти по ссылке ниже оплатить счёт.*
*Сумма:* `{amount}` *₽*
*Счёт действителен 60 минут.*
➖➖➖➖➖
"""

LAVA_PAY_TEXT = """
➖➖➖➖➖
*Для оплаты по Lava вам нужно перейти по ссылке ниже оплатить счёт.*
*Сумма:* `{amount}` *₽*
*Счёт действителен 60 минут.*
➖➖➖➖➖
"""

ERROR_AMOUNT_TEXT = """
➖➖➖➖➖
*❌Не правильная сумма пополнения.*
➖➖➖➖➖
"""

ERROR_AMOUNT_CATEGORY_TEXT = """
➖➖➖➖➖
*❌Не правильная сумма для лога.*
➖➖➖➖➖
"""

ERROR_AMOUNT_LOGS_TEXT = """
➖➖➖➖➖
*❌Вы указали не правильное количество для покупки логов.*
➖➖➖➖➖
"""