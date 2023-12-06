# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0

while not (0 < nota < 10):
    nota = int(input("Digite uma nota: "))
    if(not (0 < nota < 10)):
        print("Digite apenas notas entre 0 e 10.")

print(f"Nota {nota} validado com sucesso!!!")