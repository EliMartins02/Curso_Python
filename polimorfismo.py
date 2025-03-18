class Animal: #classe base
    def fazer_som(self):
        pass 

class Cachorro(Animal):#sublasse ou classe herdada
    def fazer_som (self):
        return "Auu au"

class Gato(Animal):#ublasse ou classe herdada
    def fazer_som (self):
         return "Meow"
#usando o polimorfismo
def fazer_animal_falar(animal: Animal):
    print(animal.fazer_som())
#criando os objetos
cachorro= Cachorro()
gato= Gato()
#chama o metodo de cada animal de forma polimorfica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)  
#Cachorro e Gato ( maiusculo) são nomes de classes e cachorro e gato são instâncias de objetos (variáveis) que são criadas a partir das classes, então começam com letra minúscula.