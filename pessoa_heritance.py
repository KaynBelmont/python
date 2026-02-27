class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome}, e tenho {self.idade} anos.')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} esta trabalhando como {self.cargo}!')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Olá {self.nome}, sua compra de R${valor_compra} foi aprovada! Seu saldo atual é de: R${self.saldo}')
        else:
            print('Saldo, insuficiente!')



f1 = Funcionario('Caio', 27, 'Prompt engineer')
f1.apresentar()
f1.trabalhar()
print('-------------------------')
c1 = Cliente('Vitoria', 25, 2500)
c2 = Cliente('Ana', 19, 230)
c1.apresentar()
c1.comprar(90)
print('-------------------------')
c2.comprar(500)