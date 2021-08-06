def maker_text(some_number_list): # Функция вывода цен в строку
    for number in some_number_list:
        cent = round(100 * (number - int(number)))
        if cent < 10:
            print(f'{int(number)} rub 0{cent} cop', end=', ')
        else:
            print(f'{int(number)} rub {cent} cop', end=', ')
    print('\n')

prices = [19.24, 45.93, 5.26, 1.09, 24.17, 84.13, 91.11, 44.75, 9.44, 68.14, 7.95, 44.74, 50.79, 21.8, 13.69]

maker_text(prices) # Просто выводим цены
maker_text(sorted(prices)) # Выводим отсортированные цены
new_list = sorted(prices, reverse=True).copy() # Как требуется по заданию, создаем новый список и сразу сортируем
maker_text(new_list) # Выводим этот список
maker_text(sorted(prices)[-5:]) # Список 5 самых дорогих покупок
