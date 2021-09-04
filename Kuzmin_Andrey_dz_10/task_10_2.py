from abc import abstractmethod, ABC

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    def __init__(self, v):
        self.veight = v

    @property
    def consumption(self):
        return round(self.veight/6.5 + 0.5, 2)

class Suit(Clothes):

    def __init__(self, h):
        self.height = h

    @property
    def consumption(self):
        return round(self.height*2 + 0.3, 2)

a = Suit(46)
print(a.consumption)