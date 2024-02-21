# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

MAX = 5

idades = []
alturas = []
contador = 0

while contador < MAX:
    try:
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        idades.append(idade)
        alturas.append(altura)
        contador += 1 
    except:
        print("Para idade digite apenas numeros inteiros para altura apenas numeros.")

print(f'idades: {idades}')
print(f'alturas: {alturas}')

idades.reverse()
alturas.reverse()

print(f'idades ordem iversa: {idades}')
print(f'alturas ordem iversa: {alturas}')