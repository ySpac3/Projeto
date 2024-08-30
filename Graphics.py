import customtkinter as ctk

log = False

def interface(users, passwords):

    log = False
    #Criando a tela de Login
    login_window = ctk.CTk()
    login_window.geometry('350x300')
    login_window.resizable(width=False, height=False)


    # Configurando a tela inicial
    login_text = ctk.CTkLabel(login_window, text='LOGIN', font=('Arial', 20)).pack(pady=10)
    #Configurando as entradas

    user_entry = ctk.CTkEntry(login_window,
                        placeholder_text="Usuário")
    user_entry.pack(pady=20)
    password_entry = ctk.CTkEntry(login_window,
                            placeholder_text="Senha",
                            show='*'
                            )
    password_entry.pack(pady=10)
    def logar():
        nonlocal log, users, passwords
        log = True
        users = user_entry.get()
        passwords = password_entry.get()
        login_window.destroy()

    btn_login = ctk.CTkButton(login_window,
                              text='Logar',
                              command=logar)
    btn_login.pack(pady=20)
    login_window.mainloop()
    if log:
        return users, passwords