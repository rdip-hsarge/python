class MyErrorClass(Exception):
    txt = 'Вы ввели не число'

print('Вы в процессе заполнения вашего списка числами, если хотите закончить, то введите exit')
user_list = []

while True:
    try:
        number = input('Введите число для вашего списка: ')
        if number == 'exit':
            break
        elif number.isdigit() or number.replace('-', '').isdigit():
            user_list.append(int(number))
        else:
            raise MyErrorClass
    except MyErrorClass:
        print(MyErrorClass.txt)
    except:
        print('Неизвестная ошибка')

print(f'Ваш список: {user_list}')