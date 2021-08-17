tutors = ['Иван', 'Анастасия', 'Петр']
klasses = ['9А', '7В']

def my_tuple(name, group):
    while len(group)<len(name):  #Самое простое что придумал для "уравнивания" количества эл-тов участников и классов
        group.append(None)
    for name, group in zip(tutors, klasses):
        yield (name, group)

result_tuple=my_tuple(tutors, klasses)
print(type(result_tuple)) # Получаемый класс 'generator'
print(next(result_tuple), next(result_tuple), next(result_tuple), next(result_tuple)) # На 4-ый раз получим истощение: