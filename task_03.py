# Задача 3.

# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


import random
my_list=[]
for i in range(10):
    my_list.append(random.randint(0,9))

print('Заданная последовательность цифр ', my_list)
result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print('Уникальные цифры ', result_list)

# или так

print('Уникальные цифры ', [i for i in my_list if my_list.count(i) == 1])


