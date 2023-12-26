# Faça um programa que calcule o mostre a média aritmética de N notas.
from statistics import median

notas = []

quantidade_notas = int(input("Digite a quantidade de notas: "))

for contador in range(1, quantidade_notas + 1):
    notas.append(float(input(f"Digite a nota {contador}: ")))

media = median(notas)

print(f"A media de {quantidade_notas} nota(s) e de {media:.2f}")