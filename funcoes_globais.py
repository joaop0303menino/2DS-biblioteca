import flet as ft
import integracao_sql as i_sql
import pandas as pd
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()

def read_table(tabela):
    try:
        query = f'SELECT * FROM {tabela}'
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        print("Resultados da query:", results)
        print("Colunas da tabela:", columns)

        read_table = pd.DataFrame(results, columns=columns)
        print("DataFrame:", read_table)

        headers = [ft.DataColumn(ft.Text(col)) for col in read_table.columns]
        rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(value))) for value in row]) for row in read_table.values]

        data_table = ft.DataTable(columns=headers, rows=rows)

        return data_table
    except:
        txt_error = f'Erro ao ver tabela {tabela}'
        print(txt_error)
        return txt_error

def check_existing(tabela, coluna, valor):
    try:
        query = f'SELECT {coluna} FROM {tabela}'
        cursor.execute(query)
        values = [row[0] for row in cursor.fetchall()]

        if valor in values:
            print('Existente')
            return True
        else:
            print('Inexistente')
            return False
    except Exception as e:
        print(f"Erro ao verificar existência: {e}")
        return False
    
def update(tabela,opcao_correspondente_a_mudanca,mudanca,pk_tabela_correspondente_a_identificacao, identificacao): 
    
    try:
        if opcao_correspondente_a_mudanca == "senha":
            mudanca = sha256(mudanca.encode()).hexdigest()
                    
        query = f"UPDATE {tabela} SET {opcao_correspondente_a_mudanca} = %s WHERE {pk_tabela_correspondente_a_identificacao} = %s"
        cursor.execute(query, (mudanca, identificacao))
        conexao.commit()

        txt_confirmation_update = 'atualizado com sucesso'
        print(txt_confirmation_update)
        return txt_confirmation_update 
    
    except:
        txt_error = f'Erro ao atualizar {mudanca}'
        return txt_error

def delete(tabela,coluna,valor):
    try:
        cursor.execute(f'DELETE FROM {tabela} WHERE {coluna} = "{valor}"')
        conexao.commit()

        txt_confirmation_remove = f'{valor} removido com sucesso'
        print(txt_confirmation_remove)
        return txt_confirmation_remove

    except:
        txt_error = f'Erro ao remover {valor}'
        return txt_error  
    
