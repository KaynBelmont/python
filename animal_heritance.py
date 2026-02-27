class Animal:
    def __init__ (self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o(a) {self.especie} chamado(a) {self.nome}, e eu sou {self.cor}')

class Gato(Animal):
    def emit_sound(self):
        print('Miau!')
    def arranhar(self):
        print(f'{self.nome} arranha doído!')

class Cachorro(Animal):
    def emit_sound(self):
        print('Au au!')

class Elefante(Animal):
    def emit_sound(self):
        print('PFFFFFFFFFFFFFFFFT!')


gato1 = Gato('Oliver', 'Preto', 'Maine coon')
gato1.apresentar()
gato1.emit_sound()
gato1.arranhar()
print('-------------------------')
cachorro1 = Cachorro('Alfredo', 'Caramelo', 'Vira-lata')
cachorro2 = Cachorro('Princesa', 'Preta', 'Vira-lata')
cachorro1.apresentar()
cachorro2.apresentar()
cachorro1.emit_sound()
print('-------------------------')
elefante1 = Elefante('Jorge', 'Cinza', 'Africano')
elefante1.apresentar()
elefante1.emit_sound()