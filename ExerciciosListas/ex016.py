# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante

PORCENTAGEM_COMISAO = 0.09
SALARIO_BASE = 200

def intervalo(valor:float) -> int:
    minimo = 200
    maximo = 299
    incremento = 100

    for i in range(0, 9):
        if minimo <= valor <= maximo:
            return i
        minimo += incremento
        maximo += incremento

    return i+1

def calculoSalario(vendas_mes):
    return (PORCENTAGEM_COMISAO*vendas_mes) + SALARIO_BASE 

def main():
    contadores =  [0 for x in range(1,11)]

    funcionarios = [3000]

    for funciario in funcionarios:
        salario_funcionario = calculoSalario(funciario) 
        contadores[intervalo(salario_funcionario)] += 1
        
    print(contadores)

if __name__ == "__main__":
    main()
