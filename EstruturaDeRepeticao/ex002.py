# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = "a"
senha = "a"

while nome.upper() == senha.upper():
    nome = input("Digite o seu nome: ")
    senha = input("Digite apenas a senha: ")
    if nome.upper() == senha.upper() :
        print("O nome e senha não podem ser o mesmo!!!")

print("O nome e a senha são diferentes senha cadastrada com sucesso!!!")