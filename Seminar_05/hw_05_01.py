"""Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

import os

def get_file_info(file_path)-> tuple:
    file_name, file_ext = os.path.splitext(file_path)
    folder_path, file_name = os.path.split(file_name)
    return (folder_path + '/', file_name, file_ext)


#2 вариант
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))

