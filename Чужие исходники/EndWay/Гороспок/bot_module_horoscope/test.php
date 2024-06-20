<?php
$back_dir = explode('/', __DIR__);;
array_pop($back_dir);
$back_dir = implode('/', $back_dir);
include_once $back_dir.'/__config.php';
include_once $back_dir.'/bot_config.php';
include_once __DIR__.'/bot_horoscope_function.php';
$key = 1;
$date = date('Y-m-d', strtotime('+1 day')); 
$result[$key] = mysqli_fetch_assoc(mysqli_query($CONNECT, "SELECT * FROM `module_horoscope` WHERE `date` = '$date'"))['aries']; 
echo $date."</br>".$result[$key]."</br>".$date."</br></br>";

horoscope_image($result[$key], 'aries', $date);

echo '<img src="image/'.$date.'_aries.jpg" alt="">';

?>
