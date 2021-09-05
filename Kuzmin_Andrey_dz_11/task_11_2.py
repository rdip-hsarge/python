class MyZeroError(ZeroDivisionError):
    txt = 'Вы поделили на ноль'

try:
    num1 = int(input('Введите делимое: '))
    num2 = int(input('Введите делитель: '))
    if num2 == 0:
        raise MyZeroError
    else:
        print(num1/num2)
except MyZeroError:
    print(MyZeroError.txt)
except:
    print('Нужно вводить числа')