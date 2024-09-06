# Login ainda não funciona

import pandas as pd
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter
import verificacao as SQLInjection
import os
import Functions as F
from PIL import Image, ImageTk


Login_atual = ''
vendedor_atual = ''

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
    dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')

    click = False

    def DEBUG():
        menu.quit()
        menu.withdraw()

    def Principal():
        nonlocal frame_1
        for i in frame_1.winfo_children():
            if i != btn_reload:
                i.destroy()
        frame_1.grid_rowconfigure(0, weight=1)
        frame_1.grid_columnconfigure(0, weight=1)
        frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent', width=1000, height=330)
        frame_principal.grid(row=1, column=0, sticky='sew')
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame_principal.grid_columnconfigure(i, weight=1)
        # Configurando tópicos
        for i, v in enumerate(['Vendedor', 'Vendas', 'Comissao', 'Valor']):
            sell = ctk.CTkLabel(frame_principal, text=v, font=('Arial', 24))
            sell.grid(row=0, column=i, pady=10, padx=10, sticky='ew')
            # Configurando valores dos Tópicos
        for i in range(0, len(dataFrame)):
            for p, v in enumerate(['nome', 'vendas', 'comissao', 'valor']):
                lastsell = ctk.CTkLabel(frame_principal, text=f"{dataFrame.loc[i, v]}", font=('Arial', 28))
                lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')
    def Upload():

        def vendedor_list(Vendedor_atual):
            nonlocal frame_1
            nonlocal second_frame
            global vendedor_atual

            vendedor_atual = Vendedor_atual
            print(vendedor_atual)


            for i in frame_1.winfo_children():
                if i != btn_reload:
                    i.destroy()
            second_frame = ctk.CTkFrame(frame_1, width=200, height=200, fg_color='purple')
            second_frame.grid(row=0, column=0, pady=80)
            # Configurando para o second frame virar um drag and drop e ficar visivel
            second_frame.configure(fg_color='purple')
            dndfiles(second_frame, singular=True)
            frame_1.grid_rowconfigure(1,weight=1)
            frame_1.grid_columnconfigure(0,weight=1)
            frame_vendedor_xlsx = ctk.CTkScrollableFrame(frame_1, width=1000, height=330, fg_color='transparent')
            frame_vendedor_xlsx.grid(row=1, column=0, sticky='sew', columnspan=2)
            for i, v in enumerate(['Vendedor', 'Vendas', 'Comissao', 'Valor']):
                sell = ctk.CTkLabel(frame_vendedor_xlsx, text=v, font=('Arial', 24))
                sell.grid(row=0, column=i, pady=10, padx=50, sticky='new')
            # Configurando valores dos Tópicos
            vendedor_db = pd.read_csv(f'./vendedores/{Login_atual}/{vendedor_atual}/{vendedor_atual}-tab.csv')
            print(vendedor_db)
            for i in range(0, len(vendedor_db)):
                for p, v in enumerate(['nome', 'vendas', 'comissao', 'valor']):
                    lastsell = ctk.CTkLabel(frame_vendedor_xlsx, text=f"{vendedor_db.loc[i, v]}", font=('Arial', 28))
                    lastsell.grid(column=p, row=i + 1, pady=10, padx=50, sticky='new')
        nonlocal frame_1

        for i in frame_1.winfo_children():
            if i != btn_reload:
                i.destroy()

        frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='transparent', width=1000, height=330)
        frame_principal.grid(row=1, column=0, sticky='sew')
        frame_principal.grid_columnconfigure(0,weight=1)
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame_principal.grid_columnconfigure(i, weight=1)
        vendedores_existentes = []
        for i, v in enumerate(dataFrame['nome']):
            if v not in vendedores_existentes:
                vendedores_existentes.append(v)
                btn_vendedor = ctk.CTkButton(frame_principal, width=1100, height=20, command=lambda i=i: vendedor_list(dataFrame.loc[i, 'nome']), text=v)
                btn_vendedor.grid(row=i, column=0, sticky='new')

        second_frame = ctk.CTkFrame(frame_1, width=200, height=200, fg_color='purple')
        second_frame.grid(row=0, column=0, pady=80)
        #Configurando para o second frame virar um drag and drop e ficar visivel
        second_frame.configure(fg_color='purple')
        dndfiles(second_frame, singular=False)
    def Vendedor():
        nonlocal frame_1

        def Cadastrar():
            nonlocal frame_1

            def cadastro():

                F.criarVendedores(Login_atual, nome_vendedor.get())

            for i in frame_1.winfo_children():
                if i != btn_reload:
                    i.destroy()
            frame_1.grid_rowconfigure(0,weight=0)
            frame_1.grid_rowconfigure(1, weight=0)
            frame_1.grid_rowconfigure(2, weight=0)
            frame_1.grid_columnconfigure(0,weight=1)


            spacer = ctk.CTkLabel(frame_1, text="", height=200)  # Define a altura do espaçamento
            spacer.grid(row=1, column=0, sticky='ew')
            nome_vendedor = ctk.CTkEntry(frame_1, placeholder_text='Nome do Vendedor')
            nome_vendedor.grid(row=2, column=0, sticky='')
            btn_vendcadastrar = ctk.CTkButton(frame_1, text='Cadastrar', command=cadastro)
            btn_vendcadastrar.grid(row=3, column=0, sticky='')
        def Deletar():
            def Delete_confirm(Vendedor_Atual):
                nonlocal frame_1
                def Delete(vendedor):
                    F.deletarVendedores(Login_atual,vendedor)
                    Vendedor()
                for i in frame_1.winfo_children():
                    if i != btn_reload:
                        i.destroy()
                btn_confirm = ctk.CTkButton(frame_1, text=f'Deletar {Vendedor_Atual}?', command=lambda: Delete(Vendedor_Atual))
                btn_confirm.grid(row=0, column=0, sticky='')

            nonlocal frame_1

            for i in frame_1.winfo_children():
                if i != btn_reload:
                    i.destroy()
            frame_1.grid_rowconfigure(0,weight=1)
            frame_1.grid_columnconfigure(0,weight=1)
            frame_principal = ctk.CTkScrollableFrame(frame_1, fg_color='purple')
            frame_principal.grid(row=0, column=0, sticky='nsew')
            frame_principal.grid_columnconfigure(0, weight=1)
            vendedores_existentes = []
            for i, v in enumerate(dataFrame['nome']):
                if v not in vendedores_existentes:
                    vendedores_existentes.append(v)
                    btn_vendedor = ctk.CTkButton(frame_principal, width=1100, height=20,
                                                 command=lambda: Delete_confirm(dataFrame.loc[i, 'nome']), text=v)
                    btn_vendedor.grid(row=i, column=0, sticky='new')

        frame_1.grid_rowconfigure(0,weight=0)
        frame_1.grid_rowconfigure(1, weight=0)


        for i in frame_1.winfo_children():
            if i != btn_reload:
                i.destroy()
        btn_cadastrar = ctk.CTkButton(frame_1, text='Cadastrar Vendedor', command=Cadastrar)
        btn_cadastrar.grid(column=0, row=0, sticky='', pady=60)
        btn_deletar = ctk.CTkButton(frame_1, text='Deletar', command=Deletar)
        btn_deletar.grid(column=0, row=1, sticky='', pady=60)
    def Atualizar():
        nonlocal dataFrame
        dataFrame = pd.read_csv(f'./vendedores/{Login_atual}/{Login_atual}-tab.csv')




    menu = TkinterDnD.Tk()
    menu.configure(bg='gray')
    menu.geometry('1280x720')

    menu.grid_rowconfigure(0, weight=1)
    menu.grid_rowconfigure(1, weight=0)
    menu.grid_columnconfigure(0, weight=1, minsize=180)
    menu.grid_columnconfigure(1, weight=1, minsize=1100)
    menu.grid_columnconfigure(1, weight=1)

    #Começando no menu principal
    frame_1 = ctk.CTkFrame(menu, fg_color='transparent', width=1100)
    frame_1.grid(row=0, column=1, sticky='nsew', rowspan=2)
    frame_1.grid_rowconfigure(1, weight=1)
    frame_1.grid_columnconfigure(0,weight=1)
    Principal()


    #Criando Frame de botões de menu
    btn_frame = ctk.CTkFrame(menu, fg_color='teal', width=250)
    btn_frame.grid(row=0, column=0, sticky='nsew', rowspan=2)
    btn_frame.grid_columnconfigure(0,weight=1)

    #Criando botões do frame de botões
    btn_menu = ctk.CTkButton(btn_frame,fg_color='transparent',text='Menu principal', font=('Arial',24), command=Principal)
    btn_menu.grid(row=0,column=0, sticky='ew',pady=10,ipady=10)
    btn_upload = ctk.CTkButton(btn_frame, fg_color='transparent', text='Menu Upload', font=('Arial', 24), command=Upload)
    btn_upload.grid(row=1, column=0, sticky='ew', ipady=10,)
    btn_vendedores = ctk.CTkButton(btn_frame, fg_color='transparent', text='vendedores', font=('Arial', 24), command=Vendedor)
    btn_vendedores.grid(row=2, column=0, sticky='ew', ipady=10)

    #botão debug
    btn_debug = ctk.CTkButton(btn_frame,fg_color='transparent', text='DEBUG', command=DEBUG)
    btn_debug.grid(row=3, column=0)

    btn_reload = ctk.CTkButton(frame_1, text='Atualizar Pagina',command=Atualizar)
    btn_reload.grid(row=0, column=0, sticky='ne')

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