"""Напишите код, который анализирует число num и сообщает  является ли оно простым или составным. Используйте правило
для проверки: “Число является простым, если это число натуральное и делитсянацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.Если число не входит в дапазон, то сообщение:
"Число должно быть больше 1 и меньше 100000"."""

num = int(input())
i = 2
count = 0
if num > 1 and num < 100000:
    while i <= num:
        if num % i==0:
            count+=1
        i+=1
    if count == 1:
        print("Простое")
    else:
        print("Не является простым")

else:
    print('Число должно быть больше 1 и меньше 100000')

#Вариант 2
if not 1 < num < 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Не является простым")
            break
    else:
        print("Простое")