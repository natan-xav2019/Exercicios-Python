# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def quantidadeConsoante( letras:list[str] ):
    total = 0
    for letra in letras:
        if not letra.upper() in ["A","E","I","O","U"]:
            total = total + 1

    return total

TAMANHO = 10
letras = []
contador = 0

while contador < TAMANHO:
    try:
        letra = input(f"{ contador + 1 } Digite a letra: ")
        
        if len(letra) == 1 and letra.isalpha() :
            letras.append( letra )
            contador += 1
        else:
            print("Apenas uma letra.")
    except:
        print("Digite apenas uma letra.")

consoante = quantidadeConsoante(letras)

print(consoante)