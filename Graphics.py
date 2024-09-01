# Login ainda não funciona

import pandas as pd
import customtkinter as ctk

dataFrame = pd.read_csv('./data/data.csv')
class login_UI:
    def __init__(self, error=False):
        self.users = None
        self.passwords = None
        self.email = None
        #Você pode achar isso estranho, mas quando eu utilizava essa variavel direto na função por algum motivo o programa só ignorava
        self.error = error
    def inicial_login_ui(self):
        #declarando variaveis
        log = False
        reg = False
        #declarando Funções
        def logar():
            nonlocal log
            self.email = user_entry.get()
            self.passwords = password_entry.get()
            if self.email and self.passwords:
                log = True
                login_window.destroy()
            else:
                log = True
                return self.email, self.passwords, reg

        def registrar():
            nonlocal reg
            reg = True
            login_window.destroy()



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
        if log:
            return self.email, self.passwords, reg
        if reg:
            return self.email, self.passwords, reg
    def incorrect_login(self):
        #declarando variaveis
        log = False
        reg = False
        #declarando Funções
        def logar():
            nonlocal log
            self.email = user_entry.get()
            self.passwords = password_entry.get()
            if self.email and self.passwords:
                log = True
                login_window.destroy()
            else:
                log = True
                return self.email, self.passwords, reg
        def registrar():
            nonlocal reg
            reg = True
            login_window.destroy()

        # Criando a tela de Login
        login_window = ctk.CTk()
        login_window.geometry('350x300')
        login_window.resizable(width=False, height=False)

        # Configurando a tela inicial
        login_text = ctk.CTkLabel(login_window, text='LOGIN', font=('Arial', 20)).pack(pady=10)
        # Configurando as entradas

        user_entry = ctk.CTkEntry(login_window,
                                  placeholder_text="Email",
                                  border_color='red')
        user_entry.pack(pady=20)
        password_entry = ctk.CTkEntry(login_window,
                                      placeholder_text="Senha",
                                      show='*',
                                      border_color='red'
                                      )
        password_entry.pack(pady=10)

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
        if log:
            return self.email, self.passwords, reg
        if reg:
            return self.email, self.passwords, reg
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
                register_window.destroy()
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

class menu:
    def __init__(self):
        self.menu = ctk.CTk()
        self.menu.geometry('1280x720')

        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=0)
        self.menu.grid_columnconfigure(0, weight=1)

        self.frame = ctk.CTkScrollableFrame(self.menu, fg_color='transparent', height=360, width=1130)
        self.frame.grid(row=1,column=0,sticky='e')

        self.frame.grid_rowconfigure(0, weight=0)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)

        self.sell = ctk.CTkLabel(self.frame, text='Vendedor', font=('Arial', 24))
        self.sell.grid(row=0, column=0, pady=10, padx=10, sticky='ew')
        self.sell = ctk.CTkLabel(self.frame, text='Email', font=('Arial', 24))
        self.sell.grid(row=0, column=1, pady=10, padx=10, sticky='ew')
        self.sell = ctk.CTkLabel(self.frame, text='Vendas', font=('Arial', 24))
        self.sell.grid(row=0, column=2, pady=10, padx=10, sticky='ew')
        self.sell = ctk.CTkLabel(self.frame, text='Item', font=('Arial', 24))
        self.sell.grid(row=0, column=3, pady=10, padx=10, sticky='ew')
        self.sell = ctk.CTkLabel(self.frame, text='Comissao', font=('Arial', 24))
        self.sell.grid(row=0, column=4, pady=10, padx=10, sticky='ew')
        self.sell = ctk.CTkLabel(self.frame, text='Valor', font=('Arial', 24))
        self.sell.grid(row=0, column=5, pady=10, padx=10, sticky='ew')
        for i in range(0, len(dataFrame)):
            # Tadeu... dataFrame[i, 'email'], não dataFrame[i]['email']
            self.lastsell = ctk.CTkLabel(self.frame,text=f'{dataFrame.loc[i, 'vendedor']}',font=('Arial',28))
            self.lastsell.grid(column=0,row=i+1,pady=10,padx=10,sticky='ew')

            self.lastsell = ctk.CTkLabel(self.frame, text=f'{dataFrame.loc[i, 'email']}', font=('Arial', 28))
            self.lastsell.grid(column=1, row=i + 1, pady=10, padx=10, sticky='')

            self.lastsell = ctk.CTkLabel(self.frame, text=f'{dataFrame.loc[i, 'vendas']}', font=('Arial', 28))
            self.lastsell.grid(column=2, row=i + 1, pady=10, padx=10, sticky='')

            self.lastsell = ctk.CTkLabel(self.frame, text=f'{dataFrame.loc[i, 'item']}', font=('Arial', 28))
            self.lastsell.grid(column=3, row=i + 1, pady=10, padx=10, sticky='')

            self.lastsell = ctk.CTkLabel(self.frame, text=f'{dataFrame.loc[i, 'comissao']}', font=('Arial', 28))
            self.lastsell.grid(column=4, row=i + 1, pady=10, padx=10, sticky='')

            self.lastsell = ctk.CTkLabel(self.frame, text=f'{dataFrame.loc[i, 'valor']}', font=('Arial', 28))
            self.lastsell.grid(column=5, row=i + 1, pady=10, padx=10, sticky='')

        self.menu.grid_rowconfigure(1, weight=0)
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.mainloop()