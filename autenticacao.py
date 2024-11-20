from flask import *
from hashlib import sha256

def autenticar(login, senha, mysql):
    cursor = mysql.connection.cursor()
    senha_criptografada = sha256(senha.encode()).hexdigest()
    
    cursor.execute("SELECT senha FROM administrador WHERE login = %s", (login,))
    admin_senha = cursor.fetchone()

    if admin_senha:
        if senha_criptografada == admin_senha[0]:
            session['dynamic'] = 'adm'
            return redirect(url_for('admin_dashboard'))

    cursor.execute("SELECT senha FROM usuario WHERE nome = %s", (login,))
    user_senha = cursor.fetchone()

    if user_senha:
        if senha_criptografada == user_senha[0]:
            session['dynamic'] = 'user'
            return redirect(url_for('user_dashboard'))

    return render_template('main.html', error='Invalid username/password')
