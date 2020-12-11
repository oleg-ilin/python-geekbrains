a = int(input("Введите значение А "))
b = int(input("Введите значение B "))
day = 1
while a <= b:
    print(day, "- й день: ", round(a, 2))
    day += 1
    a *= 1.1
print(day, "- й день: ", round(a, 2))
print("На ", day, "- й день спортсмен достиг результата — не менее ", b, "км.")
