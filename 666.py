'''
2 рекомендации
- использовать код повторно
- делайте код с учетом будущего расширения

паттерны
порождающие - про создание новых объектов
структурные - про иерархию классов
поведенческие - про взаимодействия объектов
'''

# Фабрика

from abc import ABC, abstractmethod

class Povedenie(ABC):
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def attack(self):
        pass

class Povedenie2(ABC):
    @abstractmethod
    def run(self):
        pass

class Enemy(Povedenie):
    def __init__(self, a, b):
        self.weapon = a
        self.speed = b
    def run(self):
        print('бежит', self.speed)
        pass
    def attack(self):
        print('дерется', self.weapon)
        pass

en1=Enemy('topor','sred')
en1.run()
en1.attack()

class Goblin(Enemy):    # подкласс
    def __init__(self,):  # при создании объекта
        super().__init__('nozhik' ,'bistro')  # запускает инит из родительского класса

class Troll(Enemy):
    def __init__(self):
        super().__init__('dubina','medlit')

class Factory():   # может создавать объекты
    def create(self, name):
        if name=='goblin':
            return Goblin()
        elif name == 'troll':
            return Troll()
        else:
            return 'неизвестный тип'

myfactory=Factory()
en2 = myfactory.create('goblin')
en2.run()
en3 = myfactory.create('troll')
en3.run()


