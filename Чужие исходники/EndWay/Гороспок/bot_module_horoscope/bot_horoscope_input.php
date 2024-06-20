<?php

$back_dir = explode('/', __DIR__);
array_pop($back_dir);
$back_dir = implode('/', $back_dir);

if (in_array($chat_id, $worker) OR in_array($chat_id, $admin_chat_id)) { // админ и работники
    if ($result["message"]) {
        $go = $us['page'];
    } else if ($result["callback_query"]) {        
        $go = explode('_', $button)[1];
        $param = explode('_', $button)[2];
        $param_2 = explode('_', $button)[3]; 
    }
} else { // пользователи
    $no_delete_user = true;
    $no_delete_bot = true;
    $no_old = true;
    $no_all_delete = true;
    if ($result["message"]) {     
        if ($text == "🔮 Узнать гороскоп") {        			
            $go = 'horoscope-go';	
        } else {// при вводе текста не во время
            $action[] = $us['page'];
        } 
    } else if ($result["callback_query"]) {
        $go = explode('_', $button)[1];
        $param = explode('_', $button)[2];  
        if ($go == 'horoscope-go' AND $param == 'start') {
            $channels_error = getChatMember($chat_id);
            if ($channels_error) {// обязательная проверка при нажатии на кнопку ПОДПИСАЛСЯ -  Если вошел не во все каналы
                $action = [2402, 2401];
                unset($go);
            } else {
                $action = ['horoscope-menu'];
                /* $keyboard2 = [["🔮 Узнать гороскоп"]];
                $option2 = ["chat_id" => $chat_id, "text" => "У нас ты сможешь получать актуальный астрологический прогноз каждый день! 🔮", "menu" => $keyboard2];
                telegram("sendMessage", $option2); */				
                mysqli_query($CONNECT, "UPDATE `bot_user_subscription` SET `subscription_now` = '1', `subscription_start` = '1' WHERE `chat_id` = '$chat_id'");
            }
            mysqli_query($CONNECT, "INSERT INTO `bot_user_history` (`chat_id`, `message_id`, `types`, `old`) VALUES ('$chat_id', '$message_id', 'user_message', '1')");
        } else if ($go == 'horoscope-znac') {
            $channels_error = getChatMember($chat_id);
            if ($channels_error) {
                $go = 2401;
            }
        }
    }
}
?>