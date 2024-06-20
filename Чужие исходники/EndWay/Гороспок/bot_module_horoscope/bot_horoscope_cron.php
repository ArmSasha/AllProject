<?php
$back_dir = explode('/', __DIR__);;
array_pop($back_dir);
$back_dir = implode('/', $back_dir);
include_once $back_dir.'/__config.php';
include_once $back_dir.'/bot_config.php';
include_once __DIR__.'/bot_horoscope_function.php';
if (!file_exists(__DIR__.'/bot_horoscope_cron.txt')) {file_put_contents(__DIR__.'/bot_horoscope_cron.txt', 'ok');}


echo '</br> тип версии кода 01</br></br></br>';
$now = date('H:i:s', strtotime('now'));
echo 'Старт '.$now."</br></br>"; 


$hour = date('g', strtotime('now')); 
if ($hour >= 0) {// парсим новые данне после 5 утра
    $types = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'];
    $names = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'];

    //if (!is_dir(__DIR__.'/image/'.$tomorrow)) {mkdir(__DIR__.'/image/'.$tomorrow, 0777, true);}
    $today = date('Y-m-d', strtotime('now'));  
    $load = mysqli_fetch_assoc(mysqli_query($CONNECT, "SELECT * FROM `module_horoscope` WHERE `date` = '$today'"));
    if (!$load) {
        mysqli_query($CONNECT, "INSERT INTO `module_horoscope` (`date`) VALUES ('$today')");
    }    
    foreach($types as $key => $value) {
        echo '</br>=========================================</br>'.$names[$key];
        if (!$load[$value]) {
            $url[$key] = 'https://horo.mail.ru/prediction/'.$value.'/today/';
            echo '</br>'.$url[$key].'</br>';
            $result[$key] = parsing($url[$key]);
            if ($result[$key] AND mb_stripos($result[$key], 'article__text') !== false) {
                $result[$key] = horoscope_text($result[$key]);
                horoscope_image($result[$key], $value, $today);
                mysqli_query($CONNECT, "UPDATE `module_horoscope` SET `$value` = '$result[$key]' WHERE `date` = '$today'");
                echo $result[$key];
            } else if ($hour >= 15) {
                $error .= "\nНе смогли спарсить ".$names[$key];
            }    
        } else {        
            echo '</br>Было';
        }
    }
    unset($load);
    //---------------------завтра
    $tomorrow = date('Y-m-d', strtotime('+1 day')); 
    $load = mysqli_fetch_assoc(mysqli_query($CONNECT, "SELECT * FROM `module_horoscope` WHERE `date` = '$tomorrow'"));
    if (!$load) {
        mysqli_query($CONNECT, "INSERT INTO `module_horoscope` (`date`) VALUES ('$tomorrow')");
    }    
    foreach($types as $key => $value) {
        echo '</br>=========================================</br>'.$names[$key];
        if (!$load[$value]) {
            //$url[$key] = 'https://horo.mail.ru/prediction/'.$value.'/today/';
            $url[$key] = 'https://horo.mail.ru/prediction/'.$value.'/tomorrow/';
            echo '</br>'.$url[$key].'</br>';
            $result[$key] = parsing($url[$key]);
            if ($result[$key] AND mb_stripos($result[$key], 'article__text') !== false) {
                $result[$key] = horoscope_text($result[$key]);
                horoscope_image($result[$key], $value, $tomorrow);
                mysqli_query($CONNECT, "UPDATE `module_horoscope` SET `$value` = '$result[$key]' WHERE `date` = '$tomorrow'");
                echo $result[$key];
            } else if ($hour >= 15) {
                $error .= "\nНе смогли спарсить ".$names[$key];
            }    
        } else {        
            echo '</br>Было';
        }
    }
    
} else {
    echo 'парсим новые данне после 5 утра, щас еще '.$hour;
}

if ($error) {
    foreach($admin_chat_id as $value) {
        $option = ["chat_id" => $value, "text" => "‼️ КРИТИЧЕСКАЯ ОШИБКА ‼️".$error];
        telegram("sendMessage", $option);
    }
}





$now = date('Y-m-d H:i:s', strtotime('now')); 
echo '</br></br></br>Финиш '.$now; 
?>