# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numeroIntero1 = int(input("Digite o 1° numero inteiro: "))
numeroIntero2 = int(input("Digite o 2° numero inteiro: "))
numeroReal = float(input("Digite o 2° numero real: "))

print(f"O produto do dobro do primeiro com metade do segundo: {numeroIntero1*2 + numeroIntero2/2}")
print(f"A soma do triplo do primeiro com o terceiro: {numeroIntero1*3 + numeroReal}")
print(f"O terceiro elevado ao cubo: {numeroReal**3}")