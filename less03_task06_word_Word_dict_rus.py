def int_func(word):
    d = {
        "а": "А",
        "б": "Б",
        "в": "В",
        "г": "Г",
        "д": "Д",
        "е": "Е",
        "ё": "Ё",
        "ж": "Ж",
        "з": "З",
        "и": "И",
        "й": "Й",
        "к": "К",
        "л": "Л",
        "м": "М",
        "н": "Н",
        "о": "О",
        "п": "П",
        "р": "Р",
        "с": "С",
        "т": "Т",
        "у": "У",
        "ф": "Ф",
        "х": "Х",
        "ц": "Ц",
        "ч": "Ч",
        "ш": "Ш",
        "щ": "Щ",
        "ъ": "Ъ",
        "ы": "Ы",
        "ь": "Ь",
        "э": "Э",
        "ю": "Ю",
        "я": "Я",
        }

    word = list(word)
    letter = word[0]
    word[0] = d[letter]
    word = "".join(word)
    return word

word = input("Введите на кириллице слово с маленькой буквы ")
print(int_func(word))
