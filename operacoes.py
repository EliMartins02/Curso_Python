#funcao para somar dois numeros
def somar(a, b):
    return a+b # retorna a soma de a e b

def subtrair(a, b):
    return a-b # retorna a subtração de a e b

def dividir(a, b):
    if b == 0 : #verifica se o divisor é 0
        raise ValueError("Não é possivel dividir por zero, ta sabendo não??")#raise levanta o erro se b for 0
    return a / b # retorna a divisão de a e b