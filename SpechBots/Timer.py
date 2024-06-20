#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

while True:
    i = 0 # Секунды
    ii = 0 # Минуты
    iii = 0 # Часы
    time_user = int(input("Введите кол-во секунд:"))
    comment = str(input("Введите коментарий:"))
    for q in range(time_user):
        time.sleep(1)
        i += 1
        print("Прошло секунд:", i)
        if i % 60 == 0:
            ii += 1
            print("Прошло минут", ii)
        if i % 3600 == 0:
            iii += 1
            print("Прошло минут", iii)

    print("Время вышло!")
    print("Ваш коментарий:", comment)







