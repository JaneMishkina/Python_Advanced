"""На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
"""
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
#1 вариант
backpack = {}
sorted_items = sorted(items.items(), key=lambda x: x[1] / x[1], reverse=True)

remaining_weight = max_weight

for item, weight in sorted_items:
    if weight <= remaining_weight:
        backpack[item] = weight
        remaining_weight -= weight
    if remaining_weight == 0:
        break

print(backpack)

#2 вариант
backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

print(backpack)