# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci(repetisao: int) -> list[int]:
    n1 = 1
    n2 = 1

    resultado = []

    if repetisao == 1 :
        resultado.append(n1)
    elif repetisao == 2 :
        resultado.extend(n1,n2)
    elif repetisao >= 3 :
        resultado.append(n1) 
        for cont in range(2,repetisao+1):
            n3 = n2
            n2 = n2 + n1
            n1 = n3
            resultado.append(n3)
        
    return resultado

print(fibonacci(6))