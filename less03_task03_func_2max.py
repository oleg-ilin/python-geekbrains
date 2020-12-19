def my_func():
    print(t)
    #print(type(t[0]))
    if t[0] > t[1]:
        if t[1] > t[2]:
            print("Сумма двух максимальных чисел: ", int(t[0]) + int(t[1]))
        else: print("Сумма двух максимальных чисел: ", int(t[0]) + int(t[2]))
    else:
        if t[0] > t[2]:
            print("Сумма двух максимальных чисел: ", int(t[1]) + int(t[0]))
        else: print("Сумма двух максимальных чисел: ", int(t[1]) + int(t[2]))

t = input("Введите три числа через пробел ").split()
my_func()




