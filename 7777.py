# Декоратор
from abc import ABC, abstractmethod

class Vozmo(ABC):
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def kolesa(self):
        pass

    @abstractmethod
    def optika(self):
        pass

class Car1(Vozmo):
    def color(self):
        print('Авто перекрашена')
        pass
    def kolesa(self):
        print('Колеса заменили')
        pass
    def optika(self):
        print('Оптика заменена')
        pass

class AbsDecorator(Vozmo):
    def __init__(self, object):
        self.object=object

    def color(self):
        self.object.color()
    def kolesa(self):
        self.object.kolesa()
    def optika(self):
        self.object.optika()

class Lada(AbsDecorator): # оболочка
    def color(self):
        print('Авто покрашена в цвет золото инков')
    def kolesa(self):
        print('колеса стоят 13 диаметра')
    def optika(self):
        print('Оптика галоген')

class Lada2(AbsDecorator): # оболочка
    def color(self):
        print('Авто покрашена в цвет красная плесень')
    def kolesa(self):
        print('колеса стоят 14 диаметра')
    def optika(self):
        print('Оптика ксенон')

class Lada3(AbsDecorator): # оболочка
    def color(self):
        print('Авто покрашена в цвет бордо')
    def kolesa(self):
        print('колеса стоят 15 диаметра')
    def optika(self):
        print('Оптика матричные диоды')

avto1=Car1()
avto1.color()
avto1.kolesa()
avto1.optika()
avto2=Lada(avto1)
avto2.color()
avto2.kolesa()
avto2.optika()
avto3=Lada2(avto1)
avto3.color()
avto3.kolesa()
avto3.optika()
avto4=Lada3(avto1)
avto4.color()
avto4.kolesa()
avto4.optika()