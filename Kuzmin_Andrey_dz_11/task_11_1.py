class Data:
    def __init__(self, some_data):
        self.data = some_data

    @classmethod
    def sep_date(cls, some_data):
        return [int(el) for el in some_data.split('-')]

    @staticmethod
    def correct_date(some_data):
        month, year = some_data.split('-')[1:]
        if 1 > int(month) < 12 or int(year) > 0 or month.is_integer() or year.is_integer():
            return f'Correct data'
        else:
            return f'Uncorrect data'

my_data = Data('22-3-2020')
print(my_data.data) # 22-3-2020
print(type(Data.sep_date('22-3-2020')[0])) # int
print(Data.correct_date('22-3-2020')) # Correct data