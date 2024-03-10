"""нарисуйте елку"""
rows = int(input('Введите количество рядов: '))

for i in range(rows):
    print(f'{" " * (rows - i)}{"*" * (1 + 2 * i)}')