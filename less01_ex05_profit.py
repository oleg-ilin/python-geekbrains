revenue = float(input("Введите размер выручки "))
cost = float(input("Введите размер издержек "))
profit = revenue - cost
if profit == 0:
    print("Ваша прибыль равна нулю")
elif profit > 0:
    print("Ваша прибыль ", round(profit,2))
    print("Рентабельность  ", round(profit / revenue * 100, 2), "%")
    staff = int(input("Введите количество сотрудников "))
    print("В расчете на одного сотрудника прибыль составляет ", round(profit / staff, 2))
else:
    print("У Вас убыток ", profit)


