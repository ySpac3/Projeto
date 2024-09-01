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