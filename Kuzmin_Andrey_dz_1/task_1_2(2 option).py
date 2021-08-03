my_list = [number ** 3 for number in range(1000) if number % 2] # наш список
summa = 0 # переменная, для хранения суммы подходящих чисел

for number in my_list:
    result = 0
    number_clone = number # клон проверяемого числа, нужный, чтобы отсекать от него по цифре и не трогать элементы списка
    while (number_clone > 0):
        result += number_clone % 10
        number_clone = number_clone // 10
    if result % 7 == 0:
        summa += number
print (summa)

summa_second = 0
for number in my_list:
    number += 17
    result = 0
    number_clone = number
    while (number_clone > 0):
        result += number_clone % 10
        number_clone = number_clone // 10
    if result % 7 == 0:
        summa_second += number
print (summa_second)