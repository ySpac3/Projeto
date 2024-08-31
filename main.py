import pandas as pd
import os
import Graphics as G



#sitema de login
db = pd.read_csv('./data/logins.csv')
# aqui ta a função da UI
while True:
    # Começo da tela de login aqui
    email, senha = G.login_UI().inicial_login_ui()

    login = False
    while True:
        if db['email'].isin([email]).any():
            pssword = db.loc[db['email'] == email, 'senha'].values[0]
            if pssword == senha:
                login = True

            else:
                # Ao usar uma string em um if ele já verifica se ela foi preenchida
                if email or senha:
                    email, senha = G.login_UI().incorrect_login()

        else:
            if email or senha:
                email, senha = G.login_UI().incorrect_login()
            if not email and senha:
                break

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

                            indexData = len(dataFrame['vendedor'])

                            for i in range(len(excel)):
                                # Correção você não estava verificando o valor
                                dataFrame.loc[indexData, 'vendedor'] = input('Nome do Vendedor -> ')
                                dataFrame.loc[indexData, 'vendas'] = excel.loc[i, 'vendas']
                                dataFrame.loc[indexData, 'item'] = excel.loc[i, 'item']
                                dataFrame.loc[indexData, 'comissao'] = excel.loc[i, 'comissao']
                                dataFrame.loc[indexData, 'valor'] = excel.loc[i, 'valor']


                                indexData += 1

                            dataFrame.to_csv('./data/data.csv', index=False)

                        else:
                            print('Arquivo Não Existe')
                    
                    # Verificar Vendas do Vendedor
                    case '2':
                        vendedorNome = input('Nome do Vendedor -> ')
                        dataFrame = pd.read_csv('./data/data.csv')

                        indexDF = len(dataFrame['vendedor'])

                        # Verificador se foi encontrado o vendedor
                        found = False
                        for i in range(indexDF):
                            #Correção: Você estava verificando uma coluna com base no nome do vendedor
                            if dataFrame.loc[i, 'vendedor'] == vendedorNome:
                                print('Vendedor || Vendas || Item || Comissão || Valor')
                                found = True
                                print(dataFrame.loc[i, 'vendedor'], end=' ')
                                print(dataFrame.loc[i, 'vendas'], end=' ')
                                print(dataFrame.loc[i, 'item'], end=' ')
                                print(dataFrame.loc[i, 'comissao'], end=' ')
                                print(dataFrame.loc[i, 'valor'])

                    case '0':
                        break

                    case '?':
                        print('1 - Upload de Excel')
                        print('2 - Vendas do Vendedor')
                        print('0 - Sair')
                        print('? - Ajuda')

                    case _:
                        print('Opção Invalida')

                    # A UI Vai Até Aqui



    #Aqui começa a tela de registro

    chars = [' ', ';', '>', '<', ';', ':'] # Caracteres especiais, que vão ajudar a tratar ataques de SQLInjection
    nome, senha, email = G.login_UI().register()

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
