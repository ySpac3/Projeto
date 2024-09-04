# Login ainda não funciona

import pandas as pd
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter
import verificacao as SQLInjection
import os
import Functions as F

#mas é a base de tabelas mesmo

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


        # Criando a tela de Login
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

def menu(dataFrame):

    def DEBUG():
        menu.quit()
        menu.withdraw()

    def Principal():
        nonlocal frame
        nonlocal second_frame

        # Começando no menu principal
        second_frame.configure(fg_color='transparent')
        frame.configure(fg_color='transparent', height=300, width=1130)
        frame.grid_rowconfigure(0, weight=0)
        # Configurando as colunas do frame
        for i in range(0, 4):
            frame.grid_columnconfigure(i, weight=1)
        # Configurando tópicos
        for i, v in enumerate(['Vendedor', 'Vendas', 'Item', 'Comissao', 'Valor']):
            sell = ctk.CTkLabel(frame, text=v, font=('Arial', 24))
            sell.grid(row=0, column=i, pady=10, padx=10, sticky='ew')
        # Configurando valores dos Tópicos
        for i in range(0, len(dataFrame)):
            for p, v in enumerate(['vendedor', 'vendas', 'item', 'comissao', 'valor']):
                lastsell = ctk.CTkLabel(frame, text=f"{dataFrame.loc[i, v]}", font=('Arial', 28))
                lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')

    def Upload():
        nonlocal frame
        nonlocal second_frame
        for i in frame.winfo_children():
            i.destroy()
        #Configurando para o second frame virar um drag and drop e ficar visivel
        second_frame.configure(fg_color='purple')
        dndfiles(second_frame)

    menu = TkinterDnD.Tk()
    menu.configure(bg='gray')
    menu.geometry('1280x720')

    menu.grid_rowconfigure(0, weight=1)
    menu.grid_rowconfigure(1, weight=0)
    menu.grid_columnconfigure(0, weight=1, minsize=180)
    menu.grid_columnconfigure(1, weight=1)

    #Começando no menu principal
    frame = ctk.CTkScrollableFrame(menu, fg_color='transparent', height=300, width=1130)
    frame.grid(row=1, column=1, sticky='e')
    frame.grid_rowconfigure(0, weight=0)
    # Configurando as colunas do frame
    for i in range(0, 4):
        frame.grid_columnconfigure(i, weight=1)
    # Configurando tópicos
    for i, v in enumerate(['Vendedor', 'Vendas', 'Item', 'Comissao', 'Valor']):
        sell = ctk.CTkLabel(frame, text=v, font=('Arial', 24))
        sell.grid(row=0, column=i, pady=10, padx=10, sticky='ew')
    # Configurando valores dos Tópicos
    for i in range(0, len(dataFrame)):
        for p, v in enumerate(['vendedor', 'vendas', 'item', 'comissao', 'valor']):
            lastsell = ctk.CTkLabel(frame, text=f"{dataFrame.loc[i, v]}", font=('Arial', 28))
            lastsell.grid(column=p, row=i + 1, pady=10, padx=10, sticky='ew')

    second_frame = ctk.CTkFrame(menu, width=200, height=200, fg_color='transparent')
    second_frame.grid(row=0, column=1, sticky='')

    #Criando Frame de botões de menu
    btn_frame = ctk.CTkFrame(menu, fg_color='teal', width=250)
    btn_frame.grid(row=0, column=0, sticky='nsew', rowspan=2)
    btn_frame.grid_columnconfigure(0,weight=1)

    #Criando botões do frame de botões
    btn_menu = ctk.CTkButton(btn_frame,fg_color='transparent',text='Menu principal', font=('Arial',24), command=Principal)
    btn_menu.grid(row=0,column=0, sticky='ew',pady=10,ipady=10)
    btn_upload = ctk.CTkButton(btn_frame, fg_color='transparent', text='Menu Upload', font=('Arial', 24), command=Upload)
    btn_upload.grid(row=1, column=0, sticky='ew', ipady=10,)
    #botão debug
    btn_debug = ctk.CTkButton(btn_frame,fg_color='transparent', text='DEBUG', command=DEBUG)
    btn_debug.grid(row=2,column=0)

    menu.grid_rowconfigure(1, weight=0)
    menu.grid_columnconfigure(0, weight=1)
    menu.mainloop()

class dndfiles:
    def __init__(self, root):
        self.frame = root
        self.frame.drop_target_register(DND_FILES)
        self.frame.dnd_bind('<<Drop>>', self.on_drop)


    def on_drop(self, event):
        """Função chamada quando arquivos são soltos no frame."""
        # Extrair o caminho dos arquivos
        files = self.frame.tk.splitlist(event.data)
        print(files)
        F.upload_data(files)