import unittest #unittest= framework de testes unitários do Python.

# importa as funcoes de operações do arquivo operações.py
from operacoes import somar, subtrair,  dividir #, multiplicar

class testar_operacoes(unittest.TestCase): #dentro da class criamos as funçoes... def. TestCase está em maiusculo por causa do CamelCase
    # testa a operação de soma
    def testar_somar(self): 
        # testa se 2+3 é 5
        self.assertEqual(somar(2,3),5)
        # testa se a soma de -1 e 1 é 0
        self.assertEqual(somar(-1,1),0)
        #verifica se a soma de -2 e -3 é -5
        self.assertEqual(somar(-2,-3),-5)

    def testar_dividir(self):
        # verifica se a divisão de 6 por 2 é 3
        self.assertEqual(dividir(6,2),3)

        # verifica se a divisão de 6 por 3 é -2
        self.assertEqual(dividir(-6,3),-2)

        # verifica se a divisão por zero levanta o erro correto
        with self.assertRaises(ValueError):
                dividir(1,0) #espera-se que levante o valueerror quando tentar dividir por zero


if __name__ == '__main__': #por causa do framework, precisa usar isso, pois inicia a execução dos testes.
    unittest.main() #executa todos os testes definidos na classe



