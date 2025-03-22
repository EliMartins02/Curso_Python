import pandas as pd
import matplotlib.pyplot as plt

# carregar o arquivo csv
df= pd.read_csv('base.csv')

# mostrar as primeiras 5 linhas
print(df.head()) #head mostra os 5 primeiros

# criar o grafico de colunas
df.plot(x= 'Vendas', y= ['TV', 'Radio', 'Jornal'], kind='bar', figsize=(10,6)) #os nomes tem que ser iguais aos do arquivo csv

# adicionando titulo e rótulos aos eixos
plt.title("Vendas com base na TV, Radio e Jornal")
plt.xlabel("Vendas")
plt.ylabel("Valor")

# exibe o grafico
plt.show()







