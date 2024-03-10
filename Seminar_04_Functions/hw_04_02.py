"""Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ -
значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)  # Output: {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

#2 вариант
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)  # Output: {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}