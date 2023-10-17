# Faça um Programa que leia três números e mostre o maior e o menor deles.

numeros = []

for i in range(3):
    numeros.append(float(input("Digite o numero: ")))

print(f"O maior numero é {max(numeros)}")
print(f"O Menor numero é {min(numeros)}")