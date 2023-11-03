# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
import re

dia_cada_mes = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def valida_data(data) -> bool:
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    
    limite_ano = ano > 0
    limite_mes = 0 < mes <= 12
    if(limite_ano):
        ano_bissexto = ano % 4 == 0
    else:
        return False
    
    print(f"ano_bissexto: {ano_bissexto}")

    if(ano_bissexto):
        dia_cada_mes[1] = 29
    else:
        dia_cada_mes[1] = 28


    if(limite_mes):
        if 0 < dia <= dia_cada_mes[mes-1]:
            return True
        else:
            return False
    else:
        return False

padrao = re.compile(r"^\d{2}\/\d{2}\/\d{4}$")

while True:
    texto = input("Digite a data no formato \"dd/mm/aaaa\" por favor para ser considerada valida: ")
    data = re.fullmatch(padrao, texto)
    if not (data == None) :
        dataArray = data.group().split("/")
        
        aprovado = valida_data(dataArray)
        
        if(aprovado):
            break
        else:
            print(f"A Data não esta dentro dos padrões.")
    else:
        print(f"Digite Apenas data no formato \"dd/mm/aaaa\" .")
            

print(f"Data valida: {dataArray[0]}/{dataArray[1]}/{dataArray[2]}")
