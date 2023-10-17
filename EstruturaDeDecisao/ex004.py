# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = set(["A","E","I","O","U"])

while True:
    letra = input("Digite uma letra: ")
    if(len(letra) == 1 and letra.isalpha()):
        break
    else:
        print("Digite apenas uma letra por favor.")

letra = letra.upper()

if letra in vogais:
    print(f"letra \"{letra}\" e uma vogal.")
else:
    print(f"letra \"{letra}\" e uma consoante.")