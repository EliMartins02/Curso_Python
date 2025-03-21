import pandas as pd 
import plotly.express as px #plotly faz gráficos mais completos, melhor visual

df= pd.read_csv('base.csv')
print(df.head()) # para ter certeza que carregou

#reorganizar dados
df_organizado = pd.melt(
                        df,
                        id_vars=  ["Vendas"],
                        value_vars= ['TV', 'Radio', 'Jornal'],
                        var_name = "Media",
                        value_name = "Valor"
                        )

print(df_organizado.head())

# criar grafico de pizza interativo, pie=torta em inglês 
fig = px.pie(
                df_organizado, #df=tabela
                values = "Vendas",
                names = "Media", # se fosse 1 valor apenas, não precisa de []
                title = 'Distribuição de vendas', #se tiver + de  item, coloca dentro do []
                hole = 0.3 #deixa um centro vazio para o grafico de pizza do tipo dunut
                 )
            
fig.show() #visualizar o gráfico