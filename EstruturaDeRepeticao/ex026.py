# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

class Candidato:
    def __init__(self,nome, votos):
        self.nome = nome
        self.votos = votos

    def apresentar(self):
        print(f"Votos do candidato: {self.nome}")
        print(f"Quantidade de votos: {self.votos}")


candidatos: list[Candidato] = []  
nome = ["A","B","C"]

for contador in range(1,4):
    quantidade_votos = int(input("Digite a quantidade de votos: "))
    candidato = Candidato(nome[contador-1],quantidade_votos)
    candidatos.append(candidato)

candidatos[0].apresentar()
candidatos[1].apresentar()
candidatos[2].apresentar()

 