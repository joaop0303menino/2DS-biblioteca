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

def read():
    dic = {
        "administrador":{
            "table": "administrador",
            "columns": "login, nome",
            "rename_columns": {
                'login': 'Login do ADM',
                'nome': 'Nome',
            }
        },
        
        "usuario":{
            "table": "usuario",
            "columns": "id, nome, sobrenome",
           "rename_columns": {
                'id': 'ID',
                'nome': 'Nome',
                'sobrenome': 'Sobrenome',
            }
        },
        
        "aluno": {
            "table": "aluno",
            "columns": "RA, nome, sobrenome, serie",
            "rename_columns": {
                'RA': 'RA do Aluno',
                'nome': 'Nome',
                'sobrenome': 'Sobrenome',
                'serie': 'Série'
            }
        },
        
        "livro":{
            "table":"livro",
            "columns": "codigo, nome, quantidade",
            "rename_columns":{
                'codigo': 'Código do Livro',
                'nome': 'Nome',
                'quantidade': 'Quantidade de Livros'
            }
        },
        
        "historico":{
            "table":"historico",
            "columns":"*",
            "rename_columns":{
                'id': 'ID',
                'RA_aluno': 'RA do Aluno',
                'codigo_livro': 'Código do Livro',
                'dataRetirada': 'Data da Retirada do Livro',
                'prazoDevolucao': 'Prazo de Devoluçãoo',
                'data_da_devolucao': 'Data da Devolução',
                'observacao': 'Observação',
                'estado': 'Pendente ou Entregue'
            }
        }
    }
    return dic