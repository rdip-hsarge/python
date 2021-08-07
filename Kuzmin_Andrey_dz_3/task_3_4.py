def thesaurus_adv (*list):
    biggest_dict = {} #
    for full_name in list:
        [first_name, second_name] = full_name.split(' ') # Создаем переменные, чтобы не путаться в операциях
        if second_name[0] in biggest_dict: # Есть ли ключ по фамилии в главном словаре?
            if first_name[0] in biggest_dict[second_name[0]]: # Есть ли ключ по имени в словаре (который хранится в словаре с ключом первой буквы фамилии)
                biggest_dict[second_name[0]][first_name[0]].append(full_name)
            else:
                biggest_dict[second_name[0]].update({first_name[0]: full_name})
        else:
            biggest_dict[second_name[0]] = {first_name[0]: [full_name]}
    return biggest_dict

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
