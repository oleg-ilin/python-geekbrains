def func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print("Деление на ноль")
a = int(input("Введите А "))
b = int(input("Введите В "))
print(func(a, b))