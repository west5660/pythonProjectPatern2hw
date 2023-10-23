class Transformer():
    def run(self):
        if self.fuel<=0:
            print('кончилось топливо')
            self.zapravka()
            print('заправил дизель')
        else:
            self.dist+=10
            self.fuel-=1

    def zapravka(self):
        self.fuel+=10
        print('заправился', self.diesel)

    def __init__(self):
        self.dist=0
        self.fuel=10
        self.diesel='дизель'  #publick
        self._dance='gopak'  #protected
        self.__jump='visoko'
    def onjump(self):
        return self.__jump     #енкапсуляция защищает свойство jump

fedor=Transformer()
print(fedor._dance)
print(fedor.onjump())
print(fedor.dist,fedor.fuel)
fedor.run()
fedor.run()
print(fedor.dist, fedor.fuel)

mark=Transformer()
for i in range(30):
    print(i+1, mark.dist)
    mark.run()
print('################################################')

class Autobot(Transformer):     #потомок класса Transformer
    # model = 'auto'
    def run(self):
        if self.fuel <= 0:
            print('кончилось топливо')
            self.zapravka()
            print('заправил дизель')
        else:
            self.dist += 100
            self.fuel -= 1
    def __init__(self,type='auto'):
        Transformer.__init__(self)
        self.model='robot'
        self.type = type
    def transform(self):
        if self.model!='robot':
            self.model='robor'
        else:
            self.model=self.type
        print('трансформируюсь в', self.model)


class Deseptikon(Transformer):
    def run(self):
        if self.fuel <= 0:
            print('кончилось топливо')
            self.zapravka()
            print('заправил дизель')
        else:
            self.dist += 200
            self.fuel -= 2
    def transform(self):
        if self.model!='robot':
            self.model='robor'
        else:
            self.model=self.type
        print('трансформируюсь в', self.model)

    def __init__(self, type='Samolet'):
        Transformer.__init__(self)
        self.model = 'robot'
        self.type = type

optim = Autobot('truck')
optim.run()
print(optim.dist,optim.fuel)
optim.transform()  #полиморфизм становится грузовиком и роботом
print(optim.model)
optim.transform()
print(optim.model)



mega=Deseptikon()
mega.run()
print(mega.dist,mega.fuel)
mega.transform()      #полиморфизм становится самолетом и роботом
mega.transform()
print(mega.model)