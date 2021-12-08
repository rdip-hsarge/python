a, b, c = int(input()), int(input()), int(input())

if ((a > b) and (a < c)) or ((a < b) and (a > c)):
    print (f'This is {a}')
elif ((b > a) and (b < c)) or ((b < a) and (b > c)):
    print(f'This is {b}')
else:
    print(f'This is {c}')