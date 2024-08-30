import customtkinter as ctk




#Criando a tela de Login
login_window = ctk.CTk()
login_window.geometry('350x300')
login_window.resizable(width=False, height=False)


# Configurando a tela inicial
login_text = ctk.CTkLabel(login_window, text='LOGIN', font=('Arial', 20)).pack(pady=10)
#Configurando as entradas
user = ctk.StringVar()
password = ctk.StringVar()

user_entry = ctk.CTkEntry(login_window,
                    placeholder_text='Usuário',
                    textvariable=user,).pack()
password_entry = ctk.CTkEntry(login_window,
                        placeholder_text='Senha',
                        show='*',
                        textvariable=password).pack(pady=20)
def logar():
    print(user.get())
    print(password.get())

btn_login = ctk.CTkButton(login_text,
                          text='Logar',
                          command=logar).pack(pady=20)
login_window.mainloop()