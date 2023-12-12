# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

res = 1

for e in range(int(expoente)):
    res *= base

print(f"base: {base}")
print(f"expoente: {expoente}")
print(f"resposta: {res}")
