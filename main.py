import pandas as pd
import os
import Graphics as G



#sitema de login
db = pd.read_csv('./data/logins.csv')
while True:
    # Começo da tela de login aqui
    email, senha, reg = G.login_UI().inicial_login_ui()

    login = False
    while True:
        if db['email'].isin([email]).any():
            pssword = db.loc[db['email'] == email, 'senha'].values[0]
            if pssword == senha:
                login = True

            else:
                # Ao usar uma string em um if ele já verifica se ela foi preenchida
                if email or senha:
                    email, senha, reg = G.login_UI(error=True).inicial_login_ui()


        else:
            if email or senha:
                email, senha, reg = G.login_UI(error=True).inicial_login_ui()

        if login:
                dataFrame = pd.read_csv('./data/data.csv')

                # Incrementar a UI aqui

                G.menu(dataFrame)

                while True:
                    userInput = input('Digite um numero')
                    match userInput:
                        case '3':
                            nomeDoVendedor = input('Digite o Nome do Novo Vendedor -> ').replace(' ', '-')
                            print(f'{nomeDoVendedor}')
                            os.mkdir(f'./vendedores/{nomeDoVendedor}')
                            with open(f'vendedores/{nomeDoVendedor}/{nomeDoVendedor}-tab.csv', 'w') as f:
                                f.write(' ')

                    # Busca pelo conteúdo da tabela do vendedor
                        case '4':
                            nomeDoVendedor = input('Insira o Nome do Vendedor -> ').replace(' ', '-')
                            if os.path.exists(f'./{nomeDoVendedor}'):
                                dbVendedor = pd.read_csv(f'./{nomeDoVendedor}/{nomeDoVendedor}-tab.csv')
                                print(dbVendedor)

                            else:
                                print('Vendedor Não Encontrado')

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
        if reg:
            break

                        # A UI Vai Até Aqui



        #Aqui começa a tela de registro
    try:
        nome, senha, email = G.login_UI().register()
            # Sistema básico contra SQLInjection
        erroChar = False

        if not erroChar:
            if not db['email'].isin([email]).any():
                index = len(db['email'])
                db.loc[index, 'nome'] = nome
                db.loc[index, 'email'] = email
                db.loc[index, 'senha'] = senha

                db.to_csv('./data/logins.csv', index=False)
            else:
                nome, senha, email = G.login_UI(error=True).register()
        else:
            print('Erro. Não é permitido caracteres especiais como : ";", ">", "<", ";", ":"')
            break
    except:
        print('Tela de Registro Fechada')