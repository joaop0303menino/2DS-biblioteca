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