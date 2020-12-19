def int_func(word):
    word = list(word)
    word[0] = (word[0].upper())
    word = "".join(word)
    return word


word = input("Введите слово с маленькой буквы ")
print(int_func(word))
