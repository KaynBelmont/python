class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def add_motor(self, motor):
        self.motores.append(motor)

    def list_motores(self):
        for motor in self.motores:
            print(f'Marca:{motor.marca} - {motor.potencia} cavalos!')


#Criar os Motores (objetos)
motor_v6 = Motor('Ford', 300)
motor_v8 = Motor('Ferrari', 650)
motor_v12 = Motor('Lamborghini', 950)


#Criar o Carro e adicionar o Motor
carro = Carro()
carro.add_motor(motor_v6)
carro.add_motor(motor_v8)
carro.add_motor(motor_v12)


#Listar os Motores
carro.list_motores()