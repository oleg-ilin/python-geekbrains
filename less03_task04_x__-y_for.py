def func(a, e):
    t = (a, e)
    c = a
    for e in t:
        c = c * a
    d = 1 / c
    return d
a = int(input("Введите действительное положительное число "))
b = int(input("Введите целое отрицательное число "))
e = abs(b)
print(a, "возведенное в степень", b, "равняется", func(a, b))
