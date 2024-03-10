"""Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где ключ - тип
элемента, а значение - список элементов данного типа."""
elements = (1, 1.2, 'asdf', [1,], 53, 1.23)
new_dict = {}
for i in elements:
   new_dict.setdefault(type(i), [])
   new_dict[type(i)].append(i)

print(new_dict)

