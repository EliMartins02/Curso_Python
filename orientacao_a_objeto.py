class Carro: #definição de classe
    def __init__(self, modelo, cor):
    #atributos do carro
        self.modelo = modelo
        self.cor = cor 
        self.velocidade = 0
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        #self.velocidade = self.velocidade + incremento
        print(f"O carro {self.modelo} acelerou para {self.velocidade} Km/h.")

    def parar(self):
        self.velocidade = 0
        print(f"O carro { self.modelo} parou.")


    # criar o carro
meu_carro = Carro("Fusca", "Azul")
carro_do_instrutor = Carro("Suzuki Jimmy", "Amarelo")

    # usar os métodos
meu_carro.acelerar(20) #acelerar mais 20 km/h
meu_carro.acelerar(30) #acelerar mais 30 km/h    
meu_carro.parar()

carro_do_instrutor.acelerar(5)
carro_do_instrutor.parar()