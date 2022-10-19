# Задача 4.

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0



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

