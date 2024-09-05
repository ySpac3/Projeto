import os
import pandas as pd


def upload_data_geral(path, login_atual):
    xlsx = path[0]
    
    if os.path.exists(xlsx):
        excel = pd.read_excel(xlsx)
        dataFrame = pd.read_csv(f'./vendedores/{login_atual}/{login_atual}-tab.csv')

        indexData = len(dataFrame['vendas'])

        for i in range(len(excel)):
            vendas = excel.loc[i, 'vendas']
            comissao = excel.loc[i, 'comissao']
            valor = excel.loc[i, 'valor']
            nome = excel.loc[i,'nome']

            dataFrame.loc[indexData, 'nome'] = nome
            dataFrame.loc[indexData, 'vendas'] = vendas
            dataFrame.loc[indexData, 'comissao'] = comissao
            dataFrame.loc[indexData, 'valor'] = valor

            indexData += 1

        dataFrame.to_csv(f'./vendedores/{login_atual}/{login_atual}-tab.csv', index=False)

    else:
        print('Arquivo Não Existe')

def upload_data_singular(path, login_atual, vendedor_atual):
    xlsx = path[0]
    if os.path.exists(xlsx):
        excel = pd.read_excel(xlsx)
        dataFrame = pd.read_csv(f'./vendedores/{login_atual}/{vendedor_atual}/{vendedor_atual}-tab.csv')

        indexData = len(dataFrame['vendas'])

        for i in range(len(excel)):
            vendas = excel.loc[i, 'vendas']
            comissao = excel.loc[i, 'comissao']
            valor = excel.loc[i, 'valor']
            nome = excel.loc[i, 'nome']

            dataFrame.loc[indexData, 'nome'] = nome
            dataFrame.loc[indexData, 'vendas'] = vendas
            dataFrame.loc[indexData, 'comissao'] = comissao
            dataFrame.loc[indexData, 'valor'] = valor

            indexData += 1

        dataFrame.to_csv(f'./vendedores/{login_atual}/{vendedor_atual}/{vendedor_atual}-tab.csv', index=False)

    else:
        print('Arquivo Não Existe')

# Favor usar no login, o nome do usuário
# Favor Invocar essa função ao se registrar
def criarVendedores(login: str, nomeDoVendedor: str) -> None:
    # Trabalhar com pastas que usem espaço é foda
    login = login.replace(' ', '-')
    nomeDoVendedor = nomeDoVendedor.replace(' ', '-')

    os.mkdir(f'./vendedores/{login}/{nomeDoVendedor}')

    with open(f'./vendedores/{login}/{nomeDoVendedor}/{nomeDoVendedor}-tab.csv', 'w') as tb:
        tb.write('nome,vendas,comissao,valor')
    with open(f'./vendedores/{login}/{login}-tab.csv', 'a') as tb:
        tb.write(f'\n{nomeDoVendedor},{0},{0},{0}')

# Função que retorn a tabela do vendedor
def queryVendedores(login: str, nomeDoVendedor: str) -> pd.DataFrame:
    login = login.replace(' ', '-')
    nomeDoVendedor = nomeDoVendedor.replace(' ', '-')
    if os.path.exists(f'./vendedores/{login}/{nomeDoVendedor}/{nomeDoVendedor}-tab.csv'):
        return pd.read_csv(f'./vendedores/{login}/{nomeDoVendedor}/{nomeDoVendedor}-tab.csv')
    else:
        return pd.DataFrame()
def criar_login(user):
    nomeDoLogin = user
    os.makedirs(f'./vendedores/{nomeDoLogin}', exist_ok=True)

    with open(f'./vendedores/{nomeDoLogin}/{nomeDoLogin}-tab.csv', 'w') as tb:
        tb.write('nome,vendas,comissao,valor')