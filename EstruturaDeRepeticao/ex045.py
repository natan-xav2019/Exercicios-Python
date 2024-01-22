# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

QUANTIDADE_NOTAS = 10
OPISOES_NOTA = ["A","B","C","D","E"]
gabarito = ["A","B","C","D","B","B","C","D","E","A"]

class Estudante:
    def __init__(self,respostas:list[str]) -> None:
        self.respostas = respostas
        self.nota = 0
        self.resultado()

    def resultado(self):
        for indice,questao in enumerate(self.respostas):
            if gabarito[indice] == questao:
                self.nota += 1
        
alunos:list[Estudante] = []

questao = []
denovo = False
continuar = True
contador = 0


while continuar:
    fazer_gabarito = input("Deseja Fazer o gabarito? ").upper()
    if fazer_gabarito in "S":
        continuar = False
        fazer_gabarito = True
        gabarito.clear()
        break
    elif fazer_gabarito in "N":
        continuar = False
        fazer_gabarito = False
        break
    else:
        print("Digite apenas S ou N.")

continuar = True

while fazer_gabarito:
    try:
        while contador < 10:
            if denovo:
                gabarito[contador] = input(f"Digite o gabarito da questão {contador+1} ").upper()
            else:
                denovo = True
                gabarito.append(input(f"Digite o gabarito da questão {contador+1} ").upper())
            if gabarito[contador] in OPISOES_NOTA:
                contador += 1
                denovo = False
            else:
                print(f"Digite apenas as opções {OPISOES_NOTA}") 

    except:
        print(f"Digite apenas as opções {OPISOES_NOTA}")

    if contador == 10:
        break

contador = 0

print("Digite a resposta dos alunos")
while continuar:
    try:
        while contador < 10:
            if denovo:
                questao[contador] = input(f"Digite a resposta da questão {contador+1} ").upper()
            else:
                denovo = True
                questao.append(input(f"Digite a resposta da questão {contador+1} ").upper())
            if questao[contador] in OPISOES_NOTA:
                contador += 1
                denovo = False
            else:
                print(f"Digite apenas as opções {OPISOES_NOTA}") 

    except:
        print(f"Digite apenas as opções {OPISOES_NOTA}")

    alunos.append(Estudante(questao))
    questao.clear()
    contador = 0
    while True:
        mais_aluno = input("Deseja continuar? ").upper()
        if mais_aluno in "S":
            continuar = True
            break
        elif mais_aluno in "N":
            continuar = False
            break
        else:
            print("Digite apenas S ou N.")

maior = 0
menor = 0
total_notas = 0

for indice,aluno in enumerate(alunos):
    if alunos[maior].nota < aluno.nota:
        maior = indice
    if alunos[menor].nota > aluno.nota:
        menor = indice
    total_notas += aluno.nota

nota_media = total_notas/QUANTIDADE_NOTAS

print(f"Maior nota: {alunos[maior].nota}")
print(f"Menor nota: {alunos[menor].nota}")
print(f"quantidade de alunos {len(alunos)}")
print(f"Gabarito: {gabarito}")