import pandas as pd
import os
import Graphics as G
import Functions as F



#sitema de login
db = pd.read_csv('./data/logins.csv')
while True:
    # Começo da tela de login aqui
    email, senha, reg = G.login_UI().inicial_login_ui()

    login = False

    while True:
        if db['email'].isin([email]).any():
            vemail = F.verificarEmail(email)
            if vemail:
                pssword = db.loc[db['email'] == email, 'senha'].values[0]
                if pssword == senha:
                    login = True

                else:
                    # Ao usar uma string em um if ele já verifica se ela foi preenchida
                    if email or senha:
                        email, senha, reg = G.login_UI(error=True).inicial_login_ui()
            else:
                email, senha, reg = G.login_UI(error=True).inicial_login_ui()

        else:
            if email or senha:
                email, senha, reg = G.login_UI(error=True).inicial_login_ui()

        if login:

                login_atual = db.loc[db['email'] == email, 'nome'].values[0]

                G.menu()

                while True:
                    userInput = input('Digite um numero')
                    match userInput:
                    # Busca pelo conteúdo da tabela do vendedor


                        case '4':
                            for i in range(1,13):
                                conta_mensal = F.separadoPorMes(f'{login_atual}','testando',f'{i}')
                                try:
                                    Comissao = F.vendasKit(conta_mensal)
                                except:
                                    Comissao = None

                                print(Comissao)

        if reg:
            break

                        # A UI Vai Até Aqui



        #Aqui começa a tela de registro
    nome, senha, email = G.login_UI().register()
    F.criar_login(nome)
    if not db['email'].isin([email]).any():
        index = len(db['email'])
        db.loc[index, 'nome'] = nome
        db.loc[index, 'email'] = email
        db.loc[index, 'senha'] = senha

        db.to_csv('./data/logins.csv', index=False)
    else:
        nome, senha, email = G.login_UI(error=True).register()