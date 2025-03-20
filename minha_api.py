from flask import Flask, render_template, request, url_for, redirect
from requests import get 

#criar o app
app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('inicio.html')

@app.route("/entrar/")
def fazer_login():
     return render_template('login.html')

@app.route("/welcome/")
def welcome():
     return render_template('welcome.html')

@app.route("/pagina403/")
def pagina403():
     return render_template('pagina403.html')

@app.route('/validador/' , methods=['POST','GET'])
def validador():
    acesso_u = "eliene"
    acesso_s = "123"
    if request.method == "POST":
        usuario = request.form['c_usuario']
        senha=request.form['c_senha']
        if usuario == acesso_u and senha == acesso_s:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))
    else:
        usuario = request.args.get('c_usuario')
        senha= request.args.get('c_senha')
        if usuario == acesso_u and senha == acesso_s:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))

        
#inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
