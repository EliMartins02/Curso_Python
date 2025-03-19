import sqlite3 as meu_bd

#conectar ao banco de dados ( ou criar um novo, se existir)
def conectar_banco():
    conexao =  meu_bd.connect('meu_banco.db') #nome do banco
    return conexao

#criar a tabela
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )    
   ''' )
    conexao.commit()
    conexao.close()

#inserir dados na tabela 
def inserir_usuario(lala_nome, lala_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO usuarios (nome, idade) VALUES (?, ?) 
    ''',(lala_nome, lala_idade))
    conexao.commit()
    conexao.close()

#ler dados do banco de dados
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios ") # O * é = a tudo, selecione tudo da tb usuarios...
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

#atualizar usuario
def atualizar_dados(id, novo_nome, nova_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios 
        SET nome = ?, 
            idade = ?
        WHERE id = ?
''', (novo_nome, nova_idade, id))
    conexao.commit()
    conexao.close()

#excluir usuario
def excluir_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    DELETE FROM usuarios
    WHERE id = ?                
''', (id,))
    conexao.commit()
    conexao.close()

#criando a tabela (ATENÇÃO: EXECUTEM APENAS UMA VEZ!!!)
#criar_tabela()

#inserir alguns usuarios
#inserir_usuario('Caio','55')

#atualizar dados
#atualizar_dados(1, "cah", 66)

#excluir dados
#excluir_usuario(3)

#listar todos os usuarios
#listar_usuarios()

def perguntar_e_inserir():
    while True:
        try:
            nome = input("Qual o seu nome? ")
            idade= int(input("Qual a idade? "))
            inserir_usuario(nome, idade)
            listar_usuarios()
            continuar = input("Deseja cadastrar outro usuario? \n (S/N): "). lower() # .upper()
            if continuar != "s":
                break
        except ValueError:
            print("Erro: a idade deve ser um numero inteiro")
        except Exception as deu_ruim:
            print(f"Ocorreu um erro: {deu_ruim}")

perguntar_e_inserir()




""" executar = True 
nome = input("Qual o seu nome?")
idade= input("Qual a idade?")
input("Deseja cadastrar outro usuario"?) """



""" qual o novo Novo nome, 
nova idade 
input = recebe a info
if inserir o novo nome 
quer cadastrar outro, se sim repete
for ou while """