import os
import pandas as pd
import shutil

def upload_data_geral(path, login_atual):
    xlsx = path[0]

    if os.path.exists(xlsx):
        # Tentar ler o arquivo Excel
        try:
            excel = pd.read_excel(xlsx)
        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return

        # Tentar ler o arquivo CSV principal
        csv_path = f'./vendedores/{login_atual}/{login_atual}-tab.csv'
        if os.path.exists(csv_path):
            dataFrame = pd.read_csv(csv_path)
        else:
            # Criar um DataFrame vazio com as colunas corretas
            dataFrame = pd.DataFrame(columns=['nome', 'vendas', 'comissao', 'valor'])

        # Atualizar o DataFrame principal com os dados do Excel
        indexData = len(dataFrame)
        for i in range(len(excel)):
            try:
                vendasg = excel.loc[i, 'vendas']
                comissaog = excel.loc[i, 'comissao']
                valorg = excel.loc[i, 'valor']
                nomeg = excel.loc[i, 'nome']

                dataFrame.loc[indexData] = [nomeg, vendasg, comissaog, valorg]
                indexData += 1
            except Exception as e:
                print(f"Erro ao processar a linha {i} do Excel: {e}")

        # Salvar o DataFrame atualizado no arquivo CSV principal
        try:
            dataFrame.to_csv(csv_path, index=False)
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV principal: {e}")

        # Atualizar os arquivos CSV dos vendedores
        for v in dataFrame['nome']:
            caminhos = f'./vendedores/{login_atual}/{v}/{v}-tab.csv'
            if os.path.exists(caminhos):
                try:
                    caminho = pd.read_csv(caminhos)

                    # Extrair os dados para o vendedor específico
                    vendas = excel.loc[excel['nome'] == v, 'vendas'].values
                    comissao = excel.loc[excel['nome'] == v, 'comissao'].values
                    valor = excel.loc[excel['nome'] == v, 'valor'].values
                    nome = excel.loc[excel['nome'] == v, 'nome'].values

                    if len(vendas) > 0 and len(comissao) > 0 and len(valor) > 0 and len(nome) > 0:
                        caminho.loc[len(caminho)] = {'nome': nome[0], 'vendas': vendas[0], 'comissao': comissao[0],
                                                     'valor': valor[0]}
                        caminho.to_csv(caminhos, index=False)
                except Exception as e:
                    print(f"Erro ao atualizar o arquivo {caminhos}: {e}")
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

def deletarVendedores(login: str, nomeDoVendedor: str) -> None:
        db = pd.read_csv(f'./vendedores/{login}/{login}-tab.csv')
        db = db[db['nome'] != f'{nomeDoVendedor}']
        db.to_csv(f'./vendedores/{login}/{login}-tab.csv', index=False)
        shutil.rmtree(f'./vendedores/{login}/{nomeDoVendedor}')


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