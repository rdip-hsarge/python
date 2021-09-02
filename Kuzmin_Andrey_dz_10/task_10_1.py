class Matrix:

    def __init__(self, big_list):
        self.big_list = big_list

    def __add__(self, other):
        result = []
        for first_list, second_list in self.big_list, other:
            result_list = []
            for first_el, second_el in first_list, second_list:
                # result.append(first_el + second_el)
                result_list.append(first_el + second_el)
                # return first_el + second_el
            result.append(result_list)
        return result

a = Matrix([[2, 3], [3, 5]])
b = Matrix([[3, 4], [5, 5]])

print(a + b)