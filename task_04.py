# Задача 4.

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('34_Polynomial.txt', 'w') as data:
#     data.write(polynom1)


# # Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k)
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('34_Polynomial2.txt', 'w') as data:
#     data.write(polynom2)


# k = int(input('Задайте натуральную степень многочлена k: '))
# import Func_coeff_polinom as cp
# coeff_polynom = cp.fill_coefficients_polynomial_list(k)
# my_file = 'f_polinom4_4.txt'
# import Func_call_record_func as fc
# fc.call_record_func(k, coeff_polynom, my_file)


# def ratios_list(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     if ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# from random import randint
# import itertools as it


# def ratios_list(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     if ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def polynom_list(cof, ratios):
#     op = ['*x^']*(cof-1) + ['*x']
#     polynom = [[a, b, c] for a, b, c in it.zip_longest(
#         ratios, op, range(cof, 1, -1), fillvalue='') if a != 0]
#     for x in polynom:
#         x.append(' + ')
#     polynom = list(it.chain(*polynom))
#     polynom[-1] = ' = 0'
#     return "".join(map(str, polynom)).replace(' 1*x', ' x')


# cof = randint(2, 5)
# ratios = ratios_list(cof)
# polynom = polynom_list(cof, ratios)
# print(polynom)

# with open('Polynom_33.txt', 'w') as data:
#     data.write(polynom)


# from random import randint
# k = int(input('Введите натуральную степень k: '))
# a = randint(-100, 100)
# b = randint(-100, 100)
# print(f'{a}*x^{k} + {b}*x + 5 = 0')
# with open('task_4.txt', 'w') as data:
#     data.write(f'{a}*x^{k} + {b}*x + 5 = 0')

from random import randint
import random

k = int(input('Введите число k: '))

polynom = ''
rand_numb = []
for i in range(k):
    rand_numb.append(randint(-100, 100))

znak = ['+', '-']
i = 0
j = 0
while k > 1:
    if rand_numb[i] != 0:
        polynom += (f'{rand_numb[i]}x**{k}{random.choice(znak)}')
    k -= 1
    i += 1

if rand_numb[-1] != 0:
    polynom += (f'{rand_numb[-1]}=0')
else:
    polynom += ('=0')
with open('result.txt', 'w', encoding='utf8') as file:
    file.write(f'Сгенерированные числа: {rand_numb}\nОтвет: {polynom}')
print('Сгенерированные числа: ', rand_numb)
print('Ответ: ', polynom)

