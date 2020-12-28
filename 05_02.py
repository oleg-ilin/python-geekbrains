"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке."""

with open("text2.txt", "r", encoding="UTF-8") as file:
    # print("Количество строк в файле: ", sum(1 for i in file))
    content = file.readlines()
    print(content)
    i = 0
    for line in content:
        i = i + 1
        print(line)
        print("Количесво слов в строке: ", len(line.split()), "\n")
    print("Количество строк в файле: ", i)

