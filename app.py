from flask import Flask, render_template, request, redirect, url_for,session
import integracao_sql as i_sql
import inserir as ins
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

app = Flask(__name__)

app.secret_key = f'mEninO/Oliveira/0319'

def autenticar(login, senha):
    senha_criptografada = sha256(senha.encode()).hexdigest()

    cursor.execute("SELECT senha FROM administrador WHERE login = %s", (login,))
    admin_senha = cursor.fetchone()

    if admin_senha:
        if senha_criptografada == admin_senha[0]:
            session['dynamic'] = 'adm'
            return redirect(url_for('admin_dashboard'))

    cursor.execute("SELECT senha FROM usuario WHERE nome = %s", (login,))
    user_senha = cursor.fetchone()

    if user_senha:
        if senha_criptografada == user_senha[0]:
            session['dynamic'] = 'user'
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
    if 'dynamic' in session and session['dynamic'] == 'adm':
        return render_template("administrador.html")
    return redirect(url_for('home'))

@app.route('/user-dashboard')
def user_dashboard():
    if 'dynamic' in session and session['dynamic'] == 'user':
        return render_template("responsavel.html")
    return redirect(url_for('home'))

@app.route("/user")
def usuario():
    return render_template("user.html")

@app.route("/livro-adm")
def livro():
    return render_template("livro.html")

@app.route("/historico-adm")
def historico():
    return render_template("historico.html")

@app.route("/aluno")
def aluno():
    return render_template("aluno.html")

@app.route("/adm")
def adm():
    return render_template("adm.html")

@app.route("/adm-adicionar", methods=['POST', 'GET'])
def adm_adicionar():
    if request.method == 'POST':
        login = request.form.get('text')
        senha = request.form.get('password')
        return ins.inserir_administrador(login,senha)
    return render_template("adm_adicionar.html")

@app.route("/adm-atualizar")
def adm_atualizar():
    return render_template("adm_atualizar.html")

@app.route("/adm-deletar")
def adm_deletar():
    return render_template("adm_deletar.html")

if __name__ == '__main__':
    app.run(debug=True)