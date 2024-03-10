"""✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""


def create_unicode_dict(text: str) -> dict[str, int]:
    num1, num2 = map(int, text.split())
    start = min(num1, num2)
    end = max(num1, num2)
    unicode_dict = {}

    for num in range(start, end + 1):
        char = chr(num)
        unicode_dict[char] = num

    return unicode_dict


text = "10 20"
print(create_unicode_dict(text))
