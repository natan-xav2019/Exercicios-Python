# Faça um programa que leia 5 números e informe a soma e a média dos números

from statistics import mean

numero = []

for contador in range(1,6):
    numero.append((float(input(f"Digite o {contador} numero: "))))

print(f"A soma dos numeros e {sum(numero)}")
print(f"A média e {mean(numero)}")