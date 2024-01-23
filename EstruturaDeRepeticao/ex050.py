# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

contador = int(input("Digite o valor de N para o H do enesimo termo: "))

soma = 0

for indice in range(1,contador+1):
    soma += 1 / indice

print(f"{soma:.4f}")