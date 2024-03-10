"""Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки."""


def print_words(text) ->None:
    """
    Выводит слова из строки в соотв с Unicode
    """
    words = text.split()
    longest_word_len = max(len(word) for word in words)

    for i, word in enumerate(sorted(words), start=1):
        print(f"{word:>{longest_word_len}} {i}")


text = "Какой прекрасный день сегодня"
print_words(text)

# 2 вариант
s = 'Строки нумеруются начиная с единицы.'


def string_parse(string: str) -> str:
    """
    Обрабатывает строку.
    :param string:
    :return:
    """
    data = string.split()
    data.sort()

    longest_word = len(max(data, key=len))

    res = ''
    for n, s in enumerate(data, 1):
        res += f'{n} {s:>{longest_word}}\n'

    return res


print(string_parse(s))
help(string_parse)