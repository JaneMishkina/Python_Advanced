"""
Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.

"""


def get_unicode_codes(text: str) -> list[int]:
    unique_codes = sorted(set(ord(char) for char in text), reverse=True)
    return unique_codes


text = "Какой прекрасный день сегодня"
print(get_unicode_codes(text))
