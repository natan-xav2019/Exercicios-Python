# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

TAMANHO = 20

vetor = []
par = []
impar = []
contador = 0

while contador < TAMANHO:
    try:
        numero = int(input(f"{contador+1} Digite o numero: "))
        vetor.append(numero)

        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

        contador += 1
    except:
        print("Digite apenas numeros inteiros.")

print("Vetor")
print(vetor)

print("Vetor Par")
print(par)

print("Vetor Impar")
print(impar)