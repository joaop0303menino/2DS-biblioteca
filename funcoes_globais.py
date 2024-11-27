import pandas as pd
from hashlib import sha256
from datetime import datetime

def read_table(tabela, oq_pegar, mysql,rename_columns):
    try: 
        cursor = mysql.connection.cursor()
        query = f'SELECT {oq_pegar} FROM {tabela}'
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        read_table = pd.DataFrame(results, columns=columns)
        
        if rename_columns:
            read_table = read_table.rename(columns=rename_columns)
        
        table_html = read_table.to_html(classes='dataframe table table-striped', index=False)
        return table_html
    except:
        return f"<h1>ERROR</h1>"

def update(tabela,opcao_correspondente_a_mudanca,mudanca,pk_tabela_correspondente_a_identificacao, identificacao, mysql): 
    try: 
        cur = mysql.connection.cursor()
        if opcao_correspondente_a_mudanca == "senha":
            mudanca = sha256(mudanca.encode()).hexdigest()
                        
        query = f"UPDATE {tabela} SET {opcao_correspondente_a_mudanca} = %s WHERE {pk_tabela_correspondente_a_identificacao} = %s"
        cur.execute(query, (mudanca, identificacao))
        mysql.connection.commit()
        cur.close()
    except:
        return f"<h1>ERROR</h1>"
    
def update_historico(mudanca, identificacao_RA,identificacao_codigo, mysql): 
    try: 
        cur = mysql.connection.cursor()
        data_entrega = datetime.today()  
        query = f"UPDATE historico SET data_da_devolucao = %s, observacao = %s, estado = 'entregue' WHERE RA_aluno = %s AND codigo_livro = %s AND estado = 'pendente'"
        cur.execute(query, (data_entrega,mudanca, identificacao_RA, identificacao_codigo))
        mysql.connection.commit()
        cur.close()
    except:
        return f"<h1>ERROR</h1>"
    
    
def delete(tabela,coluna,valor, mysql):
    try:
        if valor:
            query = f"DELETE FROM {tabela} WHERE {coluna} = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (valor,))
            mysql.connection.commit()
            cur.close()
    except: 
        f"<h1>ERROR</h1>"
    