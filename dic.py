def adm():
    rename_columns = {
        'id': 'ID',
        'login': 'Login do ADM',
        'nome': 'Nome',
        'senha': 'Senha'
    }
    return rename_columns

def user():
    rename_columns = {
        'id': 'ID',
        'id_administrador': 'Código do ADM',
        'nome': 'Nome',
        'sobrenome': 'Sobrenome',
        'senha': 'Senha'
    }
    return rename_columns

def aluno():
    rename_columns = {
        'RA': 'RA do Aluno',
        'id_usuario': 'Código do Responsável',
        'nome': 'Nome',
        'sobrenome': 'Sobrenome',
        'serie': 'Série'
    }
    return rename_columns

def livro():
    rename_columns = {
        'codigo': 'Código do Livro',
        'id_usuario': 'Código do Responsável',
        'nome': 'Nome',
        'quantidade': 'Quantidade de Livros'
    }
    return rename_columns

def historico():
    rename_columns = {
        'id': 'ID',
        'RA_aluno': 'RA do Aluno',
        'codigo_livro': 'Código do Livro',
        'dataRetirada': 'Data da Retirada do Livro',
        'prazoDevolucao': 'Prazo de Devoluçãoo',
        'data_da_devolucao': 'Data da Devolução',
        'observacao': 'Observação',
        'estado': 'Pendente ou Entregue'
    }
    return rename_columns