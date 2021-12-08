from random import randint, random
script = int(input('Выбери сценарий: 1 - целое число; 2 - Re число; 3 - буква\n'))

if script == 1:
    (a, b) = int(input('Выбери границы случайного числа (через Enter):')), int(input())
    print(f'random number: {randint(a, b)}')
elif script == 2:
    (a, b) = int(input('Выбери границы случайного Re числа (через Enter):')), int(input())
    print(f'random Re number: {randint(a, b-1) + random()}')
elif script == 3:
    (a, b) = ord(input('Выбери границы в буквах (через Enter):')), ord(input())
    print(f'random symbol: {chr(randint(a, b))}')
else:
    print('Try again')
    exit()
