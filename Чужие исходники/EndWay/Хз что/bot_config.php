<?php

$bot_name = 'Goroskop22_bot';//имя бота , имя это его ссылка @name_bot только без собаки спереди
$telegram_bot_token = '5393007556:AAESwE9fal4ZC586rYCNdGIX5nVIZECoZwc'; // токен бота

$admin_pass = 'fg8h2nBdM91hF1t4c8';  // пароль для ссылки для переключение на админа // обязательно должны быть буквы // https://t.me/Goroskop22_bot?start=fg8h2nBdM91hF1t4c8

$channel_check = '';// ID проверяемого канала // если канала нет, то нет Тарифа 3 для работников, и нет проверки

$qiwi_token	= ''; // токен, получить токен можно тут https://qiwi.com/api поставить 2 и 4 галочку
$qiwi_number = '';// номер кошелька - сотовый


include_once 'bot_function.php';

// дополнительные сообщения которые есть только у этого юзера
$arr_subscribed = "";
$arr_plus['user-start']["text"] = "Привет мой друг 👋🏼\nУ нас ты сможешь получать актуальный астрологический прогноз каждый день! 🔮";
$arr_plus['user-start']["photo"] = "start_horoscope_001.jpg";
$arr_plus['user-start']["keyboard"] = [[["text" => "🔮 Узнать гороскоп", "callback_data" => "action_2401"]]];


?>