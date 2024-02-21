# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
pontuasao = 0
contador = 0

print("Responda somente Sim ou Não")
while contador < len(perguntas):
    try:
        resposta = input(f'{perguntas[contador]} ')
        if resposta.upper() in ["SIM","NÃO"]:
            if resposta.upper() == "SIM":
                pontuasao += 1
            contador += 1
        else:
            print("Digite apenas Sim ou Não")
    except:
        print("Digite apenas Sim ou Não")


if pontuasao < 2:
    print("Inocente")
elif pontuasao < 3: 
    print("Suspeita")
elif pontuasao <= 4:
    print("Cúmplice")
elif pontuasao <= 5:
    print("Assassino")