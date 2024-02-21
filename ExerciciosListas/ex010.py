# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

TAMANHO = 10

vetor1 = []
vetor2 = []
contador = 0

print("Digite 10 numeros vetor 1")
while contador < TAMANHO:
    try:
        numero = int(input("Digite o numero: "))
        vetor1.append(numero)
        contador += 1
    except:
        print("Apenas numeros inteiros.")

print("Digite 10 numeros vetor 2")
contador = 0
while contador < TAMANHO:
    try:
        numero = int(input("Digite o numero: "))
        vetor2.append(numero)
        contador += 1
    except:
        print("Apenas numeros inteiros.")

contatenasao_vetor = vetor1 + vetor2

print("Vetores concatenados.")
print(contatenasao_vetor)