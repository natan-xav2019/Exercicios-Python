# Faça um Programa que leia três números e mostre-os em ordem decrescente.

QUANT_NUMEROS = 5

numeros = []

for index in  range(QUANT_NUMEROS):
    if(index == 0):
       print(f"Digite {QUANT_NUMEROS} numeros")
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

numeros = sorted(numeros, reverse=True)

print(f"os numeros em ordem decrescente ficam {numeros}")