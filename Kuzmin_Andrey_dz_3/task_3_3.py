def thesaurus(*list):
    letters = {}
    for name in list:
        if not name[0] in letters:
            letters.update({name[0]: [name]})
        else:
            letters[name[0]].append(name)
    return letters

print(thesaurus("Иван", "Мария", "Петр", "Илья"))