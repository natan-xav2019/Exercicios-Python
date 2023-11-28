# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para vitima?"
# b. "Esteve no local de crime?"
# c. "Mora perto da vitima?"
# d. "Devia para a vitima?"
# e. "Já trabalhou com a vitima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 a 4 como "Cúmplice" e 5 como "Assassíno". Caso contrário, ele será classificado como "Inocente".

nivel_classificasao = 0

perguntas = ["Telefonou para vitima?", "Esteve no local de crime?", "Mora perto da vitima?", "Devia para a vitima?", "Já trabalhou com a vitima?"]

for pergunta in perguntas:
    while True:
        try:
            resposta = input(f"{pergunta} ").upper()

            if resposta in "SIM" :
                nivel_classificasao += 1
                break
            elif resposta in "NÃO" :
                break
            else:
                print("Escreve apenas \"Sim\" ou \"Não\". ")
        except:
            print("Apenas palavras")


if(nivel_classificasao < 2):
    print(f"Classificado como Inocente")
elif(nivel_classificasao < 3):
    print(f"Classificado como Suspeita")
elif(nivel_classificasao < 5):
    print(f"Classificado como Cúmplice")
else:
    print(f"Classificado como Assassíno")