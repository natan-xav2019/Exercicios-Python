# Faça um programa que leia 5 números e informe o maior número.

numero = []

for contador in range(1,6):
    numero.append((float(input(f"Digite o {contador} numero: "))))

print(f"O maior numero e {max(numero)}")