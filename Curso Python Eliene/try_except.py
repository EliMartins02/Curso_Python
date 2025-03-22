def divisão(a, b):
    try:
        resultado = a / b 
        print(f'O resultado de {a} dividido por {b} é: {resultado}')

    except ZeroDivisionError:
        print ("erro de divisão por zero")

    except TypeError:
        print ("erro de tipo")

    except Exception as e:
        print (f"erro desconhecido:{e}")
    else:
        print ("divisão realizada com sucesso")
    finally: 
        print ("fim!!! Bom descanso pessoal!!!")


#teste 01: divisao normal
divisão(10,2)

#teste 02: divisao por zero
divisão(10,0)

#teste 03: divisão com tipos invalidos
divisão(10,"dois")

#teste 04: divisao com erro inesperado
divisão("dez", 2)