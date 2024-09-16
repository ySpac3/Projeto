

# Login ainda não funciona

import pandas as pd
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter
import verificacao as SQLInjection
import os
import Functions as F
from PIL import Image, ImageTk
import matplotlib.pyplot as mtp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Login_atual = ''
vendedor_atual = ''
vendedor_db = ''
funçao = ''

class login_UI:
    def __init__(self, error=False):
        self.users = None
        self.passwords = None
        self.email = None
        self.log = False
        self.reg = False

        #Você pode achar isso estranho, mas quando eu utilizava essa variavel direto na função por algum motivo o programa só ignorava
        self.error = error
    def inicial_login_ui(self):
        db = pd.read_csv('./data/logins.csv')
        #declarando Funções
        def logar():
            self.email = user_entry.get()
            self.passwords = password_entry.get()
            if self.email and self.passwords:
                login_window.withdraw()
                login_window.quit()
                self.log = True
            else:
                self.log = True
                user_entry.configure(border_color='red')
                password_entry.configure(border_color='red')
                return self.email, self.passwords, self.reg

        def registrar():
            self.reg = True
            login_window.withdraw()
            login_window.quit()

        # Criando a tela de Login
        login_window = ctk.CTk()
        login_window.geometry('350x300')
        login_window.resizable(width=False, height=False)

        # Configurando a tela inicial
        login_text = ctk.CTkLabel(login_window, text='LOGIN', font=('Arial', 20)).pack(pady=10)
        # Configurando as entradas

        user_entry = ctk.CTkEntry(login_window,
                                  placeholder_text="Email")
        user_entry.pack(pady=20)

        password_entry = ctk.CTkEntry(login_window,
                                      placeholder_text="Senha",
                                      show='*'
                                      )
        password_entry.pack(pady=10)
        if self.error:
            user_entry.configure(border_color='red')
            password_entry.configure(border_color='red')

        btn_login = ctk.CTkButton(login_window,
                                  text='Logar',
                                  command=logar)
        btn_login.pack(pady=20)

        btn_register = ctk.CTkButton(login_window,
                                     text='Registrar',
                                     command=registrar,
                                     fg_color='Purple')
        btn_register.pack(pady=10)

        login_window.mainloop()
        if self.log:
            global Login_atual
            try:
                Login_atual = db.loc[db['email'] == self.email, 'nome'].values[0]
            except:
                pass
            return self.email, self.passwords, self.reg

        if self.reg:
            return self.email, self.passwords, self.reg
    def register(self, error=False):
        #Declarando Variaveis
        reg = False
        #Declarando Funções
        def registrar():
            nonlocal reg
            self.users = user_entry.get().strip()
            self.passwords = password_entry.get().strip()
            self.email = email_entry.get().strip()
            if self.users and self.passwords and self.email:
                reg = True
                register_window.withdraw()
                register_window.quit()
            else:
                user_entry.configure(border_color='red')
                password_entry.configure(border_color='red')
                email_entry.configure(border_color='red')
            if self.error:
                user_entry.configure(border_color='red')
                password_entry.configure(border_color='red')
                email_entry.configure(border_color='red')



        register_window = ctk.CTk()
        register_window.geometry('350x300')
        register_window.resizable(width=False, height=False)

        # Configurando a tela inicial
        login_text = ctk.CTkLabel(register_window, text='Registrar', font=('Arial', 20)).pack(pady=10)
        # Configurando as entradas

        user_entry = ctk.CTkEntry(register_window,
                                  placeholder_text="Usuário")
        user_entry.pack(pady=10)

        password_entry = ctk.CTkEntry(register_window,
                                      placeholder_text="Senha",
                                      show='*'
                                      )
        password_entry.pack(pady=10)

        email_entry = ctk.CTkEntry(register_window,
                                   placeholder_text="Email",
                                   )
        email_entry.pack(pady=10)

        btn_registrar = ctk.CTkButton(register_window,
                                      text='Registrar',
                                      fg_color='Purple',
                                      command=registrar)
        btn_registrar.pack(pady=10)
        register_window.mainloop()
        if reg:
            return self.users, self.passwords, self.email

