
import os
import pandas as pd


def upload_data(path):
    xlsx = path[0]
    if os.path.exists(xlsx):
        excel = pd.read_excel(xlsx)
        dataFrame = pd.read_csv('./data/data.csv')

        indexData = len(dataFrame['vendedor'])

        for i in range(len(excel)):
            # Não achei o erro que você estava dizendo

            Vendedor = input('Nome do Vendedor -> ')
            vendas = excel.loc[i, 'vendas']
            item = excel.loc[i, 'item']
            comissao = excel.loc[i, 'comissao']
            valor = excel.loc[i, 'valor']

            dataFrame.loc[indexData, 'vendedor'] = Vendedor
            dataFrame.loc[indexData, 'vendas'] = vendas
            dataFrame.loc[indexData, 'item'] = item
            dataFrame.loc[indexData, 'comissao'] = comissao
            dataFrame.loc[indexData, 'valor'] = valor

            indexData += 1

        dataFrame.to_csv('./data/data.csv', index=False)

    else:
        print('Arquivo Não Existe')