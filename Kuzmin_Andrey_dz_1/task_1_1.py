duration = int(input('Enter your time in seconds: '))
day = duration // 86400
hour = (duration % 86400) // 3600
minute = (duration % 3600) // 60
second = duration % 60
if duration >= 86400: # если время больше одного дня, то выводим принт дн...
    print ('{} дн {} час {} мин {} сек'.format(day, hour, minute, second))
elif duration >= 3600: # если время больше одного часа, то выводим принт час...
    print('{} час {} мин {} сек'.format(hour, minute, second))
elif duration >= 60: # если время больше одной минуты, то выводим принт мин...
    print('{} мин {} сек'.format(minute, second))
else:
    print('{} сек'.format(second))
