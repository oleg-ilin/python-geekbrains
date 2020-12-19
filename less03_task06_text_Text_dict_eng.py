def int_func(word):
    d = {
        "q": "Q",
        "w": "W",
        "e": "E",
        "r": "R",
        "t": "T",
        "y": "Y",
        "u": "U",
        "i": "I",
        "o": "O",
        "p": "P",
        "a": "A",
        "s": "S",
        "d": "D",
        "f": "F",
        "g": "G",
        "h": "H",
        "j": "J",
        "k": "K",
        "l": "L",
        "z": "Z",
        "x": "X",
        "c": "C",
        "v": "V",
        "b": "B",
        "n": "N",
        "m": "M",
        }

    word = list(word)
    letter = word[0]
    word[0] = d[letter]
    word = "".join(word)
    return word

ans = input("Введите несколько слов через пробел: ")
listing = ans.split(" ")
for i in listing:
    word = i
    print(int_func(word), end=" ")
