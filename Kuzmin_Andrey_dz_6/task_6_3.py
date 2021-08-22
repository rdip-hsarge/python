from itertools import zip_longest
biggest_list = []
hobby_list = []
users_list = []
my_dict = {}

with open('users.csv', 'r', encoding='utf-8') as users,\
     open('hobby.csv', 'r', encoding='utf-8') as hobby:
    if len(users.readlines()) < len(hobby.readlines()):
        exit(1)
    else:
        users.seek(0), hobby.seek(0)
        for user in users:
            users_list.append(user.replace(',', '').replace('\n', ''))

        for hbby in hobby:
            hobby_list.append(hbby.replace('\n', ''))

        biggest_list = list(zip_longest(users_list, hobby_list))

        for data in biggest_list:
            my_dict[data[0]]=data[1]
        print(my_dict)

        with open('result.csv', 'w') as result:
            for key, val in my_dict.items():
                result.writelines(f'{key}: {val}\n')