# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
import numpy as np
import calendar
import datetime

data_atual = datetime.date.today()

ano = data_atual.year
mes = data_atual.month

ultimo_dia_mes = calendar.monthrange(ano, mes)[1]

data_inicio = f'{ano}-{mes:02d}-01'
data_fim = f'{ano}-{mes:02d}-{ultimo_dia_mes}'

# Calcule os dias úteis entre as datas
dias_uteis = np.busday_count(data_inicio, data_fim)

hora_trabalhadas_dia = int(input("quantas horas você trabalha no dia? "))
salario_hora = float(input("Quanto vc ganha por hora trabalhada? "))

salario = hora_trabalhadas_dia * salario_hora * dias_uteis

print(f"trabalhando {hora_trabalhadas_dia:02d}:00 e ganhando por hora R${salario_hora:.2f} tendo {dias_uteis} dias da um ganho salarial de R${salario:.2f}")




