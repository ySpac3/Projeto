import os
import pandas as pd
import shutil
import re

def upload_data_geral(path, login_atual):
    xlsx = path[0]
    if os.path.exists(xlsx):
        # Tentar ler o arquivo Excel
        try:
            excel = pd.read_excel(xlsx)
        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return

        # Caminho para o arquivo CSV principal
        csv_path = f'./vendedores/{login_atual}/{login_atual}-tab.csv'
        if os.path.exists(csv_path):
            dataFrame = pd.read_csv(csv_path)
        else:
            # Criar um DataFrame vazio com as colunas corretas
            dataFrame = pd.DataFrame(columns=['vendedor', 'comprador', 'kit', 'valor', 'comissao', 'data'])

        # Atualizar o DataFrame principal com os dados do Excel
        indexData = len(dataFrame)
        for i in range(len(excel)):
            try:
                vendedorg = excel.loc[i, 'vendedor'].upper()
                compradorg = excel.loc[i, 'comprador']
                kitg = excel.loc[i, 'kit']
                valorg = excel.loc[i, 'valor']
                comissaog = excel.loc[i, 'comissao']
                datag = excel.loc[i, 'data']
                dataFrame.loc[indexData] = [vendedorg, compradorg, kitg, valorg, comissaog, datag]
                indexData += 1
            except Exception as e:
                print(f"Erro ao processar a linha {i} do Excel: {e}")

        # Salvar o DataFrame atualizado no arquivo CSV principal
        try:
            dataFrame.to_csv(csv_path, index=False)
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV principal: {e}")

        # Atualizar os arquivos CSV dos vendedores
        for v in dataFrame['vendedor'].unique():
            caminhos = f'./vendedores/{login_atual}/{v}/{v}-tab.csv'
            if os.path.exists(caminhos):
                try:
                    vendedor_df = pd.read_csv(caminhos)

                    # Extrair os dados para o vendedor específico
                    vendedor_data = excel[excel['vendedor'] == v]

                    for _, row in vendedor_data.iterrows():
                        vendedor_row = {
                            'vendedor': row['vendedor'].upper(),
                            'comprador': row['comprador'],
                            'kit': row['kit'],
                            'valor': row['valor'],
                            'comissao': row['comissao'],
                            'data': row['data']
                        }
                        vendedor_df = vendedor_df.append(vendedor_row, ignore_index=True)

                    # Salvar o DataFrame atualizado no arquivo CSV do vendedor
                    vendedor_df.to_csv(caminhos, index=False)

                except Exception as e:
                    print(f"Erro ao atualizar o arquivo {caminhos}: {e}")
    else:
        print('Arquivo Excel Não Existe')

    # Exemplo de chamada da função

def upload_data_singular(path, login_atual, vendedor_atual):
    xlsx = path[0]
    if os.path.exists(xlsx):
        excel = pd.read_excel(xlsx)
        dataFrame = pd.read_csv(f'./vendedores/{login_atual}/{vendedor_atual}/{vendedor_atual}-tab.csv')

        indexData = len(dataFrame['vendedor'])

        for i in range(len(excel)):
            vendedor = excel.loc[i, 'vendedor']
            comprador = excel.loc[i, 'comprador']
            kit = excel.loc[i, 'kit']
            valor = excel.loc[i, 'valor']
            comissao = excel.loc[i, 'comissao']
            data = excel.loc[i, 'data']

            dataFrame.loc[indexData, 'vendedor'] = vendedor
            dataFrame.loc[indexData, 'comprador'] = comprador
            dataFrame.loc[indexData, 'kit'] = kit
            dataFrame.loc[indexData, 'valor'] = valor
            dataFrame.loc[indexData, 'comissao'] = comissao
            dataFrame.loc[indexData, 'data'] = data

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
        tb.write('vendedor,comprador,kit,valor,comissao,data')
    with open(f'./vendedores/{login}/{login}-tab.csv', 'a') as tb:
        tb.write(f'\n{nomeDoVendedor},NONE,NONE,{0},{0},{0}')
def deletarVendedores(login: str, nomeDoVendedor: str) -> None:
    # Erro de Indentação, Você Usou dois TABs
    #Isso serve para remover os registros do vendedor deletado das tabelas"
    db = pd.read_csv(f'./vendedores/{login}/{login}-tab.csv')
    db = db[db['vendedor'] != f'{nomeDoVendedor}']
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
        tb.write('vendedor,comprador,kit,valor,comissao,data')
def verificarEmail(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao, email):
        return True

    return False

def Comissao(df) -> float:
    valorTotal = 0
    dtf = df
    try:
        for i in range(len(dtf['comissao'])):
            valor = float(dtf.loc[i, 'valor'])
            comissao = float(dtf.loc[i, 'comissao'])
            valorTotal += (valor * comissao)
    except:
        return 0
    return valorTotal

