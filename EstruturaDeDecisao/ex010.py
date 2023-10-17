# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def qual_turno(case: str) -> str:
    if(case == "M"):
        return "Bom dia!"
    elif(case == "V"):
        return "Boa Tarde!"
    elif(case == "N"):
        return "Boa Noite!"
    else:
        return "Valor Inválido!"


print("digitar M- matutino ou V- Vespertino ou N- Noturno")

while True:
    turno_estuda = input("Digite o seu turno de estuda: ")
    if(len(turno_estuda) == 1 and turno_estuda.isalpha()):
        break
    else:
        print("Digite apenas uma letra por favor.")

turno_estuda = turno_estuda.upper()

print(qual_turno(turno_estuda))