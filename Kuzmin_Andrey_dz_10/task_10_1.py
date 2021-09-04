class Matrix:

    def __init__(self, big_list):
        self.big_list = big_list

    def __str__(self, input_list = None):
        my_list = input_list if input_list else self.big_list
        my_str = ''
        for list in my_list:
            my_str += ''.join(str(list)).replace(',', ' ').replace('[', '').replace(']', '') + '\n'
        return my_str

    def __add__(self, other):
        result = []
        if len(self.big_list) == len(other.big_list):
            for first_list, second_list in zip(self.big_list, other.big_list):
                if len(first_list) == len(second_list):
                    result_list = [] # Список, который пересоздается при смене строки, сюда мы будем суммировать
                    for first_el, second_el in zip(first_list, second_list):
                        result_list.append(first_el + second_el)
                    result.append(result_list) # После прохода строки, мы добавляем список в результ. список
                else:
                    print('Некорректные размеры матриц')
                    exit()
            return Matrix(result)
        else:
            print('Некорректные размеры матриц')
            exit()

a = Matrix([[2, 3, 43], [3, 5, 65], [3, 5, 34]])
b = Matrix([[3, 422, 2], [52, 5, 543], [3, 444, 4]])
c = Matrix([[3, 4, 5], [2, 2, 2]])

print(a + b) # Выведется объект класса Matrix
print(a + c) # Некорректные размеры матриц