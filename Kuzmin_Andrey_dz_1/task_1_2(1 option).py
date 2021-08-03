def summator(number): # функция, возвращающая сумму цифр числа
    result = 0
    while (number > 0):
        result += number % 10
        number = number // 10
    return result

my_list = [number ** 3 for number in range(1000) if number % 2] # наш список
summa = 0 # переменная, для хранения суммы подходящих чисел

for number in my_list:
    if summator(number) % 7 == 0:
        summa += number
print (summa)

summa_second = 0 # переменная, для хранения суммы подходящих чисел ВО ВТОРОМ СЛУЧАЕ (+17)
for number in my_list:
    number += 17
    if summator(number) % 7 == 0:
        summa_second += number
print (summa_second)