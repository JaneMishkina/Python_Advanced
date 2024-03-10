"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
сообщить является ли треугольник разносторонним, равнобедренным или равносторонним, только если треугольник существует"""
"""Варианты ответов:
Треугольник существует
Треугольник равносторонний
Треугольник равнобедренный
Треугольник разносторонний
Треугольник не существует"""
#1 вариант
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")

#2 вариант
# Функция для проверки существования треугольника
def checktriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Функция для определения типа треугольника, если он существует
def typeoftriangle(a, b, c):
    if checktriangle(a, b, c):
        if a == b and b == c:
            return "Треугольник существует\nТреугольник равносторонний"
        elif a == b or a == c or b == c:
            return "Треугольник существует\nТреугольник равнобедренный"
        else:
            return "Треугольник существует\nТреугольник разносторонний"
    else:
        return "Треугольник не существует"

# Пример использования
print(typeoftriangle(4, 4, 4)) # Треугольник существует, равносторонний