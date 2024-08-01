'''import integracao_sql as i_sql
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

def autenticar(login, senha):
    # Verifica se o login pertence a um administrador
    cursor.execute("SELECT login, senha FROM administrador WHERE login = %s", (login,))
    admin = cursor.fetchone()
    
    if admin:
        senha_criptografada = sha256(senha.encode()).hexdigest()
        if senha_criptografada == admin[1]:
            return "Bem-vindo ADM", True
        else:
            return "Senha incorreta, tente novamente", False

    # Verifica se o login pertence a um usuário
    cursor.execute("SELECT nome, senha FROM usuario WHERE nome = %s", (login,))
    user = cursor.fetchone()

    if user:
        senha_criptografada = sha256(senha.encode()).hexdigest()
        if senha_criptografada == user[1]:
            return "Bem-vindo usuário", True
        else:
            return "Senha incorreta, tente novamente", False

    return "Login inválido, tente novamente", False'''