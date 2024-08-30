import pandas as pd
import os

print('Bem Vindo ao gerenciador'.center(20))

#sitema de login
db = pd.read_csv('./data/logins.csv')
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

                    db.to_csv('./data/logins.csv', index=False)
                else:
                    print('Erro. Email já cadastrado')
            else:
                print('Erro. Não é permitido caracteres especiais como : ";", ">", "<", ";", ":"')
        case 2:
            # Fazer login pelo nome não é uma prática segura
            email = input('Digite o email ')
            senha = input('Digite a senha do usuário ')
            
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
                # Incrementar a UI aqui
                print('Opções:')
                print('1 - Upload de Arquivos Excel')
                print('0 - Sair')
                print('? - Ajuda')

                while True:
                    userInput = input(' -> ')

                    match userInput:
                        case '1':
                            xlsx = input('Caminho do Arquivo .xlsx -> ')

                            if os.path.exists(xlsx):
                                excel = pd.read_excel(xlsx)
                                dataFrame = pd.read_csv('./data/data.csv')

                                indexData = len(dataFrame['email'])

                                for i in range(len(excel)):
                                    dataFrame.loc[indexData, 'email'] = email
                                    dataFrame.loc[indexData, 'vendas'] = excel.loc[i, 'vendas']
                                    dataFrame.loc[indexData, 'item'] = excel.loc[i, 'item']
                                    dataFrame.loc[indexData, 'comissao'] = excel.loc[i, 'comissao']

                                    indexData += 1

                                dataFrame.to_csv('./data/data.csv', index=False)

                            else:
                                print('Arquivo Não Existe')

                        case '0':
                            break

                        case '?':
                            print('1 - Upload de Excel')
                            print('0 - Sair')
                            print('? - Ajuda')

                        case _:
                            print('Opção Invalida')

                        # A UI Vai Até Aqui
            else:
                print('Não entrado, Verifique se o email esta correto ou registre-se')
