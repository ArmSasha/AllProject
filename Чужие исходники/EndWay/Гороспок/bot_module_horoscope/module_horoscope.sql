-- phpMyAdmin SQL Dump
-- version 3.5.8.1
-- http://www.phpmyadmin.net
--
-- Хост: mysql99.1gb.ru
-- Время создания: Май 14 2022 г., 00:39
-- Версия сервера: 5.7.13-6-log
-- Версия PHP: 5.3.29

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `gb_dv_test3`
--

-- --------------------------------------------------------

--
-- Структура таблицы `module_horoscope`
--

CREATE TABLE IF NOT EXISTS `module_horoscope` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `aries` text NOT NULL,
  `taurus` text NOT NULL,
  `gemini` text NOT NULL,
  `cancer` text NOT NULL,
  `leo` text NOT NULL,
  `virgo` text NOT NULL,
  `libra` text NOT NULL,
  `scorpio` text NOT NULL,
  `sagittarius` text NOT NULL,
  `capricorn` text NOT NULL,
  `aquarius` text NOT NULL,
  `pisces` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=cp1251 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
