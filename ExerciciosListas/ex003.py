# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

TOTAL= 4

from statistics import mean

contador = 0
notas:list[float] = []

while contador < TOTAL:
    try:
        nota = float(input(f"{contador+1} nota: "))
        notas.append(nota)
        contador += 1
    except:
        print("Digíte apenas numeros.")

media = mean(notas)

for indice,nota in enumerate(notas):
    print(f"Nota {indice+1}: {nota:.2f} ")

print(f"Média: {media:.2f}")