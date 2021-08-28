def val_checker(conditional):
    def functional(func):
        def wrapper(num):
            if not conditional(num):
                raise ValueError(f'wrong val {num}')
            else:
                return func(num)
        return wrapper
    return functional



@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))