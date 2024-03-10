"""Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. """


def calculate_bonus(names, rate, bonus_percentages):
    bonus_dict = {}
    for name, rate, bonus_percentage in zip(names, rate, bonus_percentages):
        bonus_percentage = float(bonus_percentage.strip('%')) / 100
        bonus = rate * bonus_percentage
        bonus_dict[name] = bonus
    return bonus_dict


names = ['John', 'Alice', 'Bob']
rate = [1000, 2000, 1500]
bonus_percentages = ['10%', '5%', '7.5%']
bonus_dict = calculate_bonus(names, rate, bonus_percentages)
print(bonus_dict)
