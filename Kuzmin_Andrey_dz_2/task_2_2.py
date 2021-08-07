input_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index_numbers = []

for i in range(len(input_text)):
    if input_text[i].isdigit() or input_text[i][1:].isdigit(): # проверка: элемент списка число или число со знаком?
        index_numbers.append(i) # Сохраняем индексы элементов, которые числа (1 3 8)
        if int(input_text[i]) < 10:
            input_text[i] = '0' + input_text[i] if len(input_text[i])==1 else input_text[i][0] + '0' + input_text[i][1] # к числам меньше 10 добавляем 0

for i in reversed(index_numbers): # Этим циклом добавляем ковычки в нужные нам места
    input_text.insert(i + 1, '"')
    input_text.insert(i, '"')
print(' '.join(input_text))