def menu():

    color1='#383838'
    color2='#5c5c5c'
    color3='#3e3e3e'
    color4='#212121'




    dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')

    click = False

    def DEBUG():
        menu.quit()
        menu.withdraw()

    def Principal():
        nonlocal frame_1
        global funçao
        funçao = Principal
        nonlocal dataFrame
        global vendedor_db
        global vendedor_atual

        dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')
        vendedor_db = F.queryVendedores(Login_atual,vendedor_atual)

        def criargráfico(x, y, master, column, row, name: str):
            fig = mtp.Figure(figsize=(3.5, 3), dpi=100)
            fig.patch.set_facecolor(color4)
            fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)
            ax = fig.add_subplot(111)
            ax.patch.set_facecolor(color4)
            for i in range(len(x)):
                ax.text(x[i], y[i], f'{y[i]}', fontsize=8, ha='center', va='bottom', color='white')
            x = x
            y = y

            ax.plot(x, y)
            ax.set_title(name, color='white')
            ax.tick_params(axis='x', labelsize=6, colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.grid(linestyle='--',linewidth=0.3)
            for spine in ax.spines.values():
                spine.set_edgecolor('none')

            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.draw()
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(column=column, row=row, sticky='')


        for i in frame_1.winfo_children():
            i.destroy()
        frame_1.grid_rowconfigure(0, weight=1)
        frame_1.grid_columnconfigure(0, weight=1)

        frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent', width=1000, height=330)
        frame_principal.grid(row=1, column=0, sticky='sew', rowspan=2)

        second_frame = ctk.CTkFrame(frame_1, width=200, height=200, fg_color='transparent')
        second_frame.grid(row=0, column=0, pady=80, sticky='nsew')
        second_frame.grid_rowconfigure(0,weight=1)
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame_principal.grid_columnconfigure(i, weight=1)
        # Configurando tópicos
        for i, v in enumerate(['VENDEDOR', 'COMPRADOR', 'KIT', 'VALOR', 'COMISSAO','DATA']):
            sell = ctk.CTkLabel(frame_principal,fg_color=color3,corner_radius=30,  text=v, font=('Arial', 24))
            sell.grid(row=0, column=i, pady=10, padx=10, sticky='ew')
            # Configurando valores dos Tópicos
        for i in range(0, len(dataFrame)):
            for p, v in enumerate(['vendedor', 'comprador', 'kit', 'valor', 'comissao','data']):
                if v != 'comissao':
                    lastsell = ctk.CTkLabel(frame_principal, text=f"{dataFrame.loc[i, v]}", fg_color=color3, corner_radius=30,font=('Arial', 28))
                    lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')
                else:
                    lastsell = ctk.CTkLabel(frame_principal, text=f"{dataFrame.loc[i, 'valor'] * dataFrame.loc[i, 'comissao']}", fg_color=color3,
                                            corner_radius=30, font=('Arial', 28))
                    lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')

        # Pegando dados de vendas no mês geral e colocando em um gráfico
        valorvendas = []
        valorcomissao = []
        valorlucro = []
        for mes in range(1, 13):
            dtf = F.separadoPorMesGeral(Login_atual, mes)
            valor = F.Comissao(dtf)
            valorcomissao.append(valor)

        for mes in range(1, 13):
            dtf = F.separadoPorMesGeral(Login_atual, mes)
            valor = F.valorVendas(dtf)
            valorvendas.append(valor)

        for mes in range(1, 13):
            valorlucro.append(valorvendas[mes-1] - valorcomissao[mes-1])

        vendas = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                              valorvendas, second_frame, 0, 0, name='Vendas')
        comissoes = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                 valorcomissao,second_frame, 1, 0, name='Comissões')
        lucro = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                               valorlucro,second_frame,2,0, name='Lucro')
    def Upload():
        global funçao
        funçao = Upload
        nonlocal frame_1
        nonlocal dataFrame
        global vendedor_db
        global vendedor_atual

        dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')

        # Criar uma lista para armazenar os dados
        data_to_add = []

        # Iterar sobre as linhas do DataFrame principal
        for index, row in dataFrame.iterrows():
            vendedor = row['vendedor']

            # Caminho para o arquivo CSV do vendedor
            file_path = f'./vendedores/{Login_atual}/{vendedor}/{vendedor}-tab.csv'

            # Verificar se o arquivo existe
            if os.path.exists(file_path):
                # Adicionar a linha do DataFrame principal à lista
                vendedor_row = {
                    'vendedor': vendedor,
                    'comprador': row['comprador'],  # Assumindo que 'comprador' está presente no DataFrame principal
                    'kit': row['kit'],  # Assumindo que 'kit' está presente no DataFrame principal
                    'valor': row['valor'],  # Assumindo que 'valor' está presente no DataFrame principal
                    'comissao': row['comissao'],  # Assumindo que 'comissao' está presente no DataFrame principal
                    'data': row['data']  # Assumindo que 'data' está presente no DataFrame principal
                }

                # Adiciona a linha à lista
                data_to_add.append(vendedor_row)
        # Criar o DataFrame final usando pd.concat()
        db = pd.DataFrame(columns=['vendedor', 'comprador', 'kit', 'valor', 'comissao', 'data'])
        db = pd.concat([db, pd.DataFrame(data_to_add)], ignore_index=True)

        vendedor_db = F.queryVendedores(Login_atual,vendedor_atual)

        def vendedor_list(Vendedor_atual):
            nonlocal frame_1
            nonlocal second_frame
            global vendedor_atual
            global vendedor_db

            vendedor_atual = Vendedor_atual

            for i in frame_1.winfo_children():
                i.destroy()
            second_frame = ctk.CTkFrame(frame_1, width=200, height=200, fg_color='transparent', border_color=color3,
                                        border_width=3, )
            second_frame.grid(row=0, column=0, pady=80)
            dnd_label = ctk.CTkLabel(second_frame, text='Arraste seus arquivos arquivo .xlsx aqui',
                                     bg_color='transparent', text_color=color3, font=('Arial', 24))
            dnd_label.grid(row=0, column=0, pady=80)
            # Configurando para o second frame virar um drag and drop e ficar visivel
            dndfiles(second_frame, singular=True)
            frame_1.grid_rowconfigure(1,weight=1)
            frame_1.grid_columnconfigure(0,weight=1)
            frame_vendedor_xlsx = ctk.CTkScrollableFrame(frame_1, width=1000, height=330, fg_color='transparent',)
            frame_vendedor_xlsx.grid(row=1, column=0, sticky='sew', columnspan=2)
            for i, v in enumerate(['VENDEDOR', 'COMPRADOR', 'KIT', 'VALOR', 'COMISSAO', 'DATA']):
                sell = ctk.CTkLabel(frame_vendedor_xlsx, text=v, font=('Arial', 24))
                frame_vendedor_xlsx.grid_columnconfigure(i,weight=1)
                sell.grid(row=0, column=i, pady=10, padx=10, sticky='new')
            # Configurando valores dos Tópicos
            vendedor_db = F.queryVendedores(Login_atual, vendedor_atual)
            for i in range(0, len(vendedor_db)):
                for p, v in enumerate(['vendedor', 'comprador', 'kit', 'valor', 'comissao', 'data']):
                    if v != 'comissao':
                        lastsell = ctk.CTkLabel(frame_vendedor_xlsx, text=f"{dataFrame.loc[i, v]}", fg_color=color3,
                                                corner_radius=30, font=('Arial', 28))
                        lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')
                    else:
                        lastsell = ctk.CTkLabel(frame_vendedor_xlsx,
                                                text=f"{dataFrame.loc[i, 'valor'] * dataFrame.loc[i, 'comissao']}",
                                                fg_color=color3,
                                                corner_radius=30, font=('Arial', 28))
                        lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')


        for i in frame_1.winfo_children():
            i.destroy()

        frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent', width=100, height=330)
        frame_principal.grid(row=1, column=0, sticky='sew')
        frame_principal.grid_columnconfigure(0,weight=1)
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame_principal.grid_columnconfigure(i, weight=1)
        #Criando botões de vendedores
        vendedores_existentes = []
        for i, v in enumerate(db['vendedor']):
            if v not in vendedores_existentes:
                vendedores_existentes.append(v)
                btn_vendedor = ctk.CTkButton(frame_principal,
                                             width=700,
                                             height=20,
                                             command=lambda i=i: vendedor_list(db.loc[i, 'vendedor']),
                                             text=v,
                                             font=('Arial', 24),
                                             border_spacing=17,
                                             corner_radius=100,
                                             fg_color=color3,
                                             )
                btn_vendedor.grid(row=i, column=1, sticky='n', columnspan=2, pady=5)

        second_frame = ctk.CTkFrame(frame_1, width=200, height=200,fg_color='transparent', border_color=color3, border_width=3,)
        second_frame.grid(row=0, column=0, pady=80)
        dnd_label = ctk.CTkLabel(second_frame,text='Arraste seus arquivos arquivo .xlsx aqui',font=('Arial',24), bg_color='transparent', text_color=color3)
        dnd_label.grid(row=0, column=0, pady=80)
        #Configurando para o second frame virar um drag and drop e ficar visivel
        dndfiles(second_frame, singular=False)
    def Vendedor():
        nonlocal frame_1
        global funçao
        global funçao
        funçao = Vendedor
        nonlocal dataFrame
        global vendedor_db
        global vendedor_atual

        dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')

        # Criar uma lista para armazenar os dados
        data_to_add = []

        # Iterar sobre as linhas do DataFrame principal
        for index, row in dataFrame.iterrows():
            vendedor = row['vendedor']

            # Caminho para o arquivo CSV do vendedor
            file_path = f'./vendedores/{Login_atual}/{vendedor}/{vendedor}-tab.csv'

            # Verificar se o arquivo existe
            if os.path.exists(file_path):
                # Adicionar a linha do DataFrame principal à lista
                vendedor_row = {
                    'vendedor': vendedor,
                    'comprador': row['comprador'],  # Assumindo que 'comprador' está presente no DataFrame principal
                    'kit': row['kit'],  # Assumindo que 'kit' está presente no DataFrame principal
                    'valor': row['valor'],  # Assumindo que 'valor' está presente no DataFrame principal
                    'comissao': row['comissao'],  # Assumindo que 'comissao' está presente no DataFrame principal
                    'data': row['data']  # Assumindo que 'data' está presente no DataFrame principal
                }

                # Adiciona a linha à lista
                data_to_add.append(vendedor_row)
        # Criar o DataFrame final usando pd.concat()
        db = pd.DataFrame(columns=['vendedor', 'comprador', 'kit', 'valor', 'comissao', 'data'])
        db = pd.concat([db, pd.DataFrame(data_to_add)], ignore_index=True)

        vendedor_db = F.queryVendedores(Login_atual,vendedor_atual)

        def Cadastrar():
            nonlocal frame_1

            def cadastro():

                F.criarVendedores(Login_atual, nome_vendedor.get())
                Principal()

            for i in frame_1.winfo_children():
                i.destroy()
            frame_1.grid_rowconfigure(0, weight=1, minsize=360)
            frame_1.grid_rowconfigure(1, weight=0,minsize=360)
            frame_1.grid_rowconfigure(2, weight=0)
            frame_1.grid_columnconfigure(0,weight=1)

            nome_vendedor = ctk.CTkEntry(frame_1, placeholder_text='Nome do Vendedor')
            nome_vendedor.grid(row=0, column=0, sticky='s',pady=5)
            btn_vendcadastrar = ctk.CTkButton(frame_1, text='Cadastrar', command=cadastro)
            btn_vendcadastrar.grid(row=1, column=0, sticky='n',pady=5)

        def Deletar():
            def Delete_confirm(Vendedor_Atual):
                nonlocal frame_1
                def Delete(vendedor):
                    F.deletarVendedores(Login_atual,vendedor)
                    Vendedor()
                for i in frame_1.winfo_children():
                    i.destroy()
                btn_confirm = ctk.CTkButton(frame_1, text=f'Deletar {Vendedor_Atual}?', command=lambda: Delete(Vendedor_Atual))
                btn_confirm.grid(row=0, column=0, sticky='')

            nonlocal frame_1

            for i in frame_1.winfo_children():
                i.destroy()
            frame_1.grid_rowconfigure(0,weight=1)
            frame_1.grid_columnconfigure(0,weight=1)
            frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent')
            frame_principal.grid(row=0, column=0, sticky='nsew',rowspan=2)
            frame_principal.grid_columnconfigure(0, weight=1)
            vendedores_existentes = []
            for i, v in enumerate(dataFrame['vendedor']):
                if v not in vendedores_existentes:
                    vendedores_existentes.append(v)
                    btn_vendedor = ctk.CTkButton(frame_principal, width=1100, height=20,fg_color=color3,
                                                 command=lambda i=i: Delete_confirm(dataFrame.loc[i, 'vendedor']), text=v)
                    btn_vendedor.grid(row=i, column=0, sticky='new')
        def criargráfico(x, y, master, column, row, name: str):
            fig = mtp.Figure(figsize=(3.5, 3), dpi=100)
            fig.patch.set_facecolor(color4)
            fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)
            ax = fig.add_subplot(111)
            ax.patch.set_facecolor(color4)
            for i in range(len(x)):
                ax.text(x[i], y[i], f'{y[i]}', fontsize=8, ha='center', va='bottom', color='white')
            x = x
            y = y

            ax.plot(x, y)
            ax.set_title(name, color='white')
            ax.tick_params(axis='x', labelsize=6, colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.grid(linestyle='--',linewidth=0.3)
            for spine in ax.spines.values():
                spine.set_edgecolor('none')

            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.draw()
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(column=column, row=row, sticky='nsew')

        def vendedor_list(Vendedor_atual):
            nonlocal frame_1
            nonlocal second_frame
            global vendedor_atual
            global vendedor_db

            vendedor_atual = Vendedor_atual

            for i in frame_1.winfo_children():
                i.destroy()

            second_frame = ctk.CTkFrame(frame_1, width=200, height=200, fg_color='transparent',)
            second_frame.grid(row=0, column=0, pady=80)

            frame_1.grid_rowconfigure(1,weight=1)
            frame_1.grid_columnconfigure(0,weight=1)
            frame_vendedor_xlsx = ctk.CTkScrollableFrame(frame_1, width=1000, height=330, fg_color='transparent',)
            frame_vendedor_xlsx.grid(row=1, column=0, sticky='sew', columnspan=2)
            for i, v in enumerate(['VENDEDOR', 'COMPRADOR', 'KIT', 'VALOR', 'COMISSAO', 'DATA']):
                sell = ctk.CTkLabel(frame_vendedor_xlsx, text=v, font=('Arial', 24))
                frame_vendedor_xlsx.grid_columnconfigure(i,weight=1)
                sell.grid(row=0, column=i, pady=10, padx=10, sticky='new')
            # Configurando valores dos Tópicos
            vendedor_db = F.queryVendedores(Login_atual, vendedor_atual)
            for i in range(0, len(vendedor_db)):
                for p, v in enumerate(['vendedor', 'comprador', 'kit', 'valor', 'comissao', 'data']):
                    if v != 'comissao':
                        lastsell = ctk.CTkLabel(frame_vendedor_xlsx, text=f"{vendedor_db.loc[i, v]}", fg_color=color3,
                                                corner_radius=30, font=('Arial', 28))
                        lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')
                    else:
                        lastsell = ctk.CTkLabel(frame_vendedor_xlsx,
                                                text=f"{vendedor_db.loc[i, 'valor'] * vendedor_db.loc[i, 'comissao']}",
                                                fg_color=color3,
                                                corner_radius=30, font=('Arial', 28))
                        lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')
            valorvendas = []
            valorcomissao = []
            valorlucro = []
            for mes in range(1, 13):
                dtf = F.separadoPorMes(Login_atual,vendedor_atual, mes)
                valor = F.Comissao(dtf)
                valorcomissao.append(valor)

            for mes in range(1, 13):
                dtf = F.separadoPorMes(Login_atual,vendedor_atual, mes)
                valor = F.valorVendas(dtf)
                valorvendas.append(valor)

            for mes in range(1, 13):
                valorlucro.append(valorvendas[mes - 1] - valorcomissao[mes - 1])

            vendas = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                  valorvendas, second_frame, 0, 0, name='Vendas')
            comissoes = criargráfico(
                ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                valorcomissao, second_frame, 1, 0, name='Comissões')
            lucro = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                 valorlucro, second_frame, 2, 0, name='Lucro')

        nonlocal frame_1

        for i in frame_1.winfo_children():
            i.destroy()

        frame_1.grid_rowconfigure(0, weight=1,minsize=450)
        frame_1.grid_rowconfigure(1, weight=1, minsize=30)
        frame_1.grid_rowconfigure(2, weight=1,minsize=100)

        frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent', width=100, height=260)
        frame_principal.grid(row=2, column=0, sticky='sew')
        frame_principal.grid_columnconfigure(0,weight=1)
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame_principal.grid_columnconfigure(i, weight=1)
        #Criando botões de vendedores
        vendedores_existentes = []
        for i, v in enumerate(db['vendedor']):
            if v not in vendedores_existentes:
                vendedores_existentes.append(v)
                btn_vendedor = ctk.CTkButton(frame_principal,
                                             width=700,
                                             height=20,
                                             command=lambda i=i: vendedor_list(db.loc[i, 'vendedor']),
                                             text=v,
                                             font=('Arial', 24),
                                             border_spacing=5,
                                             corner_radius=100,
                                             fg_color=color3,
                                             )
                btn_vendedor.grid(row=i, column=1, sticky='n', columnspan=2, pady=5)


        second_frame = ctk.CTkFrame(frame_1, width=200, height=200,fg_color='transparent')
        second_frame.grid(row=0, column=0, pady=80)

        # Pegando dados de vendas no mês geral e colocando em um gráfico
        valorvendas = []
        valorcomissao = []
        valorlucro = []
        for mes in range(1, 13):
            dtf = F.separadoPorMesGeral(Login_atual, mes)
            valor = F.Comissao(dtf)
            valorcomissao.append(valor)

        for mes in range(1, 13):
            dtf = F.separadoPorMesGeral(Login_atual, mes)
            valor = F.valorVendas(dtf)
            valorvendas.append(valor)

        for mes in range(1, 13):
            valorlucro.append(valorvendas[mes - 1] - valorcomissao[mes - 1])

        vendas = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                              valorvendas, second_frame, 0, 0, name='Vendas')
        comissoes = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                 valorcomissao, second_frame, 1, 0, name='Comissões')
        lucro = criargráfico(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                             valorlucro, second_frame, 2, 0, name='Lucro')

        btn_cadastrar = ctk.CTkButton(frame_1, text='Cadastrar Vendedor', command=Cadastrar, fg_color=color3)
        btn_cadastrar.grid(column=0, row=1, sticky='w', padx=400)
        btn_deletar = ctk.CTkButton(frame_1, text='Deletar', command=Deletar, fg_color=color3)
        btn_deletar.grid(column=0, row=1, sticky='e', padx=400)





    menu = TkinterDnD.Tk()
    menu.configure(bg=color4)
    menu.geometry('1280x720')

    menu.grid_rowconfigure(0, weight=1)
    menu.grid_rowconfigure(1, weight=0)
    menu.grid_columnconfigure(0, weight=1, minsize=180)
    menu.grid_columnconfigure(1, weight=1, minsize=1100)

    #Começando no menu principal
    frame_1 = ctk.CTkFrame(menu, fg_color='transparent', width=1100)
    frame_1.grid(row=0, column=1, sticky='nsew', rowspan=2)
    frame_1.grid_rowconfigure(1, weight=1)
    frame_1.grid_columnconfigure(0,weight=1)
    Principal()


    #Criando Frame de botões de menu
    btn_frame = ctk.CTkFrame(menu, fg_color=color3, width=200)
    btn_frame.grid(row=0, column=0, sticky='nsew', rowspan=2)
    btn_frame.grid_columnconfigure(0,weight=1)

    #Criando botões do frame de botões
    btn_menu = ctk.CTkButton(btn_frame,fg_color='transparent',text='Menu principal', font=('Arial',24), command=Principal)
    btn_menu.grid(row=0,column=0, sticky='ew',pady=10,ipady=10)
    btn_upload = ctk.CTkButton(btn_frame, fg_color='transparent', text='Menu Upload', font=('Arial', 24), command=Upload)
    btn_upload.grid(row=1, column=0, sticky='ew', ipady=10,)
    btn_vendedores = ctk.CTkButton(btn_frame, fg_color='transparent', text='Vendedores', font=('Arial', 24), command=Vendedor)
    btn_vendedores.grid(row=2, column=0, sticky='ew', ipady=10)

    menu.grid_rowconfigure(1, weight=0)
    menu.grid_columnconfigure(0, weight=1)
    menu.mainloop()

class dndfiles:
    def __init__(self, root, singular):
        self.frame = root
        self.frame.drop_target_register(DND_FILES)
        if not singular:
            self.frame.dnd_bind('<<Drop>>', self.on_drop)
        else:
            self.frame.dnd_bind('<<Drop>>', self.on_drop_singular)

    def on_drop(self, event):
        """Função chamada quando arquivos são soltos no frame."""
        # Extrair o caminho dos arquivos
        files = self.frame.tk.splitlist(event.data)
        print(files)
        F.upload_data_geral(files, login_atual=Login_atual)
    def on_drop_singular(self, event):
        """Função chamada quando arquivos são soltos no frame."""
        # Extrair o caminho dos arquivos
        files = self.frame.tk.splitlist(event.data)
        print(files)
        F.upload_data_singular(files, login_atual=Login_atual, vendedor_atual=vendedor_atual)
