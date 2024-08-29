from Functions import Strings as st
from Functions import resfunctions as res
import mysql.connector

st.tittle('Bem Vindo ao gerenciador')
#sitema de login
while True:
    try:
        r = int(input('O que deseja fazer?\nRegistrar - 1 Logar - 2 '))
    except TypeError: # Adicionei o Except Correto
        print('Comando invalido tente novamente')

    match r:
        case 1:
            # input() já retorna str
            chars = [' ', ';', '>', '<', ';', ':'] # Caracteres especiais, que vão ajudar a tratar ataques de SQLInjection
            nome = input('Digite seu nome ')
            senha = input('Digite sua senha ')
            email = input('Digite seu email ')
            
            # Sistema básico contra SQLInjection
            erroChar = False
            for inp in [nome, senha, email]:
                if any(char in inp for char in chars):
                    erroChar = True

            if not erroChar:
                res.resconfirmation(nome, senha, email)
            else:
                print('Erro. Não é permitido caracteres especiais como : ";", ">", "<", ";", ":"')
        case 2:
            nome = input('Digite o nome de usuário ')
            senha = input('Digite a senha do usuário ')
            login = res.logconfirmantion(nome=nome, senha=senha)
            if login:
                break
            else:
                print('Não entrado, Verifique se o nome esta correto ou registre-se')
