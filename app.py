from flask import Flask, render_template, request, redirect, url_for
import integracao_sql as i_sql
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

app = Flask(__name__)

def autenticar(login, senha):
    senha_criptografada = sha256(senha.encode()).hexdigest()

    cursor.execute("SELECT senha FROM administrador WHERE login = %s", (login,))
    admin_senha = cursor.fetchone()

    if admin_senha:
        if senha_criptografada == admin_senha[0]:
            return redirect(url_for('admin_dashboard'))

    cursor.execute("SELECT senha FROM usuario WHERE nome = %s", (login,))
    user_senha = cursor.fetchone()

    if user_senha:
        if senha_criptografada == user_senha[0]:
            return redirect(url_for('user_dashboard'))

    return render_template('main.html', error='Invalid username/password')

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/pagina-main', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('text')
        senha = request.form.get('password')
        return autenticar(login, senha)
    return redirect(url_for('home'))

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template("administrador.html")

@app.route('/user-dashboard')
def user_dashboard():
    return render_template("responsavel.html")

@app.route("/user")
def usuario():
    return render_template("user.html")

@app.route("/livro-adm")
def livro():
    return render_template("livro.html")

@app.route("/historico-adm")
def historico():
    return render_template("historico.html")

if __name__ == '__main__':
    app.run(debug=True)