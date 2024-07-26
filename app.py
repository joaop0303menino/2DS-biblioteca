from flask import Flask, render_template, request, redirect, url_for,session
import integracao_sql as i_sql
import pandas as pd
import inserir as ins
import funcoes_globais as devs
from datetime import datetime, timedelta
from flask_mysqldb import MySQL
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

app = Flask(__name__)

app.secret_key = f'mEninO/Oliveira/0319'


app.config['MYSQL_HOST'] = "149.100.155.154"
app.config['MYSQL_USER'] = "u895973460_carlos_gomes"
app.config['MYSQL_PASSWORD'] = "123456789Carlos_gomes"
app.config['MYSQL_DB'] = "u895973460_Biblioteca"

mysql = MySQL(app)

def read_table(tabela):
    
    cursor = mysql.connection.cursor()
    query = f'SELECT * FROM {tabela}'
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    read_table = pd.DataFrame(results, columns=columns)
    table_html = read_table.to_html(classes='dataframe table table-striped', index=False)
    return table_html

def update(tabela,opcao_correspondente_a_mudanca,mudanca,pk_tabela_correspondente_a_identificacao, identificacao): 
    
    cur = mysql.connection.cursor()
    if opcao_correspondente_a_mudanca == "senha":
        mudanca = sha256(mudanca.encode()).hexdigest()
                    
    query = f"UPDATE {tabela} SET {opcao_correspondente_a_mudanca} = %s WHERE {pk_tabela_correspondente_a_identificacao} = %s"
    cur.execute(query, (mudanca, identificacao))
    mysql.connection.commit()
    cur.close()

def delete(tabela,coluna,valor):
    query = f"DELETE FROM {tabela} WHERE {coluna} = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (valor,))
    mysql.connection.commit()
    cur.close()
    
def inserir_administrador(login, senha):
    senha_criptografada = sha256(senha.encode()).hexdigest()
    query = "INSERT INTO administrador(login, senha) VALUES (%s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (login, senha_criptografada))
    mysql.connection.commit()
    cur.close()

def inserir_usuario(nome, sobrenome, senha):
    senha_criptografada = sha256(senha.encode()).hexdigest()
    query = "INSERT INTO usuario(nome, sobrenome, senha) VALUES (%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (nome, sobrenome, senha_criptografada))
    mysql.connection.commit()
    cur.close()

def inserir_aluno(ra, nome, sobrenome, serie):
    query = "INSERT INTO aluno(RA, nome, sobrenome, serie) VALUES (%s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (ra, nome, sobrenome, serie))
    mysql.connection.commit()
    cur.close()

def inserir_livros(codigo, nome, quantidade):
    query = "INSERT INTO livro(codigo, nome, quantidade) VALUES (%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (codigo,nome,quantidade))
    mysql.connection.commit()
    cur.close()

def inserir_historico(ra, codigo_livro, obs, estado):
    data_retirada = datetime.today()
    data_devolucao = data_retirada + timedelta(days=30)

    query = "INSERT INTO historico(RA_aluno, codigo_livro, dataRetirada, dataDevolucao, observacao, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (ra, codigo_livro, data_retirada, data_devolucao, obs, estado))
    mysql.connection.commit()
    cur.close()
    

def autenticar(login, senha):
    cursor = mysql.connection.cursor()
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

#Funções adm
@app.route("/read_table_adm")
def read_table_adm():
    tabela = 'administrador'
    table = read_table(tabela)
    return render_template("read_table_adm.html",table=table)

@app.route("/create_adm", methods=['POST', 'GET'])
def create_adm():
    if request.method == 'POST':
        login = request.form.get('text')
        senha = request.form.get('password')
        inserir_administrador(login,senha)
    return render_template("create_adm.html")

@app.route("/update_adm", methods=['POST', 'GET'])
def update_adm():
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        id = request.form.get('id')
        update("administrador",opcao,alteracao,'id',id)
    return render_template("update_adm.html")

