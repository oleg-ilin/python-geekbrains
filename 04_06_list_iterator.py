'''Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

from itertools import cycle
my_list = ["SPb", "Msk", "Amst"]
iter = cycle(my_list)
print("Итератор, повторяющий элементы некоторого списка, определенного заранее."
      "\nВводите любую клавишу для продолжения или s для остановки ")
for el in iter:
    print(next(iter), end=" ")
    command = input()
    if command == "s":
        break
    else:
        continue

