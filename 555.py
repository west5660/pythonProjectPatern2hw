from abc import ABC, abstractmethod

class Iweapon(ABC):
    @abstractmethod
    def fire(self):
        pass

class Rocket(Iweapon):
    def fire(self):
        print('стреляю ракетой')

class Laser(Iweapon):
    def fire(self):
        print('стреляю лазером')

class Ienergy(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def load(self):
        pass

class Atom(Ienergy):
    def generate(self):
        print("работает реактор")
    def load(self):
        print('запрвился ураном')

class Diesel(Ienergy):
    def generate(self):
        print('работат двигатель')

    def load(self):
        print('заправился бензином')

class Transformer():
    def installGun(self,gun):
        self.mygun = gun

    def installEnergy(self,enr):
        self.myenergy = enr

fedor = Transformer()
gun1 = Laser()
fedor.installGun(gun1)
reactor1 = Diesel()
fedor.installEnergy(reactor1)
fedor.mygun.fire()
fedor.myenergy.load()

class Factory():
    def constructRA(self):
        robot=Transformer()
        gun=Rocket()
        reaktor=Atom()
        robot.installGun(gun)
        robot.installEnergy(reaktor)
        return robot

myfactory = Factory()
mega = myfactory.constructRA()
mega.mygun.fire()
mega.myenergy.load()