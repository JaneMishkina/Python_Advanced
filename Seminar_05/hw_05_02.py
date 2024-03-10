"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
ставка int, премия str с указанием процентов вида 10.25%. В результате result получаем словарь с именем в качестве
ключа и суммой премии в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии."""


names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

print({name: sal * float(perc.strip('%')) / 100 for name, sal, perc in zip(names, salary, bonus)})

#2 вариант
result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)