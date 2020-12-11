number = (input("Введите целое число "))
number = list(number)
length = int(len(number))
i = int(0)
max = int(number[i])
while i < length - 1:
    if max >= int(number[i + 1]):
        i = (i + int(1))
        continue
    else: max = int(number[i + 1])
    i = (i + int(1))
print("Наибольшее число: %d" % max)