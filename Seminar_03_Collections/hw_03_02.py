"""В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать
знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания
апостроф) считать двумя словами. Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов."""

#На выходе: [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

#1 вариант
"""text = 'Hello world. Hello Python. Hello again.'
# Создаем словарь для подсчета слов
word_counts = {}
text = text.lower()
text = text.replace(',', ' ')
text = text.replace('.', ' ')
text = text.replace("'", ' ')
text = text.replace("!", ' ')
text = text.replace("?", ' ')
words = text.split()

for word in words:
    if word.isalpha(): # Игнорируем слова, содержащие цифры
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_10_words = sorted_words[:10]
print(top_10_words)"""

#2 вариант

import re
from collections import Counter

text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)