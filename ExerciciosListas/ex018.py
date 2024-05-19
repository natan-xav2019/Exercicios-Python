# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

import os.path

def apurasao_votos_indice(quantidade_votos:int,candidatos:list[list[int,int]]):
    for index, candidato in enumerate(candidatos):
        if candidato[1] == quantidade_votos:
            return index
        
candidatos = [ [x,0] for x in range(1,24) ]

while True:
    try:
        voto_numero = int(input("Número do jogador (0=fim): "))
        if voto_numero == 0:
            break
        candidatos[voto_numero-1][1] = candidatos[voto_numero-1][1]+1
    except:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")


total_votos = sum([ candidato[1] for candidato in candidatos ])
candidato_vencedor = max([ votos for candidato,votos in candidatos ])
indice_vencedor = apurasao_votos_indice(candidato_vencedor,candidatos)

caminho = "C:/xampp/htdocs/Exercicios-Python/ExerciciosListas/melhorJogador.txt"

if os.path.isfile(caminho):
    arquivo = open(caminho,"w",encoding="utf-8")
else:
    arquivo = open(caminho,"x",encoding="utf-8")

print("Resultado da votação:")
arquivo.write("Resultado da votação:\n")
print(f"Foram computados {total_votos} votos.")
arquivo.write(f"Foram computados {total_votos} votos.\n")
print("Jogador\tVotos\t%")
arquivo.write("Jogador\t\tVotos\t\t%\n")
for candidato in candidatos:
    if(candidato[1] != 0):
        print(f"{candidato[0]:2d}\t{candidato[1]:2d}\t{candidato[1]/total_votos:.1%}")
        arquivo.write(f"{candidato[0]:2d}\t\t{candidato[1]:2d}\t\t{candidato[1]/total_votos:.1%}\n")

print(f"O melhor jogador foi o número {candidatos[indice_vencedor][0]:2d}, com {candidatos[indice_vencedor][1]:2d} votos, correspondendo a {candidatos[indice_vencedor][1]/total_votos:.1%} do total de votos.")
arquivo.write(f"O melhor jogador foi o número {candidatos[indice_vencedor][0]:2d}, com {candidatos[indice_vencedor][1]:2d} votos, correspondendo a {candidatos[indice_vencedor][1]/total_votos:.1%} do total de votos.\n")

arquivo.close()