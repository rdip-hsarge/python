def type_logger(func):

    def wrapper(*args):
        for el in args:
            print(el, type(el), end=', ')
    return wrapper


@type_logger
def calc_cube(x):
    # for el in args:
    #     return el ** 3
    return x ** 3

print(calc_cube(5, 5.5, '8'))
