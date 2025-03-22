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

fig = px.bar(
    df_organizado,
    x = "Media",
    y = "Valor",
    color = "Media",
    title = 'Distribuição de vendas',
    labels = {'Media': "Media", "Valor":"Vendas"}, 
    text = "Valor",
    template = "plotly_dark" 
)

#salvar grafico como jpeg
fig.write_image ('meu_grafico_pronto.jpeg')

#salvar o dataframe como uma planilha do excel
df_organizado.to_excel('minha_base_organizada.xlsx', index=False) #False mantem a serie..1,2,3

fig.show()

#pip install kaleido
