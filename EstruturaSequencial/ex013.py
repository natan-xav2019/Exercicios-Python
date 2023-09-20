# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

calculoAlturaIdealHomem = lambda altura : (72.7*altura) - 58
calculoAlturaIdealMulher = lambda altura : (62.1*altura) - 44.7

while True:
    try:
        altura = float(input("Digite seu altura: "))
        if(altura > 0):
            break
        else:
            print("digite um numero possitivo")
    except:
        print("Digite apenas numeros")

alturaIdealHomem = calculoAlturaIdealHomem(altura)
alturaIdealMulher = calculoAlturaIdealMulher(altura)

print(f"Altura ideal para Homens: {alturaIdealHomem:.2f}")
print(f"Altura ideal para Mulheres: {alturaIdealMulher:.2f}")