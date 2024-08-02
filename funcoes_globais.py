'''import flet as ft
import integracao_sql as i_sql
import pandas as pd
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

def read_table(tabela):

    query = f'SELECT * FROM {tabela}'
    cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    read_table = pd.DataFrame(results, columns=columns)
    return read_table

def check_existing(tabela, coluna, valor):
    
    query = f'SELECT {coluna} FROM {tabela}'
    cursor.execute(query)
    values = [row[0] for row in cursor.fetchall()]

    if valor in values:
        print('Existente')
        return True
    else:
        print('Inexistente')
        return False
    
def update(tabela,opcao_correspondente_a_mudanca,mudanca,pk_tabela_correspondente_a_identificacao, identificacao): 
    
    if opcao_correspondente_a_mudanca == "senha":
        mudanca = sha256(mudanca.encode()).hexdigest()
                    
    query = f"UPDATE {tabela} SET {opcao_correspondente_a_mudanca} = %s WHERE {pk_tabela_correspondente_a_identificacao} = %s"
    cursor.execute(query, (mudanca, identificacao))
    conexao.commit()

    txt_confirmation_update = 'atualizado com sucesso'
    print(txt_confirmation_update)
    return txt_confirmation_update 



def delete(tabela,coluna,valor):
    query = f'DELETE FROM {tabela} WHERE {coluna} = %s'
    cursor.execute(query, (valor,))
    conexao.commit()


    
'''