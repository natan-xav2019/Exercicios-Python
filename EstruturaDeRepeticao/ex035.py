# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


def E_primo(numero: int) -> bool:
    quantidade_divisores = 0

    for contador in range(1, numero+1 ):

        if numero % contador == 0:
            quantidade_divisores += 1

        if(quantidade_divisores  > 2):
            return False

    return True

ate_onde_numeros_primos = int(input("Digite 1 ate N numeros para mostrar os primos "))

primos = []

for numero in range(1, ate_onde_numeros_primos+1):
    if E_primo(numero) :
        primos.append(numero)
        
print(primos)