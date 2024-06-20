# Модуди
import random
import time

# Переменные
defuse_play = True
menu_list = [1, 2, 3, 4, 5]
menu_space = True

# Система статистики
rang = 'Новичок'
exp = 0
lucky_defuse = 0
but_lucky_defuse = 0
total_defuse = 0


# Очистка экрана
def clear_screen():
    print('\n' * 1000)


# Основной цикл
def play():
    global defuse_play
    global menu_space

    # Использование системы статистики глобально
    global total_defuse
    global but_lucky_defuse
    global lucky_defuse
    global exp
    global rang

    while defuse_play == True:
        # Система статистики
        if total_defuse == 10:
            exp += 5
        if total_defuse == 20:
            exp += 5
        if total_defuse == 30:
            exp += 5
        if total_defuse == 40:
            exp += 5
        if total_defuse == 50:
            exp += 5
        if total_defuse == 60:
            exp += 5
        if total_defuse == 70:
            exp += 5
        if total_defuse == 80:
            exp += 5
        if total_defuse == 90:
            exp += 5
        if total_defuse == 100:
            exp += 5
        if exp == 25:
            rang = 'Опытный'
        if exp == 50:
            rang = 'Золотые руки(достиг максимум развития)'

        bomba = random.randint(1, 2)  # Рандомный выбор нужного провода
        print('\n\nКакой провод перерезать?')
        print('*' * 32)
        print('\n[1] Красный\n[2] Синий\n', '-' * 31, '\n[4] Меню\n[5] Выход')
        print('*' * 32)
        defuse = int(input('Сделай выбор: '))
        if defuse in menu_list:
            if defuse == 4:  # Обмен значениями
                clear_screen()
                menu()
                continue
            if defuse == bomba:
                clear_screen()
                print('Ты перерезал правельный провод!')
                total_defuse += 1
                lucky_defuse += 1
            if defuse != bomba:
                print('Ты проиграл!')
                but_lucky_defuse += 1
                total_defuse += 1

                if bomba == 1:
                    clear_screen()
                    print('Нужно было перерезать красный...')
                if bomba == 2:
                    clear_screen()
                    print('Нужно было перерезать синий...')
            if defuse == 3:  # Очистка экрана
                clear_screen()

            if defuse == 5:  # Завершение игры
                clear_screen()
                print('Игра заверешена, приятного дня!')
                time.sleep(1)
                defuse_play = False
                menu_space = False
        else:
            print('Введите номер действия!')
            continue


# Меню игры
def menu():
    global defuse_play
    global menu_space

    # Использование системы статистики глобально
    global total_defuse
    global but_lucky_defuse
    global lucky_defuse
    global exp
    global rang

    while menu_space == True:
        print('[Меню игры]')
        print('-' * 32)
        print('[1] Играть\n[2] Магазин\n[3] Статистика\n[4] Очистить экран\n[5] Выход')
        menu_input = int(input('Введите действие: '))
        if menu_input == 1:
            clear_screen()
            play()
        if menu_input == 3:
            clear_screen()
            print('[Статистика игрока]')
            print(
                '\n[Ранг: {0}]\n[Опыт: {1}]\n[Удачно разминирование бомбы: {2}]\n[Не удачно разминирование бомбы: {3}]\n[Всего разминирований: {4}]'.format(
                    rang, exp, lucky_defuse, but_lucky_defuse, total_defuse))
            print('\n')

        if menu_input == 4:
            clear_screen()
        if menu_input == 5:
            clear_screen()
            print('Игра заверешена, приятного дня!')
            time.sleep(1)
            defuse_play = False
            menu_space = False


clear_screen()  # Очистка экрана
play()  # Запуск игрового цикла