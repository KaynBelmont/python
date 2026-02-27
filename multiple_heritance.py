#Herança multipla E de multinível

#Classe avõ
class Animal:
    def __init__(self, nome):
        self.nome = nome

#Classes pai
class Predador(Animal):
    def cacando(self):
        print(f'O Animal {self.nome} está caçando.')

class Presa(Animal):
    def fugir(self):
        print(f'O Animal {self.nome} está fugindo!')

#Classes filho
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Presa, Predador):
    pass


coelho1 = Coelho('Buggs')
coelho1.fugir()
print('-------------------------')
tigre1 = Tigre('Kid Bengala')
tigre1.cacando()
print('-------------------------')
golfinho1 = Golfinho('Belzebu')
golfinho1.cacando()