# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

quantidade_total_divisao = 0

def E_primo(numero: int) -> bool:
    quantidade_divisores = 0

    for contador in range(1, numero+1 ):
        global quantidade_total_divisao
        quantidade_total_divisao += 1

        if numero % contador == 0:
            quantidade_divisores += 1

        if(quantidade_divisores  > 2):
            return False

    return True

ate_onde_numeros_primos = int(input("Digite 1 ate N numeros para mostrar os primos "))

primos = []

for numero in range(1, ate_onde_numeros_primos+1):
    if( E_primo(numero) ):
        print(f"O numero e primo {numero}")
        primos.append(numero)
        

print(f"total de visizoes realizadas: {quantidade_total_divisao}")