# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

contador = int(input("Digite N termo da série: "))

soma = 0
dividendo = 1
divisor = 1

for indice in range(contador):
    soma += dividendo / divisor
    dividendo += 1
    divisor += 2

print(f"{soma:.4f}")