# Faça um Programa que peça dois números e imprima o maior deles.

numeros = []

for i in range(2):
    numeros.append(float(input("Digite um numero ")))

print(f"O maior numero é {max(numeros)}")