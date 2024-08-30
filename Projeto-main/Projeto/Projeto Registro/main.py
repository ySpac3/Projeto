import pandas as pd
import Graphics as G


#sitema de login
db = pd.read_csv('./data/data.csv')
while True:
    try:
        r = int(input('O que deseja fazer?\nRegistrar - 1 Logar - 2 '))
    except TypeError: # Adicionei o Except Correto
        print('Comando invalido tente novamente')

    match r:
        case 1:
            # input() já retorna str
            chars = [' ', ';', '>', '<', ';', ':'] # Caracteres especiais, que vão ajudar a tratar ataques de SQLInjection
            nome = input('Digite seu nome ')
            senha = input('Digite sua senha ')
            email = input('Digite seu email ')
            
            # Sistema básico contra SQLInjection
            erroChar = False
            for inp in [nome, senha, email]:
                if any(char in inp for char in chars):
                    erroChar = True

            if not erroChar:
                if not db['email'].isin([email]).any():
                    index = len(db['email'])
                    db.loc[index, 'nome'] = nome
                    db.loc[index, 'email'] = email
                    db.loc[index, 'senha'] = senha

                    db.to_csv('./data/data.csv', index=False)
                else:
                    print('Erro. Email já cadastrado')
            else:
                print('Erro. Não é permitido caracteres especiais como : ";", ">", "<", ";", ":"')
        case 2:
            email, senha = G.interface('', '')

            login = False
            if db['email'].isin([email]).any():
                pssword = db.loc[db['email'] == email, 'senha'].values[0]
                if pssword == senha:
                    login = True

                else:
                    print('Senha Incorreta')
            
            else:
                print('Email não encontrado')
        
            if login:
                break
            else:
                print('Não entrado, Verifique se o email esta correto ou registre-se')
