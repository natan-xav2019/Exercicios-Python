# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero = []

for contador in range(1,3):
    numero.append(float(input("Digite o numero: ")))

meio_inteiro = sum(numero) // 2

print(f"Meio inteiro: {meio_inteiro:.0f}")