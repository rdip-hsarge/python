def text_maker(some_list): # Функция которая выводит цены в одну строку, через запятую
    for i in range(len(some_list)):
        if some_list[i][1] < 10:
            print(f'{some_list[i][0]} rub 0{some_list[i][1]} cop', end=', ')
        else:
            print(f'{some_list[i][0]} rub {some_list[i][1]} cop', end=', ')
    print('\n')

prices = [19.24, 45.93, 5.26, 1.09, 24.17, 84.13, 91.11, 44.75, 9.44, 68.14, 7.95, 44.74, 50.79, 21.8, 13.69]
update_prices=[]

for i in range(15):
    update_prices.append([int(prices[i]), round(prices[i]*100 % 100)]) # Обновленный список где каждый элемент - список [Рубли, копейки]
text_maker(update_prices)
#print(id(update_prices))

update_prices.sort() # Сортируем список в порядке возрастания
text_maker(update_prices)
#print(id(update_prices)) # и строка (15) для проверки - является ли отсортированный список, тем же объектом - ДА

new_prices=update_prices.copy() # Копируем список цен
new_prices.sort(reverse=True)   # Сортируем в порядке убывания
text_maker(new_prices)

text_maker(update_prices[len(update_prices)-5:len(update_prices)]) # Вывод 5 самых дорогих товаров