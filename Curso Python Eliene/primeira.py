print("Hello 'super' Word")


'''
comentario dsdsndsnd




#---------- variavel com string
nome= "Eliene Mesquita Martins"
#nome= 'Eliene Mesquita Martins' ( o texto pode estar entre aspas simples ou duplas)
print(nome)

#---------- variavel com int
idade_do_usuario = 32
print(idade_do_usuario)

#----------operando as variaveis

total = idade_do_usuario + idade_do_usuario 
print("idade total é "+ str(total))


#  trabalhando com os inputs(input=entrada)
escolha = input("Qual a cor da sua camiseta?")
print("sua camiseta ", escolha, " é muito bonita")


# instrução de descisão
media = input('Qual a sua média final?')           
media = int(media)
if media >= 7: #dois pontos= então
    print("aprovado")
else:    
    print("reprovado")
''' #finaliza aqui o comentario
#instruções de loopings

contador = 0
rodar = True #ctrlC pára o looping

while rodar: #enquanto o rodar for true, faça
    print(contador)
    contador = contador + 1
    if contador == 10: #o resultado vai aparecer de 1 a 9, pq conta a partir do 0
        rodar = False 
print('fim do sistema')        





