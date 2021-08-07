def get_jokes(num, flag = False): # Функция с флагом (изначально поднят, т.е. повторять элементы можно)
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(num):
        if flag: #
            from random import randint # Если флаг опущен, мы будем с помощью pop вытаскивать случайные элементы в списках и удалять их, чтобы не повторялись
            print(nouns.pop(randint(0, len(nouns)-1)), adverbs.pop(randint(0, len(adverbs)-1)), adjectives.pop(randint(0, len(adjectives)-1)))
        else:
            from random import choice # Флаг не опущен, простым choice выбираем случайные элементы с возможным повторением
            print(choice(nouns), choice(adverbs), choice(adjectives))

get_jokes(3, True)