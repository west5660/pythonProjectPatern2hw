class Ship:
    def __init__(self, name, gun, speed):      #супер класс
        self.name = name
        self.gun = gun
        self.speed = speed
        self.distance = 0

    def run(self, distance):
        self.distance += distance
        print(f"{self.name} проплыл {distance} миль.")

    def yakor(self):
        print(f"{self.name} отдал якорь и пришвартовался в порту.")


class Frigate(Ship):
    def __init__(self, name):
        super().__init__(name, gun=20, speed=30)                 #вызываем супер класс с параметрами

    def fire(self):
        print(f"{self.name} выпустил залп из {self.gun} пушек!")


class Yacht(Ship):
    def __init__(self, name):
        super().__init__(name, gun=2, speed=10)                   #вызываем супер класс с параметрами

    def fire(self):
        print(f"{self.name} выпустил залп из {self.gun} пушек!")


# Создаем корабли
ship = Ship("Обычный корабль", gun=0, speed=20)
frigate = Frigate("Фрегат 'Крутой'")
yacht = Yacht("Яхта 'Мелкая'")

# Функции с короблями
ship.run(100)
ship.yakor()

frigate.run(150)
frigate.fire()
frigate.yakor()

yacht.run(50)
yacht.fire()
yacht.yakor()

