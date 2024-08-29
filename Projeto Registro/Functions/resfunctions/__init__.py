import mysql.connector

def resconfirmation(nome,senha,email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='Standart',
        password='101520cC',
        database='registertable',
    )
    try:
        cursor = conexao.cursor()
        comando = f'SELECT * FROM users WHERE Email = "{email}" OR Name = "{nome}"'
        cursor.execute(comando)
        resultado = cursor.fetchone() # ler o banco de dados
        if resultado is None:
            comando = f'INSERT INTO users (Name, Passworld, Email) VALUES ("{nome}", "{senha}", "{email}")'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados
            print('Parabéns Usuario Registrado')
        elif email in resultado:
            print('Email já cadastrado tente outro')
        elif senha in resultado:
            print('Nome de Usuario ja Cadastrado tente outro')
    finally:
        cursor.close()
        conexao.close()

def logconfirmantion(nome='',senha=''):
    conexao = mysql.connector.connect(
        host='192.168.15.4',
        user='Standart',
        password='101520cC',
        database='registertable',
    )
    try:
        cursor = conexao.cursor()
        comando = f'SELECT * FROM users WHERE Name = "{nome}" AND Passworld = "{senha}"'
        cursor.execute(comando)
        resultado = cursor.fetchone()
        if nome and senha in resultado:
            return True
    except:
        return False
    finally:
        cursor.close()
        conexao.close()
