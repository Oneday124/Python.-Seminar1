# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели и проверяет является ли этот день выходным
# number = int(input("Введите номер дня недели: "))
# if number > 7 or number <= 0:
#     print("Введенное значение не является днем недели")
# elif number < 6:
#     print("Нет")
# else:
#     print("Да")

# Напишите программу для проверки истинности утверждения not(x[0] or x[1] or x[2] = not x[0] and not x[1] and notx[2])
# Для всех значений предикат

# x = int(input('Введите значение x: '))
# y = int(input('Введите значение y: '))
# z = int(input('Введите значение z: '))
# if not(x or y or z) == (not x and not y and not z):
#     print("True")
# else:
#     print("False")

# Напишите программу, которая на вход принимает координаты точки (х и y), причем x != 0 и y != 0
# и выдает номер четверти плоскости, в которой находится эта точка
# x = int(input('Введите значение X, не равное 0: '))
# y = int(input('Введите значение Y, не равное 0: '))
# if x > 0 and y > 0:
#     print(f'({x};{y}) 1 четверть')
# elif x < 0 and y > 0:
#     print(f'({x};{y}) 2 четверть')
# elif x < 0 and y < 0:
#     print(f'({x};{y}) 3 четверть')
# elif x > 0 and y < 0:
#     print(f'({x};{y}) 4 четверть')
# else:
#     print('Введено не корректное значение')

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти

# number = int(input('Введите номер четверти: '))
# if number > 4 or number < 1:
#     print('Введено не корректное значение')
# elif number == 1:
#     print(f'x (0;...); y (0;...)')
# elif number == 2:
#     print(f'x (...;0); y (0;...)')
# elif number == 3:
#     print(f'x (...;0); y (...;0)')
# else:
#     print(f'x (0;...); y (...;0)')

# НАпигите программу, которая на вход принимает координаты 2х точек
# и находит расстояние между ними в 2D пространстве

# x1 = int(input("Введите координаты точки x1: "))
# y1 = int(input("Введите координаты точки y1: "))
# x2 = int(input("Введите координаты точки x2: "))
# y2 = int(input("Введите координаты точки y2: "))
# print(((x1-x2)**2 + (y1-y2)**2)**0.5)
