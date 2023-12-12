# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

MAX_NUM = 10

print("Digite 10 numeros")

quantidade_pares = 0
quantidade_impar = 0

for cont in range(MAX_NUM):
    numero = int(input("Digite o numero: "))
    if numero % 2 == 0:
        quantidade_pares += 1
    elif numero % 2 != 0:
        quantidade_impar += 1

print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de impares: {quantidade_impar}")