# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

from statistics import mean

valores = []
valor = 0


while valor != -1:
    try:
        valor = input("Digite um numero: ")
        valor = float(valor)
        if valor != -1:
            valores.append(valor)
        else:
            break
    except:
        print("Somente escreva numeros.")
    

print(f"Quantidade de valores lidos: {len(valores)}")
valores.reverse()
print(f"Valores na ordem inversa:")
for val in valores:
    print(val)

valores_media = mean(valores)
valores_soma = sum(valores)
print(f"Soma dos valores: {valores_soma}")

print(f"Media dos valores: {valores_media}")


valores_acima_media = list(filter(lambda valor: valor > valores_media  , valores))
valores_abaixo_sete = list(filter(lambda valor: valor < 7  , valores))

print(valores_acima_media)
print(valores_abaixo_sete)

print("Programa finalizado com sucesso!")
