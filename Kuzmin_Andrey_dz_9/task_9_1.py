from time import sleep

class TrafficLight:

    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for clr, tm in TrafficLight.__color.items():
            print(clr)
            sleep(tm)

a = TrafficLight()

a.running()