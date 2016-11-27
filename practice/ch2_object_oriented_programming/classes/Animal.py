# R-2.17
class Animal:
    def __init__(self):
        pass

class Goat(Animal):
    def __init__(self, tail):
        super().__init__()
        self._tail = tail

    def milk(self):
        pass

    def jump(self):
        pass

class Pig(Animal):
    def __init__(self, nose):
        super().__init__()
        self._nose = nose

    def eat(self, food):
        pass

    def wallow(self):
        pass

class Horse(Animal):
    def __init__(self, height, color):
        super().__init__()
        self._height = height
        self._color = color

    def run(self):
        pass

    def jump(self):
        pass

class Racer(Horse):
    def race(self):
        pass

class Equestrian(Horse):
    def __init__(self, weight):
        super().__init__()
        self._weight = weight

    def trot(self):
        pass

    def is_trained(self):
        pass




