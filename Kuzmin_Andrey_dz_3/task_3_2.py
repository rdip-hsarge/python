def num_translate(num):
    trans = {'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
             'zero': 'нуль', 'ten': 'десять'}
    big_letter = False

    if num == num.title():
        num = num.lower()
        big_letter = True
    if num in trans:
        return trans[num].title() if big_letter else trans[num]
    else:
        return None

print(num_translate('two'))