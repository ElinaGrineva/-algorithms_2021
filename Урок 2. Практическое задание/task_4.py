"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

# Я поняла это задание вот так:

num_list = [1, -0.5, 0.25, -0.125]


def summa(n, el_list=[]):
    if n == 0:
        return el_list
    else:
        c = num_list.pop(0)
        el_list.append(c)
        return summa(n-1)


number = int(input('Введите количество элементов:'))

empty_list = summa(number)

total = 0

for el in empty_list:
    total += el

print(f'Количество элементов: {number}, их сумма:{total}')