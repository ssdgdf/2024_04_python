# abstraction(추상화)
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return  3.14*self.radius**2

# ractangle , triangle

class Triangle(Shape):
    def __init__(self,height,line):
        self.height = height
        self.line = line

    def area(self):
        return (self.height*self.line)*0.5

class ractangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2