#coding=utf-8
from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self,shape):
        pass

class Line(Shape):
    name = "Line"
    def draw(self):
       self.color.paint(self)

class Red(Color):
    def paint(self,shape):
        print("Red color " + shape.name)


class Blue(Color):
    def paint(self,shape):
        print("Blue color " + shape.name)


line1 = Line(Red())
line1.draw()

line2 = Line(Blue())
line2.draw()

