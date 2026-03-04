class Classes():
    def falar(self):
        print('Eu sou uma classe')
    

class Warrior(Classes):
    def falar(self):
        print('Eu sou um warrior ARMS')

class Mage(Classes):
    def falar(self):
        print('Eu sou um mage FIRE')

class Hunter(Classes):
    def falar(self):
        print('Eu sou um hunter BM')



classes = [Warrior(), Mage(), Hunter()]

for c in classes:
    c.falar()
