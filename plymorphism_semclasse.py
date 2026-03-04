
class Pessoa1:
    def microfone(self):
        print('Meu nome é Caio')

class Pessoa2:
    def microfone(self):
        print('Meu nome é Vitoria')

class Pessoa3:
    def microfone(self):
        print('Meu nome é Oliver')

class Pessoa4:
    def microfone(self):
        print('Meu nome é Emaline')


sala = [Pessoa1(), Pessoa2(), Pessoa3(), Pessoa4()]

for pessoas in sala:
    pessoas.microfone()
