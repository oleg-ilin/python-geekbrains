

list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
try:  # защита от ввода нечислового значения
    month = int(input("Введите номер месяца от 1 до 12 ")) - 1
    if month < 0 or month > 11:    # что бы не получилось, что нулевой месяц это зима
        print("Неверный номер! Введите от 1 до 12")

    else: print("Это", (list[month]))
except:
    print("Ввести надо номер")
