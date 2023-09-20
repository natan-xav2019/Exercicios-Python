# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

import numpy as np
import calendar
import datetime
import locale

def main():
    IMPOSTO_IR = 0.11
    IMPOSTO_INSS = 0.08
    IMPOSTO_SINDICADO = 0.05

    locale.setlocale(locale.LC_MONETARY,"pt-BR")
    data_atual = datetime.date.today()

    ano = data_atual.year
    mes = data_atual.month

    ultimo_dia_mes = calendar.monthrange(ano, mes)[1]

    data_inicio = f'{ano}-{mes:02d}-01'
    data_fim = f'{ano}-{mes:02d}-{ultimo_dia_mes}'

    # Calcule os dias úteis entre as datas
    dias_uteis = np.busday_count(data_inicio, data_fim)

    while True:
        try:
            hora_trabalhadas_dia = int(input("Quantas horas você trabalha no dia? "))
            if(hora_trabalhadas_dia > 0):
                break
            print("Horas somente positiva")
        except:
            print("Digite somente Numeros")

    while True:
        try:
            salario_hora = float(input("Quanto vc ganha por hora trabalhada? "))
            if(salario_hora > 0):
                break
            print("Ganho somente positiva")
        except:
            print("Digite somente Numeros")

    valor_bruto = hora_trabalhadas_dia * salario_hora * dias_uteis
    valor_ir = valor_bruto * IMPOSTO_IR
    valor_inss = valor_bruto * IMPOSTO_INSS
    valor_sindicato = valor_bruto * IMPOSTO_SINDICADO
    valor_liquido = valor_bruto - valor_ir - valor_inss - valor_sindicato

    print(f"\n+ Salário Bruto : {locale.currency(valor_bruto)}") 
    print(f"- IR (11%) : {locale.currency(valor_ir)}")
    print(f"- INSS (8%) : {locale.currency(valor_inss)}")
    print(f"- Sindicato ( 5%) : {locale.currency(valor_sindicato)}")
    print(f"= Salário Liquido : {locale.currency(valor_liquido)}")

if __name__ == "__main__":
    main()