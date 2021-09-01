class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction): # В direction указать куда поворачивает
        self.direction = direction
        return f'Машина {self.name} повернула ({direction})'

    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed}'

class SportCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed}' if self.speed < 60 else f'Превышена скорость.'

class WorkCar(Car):
    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed}' if self.speed < 40 else 'Превышена скорость.'

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed)
        self.is_police = is_police

# p = TownCar('Lada', 'black', 39)
# print(p.is_police)
# print(p.show_speed())
# print(p.go())