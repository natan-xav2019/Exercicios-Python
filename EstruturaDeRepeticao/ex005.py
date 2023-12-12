# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def quantos_anos_igual(populasao: list[int],taxa: list[float]) -> int:
    anos = 0
    
    if populasao[0] == populasao[1]:
        return anos
    elif populasao[0] > populasao[1]:
        populasao.reverse()
        taxa.reverse()

    while populasao[0] < populasao[1]:
        populasao[0] = int(populasao[0] * (1+taxa[0]))
        populasao[1] = int(populasao[1] * (1+taxa[1]))
        anos += 1

    return anos

taxa_populasao_ano = [0,0]
populasao = [0,0]
escolhas = ["A","B"]

for index,escolha in enumerate(escolhas):
    taxa_populasao_ano[index] = (float(input(f"Digite por qual taxa da população {escolha} desejada: "))) / 100

for index,escolha in enumerate(escolhas):
    populasao[index] = int(input(f"Digite a população {escolha} desejada: "))

anos = quantos_anos_igual(populasao,taxa_populasao_ano)

print(f"A: {populasao[0]}")
print(f"B: {populasao[1]}")
print(f"Com {anos} ano(s) a população A ira conseguir alcançar a população B.")