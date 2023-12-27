# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

from statistics import median

temperaturas:list[float] = []

continuar = True
while True:
    temperaturas.append(float(input("Digite a temperatura: ")))

    while True:
        escolha = input("Dígite a sua escolha: ").upper()

        if escolha == "S":
            continuar = True
            break
        elif escolha == "N":
            continuar = False
            break
        else:
            print("Digite apenas S ou N.")

    if not continuar:
        break

minimo = min(temperaturas)
maximo = max(temperaturas)
media = median(temperaturas)

print(f"Menor temperatura {minimo}°C .")
print(f"Maior temperatura {maximo}°C .")
print(f"Média das temperaturas {media}°C .")