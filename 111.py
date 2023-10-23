
class Turtle():
    speed=10
    def run(self):
        print('бежит со скоростью ', self.speed)

    def __init__(self, name, color='blue'):
        self.myname = name
        self.mycolor = color

leo  = Turtle('leo')
leo.run()
print(leo.myname,leo.mycolor)

don=Turtle('don','violety')
print(don.myname, don.mycolor)

'''
фбстракция
наследование
полиморфизм
инкапсуляция
'''