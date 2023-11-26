# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
MAXIMO_NOTA = [10, 600]
notas_disponiveis = [ 100, 50, 10, 5, 1 ]
notas_extenso = ["zero", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez" ]

dinheiro = 399
troco = f"Para sacar a quantia de {dinheiro} reais, o programa fornece "


if( MAXIMO_NOTA[0] <= dinheiro <= MAXIMO_NOTA[1] ):                
    indice = 0
    while dinheiro != 0:
        nota = int( dinheiro / notas_disponiveis[indice] )
        if(nota !=0):
            if(nota > 1):
                troco += f"{notas_extenso[nota]} notas de {notas_disponiveis[indice]}, "
            else:
                troco += f"{notas_extenso[nota]} nota de {notas_disponiveis[indice]}, "
                
        dinheiro = dinheiro % notas_disponiveis[indice]

        indice += 1

    troco = troco[:-2]
    troco += "."

    posisao_virgula = troco.rfind(',')

    troco = f"{troco[:posisao_virgula]} e{troco[posisao_virgula + 1:]}"

    print(troco)
else:
    print(F"O intervalo de retirada e de {MAXIMO_NOTA[0]} e {MAXIMO_NOTA[1]}")



