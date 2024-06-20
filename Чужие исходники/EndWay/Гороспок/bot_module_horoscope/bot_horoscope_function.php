<?php

// парсер страницы
function parsing($url) {
    $arr = [
        CURLOPT_URL => $url ,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_SSL_VERIFYHOST => false,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_TIMEOUT => 20, 
        CURLOPT_CONNECTTIMEOUT => 10, 
        CURLOPT_MAXREDIRS => 10, 
        CURLOPT_FAILONERROR => true, 
        CURLOPT_HEADER => 0,
        CURLOPT_ENCODING => "",
        CURLOPT_AUTOREFERER => true,
        CURLOPT_REFERER => 'http://www.google.com/',
        CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    ];  
    $curl = curl_init();
    curl_setopt_array($curl, $arr);
    $answer = curl_exec($curl);	
    curl_close($curl);
    return $answer;
}

// обрезатель лишнего
function pruning($string, $start, $end, $tags = false, $start_delete = false) {//строка, начало, конец, удалить все теги?, удалить из строки часть кода $start
    $num1 = mb_strpos($string, $start);
    if ($num1 !== false) {
        if ($start_delete) {$num1 = $num1 + mb_strlen($start);}
        $num2 = mb_substr($string, $num1);
        $result = trim(mb_substr($num2, 0, mb_strpos($num2, $end)));
        if ($tags) {$result = trim(strip_tags($result));} 
    }
    return $result;
} 

// обработка текста
function horoscope_text($text) {    
    $text = '<div class="'.pruning($text, "article__text", "</p>");//покороче
    //$text = '<div class="'.pruning($text, "article__text", "</div>");
    $text = str_replace('</p>', " **** ", $text); 
    $text = str_replace('&nbsp;', ' ', $text); 
    $text = str_replace('&ndash;', '-', $text); 
    $text = trim(strip_tags($text, "<br>"));
    $text = preg_replace("/^(\<(\/)?br\>|\n|\s)+|(\<(\/)?br\>|\n|\s|\*)+$|/", '', $text);
    $array = preg_split("/(\s)+/", $text, 0, PREG_SPLIT_NO_EMPTY);
    $count = count($array) - 1;
    foreach($array as $key => $value) {  
        if (iconv_strlen($str_new." ".$value, 'UTF-8') >= 41 OR $value == '****') {  // iconv_strlen - длина строки с поерделенной кодировкой , а то cron с    mb_substr тупил
            //if (!file_exists(__DIR__.'/__1_.txt')) {file_put_contents(__DIR__.'/__1_.txt', iconv_strlen($str_new." ".$value, 'UTF-8')." / ".$str_new." / ".$value);}       
            $str_all .= $str_new."</br>"; 
            unset($str_new); 
            $str_new .= $value; 
        } else {
            if ($str_new) {$str_new .= " ";}
            $str_new .= $value; 
        }  
        if ($count == $key) {
            $str_all .= $str_new;
        }
    }
    $str_all = str_replace('****', "</br></br>", $str_all); 
    $str_all = preg_replace("/((\<\/br\>){2,})/", '</br></br>', $str_all);
    return $str_all;
}


