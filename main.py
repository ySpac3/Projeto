import pandas as pd
import os
import Graphics as G
import verificacao as SQLInjection


#sitema de login
db = pd.read_csv('./data/logins.csv')
while True:
    # Começo da tela de login aqui
    email, senha, reg = G.login_UI().inicial_login_ui()

    login = False
    while True:
        # Me dei conta que isso daqui não é gambiarra, nem artimanha nem maracutaia. É assim mesmo
        #setafuncionandonãomexe
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
                print('Opções:')
                print('1 - Upload de Arquivos Excel')
                print('0 - Sair')
                print('? - Ajuda')
                G.menu(dataFrame)
                userInput = input('input')
                while True:
                    print(userInput)
                    match userInput:
                        case '1':
                            xlsx = input('Caminho do Arquivo .xlsx -> ')

                            if os.path.exists(xlsx):
                                excel = pd.read_excel(xlsx)
                                dataFrame = pd.read_csv('./data/data.csv')

                                indexData = len(dataFrame['vendedor'])

                                for i in range(len(excel)):
                                    # Não achei o erro que você estava dizendo

                                    nomeDoVendedor = input('Nome do Vendedor -> ')
                                    vendas = excel.loc[i, 'vendas']
                                    item = excel.loc[i, 'item']
                                    comissao = excel.loc[i, 'comissao']
                                    valor = excel.loc[i, 'valor']

                                    tryAgainSQLInjection = False
                                    for inp in [nomeDoVendedor, vendas, item, comissao, valor]:
                                        if not SQLInjection.antiSQLInjection(inp):
                                            dataFrame.loc[indexData, 'vendedor'] = nomeDoVendedor
                                            dataFrame.loc[indexData, 'vendas'] = vendas
                                            dataFrame.loc[indexData, 'item'] = item
                                            dataFrame.loc[indexData, 'comissao'] = comissao
                                            dataFrame.loc[indexData, 'valor'] = valor


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

                        # Cria novas pastas para cada novo vendedor adicionado
                        case '3':
                            nomeVendedor = input('Digite o Nome do Novo Vendedor -> ').replace(' ', '-')
                            os.system(f'mkdir vendedores/{nomeDoVendedor}')
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

                        case '0':
                            break

                        case '?':
                            print('1 - Upload de Excel')
                            print('2 - Vendas do Vendedor')
                            print('3 - Adicionar Novo Vendedor')
                            print('4 - Verificar Vendas do Vendedor')
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