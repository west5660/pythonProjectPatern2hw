# наблюдатель поведенческая

class CameraSystem():
    def __init__(self):
        self.observers = set()

    def podkl(self,obs):
        self.observers.add(obs)

    def otkl(self,obs):
        self.observers.remove(obs)

    def signal(self):
        global obs
        for obs in self.observers:
        #     if 'камера' in obs.name:
        #         obs.photo()
        #     if 'турель' in obs.name:
        #         obs.fire()
            if isinstance(obs ,Camera):
                obs.photo()
            if isinstance(obs ,Turret):
                obs.fire()


from abc import ABC, abstractmethod

class PovedenieCam(ABC):                  # интерфейск камеры
    @abstractmethod
    def photo(self):
        pass

class Camera(PovedenieCam):
    def __init__(self, name):                 # сама камреа
        self.name=name
    def photo(self):
        print(self.name, 'сделала фото')

class PovedenieTur(ABC):
    @abstractmethod
    def fire(self):
        pass

class Turret(PovedenieTur):
    def __init__(self, name):
        self.name=name
    def fire(self):
        print(self.name, 'ta -ta-ta')

CamSys = CameraSystem()         #создаем систему
cam1 = Camera('камера1')        #создаем объекты
cam2 = Camera('камера2')
cam3 = Camera('камера3')
tur1 = Turret('турель1')
tur2 = Turret('турель2')
CamSys.podkl(cam1)      # подлючаем объекты к системе
CamSys.podkl(cam2)
CamSys.podkl(cam3)
CamSys.podkl(tur1)
CamSys.podkl(tur2)
CamSys.signal()         #все начинают работать