from datetime import datetime, timedelta
from hashlib import sha256

def inserir_administrador(login,nome, senha,mysql):
    senha_criptografada = sha256(senha.encode()).hexdigest()
    query = "INSERT INTO administrador(login,nome senha) VALUES (%s,%s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (login, nome, senha_criptografada))
    mysql.connection.commit()
    cur.close()

def inserir_usuario(id, nome, sobrenome, senha,mysql):
    senha_criptografada = sha256(senha.encode()).hexdigest()
    query = "INSERT INTO usuario(id_administrador,nome, sobrenome, senha) VALUES (%s,%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (id, nome, sobrenome, senha_criptografada))
    mysql.connection.commit()
    cur.close()

def inserir_aluno(ra, nome, sobrenome, serie,mysql):
    query = "INSERT INTO aluno(RA, nome, sobrenome, serie) VALUES (%s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (ra, nome, sobrenome, serie))
    mysql.connection.commit()
    cur.close()

def inserir_livros(codigo, nome, quantidade,mysql):
    query = "INSERT INTO livro(codigo, nome, quantidade) VALUES (%s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (codigo,nome,quantidade))
    mysql.connection.commit()
    cur.close()

def inserir_historico(ra, codigo_livro, obs, estado,mysql):
    data_retirada = datetime.today()
    data_devolucao = data_retirada + timedelta(days=30)
    prazo = ""

    query = "INSERT INTO historico(RA_aluno, codigo_livro, dataRetirada, prazoDevolucao, data_da_devolucao, observacao, estado) VALUES (%s,%s, %s, %s, %s, %s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(query, (ra, codigo_livro, data_retirada, data_devolucao,prazo , obs, estado))
    mysql.connection.commit()
    cur.close()