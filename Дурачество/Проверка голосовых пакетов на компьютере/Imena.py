#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyttsx3
tts = pyttsx3.init() # Инициализировать голосовой движок.
voices = tts.getProperty('voices') # Получить список голосов
# Перебрать установленные голоса и вывести имя каждого
for voice in voices:
    print(voice.name)
    
    # Microsoft
    # Anna - English(UnitedStates)
    # Aleksandr  # Хороший
    # Anna
    # Elena
    # Irina  # Хороший