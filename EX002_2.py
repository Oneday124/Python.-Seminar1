import math
# За день машина проезжает n км, сколько дней потребуется чтобы проехать m км.
# Не использовать if, циклы и модуль
# n = 700
# m = 750
# output = 2

n = int(input('Введите колличество километров, которое машина проезжает за день: '))
m = int(input('Введите количество километров, которое необходимо проехать: '))
print(f'Потребуется {math.ceil(m/n)} дней')

print((m+n-1)//n)

# В школе решили набрать 3 новых математических класса и оборудовать кабинеты для них новыми партами
# За каждой партой может сидеть 2 учащихся
# Известно количество учащихся в каждом из 3х классов. Выведите наименьшее число парт, которое нужно купить
# input: 20, 21, 22
# output: 32

a = int(input('Введите число учеников класса 1: '))
b = int(input('Введите число учеников класса 2: '))
c = int(input('Введите число учеников класса 3: '))
print(f'Необходимо закупить {math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)} парт')
print((a+1)//2 + (b+1)//2 + (c+1)//2)
