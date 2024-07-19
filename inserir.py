import integracao_sql as i_sql
from hashlib import sha256
from datetime import datetime, timedelta

cursor, conexao = i_sql.juncao_sql()

def inserir_administrador(login,senha):
    senha_criptografada = sha256(senha.encode()).hexdigest() 
    query = "INSERT INTO administrador(login, senha) VALUES (%s, %s)"
    cursor.execute(query, (login, senha_criptografada))
    conexao.commit()
    
def inserir_usuario(nome,senha,sobrenome):
    senha_criptografada = sha256(senha.encode()).hexdigest()
    query = "INSERT INTO usuario(nome,sobrenome,senha) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome,sobrenome,senha_criptografada))
    conexao.commit()
    
    
def inserir_aluno(ra,nome,sobrenome,serie):
    query = "INSERT INTO aluno(RA,nome,sobrenome,serie) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (ra,nome,sobrenome,serie))
    conexao.commit()
    
def inserir_livros(codigo_livro,nome_livro,quantidade):
    query = "INSERT INTO livro(codigo,nome,quantidade) VALUES (%s, %s, %s)"
    cursor.execute(query,(codigo_livro,nome_livro,quantidade))
    conexao.commit()  
    
def inserir_historico(RA, codigo_livro, obs, estado):  
#estado = 'pendente' ou 'entregue' 
    data_retirada = datetime.today()
    data_retirada_formatada = data_retirada.strftime("%d/%m/%y")
                        
    data_devolucao = data_retirada + timedelta(days=30)
    data_devolucao_formatada = data_devolucao.strftime("%d/%m/%y")
    
    query = "INSERT INTO historico(RA_aluno,codigo_livro,dataRetirada,dataDevolucao,observacao,estado) VALUES (%s, %s, %s, %s, %s,%s)"
    cursor.execute(query, (RA, codigo_livro, data_retirada_formatada, data_devolucao_formatada, estado, obs))
    conexao.commit()  
    
