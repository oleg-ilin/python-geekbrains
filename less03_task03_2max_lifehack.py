def my_func():
    t.sort()
    t.reverse()
    print("Сумма двух максимальных чисел: ", int(t[0]) + int(t[1]))
t = input("Введите три значения через пробел ").split()
my_func()
