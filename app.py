from flask import Flask, render_template, request, make_response, redirect, abort

app = Flask(__name__)

# 1ª rota 
@app.route('/')
def home():
    return render_template('index.html')

# 2ª rota - nome na URL
@app.route('/user/<nome>')
def hello_name(nome):
    return f"<h1>Hello, {nome}!</h1>"

# 3ª rota - mostra o User-Agent
@app.route('/contextorequisicao')
def contexto_requisicao():
    ua = request.headers.get('User-Agent')
    return f"Your browser is {ua}"

# 4ª rota - código de status diferente (400 Bad Request)
@app.route('/codigostatusdiferente')
def codigo_status():
    return "Bad request", 400

# 5ª rota - objeto de resposta com cookie
@app.route('/objetoresposta')
def objeto_resposta():
    resp = make_response("<h1>This document carries a cookie!</h1>")
    resp.set_cookie("meucookie", "valor")
    return resp

# 6ª rota - redirecionamento
@app.route('/redirecionamento')
def redirecionar():
    return redirect("https://ptb.ifsp.edu.br/")

# 7ª rota - abortar com 404
@app.route('/abortar')
def abortar():
    abort(404, description="Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")

if __name__ == "__main__":
    app.run(debug=True)
