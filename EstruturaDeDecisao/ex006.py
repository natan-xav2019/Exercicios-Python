# Faça um Programa que leia três números e mostre o maior deles.

numeros = []

for i in range(3):
    numeros.append(float(input("Digite um numero ")))

print(max(numeros))