function horoscope_image($text, $znac, $date) {//созадение картинки  
    $file_new = __DIR__.'/image/'.$date.'_'.$znac.'.jpg';
    if (file_exists($file_new)) {
        unlink($file_new);
    }

    //  изображение
    $image_path = __DIR__."/image_new/bg.jpg";
    $img = ImageCreateFromJPEG($image_path);
    $size = getimagesize($image_path); //Узнаем размер изображения
    $w = (int)$size[0]; // ширина
    $h = (int)$size[1]; // высота

    
    // ========= ГЛАВНЫЙ ТЕКСТ =========
    // ========= ГЛАВНЫЙ ТЕКСТ =========  
    $color = imageColorAllocate($img, 255, 255, 255);// определяем цвет, в RGB 
    $font = __DIR__.'/image_new/arial.ttf';// шрифт
    $font_size = 32;// размер шрифта
    //обводка
    $shadow = imageColorAllocate($img, 0, 0, 0); // цвет обводки

    $array = preg_split("/(\<\/br\>)+/", $text, 0, PREG_SPLIT_NO_EMPTY);
    $text_array = array_diff(explode('</br>', $text), ['']);
    $row_count = count($text_array);
    $row_start = (-1) * floor($row_count / 2);
    foreach($text_array as $value_text) {      
        $row_start++;  
        $value_text = urldecode($value_text);
        $box = imagettfbbox($font_size, 0, $font, $value_text);
        $x = ($w/2)-($box[2]-$box[0])/2; //по оси x
        $y = ($h/2)-($box[3]-$box[5])/2 + (($font_size * 1.9) * $row_start) + 100; //по оси y
        //Обводка 
        for ($i = 1; $i <= 2; $i++) {
            imagettftext($img, $font_size, 0, $x+$i, $y, $shadow, $font, $value_text);
            imagettftext($img, $font_size, 0, $x-$i, $y, $shadow, $font, $value_text);
            imagettftext($img, $font_size, 0, $x, $y+$i, $shadow, $font, $value_text);
            imagettftext($img, $font_size, 0, $x, $y-$i, $shadow, $font, $value_text);        
        }
        //главный текст
        imagettftext($img, $font_size, 0, $x, $y, $color, $font, $value_text); //картинка , размер шрифта, угол поворота, смещение по горизонтали, смещение по вертикали
    }

    // ========= дата =========
    // ========= дата =========  
    $array_date = explode('-', $date);
    if ($array_date[1] == '01') {$mount = 'Января';}
    else if ($array_date[1] == '02') {$mount = 'Февраля';}
    else if ($array_date[1] == '03') {$mount = 'Марта';}
    else if ($array_date[1] == '04') {$mount = 'Апреля';}
    else if ($array_date[1] == '05') {$mount = 'Мая';}
    else if ($array_date[1] == '06') {$mount = 'Июня';}
    else if ($array_date[1] == '07') {$mount = 'Июля';}
    else if ($array_date[1] == '08') {$mount = 'Августа';}
    else if ($array_date[1] == '09') {$mount = 'Сентября';}
    else if ($array_date[1] == '10') {$mount = 'Октября';}
    else if ($array_date[1] == '11') {$mount = 'Ноября';}
    else if ($array_date[1] == '12') {$mount = 'Декабря';}
    //день    
    $font = __DIR__.'/image_new/arial_b.ttf';// шрифт
    $font_size = 140;// размер шрифта
    if (mb_substr($array_date[2], 0, 1) == 0) {$array_date[2] = mb_substr($array_date[2], 1);}
    imagettftext($img, $font_size, 0, 20, 180, $color, $font, $array_date[2] ); 
    $box = imagettfbbox($font_size, 0, $font, $array_date[2]);
    //месяц
    $font_size = 60;// размер шрифта
    $x = ($box[2]-$box[0]) + 70; //по оси x
    if (mb_substr($array_date[2], 0, 1) == 0) {$array_date[2] = mb_substr($array_date[2], 1);}
    imagettftext($img, $font_size, 0, $x, 180, $color, $font, $mount ); 

    // ========= Подпись канала ========= 
    // ========= Подпись канала ========= 
    global $bot_name;
    $font = __DIR__.'/image_new/arial.ttf';// шрифт
    $text = "@".$bot_name;
    $font_size = 20;// размер шрифта
    $color = imageColorAllocate($img, 150, 150, 150);// определяем цвет, в RGB 
    $box = imagettfbbox($font_size, 0, $font, $text);
    $x = ($w/2)-($box[2]-$box[0])/2; //по оси x
    $y = $h - 30; //по оси y
    imagettftext($img, $font_size, 0, $x, $y, $color, $font, $text); //картинка , размер шрифта, угол поворота, смещение по горизонтали, смещение по вертикали

    // ========= Сохраняем ========= 
    // ========= Сохраняем ========= 

    imagejpeg($img, $file_new, 100);

    // ========= Добавляем знак зодиака картинку ========= 
    // ========= Добавляем знак зодиака картинку =========   

    // ветермарк
    $wtrmrk_file = __DIR__.'/image_new/'.$znac.'.png';
    $watermark = imagecreatefrompng($wtrmrk_file);
    imagealphablending($watermark, false);
    imagesavealpha($watermark, true);
    $watermark_width = imagesx($watermark);
    $watermark_height = imagesy($watermark);
    //узнаем размер JPG
    $img = imagecreatefromjpeg($file_new);
    $img_w = imagesx($img);
    $img_h = imagesy($img);
	//Координаты
    $dst_x = $img_w - $watermark_width - 25;
    $dst_y = 15;

    imagecopyresampled($img, $watermark, $dst_x, $dst_y, 0, 0, $watermark_width, $watermark_height, $watermark_width, $watermark_height);
	//$finish_image = str_replace('.jpg', '_result.jpg', $file_new); 	
    imagejpeg($img, $file_new, 100);//сохраняем туда же где взяли
    imagedestroy($img);
    imagedestroy($watermark);
}
?>