# class Number:
#     def __init__(self, num):
#         self.num = num
# n = Number(42)
# print(f'{callable(Number) = }')
# print(f'{callable(n) = }')

from collections import defaultdict
# class Storage:
#     def __init__(self):
#         self.storage = defaultdict(list)
#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in
#         self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'
#     def __call__(self, value):
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'
# s = Storage()
# print(s(42))
# print(s(72))
# print(s('Hello world!'))
# print(s(0))
# print(s)

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b})'
#     def __call__(self, *args, **kwargs):
#         self.a.append(args)
#         self.b.update(kwargs)
#         return True
# x = MyClass([42], {73: True})
# y = x(3.14, 100, 500, start=1)
# x(y=y)
# print(x)

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
# fib = Fibonacci(20, 100)
# for num in fib: # TypeError: 'Fibonacci' object is not iterable
#     print(num)


# class Fibonacci:
#     def __init__(self, start, stop):
#
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#
# fib = Fibonacci(20, 100)
# for num in fib:  # TypeError: iter() returned non-iterator of type 'Fibonacci'
#     print(num)

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.first < self.stop:
#             self.first, self.second = self.second, self.first  + self.second
#             if self.start <= self.first < self.stop:
#                 return self.first
#         raise StopIteration
# fib = Fibonacci(20, 100)
# for num in fib:
#     print(num)

# class Iter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         for i in range(self.start, self.stop):
#             return chr(i)
#         raise StopIteration
# chars = Iter(65, 91)
# for c in chars:
#     print(c) #Бесконечный вызов символа под номером 65 из ascii(A)

# import sqlite3
# class DB:
#     def __init__(self, name):
#         self.name = name
#         self.connection = None
#         self.cursor = None
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.name)
#         self.cursor = self.connection.cursor()
#         return self.cursor
# db = DB('sqlite.db')
# with db as cur: # AttributeError: __exit__
#     cur.execute("""create table if not exists users(name, age);""")
# cur.execute("""insert into users values ('Гвидо', 66);""")

# class MyCls:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def __enter__(self):
#         self.full_name = self.first_name + ' ' + self.last_name
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.full_name = self.full_name.upper()
# x = MyCls('Гвидо ван', 'Россум')
# with x as y:
#     print(y.full_name)
#     print(x.full_name)
# print(y.full_name)
# print(x.full_name)

# Гвидо ван Россум
# Гвидо ван Россум
# ГВИДО ВАН РОССУМ
# ГВИДО ВАН РОССУМ


# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
# user = User('Стивен', 'Спилберг')
# print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# user.full_name = 'Стивен Хокинг' # AttributeError: can't set attribute 'full_name'
# user.last_name = 'Хокинг'
# print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#         else:
#             raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
#     @age.deleter
#     def age(self):
#         self._age = 0
# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло много лет. Изобретена технология перерождения.')
# del user.age
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')

# class Student:
#     def __init__(self, name, age, grade, office):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.office = office
#     def __repr__(self):
#         return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'
# std1 = Student('Шурик', 7, 1, 12)
# print(std1)

# class Range:
#     def __init__(self, min_value: int = None, max_value: int =
#     None):
#         self.min_value = min_value
#         self.max_value = max_value
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)
#     def __delete__(self, instance):
#         raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
#     def validate(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f'Значение {value} должно быть целым числом')
#         if self.min_value is not None and value < self.min_value:
#             raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
#         if self.max_value is not None and value >= self.max_value:
#             raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')
# class Student:
#     age = Range(3, 103)
#     grade = Range(1, 11 + 1)
#     office = Range(3, 42 + 1)
#     def __init__(self, name, age, grade, office):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.office = office
#     def __repr__(self):
#         return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'
# if __name__ == '__main__':
#     std_one = Student('Архимед', 12, 4, 29)
#     std_other = Student('Аристотель', 2406, 5, 17)
#     # ValueError: Значение 2406 должно быть меньше 103
#     print(f'{std_one = }')
#     std_one.age = 15
#     print(f'{std_one = }')
#     std_one.grade = 11.0
#     # TypeError: Значение 11.0 должно быть целым числом
#     std_one.office = 73
#     # ValueError: Значение 73 должно быть меньше 42
#     del std_one.age # AttributeError: Свойство "_age" нельзя удалять
#     print(f'{std_one.__dict__ = }')

# class Text:
#     def __init__(self, param):
#         self.param = param
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#     def __set__(self, instance, value):
#         if self.param(value):
#             setattr(instance, self.param_name, value)
#         else:
#             raise ValueError(f'Bad {value}')
# class User:
#     first_name = Text(str.istitle)
#     last_name = Text(str.isupper)
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def __repr__(self):
#         return f'Student(age={self.first_name} grade={self.last_name})'
# if __name__ == '__main__':
#     std_one = User('Гвидо ван', 'Россум')
# #ValueError: Bad Гвидо ван

from math import sqrt
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'
    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second
    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area
    def __lt__(self, other):
        return self.area() < other.area()
    def __hash__(self):
        return hash((self._a, self._b, self._c))
triangle = Triangle(3, 4, 5)
print(triangle)
print(triangle.__dict__)
print(Triangle.__dict__)