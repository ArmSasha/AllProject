# Autoshop
Автор: [t.me/djimbox](https://t.me/djimbox)

Модификация: [t.me/rantuhin](https://t.me/djimbox)

## Оригинальная страница:
https://lolz.guru/threads/1888814/



## Отличия от оригинала
* Оплата через [CrystalPay](crystalpay.ru/)
* Список администрации в `settings.ini` можно указывать через пробел
* Возможность включать и выключать платёжки

## Конфигурация
Файл ```settings.ini```

Секция `crystal` - регистрация кассы в `@CrystalPAY_bot` боте

Секция `payments` - enabled=включенные платёжки через запятую (`qiwi` и `crystal`)
```ini
# - *- coding: utf- 8 - *-
[settings]
token=Токен вашего бота
admin_id=Список администрации, через запятую
[crystal]
nickname=Никнейм кассы в CrystalPay
secret_1=Секретный ключ кассы
[payments]
enabled=qiwi, crystal
```
