dict = {
    "1" : "зима",
    "2" : "зима",
    "3" : "весна",
    "4" : "весна",
    "5" : "весна",
    "6" : "лето",
    "7" : "лето",
    "8" : "лето",
    "9" : "осень",
    "10" : "осень",
    "11" : "осень",
    "12" : "зима",
}
try:  # защита от ввода нечислового значения
    month = input("Введите номер месяца от 1 до 12 ")
    if int(month) < 1 or int(month) > 12:    # что бы не получилось, что нулевой месяц это зима
        print("Неверный номер! Введите от 1 до 12")
    else:
        print("Это", dict[month])
except:
    print("Ввести надо номер")