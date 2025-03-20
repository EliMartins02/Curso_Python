from flask import Flask, render_template #Flask maiusculo é o módulo 

#criação do app
app = Flask (__name__)

#rota da pagina inicial
@app.route("/")
def home():
    return "<h1>Bem-vindo ao melhor site do mundo!!!</h1>"

#rota do sobre
@app.route("/sobre")
def sobre():
    return "<a href='http://w3c.org'>Documentação do html</a>"

#rota do nome
@app.route("/ola/<nome>")#@=decorator
def ola(nome):
    return f"<h1>Olá meu querido {nome}!♥♥♥</h1>"

#rota de login
@app.route("/login")
def login():
    return "<h1> Acesso restrito!</h1>"

#inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)



