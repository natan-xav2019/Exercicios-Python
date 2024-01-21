# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

class Candidato:
    def __init__(self,nome:str,codigo:int) -> None:
        self.nome = nome
        self.codigo = codigo
        self.quantidade_votos = 0
    
    def votar(self) -> None:
        self.quantidade_votos += 1

def resultado(candidatos:list[Candidato]) -> bool:
    maior = 0
    for indice,candidato in enumerate(candidatos):        
        if candidato.quantidade_votos > candidatos[maior].quantidade_votos:
            maior = indice

    return maior

candidatos:list[Candidato] = []

candidatos.append(Candidato("Jose",1))
candidatos.append(Candidato("João",2))
candidatos.append(Candidato("Taynara",3))
candidatos.append(Candidato("Natan",4))
candidatos.append(Candidato("Nulo",5))
candidatos.append(Candidato("Branco",6))

while True:
    try:
        codigo = int(input("Digite o codigo que deseja voltar:"))
        for candidato in candidatos:
            if codigo == candidato.codigo:
                print(f"Voto: {candidato.codigo}")
                print(f"Candidato: {candidato.nome}")
                candidato.votar()
        if codigo == 0:
            break
    except:
        print("Digite um codigo valido.")

total_votos = sum([ candidato.quantidade_votos for candidato in candidatos ])
        
if candidatos[4].quantidade_votos != 0:
    porcentagem_votos_nulos = candidatos[4].quantidade_votos/total_votos
else:
    porcentagem_votos_nulos = 0
if candidatos[5].quantidade_votos != 0:
    porcentagem_votos_banco = candidatos[5].quantidade_votos/total_votos
else:
    porcentagem_votos_banco = 0

for candidato in candidatos:
    print(f"Candidato: {candidato.nome}")
    print(f"Codigo: {candidato.codigo}")
    print(f"O total de votos: {candidato.quantidade_votos}")

print(f"A percentagem de votos nulos sobre o total de votos: {porcentagem_votos_nulos}")
print(f"A percentagem de votos em branco sobre o total de votos: {porcentagem_votos_banco}")