class Stationery:

    title = 'Какое-то название'

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):

    def draw(self):
        return f'Запуск отрисовки РУЧКОЙ'

class Pencil(Stationery):

    def draw(self):
        return f'Запуск отрисовки КАРАНДАШОМ'

class Handle(Stationery):

    def draw(self):
        return f'Запуск отрисовки МАРКЕРОМ'

a, b, c = Pen(), Pencil(), Handle() # записано в строчку, только потому что мало переменных

print(a.draw(), b.draw(), c.draw(), sep='\n')
