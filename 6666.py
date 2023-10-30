#фабрика
from abc import ABC, abstractmethod

class Car1(ABC):
    @abstractmethod
    def edet(self):
        pass
    @abstractmethod
    def razgon(self):
        pass
    @abstractmethod
    def tormozit(self):
        pass
    @abstractmethod
    def edetzad(self):
        pass

class Enemy(Car1):
    def __init__(self, a, b, c, d):
        self.speed = a
        self.raz = b
        self.tor =c
        self.zad = d
    def edet(self):
        print('Максимальная скорость авто ', self.speed)
        pass
    def razgon(self):
        print('Разгоняется до 100 за ', self.raz)
        pass

    def tormozit(self):
        print('Длина тормозного пути ', self.tor)
        pass

    def edetzad(self):
        print('Возможность ехать задом ', self.zad)
        pass

class Lada(Enemy):    # подкласс
    def __init__(self,):  # при создании объекта
        super().__init__('180 км/ч' ,'16 сек','8 метров при тормежении от скорости 100 км/ч','имеется')  # запускает инит из родительского класса

class Audi(Enemy):    # подкласс
    def __init__(self,):  # при создании объекта
        super().__init__('260 км/ч' ,'7 сек','5 метров при тормежении от скорости 140 км/ч','имеется')  # запускает инит из родительского класса

class Zavod():   # может создавать объекты
    def create(self, name):
        if name=='lada':
            return Lada()
        elif name == 'Audi':
            return Audi()
        else:
            return 'неизвестный тип'

myzavod = Zavod()
avto1 = myzavod.create('lada')
avto1.edet()
avto1.edetzad()
avto1.razgon()
avto1.tormozit()
avto2 = myzavod.create('Audi')
avto2.edet()
avto2.edetzad()
avto2.razgon()
avto2.tormozit()

