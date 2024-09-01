# ->TADEU FAVOR CORRIGIR<-
# AO EXECUTAR O CÓDIGO E FAZER LOGIN A TELA SIMPLESMENTE FECHA
# -> invalid command name "1592445479232update"
#    while executing
#"1592445479232update"
#    ("after" script)
#invalid command name "1592506645440check_dpi_scaling"
#    while executing
#"1592506645440check_dpi_scaling"
#    ("after" script)
#invalid command name "1592506645504_click_animation"
#    while executing
#"1592506645504_click_animation"
#    ("after" script)

# AO CLICAR EM REGISTRAR A TELA SIMPLESMENTE FECHA

# E O CÓDIGO CONTINUA RODANDO NORMALMENTE


import customtkinter as ctk

log = False




class login_UI:
    def __init__(self):
        self.users = None
        self.passwords = None
        self.email = None

    def inicial_login_ui(self):
        #declarando variaveis
        log = False
        reg = False
        #declarando Funções
        def logar():
            nonlocal log  # Variavel Verificando se vai logar
            log = True
            self.email = user_entry.get()
            self.passwords = password_entry.get()
            login_window.destroy()

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
            return self.email, self.passwords
        if reg:

            return self.email, self.passwords
    def incorrect_login(self):
        #declarando variaveis
        log = False
        reg = False
        #declarando Funções
        def logar():
            nonlocal log
            log = True
            self.email = user_entry.get()
            self.passwords = password_entry.get()
            login_window.destroy()
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
            return self.email, self.passwords
        if reg:
            return self.email, self.passwords

    def register(self):
        #Declarando Variaveis
        reg = False
        #Declarando Funções
        def registrar():
            nonlocal reg
            reg = True
            self.users = user_entry.get()
            self.passwords = password_entry.get()
            self.email = email_entry.get()
            register_window.destroy()

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