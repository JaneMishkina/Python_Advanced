"""Задание №6
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки."""

txt = input("Введите текст ")
words = txt.split()
sort_words = sorted(words)
max_len = len(sort_words[-1])
for i, word in enumerate(sort_words, 1):
    str_1 = f'{i:2}. {word:>{max_len}}'
    print(str_1)

"""Задание №7
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях"""

txt = input("Введите текст ")
freq_letter = {}
for letter in txt:
    freq_letter[letter] = freq_letter.get(letter, 0) + 1
print(freq_letter)

#2 вариант
txt = input("Введите текст ")
freq_letter = {}
for letter in txt:
    freq_letter[letter] = txt.count(letter)
print(freq_letter)