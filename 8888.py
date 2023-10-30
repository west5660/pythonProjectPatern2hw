# наблюдатель поведенческая

class CarSystem():
    def __init__(self):
        self.observers = set()

    def zapysk(self,obs):
        self.observers.add(obs)

    def zaglyhit(self,obs):
        self.observers.remove(obs)

    def signal(self):
        global obs
        for obs in self.observers:
            if isinstance(obs ,Car):
                obs.zap()
            if isinstance(obs ,biip):
                obs.Bip()


from abc import ABC, abstractmethod

class PovedenieCar(ABC):
    @abstractmethod
    def zap(self):
        pass

class Car(PovedenieCar):
    def __init__(self, name):
        self.name=name
    def zap(self):
        print(self.name, 'Запуск двигателя произведен')

class PovedenieBip(ABC):
    @abstractmethod
    def Bip(self):
        pass

class biip(PovedenieBip):
    def __init__(self, name):
        self.name=name
    def Bip(self):
        print(self.name, 'biiip-bbbbiiiip-biiippp')

Carsis = CarSystem()         #создаем систему
car1 = Car('Автомобиль 1 ')        #создаем объекты
car2 = Car('Автомобиль 2 ')
car3 = Car('Автомобиль 3 ')
bi1 = biip('Авто 4 ')
bi2 = biip('Авто 5 ')
Carsis.zapysk(car1)
Carsis.zapysk(car2)
Carsis.zapysk(car3)
Carsis.zapysk(bi1)
Carsis.zapysk(bi2)
Carsis.signal()

