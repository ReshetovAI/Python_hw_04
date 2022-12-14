# Задача 5.

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import random

# запись в файл


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100


def rnd():
    return random.randint(0, 101)

# создание коэффициентов многочлена


def ratio_pl(k):
    lst = [rnd() for i in range(k+1)]
    return lst

# создание многочлена в виде строки


def pl_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена


def degree_pl(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена


def ratio_member_pl(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов


def calc_pl(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if degree_pl(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l-1  # индекс
    while ii >= 0:
        if degree_pl(st[ii]) != -1 and degree_pl(st[ii]) == i:
            lst.append(ratio_member_pl(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst

# создание двух файлов


k1 = int(input("Введите натуральную степень для первого файла k1 = "))
k2 = int(input("Введите натуральную степень для второго файла k2 = "))
ratio1 = ratio_pl(k1)
ratio2 = ratio_pl(k2)
write_file("task_5_1.txt", pl_str(ratio1))
write_file("task_5_2.txt", pl_str(ratio2))

# нахождение суммы многочлена

with open('task_5_1.txt', 'r') as data:
    polinom1 = data.readlines()
with open('task_5_2.txt', 'r') as data:
    polinom2 = data.readlines()

print(f"Первый многочлен: {polinom1}")
print(f"Второй многочлен: {polinom2}")

lst1 = calc_pl(polinom1)
lst2 = calc_pl(polinom2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("task_5_res.txt", pl_str(lst_new))
with open('task_5_res.txt', 'r') as data:
    st3 = data.readlines()

print(f"Результирующий многочлен: {st3}")
