# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

TAMANHO = 10

vetor1 = []
vetor2 = []
vetor3 = []
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

print("Digite 10 numeros vetor 3")
contador = 0
while contador < TAMANHO:
    try:
        numero = int(input("Digite o numero: "))
        vetor3.append(numero)
        contador += 1
    except:
        print("Apenas numeros inteiros.")

contatenasao_vetor = vetor1 + vetor2 + vetor3

print("Vetores concatenados.")
print(contatenasao_vetor)