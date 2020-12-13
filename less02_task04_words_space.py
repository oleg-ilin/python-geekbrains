ans = input("Введите несколько слов через пробел: ")
l = (ans.split(" "))
i = len(l) + 1
for i, el in enumerate(l):     # перебираем по индексам и элементам
    print(f"{i + 1}:{el[0:10]}")