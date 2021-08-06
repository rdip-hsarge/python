input_list=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0

while (i < len(input_list)):
    print(f' Hello, {input_list[i].split(" ")[-1].title()}|')
    i+=1