# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

TAMANHO = 10
contador = 0
vetor:list[float] = []

while contador < TAMANHO:
    try:
        numero = float(input(f"{contador+1} Digite o numero: "))
        vetor.append(numero)
        contador += 1
    except:
        print("Digite apenas numeros inteiros.")

vetorInvertido = vetor[::-1]

print("Vetor Normal")
print(vetor)

print("Vetor Inverter")
print(vetorInvertido)