l = ["word", 25, print, 3.56]  # вариант с индексом и элементом
t = []
length = int(len(l))
i = 0
while i < length:
    t.append(type(l[i]))       # создаем список классов
    i += 1
for i, el in enumerate(t):     # перебираем по индексам и элементам
    print(f"{i}:{el}")