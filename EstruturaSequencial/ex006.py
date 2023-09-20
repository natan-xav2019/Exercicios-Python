# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

areaCirculo = lambda raio : math.pi * raio**2

while True:
    try:
        raio = float(input("Digite o raio: "))
        break
    except:
        print("Por favor digite apenas numeros por favor!")

area = areaCirculo(raio)

print(f"{area:.2f}")