@app.route("/delete_adm", methods=['POST', 'GET'])
def delete_adm():
    if request.method == 'POST':
        id = request.form.get('text')
        delete('administrador','id',id)
    return render_template("delete_adm.html")

#Funções do usuário
@app.route("/create_usuario", methods=['POST', 'GET'])
def create_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        senha = request.form.get('password')
        inserir_usuario(nome,sobrenome, senha)
    return render_template("create_usuario.html")

@app.route("/read_table_usuario")
def read_table_usuario():  
    tabela = 'usuario'
    table = read_table(tabela) 
    return render_template("read_table_usuario.html", table=table)

@app.route("/update_usuario", methods=['POST', 'GET'])
def update_usuario():   
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        id = request.form.get('id')
        update("usuario",opcao,alteracao,'id',id)
    return render_template("update_usuario.html")

@app.route("/delete_usuario", methods=['POST', 'GET'])
def delete_usuario():   
    if request.method == 'POST':
        tabela = 'usuario'
        coluna ='id'
        id = request.form.get('text')
        delete(tabela, coluna, id)
    return render_template("delete_usuario.html")

#Funções do livro
@app.route("/create_livro", methods=['POST', 'GET'])
def create_livro():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        inserir_livros(codigo,nome,quantidade)
    return render_template("create_livro.html")

@app.route("/read_table_livro")
def read_table_livro():  
    tabela = 'livro'
    table = read_table(tabela) 
    return render_template("read_table_livro.html", table=table)

@app.route("/update_livro", methods=['POST', 'GET'])
def update_livro():  
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        codigo = request.form.get('codigo')
        update("livro",opcao,alteracao,'codigo',codigo) 
    return render_template("update_livro.html")

@app.route("/delete_livro", methods=['POST', 'GET'])
def delete_livro(): 
    if request.method == 'POST':
        tabela = 'livro'
        coluna ='codigo'
        codigo = request.form.get('text')
        delete(tabela,coluna,codigo) 
    return render_template("delete_livro.html")

#Funções do histórico
@app.route("/create_historico", methods=['POST', 'GET'])
def create_historico():   
    if request.method == 'POST':
        ra = request.form.get('ra')
        codigo = request.form.get('codigo')
        observacao = request.form.get('observacao')
        estado = request.form.get('estado')
        inserir_historico(ra, codigo, observacao, estado)
    return render_template("create_historico.html")

@app.route("/read_table_historico")
def read_table_historico():  
    tabela = 'historico'
    table = read_table(tabela)
    return render_template("read_table_historico.html", table=table)

@app.route("/update_historico", methods=['POST', 'GET'])
def update_historico():   
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        id = request.form.get('id')
        update("historico",opcao,alteracao,'id',id) 
    return render_template("update_historico.html")

@app.route("/delete_historico", methods=['POST', 'GET'])
def delete_historico(): 
    if request.method == 'POST':
        tabela = 'historico'
        coluna ='RA_aluno'
        ra = request.form.get('text')
        delete(tabela,coluna,ra)    
    return render_template("delete_historico.html")

#Funções do aluno
@app.route("/create_aluno", methods=['POST', 'GET'])
def create_aluno():  
    if request.method == 'POST':
        ra = request.form.get('ra')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        serie = request.form.get('serie')
        inserir_aluno(ra, nome,sobrenome, serie)
    return render_template("create_aluno.html")

@app.route("/read_table_aluno")
def read_table_aluno():   
    tabela = 'aluno'
    table = read_table(tabela)
    return render_template("read_table_aluno.html", table=table)

@app.route("/update_aluno", methods=['POST', 'GET'])
def update_aluno():   
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        ra = request.form.get('ra')
        update("aluno",opcao,alteracao,'RA',ra) 
    return render_template("update_aluno.html")

@app.route("/delete_aluno", methods=['POST', 'GET'])
def delete_aluno(): 
    if request.method == 'POST':
        tabela = 'aluno'
        coluna ='ra'
        ra = request.form.get('text')
        delete(tabela,coluna,ra)  
    return render_template("delete_aluno.html")

if __name__ == '__main__':
    app.run(debug=True)
