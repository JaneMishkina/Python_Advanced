"""Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные
случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на
одной вертикали, горизонтали или диагонали.
Список из 4-х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо."""
"""from chess_module 
import check_queens from chess_module 
import is_attacking import random 

Основное отличие от 
randint () в том, что в randrange () можно указать шаг. Данная функция похожа на range (). Функцию randrange () можно 
вызвать с одним, двумя или тремя параметрами. Значение от 0 до 5. print (random.randrange (5)). Значение в диапазоне 
от 12 до 22. print (random. randrange (12, 22)).

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        queens = [(random.randrange(1, 9), random.randrange(1, 9)) for _ in range(4)]
        if check_queens(queens):
            board_list.append(queens)
    return board_list

print(generate_boards())"""

#2 вариант
import random
from itertools import combinations

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 9):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

print(generate_boards())