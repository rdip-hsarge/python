class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'Full name worker: {str(self.name)} {str(self.surname)}'

    def get_total_income(self):
        return f'Total income worker: {self._income["wage"] + self._income["bonus"]}'

a=Position('Barry', 'Allen', 'courier', 35000, 5000)
print(a.get_full_name())
print(a.get_total_income())
# print(a._income)