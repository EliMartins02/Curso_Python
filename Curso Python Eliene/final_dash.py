import dash 
from dash import dcc, html 
import plotly.graph_objs as go

#iniciar nosso aplicativo dash
app = dash.Dash()

#definir nosso layout do dashboard
app.layout = html.Div([
    html.H1("Grafico interativo com Dash e Plotly"), # H1 = titulo principal
    dcc.Graph(
        id= "grafico01",
        figure={
            'data' : [
                go.Scatter( #função do plotly que cria graficos de dispersão
                    x= [1,2,3,4,5],
                    y=[10,11,12,13,14],
                    mode= "lines+markers", # lines= grafico de linhas
                    name= "Linha 1" 
                ),
            ],
            'layout': go.Layout(
                title = "Grafico de Linha interativo",
                xaxis= {'title': 'Eixo X'}, # eixo X
                yaxis= {'title': 'Eixo Y'} # eixo Y
            )
        } 
    )
])

if __name__ == '__main__':
    app.run(debug=True)
