from flask_mysqldb import MySQL

def intergracao(app):
    try:
        app.secret_key = f'mEninO/Oliveira/0319'

        app.config['MYSQL_HOST'] = "149.100.155.154"
        app.config['MYSQL_USER'] = "u895973460_carlos_gomes"
        app.config['MYSQL_PASSWORD'] = "123456789Carlos_gomes"
        app.config['MYSQL_DB'] = "u895973460_Biblioteca"

        mysql = MySQL(app)
        
        return mysql
    except:
        return f"<h1>ERROR Ao tentar se conectar ao banco de dados</h1>"