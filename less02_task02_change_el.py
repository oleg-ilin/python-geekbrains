n = int(input("Введите количество элементов "))
list = []
for i in range(0, n):         # пользователь вводит список
    el = int(input())
    list.append(el)
length = int(len(list))       # определяем длину списка
list_2 = []
k = 0
while k < length - 1:         # -1 защищает от ошибки k+1 при нечетном кол-ве элементов
    list_2.append(list[k+1])  # правый элемент пары ставим налево
    list_2.append(list[k])    # левый элемент пары ставим направо
    k += 2                    # делаем два шага
if length % 2 != 0:
    list_2.append(list[-1])   # добавляем в список последний нечетный элемент, если он есть
    print("Количество элементов нечетное. Сохраняем последний на своем месте")
else: print("Количество элементов четное")
print(list, "- исходный список")
print(list_2, "- обмен элементов произведен")