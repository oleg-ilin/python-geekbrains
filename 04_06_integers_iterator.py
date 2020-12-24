'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,'''

from itertools import count
start = int(input("Начинаем генерировать целые числа\nВведите начальное целое число: "))
stop = int(input("Введите конечное целое число: "))

for el in count(start):
    if el > stop:
        break
    else:
        print(el)

