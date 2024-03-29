"""Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные
(без повтора) элементы исходного списка. *Подготовьте два решения, короткое и длинное, которое не использует другие
коллекции помимо списков"""
numbers = [1, 3, 5, 8, 9, 7, 1, 3]
un_numbers = list(set(numbers))
print(un_numbers)

numbers_01 = [1, 3, 5, 8, 9, 7, 1, 3]
uni_numbers = []
for number in numbers_01:
    if number not in uni_numbers:
        uni_numbers.append(number)
print(uni_numbers)

"""Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды"""
lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, ]

for i in set(lst):
    counter = lst.count(i)
    if counter > 1:
        for _ in range(counter):
            lst.remove(i)

print(lst)

"""Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных 
элементов исходного списка. Нумерация начинается с единицы."""
# Создаем список с повторяющимися целыми числами
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 1, 7, 8, 9]
# Формируем список с порядковыми номерами нечетных элементов
odd_indices = [index + 1 for index, num in enumerate(my_list) if num % 2 != 0]
# Выводим список с порядковыми номерами нечетных элементов
print(odd_indices)

#2 вариант
numbers = [13, 2, 3, 5, 7, 2, 5]
odd_indexes = []
for i, elem in enumerate(numbers, 1):
    if elem % 2 != 0:
        odd_indexes.append(i)

print(odd_indexes)