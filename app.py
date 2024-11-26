from flask import *
import integracao_sql as i_sql
import autenticacao as au
import funcoes_globais as devs
import inserir as ins
import dic

app = Flask(__name__)

mysql = i_sql.intergracao(app)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/pagina-main', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('text')
        senha = request.form.get('password')
        return au.autenticar(login, senha, mysql)
    return redirect(url_for('home'))

@app.route('/collaborators')
def collaborators():
    return render_template("collaborators.html")

@app.route('/admin-dashboard')
def admin_dashboard():
    if 'dynamic' in session and session['dynamic'] == 'adm':
        entidades = dic.read()
        oq_pegar = entidades["historico"]["columns"]
        tabela = entidades["historico"]["table"]
        rename_columns = entidades["historico"].get("rename_columns", {})
        table = devs.read_table(tabela, oq_pegar,mysql=mysql, rename_columns=rename_columns)
        return render_template("administrador.html", table=table)
    return redirect(url_for('home'))

@app.route('/user-dashboard')
def user_dashboard():
    if 'dynamic' in session and session['dynamic'] == 'user':
        entidades = dic.read()
        oq_pegar = entidades["historico"]["columns"]
        tabela = entidades["historico"]["table"]
        rename_columns = entidades["historico"].get("rename_columns", {})
        table = devs.read_table(tabela, oq_pegar,mysql=mysql, rename_columns=rename_columns)
        return render_template("responsavel.html",table=table)
    return redirect(url_for('home'))

@app.route("/read/<entity>")
def read_entity(entity):
    entidades = dic.read()
    oq_pegar = entidades[entity]["columns"]
    tabela = entidades[entity]["table"]
    rename_columns = entidades[entity].get("rename_columns", {})
    try:
        table = devs.read_table(tabela, oq_pegar, mysql=mysql, rename_columns=rename_columns)
        return render_template("read.html",table=table)
    except:
        return render_template("read.html",table=table, erro="erro")
    
#Funções adm

@app.route("/create_adm", methods=['POST', 'GET'])
def create_adm():
    if request.method == 'POST':
        login = request.form.get('text')
        nome = request.form.get('name')
        senha = request.form.get('password')
        ins.inserir_administrador(login,nome, senha,mysql)
    return render_template("create_adm.html")

@app.route("/update_adm", methods=['POST', 'GET'])
def update_adm():
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        id = request.form.get('id')
        devs.update("administrador",opcao,alteracao,'id',id, mysql)
    return render_template("update_adm.html")

@app.route("/delete_adm", methods=['POST', 'GET'])
def delete_adm():
    if request.method == 'POST':
        id = request.form.get('text')
        devs.delete('administrador','id',id,mysql)
    return render_template("delete_adm.html")

#Funções do usuário
@app.route("/create_usuario", methods=['POST', 'GET'])
def create_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        senha = request.form.get('password')
        ins.inserir_usuario(id, nome ,sobrenome, senha,mysql)
    return render_template("create_usuario.html")


@app.route("/update_usuario", methods=['POST', 'GET'])
def update_usuario():   
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        id = request.form.get('id')
        devs.update("usuario",opcao,alteracao,'id',id,mysql)
    return render_template("update_usuario.html")

@app.route("/delete_usuario", methods=['POST', 'GET'])
def delete_usuario():   
    if request.method == 'POST':
        tabela = 'usuario'
        coluna ='id'
        id = request.form.get('text')
        devs.delete(tabela, coluna, id,mysql)
    return render_template("delete_usuario.html")

#Funções do livro
@app.route("/create_livro", methods=['POST', 'GET'])
def create_livro():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        ins.inserir_livros(codigo,nome,quantidade,mysql)
    return render_template("create_livro.html")

@app.route("/update_livro", methods=['POST', 'GET'])
def update_livro():  
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        codigo = request.form.get('codigo')
        devs.update("livro",opcao,alteracao,'codigo',codigo,mysql) 
    return render_template("update_livro.html")

@app.route("/delete_livro", methods=['POST', 'GET'])
def delete_livro():
    if request.method == 'POST':
        tabela = 'livro'
        coluna ='codigo'
        codigo = request.form.get('text')
        devs.delete(tabela,coluna,codigo,mysql) 
    return render_template("delete_livro.html")

#Funções do histórico
@app.route("/lend_book", methods=['POST', 'GET'])
def lend_book():   
    response_server = ' '
    if request.method == 'POST':
        try:
            ra = request.form.get('ra')
            codigo = request.form.get('codigo')
            observacao = request.form.get('observacao')
            estado = request.form.get('estado')
            ins.inserir_historico(ra, codigo, observacao, estado, mysql)
            response_server = 'Livro emprestado com sucesso'

        except Exception as e:
            response_server = f'Error: \n{e}'
            print(response_server)


    return render_template("lend_book.html", response_server=response_server)


@app.route("/return_book", methods=['POST', 'GET'])
def return_book():   
    response_server = ' '
    if request.method == 'POST':
        try:
            alteracao = request.form.get('alteracao')
            id = request.form.get('id')
            opcao = request.form.get('observacao')
            devs.update("historico", opcao, alteracao, 'id', id, mysql) 
        except Exception as e:
            response_server = f'Error: \n{e}'
            print(response_server)
    return render_template("return_book.html", response_server=response_server)

#Funções do aluno
@app.route("/create_aluno", methods=['POST', 'GET'])
def create_aluno():  
    if request.method == 'POST':
        ra = request.form.get('ra')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        serie = request.form.get('serie')
        ins.inserir_aluno(ra, nome,sobrenome, serie,mysql)
    return render_template("create_aluno.html")


@app.route("/update_aluno", methods=['POST', 'GET'])
def update_aluno():   
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        alteracao = request.form.get('alteracao')
        ra = request.form.get('ra')
        devs.update("aluno",opcao,alteracao,'RA',ra, mysql) 
    return render_template("update_aluno.html")

@app.route("/delete_aluno", methods=['POST', 'GET'])
def delete_aluno(): 
    if request.method == 'POST':
        tabela = 'aluno'
        coluna ='ra'
        ra = request.form.get('text')
        devs.delete(tabela,coluna,ra,mysql)  
    return render_template("delete_aluno.html")

if __name__ == '__main__':
    app.run(debug=True)