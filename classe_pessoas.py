class Pessoa:
    def __init__ (self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}!')

    def att_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else:
            print('A nova idade deve ser maior que a anterior!')

colaborador1 = Pessoa('Caio', 26, 'Prompt engineer I')
colaborador2 = Pessoa('Vitoria', 25, 'Assistente Administrativa I')

print('-------------------------')
colaborador1.informacoes()
colaborador1.promover('Prompt engineer II')
print('-------------------------')
colaborador2.informacoes()
colaborador2.att_idade(23)
print('-------------------------')