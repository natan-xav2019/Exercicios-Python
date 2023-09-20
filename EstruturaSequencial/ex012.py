# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

calculoPesoIdeal = lambda altura : (72.7*altura) - 58

while True:
    try:
        altura = float(input("Seu peso: "))
        break
    except:
        print("Digite apenas numeros")

PesoIdeal = calculoPesoIdeal(altura)

print(f"Com altura {altura}m teria que ter um peso ideal de {PesoIdeal:.2f}.")