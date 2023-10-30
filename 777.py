# дЕКОРАТОР СТРУКТУРНЫЙ

from abc import ABC, abstractmethod

class Povedenie(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def eat(self):
        pass

class Animal(Povedenie):
    def move(self):
        print('я двигаюсь')
        pass
    def eat(self):
        print('я ем еду')
        pass

class AbsDecorator(Povedenie):     # декоратор позволяет одеть несколько оболочек на объект
    def __init__(self, object):
        self.object=object

    def move(self):
        self.object.move()
    def eat(self):
        self.object.eat()

class Swim(AbsDecorator): # оболочка
    def move(self):
        print('я плаваю')

class Fly(AbsDecorator):  # оболочка
    def move(self):
        print('я летаю')

class Predator(AbsDecorator):  # оболочка
    def eat(self):
        print('Я ем мясо')
class travo(AbsDecorator):   # оболочка
    def eat(self):
        print('Я ем траву')

ani=Animal()
ani.eat()
ani=Fly(ani)
ani.move()
ani = Predator(ani)
ani.move()
ani.eat()