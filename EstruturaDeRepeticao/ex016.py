# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500

def fibonacci(repetisao: int) -> list[int]:
    n1 = 1
    n2 = 1

    resultado = []

    if repetisao == 1 :
        resultado.append(n1)
    elif repetisao == 2 :
        resultado.extend([n1,n2])
    elif repetisao >= 3 :
        resultado.append(n1) 
        for cont in range(2,repetisao):
            n3 = n2
            n2 = n2 + n1
            n1 = n3
            resultado.append(n3)
        
    return resultado

flag = 1
cont = 1

while flag <= 500:
    resposta = fibonacci(cont)
    flag = resposta[-1]
    cont += 1

print(resposta)

