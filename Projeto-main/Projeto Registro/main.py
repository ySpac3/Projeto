from Functions import Strings as st
from Functions import resfunctions as res
import mysql.connector

st.tittle('Bem Vindo ao gerenciador')
#sitema de login
while True:
    try:
        r = int(input('O que deseja fazer?\nRegistrar - 1 Logar - 2 '))
    except:
        print('Comando invalido tente novamente')
    if r == 1:
        nome = str(input('Digite seu nome '))
        senha = str(input('Digite sua senha '))
        email = str(input('Digite seu email '))
        res.resconfirmation(nome, senha, email)
    if r == 2:
        nome = str(input('Digite o nome de usuário '))
        senha = str(input('Digite a senha do usuário '))
        login = res.logconfirmantion(nome=nome, senha=senha)
        if login:
            break
        else:
            print('Não entrado, Verifique se o nome esta correto ou registre-se')
