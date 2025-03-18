class Calculadora:
    def somar(self,*args): # *args= todos os argumentos, qualquer tipo de arg valido, qtde ilimitada
        return sum (args)
    


calc= Calculadora()
#pode passar qaulquer numero de argumentos

print(calc.somar(1,2))
print(calc.somar(1,1,2,2,3,3,4,4,))