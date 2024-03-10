# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#         print(f'Создал {self} со свойствами:\n' f'{self.name = },\t{self.equipment = },\t{self.life = }')
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         print(f'Создал класс {cls}')
#         return instance
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман')
# print('Создаём третий раз')
# u_3 = User(name='Стэнц')

# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')


# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, name: str):
#         self.name = name
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# u_2 = User('Венкман')

# import sys
# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# del u_1
# print(sys.getrefcount(u_2))
# print('Завершение работы')

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
# user = User('Спенглер')
# print(user)

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
# user = User('Спенглер')
# print(user)

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#     def __repr__(self):
#         return f'User({self.name})'
# user = User('Спенглер')
# print(user)


# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)


# class User:
#
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)
# print(f'{user}')
# print(repr(user))
# print(f'{user = }')

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# u_1 = User('Спенглер')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
# ghostbusters = [u_1, u_2, u_3]
# print(ghostbusters)
# print(f'{ghostbusters}')
# print(repr(ghostbusters))
# print(f'{ghostbusters = }')
# print(*ghostbusters, sep='\n')

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
# a = Vector(2, 4)
# b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')

# from random import choices
# class Closet:
#     CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom
#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'
#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))
# storeroom = Closet(10)
# print(storeroom)
# for _ in range(4):
#     storeroom = storeroom >> 3
#     print(storeroom)

# class StrPro(str):
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args, **kwargs)
#         return instance
#     def __rmul__(self, other: str):
#         words = other.split()
#         result = self.join(words)
#         return StrPro(result)
# text = 'Каждый охотник желает знать где сидит фазан'
# s = StrPro(' (=^.^=) ')
# print(f'{text = }\n{s = }')
# print(text * s)
# print(s * text) # TypeError: 'str' object cannot be interpreted as an integer

# from decimal import Decimal
# class Money:
#     def __init__(self, value: int | float):
#         self.value = Decimal(value)
#     def __repr__(self):
#         return f'Money({self.value:.2f})'
#     def __imod__(self, other):
#         self.value = self.value * Decimal(1 + other / 100)
#         return self
# m = Money(100)
# print(m)
# m %= 50
# print(m)
# m %= 100
# print(m)

# class MyClass:
#     def __init__(self, data):
#         self.data = data
#     def __and__(self, other):
#         return MyClass(self.data + other.data)
#     def __str__(self):
#         return str(self.data)
# a = MyClass((1, 2, 3, 4, 5))
# b = MyClass((2, 4, 6, 8, 10))
# print(a & b) #(1, 2, 3, 4, 5, 2, 4, 6, 8, 10)

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# print(one == two)
# print(one == three)

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))
#         second = sorted((other.a, other.b, other.c))
#         return first == second
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }')
# print(f'{one == three = }')
# print(f'{one == four = }')
# print(f'{one != one = }')

from math import sqrt
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#     def __repr__(self):
#         return f'Triangle({self.a}, {self.b}, {self.c})'
#     # def __eq__(self, other):
#     #     first = sorted((self.a, self.b, self.c))
#     #     second = sorted((other.a, other.b, other.c))
#     #     return first == second
#     def area(self):
#         p = (self.a + self.b + self.c) / 2
#         _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#         return _area
#     def __lt__(self, other):
#         return self.area() < other.area()
# # one = Triangle(3, 4, 5)
# # two = Triangle(5, 5, 5)
# # print(f'{one} имеет площадь {one.area():.3f} у.е.²')
# # print(f'{two} имеет площадь {two.area():.3f} у.е.²')
# # print(f'{one > two = }\n{one < two = }')
# # data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
# # result = sorted(data)
# # print(result)
# # print(', '.join(f'{item.area():.3f}' for item in result))
#
#
# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4,4, 4), Triangle(3, 5, 3)}
# print(triangle_set)
# print(', '.join(f'{hash(item)}' for item in triangle_set))

# from math import sqrt
# class Triangle:
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
#     def __repr__(self):
#         return f'Triangle({self._a}, {self._b}, {self._c})'
#     def __eq__(self, other):
#         first = sorted((self._a, self._b, self._c))
#         second = sorted((other._a, other._b, other._c))
#         return first == second
#     def area(self):
#         p = (self._a + self._b + self._c) / 2
#         _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
#         return _area
#     def __lt__(self, other):
#         return self.area() < other.area()
#     def __hash__(self):
#         return hash((self._a, self._b, self._c))
# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
# print(triangle_set)
# print(', '.join(f'{hash(item)}' for item in triangle_set))

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
# a = Vector(2, 4)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
# a = Vector(2, 4)
# #print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
# a = Vector(2, 4)
# #print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
# #a.z = 73 # AttributeError: У нас вектор на плоскости, а не в пространстве
# a.x = 3
# print(f'{a = }')

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#     def __getattr__(self, item):
#         return None
# a = Vector(2, 4)
# print(a.z) # None
# print(f'{a = }')

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return None
    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)
a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(f'{a = }, {a.s = }')