# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

LIMITE_TABUADA = [1,10]

while True:
    try:
        tabuada = int(input("Digite o numero para ver a tabuada: "))
        if LIMITE_TABUADA[0] <= tabuada <= LIMITE_TABUADA[1]:
            break
        else:
            print(f"Digite apenas numeros entre {LIMITE_TABUADA[0]} e {LIMITE_TABUADA[1]}")
    except:
        print("Apenas numeros!!!")

for cont in range(1,11):
    print(F"{tabuada:2d} X {cont:2d} = { tabuada * cont }")