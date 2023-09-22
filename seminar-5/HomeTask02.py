# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os


def pars_url(urli):
    file_name = os.path.basename(urli)  # имя файла
    file_path = os.path.dirname(urli)  # путь
    file_name, file_extension = os.path.splitext(file_name)  # разбираем до расширения

    return file_path, file_name, file_extension


url = '/upload/pic/picture.jpg'
tiple_url = pars_url(url)
print(tiple_url)
