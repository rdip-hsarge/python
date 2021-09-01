class Road:
    def __init__(self):
        self._weight_square_meter = 25
        self._thickness = 5

    def mass_asph(self, _length = 1, _width = 1):
        self._length = _length
        self._width = _width
        return f'{int(_length*_width*self._weight_square_meter*self._thickness/1000)} т.'

r = Road()
print(r.mass_asph(20, 5000))