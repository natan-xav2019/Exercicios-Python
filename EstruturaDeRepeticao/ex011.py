# Altere o programa anterior para mostrar no final a soma dos números.

numero = []

for contador in range(1,3):
    numero.append(float(input("Digite o numero: ")))

print(f"Soma de dois números: {sum(numero)}.")