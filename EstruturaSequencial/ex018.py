# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

megabytes = float(input("quantidade de MB do arquivo: "))
megabits_por_segundo = float(input("velocidade da internet em Mbps: "))

megabits = megabytes * 8
segundos = megabits / megabits_por_segundo
minutos = segundos / 60

print(f"vali demorar {minutos:.2f} minuto(s).")