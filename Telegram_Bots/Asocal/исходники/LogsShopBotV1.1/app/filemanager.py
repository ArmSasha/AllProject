"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Файл для работы с файлами :D

"""

import shutil
import os
from random import randint


def create_archive(files):
    """Создаем архив с заказом."""

    name_dir = rf"cache{randint(0,9999999999999999999999999)}"
    os.mkdir(rf"cache/{name_dir}")

    for file in files:
        shutil.move(r'logs/' + file, fr"cache/{name_dir}")

    shutil.make_archive(fr"cache_zip/Logs{len(files)}", 'zip', rf"cache/{name_dir}")
    return (fr"Logs{len(files)}.zip", name_dir)


def delete_files(cache1, cache2):
    try:
        os.remove(cache1)
        shutil.rmtree(cache2)
    except Exception as e:
        print(e)
        pass