<?php

if (!$dop_but['back']) { $dop_but['back'] = "⬅️ Назад";}

$back_dir = explode('/', __DIR__);
array_pop($back_dir);
$back_dir = implode('/', $back_dir);


$types = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'];
$names = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'];
$smile = ['♈️', '♉️', '♊️', '♋️', '♌️', '♍️', '♎️', '♏️', '♐️', '♑️', '♒️', '♓️'];

if (in_array('horoscope-go', $action)) {
    file_put_contents(__DIR__.'/__601.txt', $text);
    if (!$arr['horoscope-go']["text"]) {$arr['horoscope-go']["text"] = "Выбери знак для которого хочешь получить предсказание 👇🏼";}
    
    for ($i = 0; $i <= 11; $i++) {
        $ii = floor($i/3);
        $arr['horoscope-go']["keyboard"][$ii][] = ["text" => $smile[$i]." ".$names[$i], "callback_data" => "horoscope_horoscope-znac_".$i];    
    }
    file_put_contents(__DIR__.'/__602.txt', $text);
}

if (in_array('horoscope-znac', $action)) {
    $date = date('Y-m-d', strtotime('now')); 
    $load = mysqli_fetch_assoc(mysqli_query($CONNECT, "SELECT * FROM `module_horoscope` WHERE `date` = '$date'")); 
    $arr['horoscope-znac']["photo"] = $website."/bot_module_horoscope/image/".$date."_".$types[$param].".jpg";
    $arr['horoscope-znac']["text"] = $smile[$param]." <b>".$names[$param]."</b> на ".preg_replace("/(\d+)-(\d+)-(\d+)/", '$3.$2.$1', $date)."\n\n<i>Ежедневный гороскоп в боте: @".$bot_name."</i>";
    $arr['horoscope-znac']["keyboard"][] = [["text" => $dop_but['back'], "callback_data" => "horoscope_horoscope-go"]];
}

if (!$arr['horoscope-menu']["text"]) {$arr['horoscope-menu']["text"] = "У нас ты сможешь получать актуальный астрологический прогноз каждый день! 🔮";}
$arr['horoscope-menu']["menu"] = [["🔮 Узнать гороскоп"]];
?>