def vendasKit(df) -> dict:
    dictKits = {}
    dtf = df

    for i in range(len(dtf['kit'])):
        kit = dtf.loc[i, 'kit']
        if kit not in dictKits:
            dictKits[kit] = 1
        else:
            dictKits[kit] += 1

    return dictKits
def valorVendas(df) -> float:
    dtf = df
    total = 0

    try:
        for i in range(len(dtf['valor'])):
            total += float(dtf.loc[i, 'valor'])
    except:
        total = 0
    return total
def separadoPorMes(login: str, vendedor: str, mes: int) -> pd.DataFrame:
    dtf = pd.read_csv(f'./vendedores/{login}/{vendedor}/{vendedor}-tab.csv')
    dtfMes = pd.DataFrame()

    indexFilter = 0
    for i in range(len(dtf['data'])):
        if mes > 0 and mes < 10:

            if f'-0{mes}-' in str(dtf.loc[i, 'data']):
                dtfMes.loc[indexFilter, 'vendedor'] = dtf.loc[i, 'vendedor']
                dtfMes.loc[indexFilter, 'kit'] = dtf.loc[i, 'kit']
                dtfMes.loc[indexFilter, 'comprador'] = dtf.loc[i, 'comprador']
                dtfMes.loc[indexFilter, 'comissao'] = dtf.loc[i, 'comissao']
                dtfMes.loc[indexFilter, 'valor'] = dtf.loc[i, 'valor']
                dtfMes.loc[indexFilter, 'data'] = dtf.loc[i, 'data']
                indexFilter+=1
        else:
            if f'/{mes}/' in str(dtf.loc[i, 'data']):
                dtfMes.loc[indexFilter, 'vendedor'] = dtf.loc[i, 'vendedor']
                dtfMes.loc[indexFilter, 'kit'] = dtf.loc[i, 'kit']
                dtfMes.loc[indexFilter, 'comprador'] = dtf.loc[i, 'comprador']
                dtfMes.loc[indexFilter, 'comissao'] = dtf.loc[i, 'comissao']
                dtfMes.loc[indexFilter, 'valor'] = dtf.loc[i, 'valor']
                dtfMes.loc[indexFilter, 'data'] = dtf.loc[i, 'data']
                indexFilter+=1

    return dtfMes
def separadoPorMesGeral(login: str, mes: str) -> pd.DataFrame:
    dtf = pd.read_csv(f'./vendedores/{login}/{login}-tab.csv')
    dtfMes = pd.DataFrame()

    indexFilter = 0
    for i in range(len(dtf['data'])):
        if mes > 0 and mes < 10:
            if f'-0{mes}-' in str(dtf.loc[i, 'data']):
                dtfMes.loc[indexFilter, 'vendedor'] = dtf.loc[i, 'vendedor']
                dtfMes.loc[indexFilter, 'kit'] = dtf.loc[i, 'kit']
                dtfMes.loc[indexFilter, 'comprador'] = dtf.loc[i, 'comprador']
                dtfMes.loc[indexFilter, 'comissao'] = dtf.loc[i, 'comissao']
                dtfMes.loc[indexFilter, 'valor'] = dtf.loc[i, 'valor']
                dtfMes.loc[indexFilter, 'data'] = dtf.loc[i, 'data']
                indexFilter += 1
            elif f'/{mes}/' in str(dtf.loc[i, 'data']):
                dtfMes.loc[indexFilter, 'vendedor'] = dtf.loc[i, 'vendedor']
                dtfMes.loc[indexFilter, 'kit'] = dtf.loc[i, 'kit']
                dtfMes.loc[indexFilter, 'comprador'] = dtf.loc[i, 'comprador']
                dtfMes.loc[indexFilter, 'comissao'] = dtf.loc[i, 'comissao']
                dtfMes.loc[indexFilter, 'valor'] = dtf.loc[i, 'valor']
                dtfMes.loc[indexFilter, 'data'] = dtf.loc[i, 'data']
                indexFilter += 1
        else:
            if f'/{mes}/' in str(dtf.loc[i, 'data']):
                dtfMes.loc[indexFilter, 'vendedor'] = dtf.loc[i, 'vendedor']
                dtfMes.loc[indexFilter, 'kit'] = dtf.loc[i, 'kit']
                dtfMes.loc[indexFilter, 'comprador'] = dtf.loc[i, 'comprador']
                dtfMes.loc[indexFilter, 'comissao'] = dtf.loc[i, 'comissao']
                dtfMes.loc[indexFilter, 'valor'] = dtf.loc[i, 'valor']
                dtfMes.loc[indexFilter, 'data'] = dtf.loc[i, 'data']
                indexFilter += 1
    return dtfMes