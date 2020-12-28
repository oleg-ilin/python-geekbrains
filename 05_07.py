'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.'''


import json
with open("text7.txt", "r", encoding = "UTF-8") as file:
    firms_list = file.readlines()
    dict_firms = {}
    dict_average ={}
    result_list = []
    sum_profit = 0
    i = 0
    k = 0
    profit = []
    with open("result.txt", "a", encoding="UTF-8") as file_01:
        for el in firms_list:
            key_df = firms_list[i].split()[0]
            profit = int(firms_list[i].split()[2]) - int(firms_list[i].split()[3])
            dict_firms[key_df] = profit
            profit_info = [str(key_df) + " Прибыль: " + str(profit) + "\n"]
            file_01.writelines(profit_info)
            if profit >= 0:
                sum_profit += profit
                k += 1
            i = i + 1
        average_info = ["Средняя прибыль: " + str(round(sum_profit / k, 2)) + "\n" ]
        file_01.writelines(average_info)
        dict_average["average_profit"] = round(sum_profit / k, 2)
        result_list.append(dict_firms)
        result_list.append(dict_average)
with open("data.json", "w", encoding="UTF-8") as f:
    json.dump(result_list, f, ensure_ascii=False)

