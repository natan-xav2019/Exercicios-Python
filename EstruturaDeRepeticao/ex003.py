# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

import locale

locale.setlocale(locale.LC_MONETARY,"pt-BR")

def resposta_sexo(sexo:str) -> str:
    if sexo.upper() == "M":
        return "Masculino"
    elif sexo.upper() == "F":
        return "Feminino"

def resposta_civil(estado_civil:str, sexo:str) -> str:
    resposta = ""

    if estado_civil.lower() == "s":
        resposta = "Solteir"
    elif estado_civil.lower() == "c":
        resposta = "Casad"
    elif estado_civil.lower() == "v":
        resposta = "Viuv"
    elif estado_civil.lower() == "d":
        resposta = "Divorciad"

    if sexo.upper() == "M":
        resposta += "o"
    elif sexo.upper() == "F":
        resposta += "a"

    return resposta

nome = ""
idade = -1
salario = -1
sexo = ""
estado_civil = ""

while len(nome) <= 2:
    nome = input("Digite o nome: ")
    if len(nome) <= 2:
        print("O nome tem que ser maior que 2.")

while not 0 <= idade <= 150:
    idade = int(input("Digite a idade: "))
    if not 0 <= idade <= 150:
        print("A idade tem que ser entre 0 e 150")

while not 0 <= salario:
    salario = float(input("Digite o salário: "))
    if not 0 <= salario:
        print("O Salário não pode ser negativo.")

while not sexo.upper() in ["F","M"]:
    sexo = input("Digite o Sexo: ")
    if not sexo.upper() in ["F","M"]:
        print("para informar o sexo digite F ou M.")

while not estado_civil.upper() in ["S","C","V","D"]:
    estado_civil = input("Digite o Estado cívil: ")
    if not len(nome) <= 2:
        if sexo.upper() == "M":
            print("para informar o Estado cívil digite S(Solteiro), C(casado), V(viuvo), D(divorciado).")
        elif sexo.upper() == "F":
            print("para informar o Estado cívil digite S(Solteira), C(casada), V(viuva), D(divorciada).")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {locale.currency(salario)}")
print(f"Sexo: {resposta_sexo(sexo)}")
print(f"Estado Civil: {resposta_civil(estado_civil,sexo)}")
