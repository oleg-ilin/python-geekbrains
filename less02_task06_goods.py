i = 1
t = ()
listing =[]
choice = "y"
while choice.lower() == "y":
    good = input("Введите наименование: ")
    price = input("Введите цену ")
    quant = input("Введите количество ")
    unit = input("Введите единицу измерения ")
    d = {
        "Наименование" : good,
        "Цена" : price,
        "Количество" : quant,
        "Ед." : unit
    }
    t = (i, d)
    listing.append(t)
    i += 1
    choice = input("Для продолжения ввода нажмите `y`, для окончания `n` ")

# text = '\n'.join(' '.join(map(str, x)) for x in l)
# print(text)
# da = {}
# for key, value in l.items:

dict_analitic = {}
for goods in listing:
    for key, value in goods[1].items():
        if key in dict_analitic:
            dict_analitic[key].append(value)
        else:
         dict_analitic[key] = [value]
#print(dict_analitic)
for key, value in dict_analitic.items():
    print("{0}: {1}".format(key, value))