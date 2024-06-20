#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date, time

import pyttsx3, time

tts = pyttsx3.init()

tts.setProperty('voice', 'ru')  # Наш голос по умолчанию

tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)

tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)

def set_voice(): # Найти и выбрать нужный голос по имени

    voices = tts.getProperty('voices')

    for voice in voices:

        if voice.name == 'Aleksandr':

           tts.setProperty('voice', voice.id)

        else:

            pass

def say_time(msg): # Функция, которая будет называть время в заданном формате

    set_voice() # Настроить голос

    tts.say(msg)

    tts.runAndWait() # Воспроизвести очередь реплик и дождаться окончания речи

while True:

    time_checker = datetime.now() # Получаем текущее время с помощью datetime

    if time_checker.second == 0:

        say_time('{h} {m}'.format(h=time_checker.hour, m=time_checker.minute))

        time.sleep(10)

    else:

        pass