# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

index = 0
soma = 0
notas = []

print("Digite as 4 notas")

while index < 4:
    eLimite = True
    notas.append(float(input("nota : ")))
    while eLimite:

        if(not(notas[index] < 0 or notas[index] > 10)):
            eLimite = False
            break
        print(f"A nota precisa ser entre 0 e 10. por favor, digite novamente!!")
        notas[index] = float(input("nota : "))

    soma = soma + notas[index]
    index = index + 1

media = soma/index

print(f"A media desse bimestre e {media}")

for index, nota  in enumerate(notas):
    print(f"nota {index+1}: {nota}")