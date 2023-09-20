# Faça um Programa que converta metros para centímetros

from numbers import Number

conversorMetro = lambda metro : metro * 100

while True:
    try:
        metro = float(input("Digite em metros para converter para centimetros: "))
        break
    except:
        print(f"por favor digite um numero")

print(f"{metro} metro(s) para {conversorMetro(metro)} centimento(s)")