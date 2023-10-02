# 1. Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# 2. Для дочерних объектов указывайте родительскую директорию.
# 3. Для каждого объекта укажите файл это или директория.
# 4. Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий. 3. Соберите из созданных
# на уроке и в рамках домашнего задания функций пакет для работы с файлами разных
# форматов.

import os
import json
import pickle
import csv


def get_size(path):
    total_size = 0
    for path_dir, dir_names, file_names in os.walk(path):
        for f in file_names:
            fp = os.path.join(path_dir, f)
            total_size += os.path.getsize(fp)
    return total_size


def find_files(path, parent=None, lev=0):
    files_list = []

    for i in os.listdir(path):
        item_path = os.path.join(path, i)
        item_size = os.path.getsize(item_path) if os.path.isfile(item_path) else get_size(item_path)
        item_type = "файл" if os.path.isfile(item_path) else "директория"
        files_list.append([lev, item_type, i, item_size, parent])

        if os.path.isdir(item_path):
            files_list.extend(find_files(item_path, parent=i, lev=lev + 1))

    return files_list


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Уровень', 'Тип', 'Имя', 'Размер', 'Родительская директория'])
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def main(directory):
    files_list = find_files(directory)

    save_to_json(files_list, 'files_info.json')
    save_to_csv(files_list, 'files_info.csv')
    save_to_pickle(files_list, 'files_info.pkl')


if __name__ == "__main__":
    main(".")
