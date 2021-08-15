from requests import get
from datetime import date
import re

def currency_rates(my_key):

    all_txt = get('http://www.cbr.ru/scripts/XML_daily.asp').text # Получаем строку из нашего запроса
    actual_data = all_txt[all_txt.index('Date') + 6:all_txt.index('Date') + 16].split('.') # В этом месте мы берем срез со всей строки и берем 10 символов "ДД.ММ.ГГГГ"
    actual_data.reverse()
    all_txt=re.split('<CharCode>|</CharCode><Nominal>|</Nominal>|<Value>|</Value>', all_txt) # Делим нашу строку по пяти разделителям
    vallute_dict={}

    for i in range(len(all_txt)): # Вот никак не смог без индексов сделать эту задачу
        if i % 5 == 1:
            key = all_txt[i]
        elif i % 5 == 2:
            nominal = float(all_txt[i])
        elif i % 5 == 4:
            value = float(all_txt[i].replace(',', '.')) # Присваиваем нашей переменной цену за валюту, меняем ее тип на float, но перед этим меняем , на .
            vallute_dict[key]=round(value/nominal, 2)
    if my_key.upper() in vallute_dict: #
        return f'Per unit of {my_key}: {vallute_dict[my_key.upper()]} rubles (at the time of {date(*list(map(lambda x: int(x), actual_data)))})'
    else:
        return None

if __name__ == '__main__': # Для выполнения только в этом модуле
    print(currency_rates('USD'))
    print(currency_rates('byn'))