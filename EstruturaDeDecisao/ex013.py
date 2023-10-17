# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = ["Domingo","Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado"]

dia = int(input("Digite um numero de 0 a 6 para indicar o dia da semana: "))

if( dia >= 0 and dia <= 6):
    print(f"Hoje e {semana[dia]}.")
else:
    print("Valor inválido.")