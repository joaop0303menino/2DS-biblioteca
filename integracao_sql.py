import mysql.connector

def juncao_sql():
    mydb = mysql.connector.connect(
        host="149.100.155.154",
        user="u895973460_carlos_gomes",
        password="123456789Carlos_gomes",
        database="u895973460_Biblioteca"
    )
    
    try:
        print('Conexão bem sucedida')
        cursor = mydb.cursor()
        return cursor, mydb
    except:
        return "Erro na conexão"


