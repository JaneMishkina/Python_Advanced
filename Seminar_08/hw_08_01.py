import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            total_size += size
        for name in dirs:
            path = os.path.join(root, name)
            total_size += get_dir_size(path)
    return total_size

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)

#directory = input("Enter the directory path: ")
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pickle')

"""В начале кода определены три функции:

   - get_dir_size(directory): Эта функция рекурсивно проходит через директорию и вычисляет общий размер всех файлов в 
   данной директории в байтах. Она используется для вычисления размера всех файлов и директорий внутри родительской 
   директории.
   
   - traverse_directory(directory): Эта функция рекурсивно обходит указанную директорию и все вложенные директории. 
   Для каждого файла в директории добавляется информация о пути к файлу, типе (файл или директория) и размере (в 
   байтах) в список результатов. Для директорий также добавляется размер, учитывая все вложенные файлы и директории.
   
   - save_results_to_json(results, output_file): Эта функция сохраняет результаты в формате JSON в указанный файл.
   
   - save_results_to_csv(results, output_file): Эта функция сохраняет результаты в формате CSV (таблица) в указанный файл.
   
   - save_results_to_pickle(results, output_file): Эта функция сохраняет результаты в формате Pickle в указанный файл.

2. Пользователь вводит путь к директории в переменную directory.

3. Функция traverse_directory(directory) вызывается с переданным пользователем путем директории. Результаты обхода 
сохраняются в переменной results.

4. Функции save_results_to_json, save_results_to_csv и save_results_to_pickle вызываются со списком результатов и 
именами файлов, в которые нужно сохранить результаты. Результаты сохраняются в трех различных файлах с помощью 
соответствующих функций.

Этот код позволяет рекурсивно обойти директорию и сохранить информацию о каждом файле и директории в указанных 
форматах для последующего анализа или использования."""