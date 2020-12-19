result = 0
a = 1
while a == 1:
    listing = input("Введите числа через пробел.\nПоследним введите значение 's', если хотите закончить вычисления: ").split()
    if listing[-1] == "s":
        listing.pop()
        listing = [int(item) for item in listing]
        for i in listing:
            result += i
        print("Вычисления закончены, сумма всех введенных чисел: ", result)
        break
    else:
        listing = [int(item) for item in listing]
        for i in listing:
            result += i
        print(result)
