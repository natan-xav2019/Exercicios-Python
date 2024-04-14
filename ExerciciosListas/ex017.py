# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

from statistics import mean

SALTOS_EXTENSO = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"] 

def entradaSaltos() -> list[float]:
    saltos: list[float] = []
    i = 0
    while i < 5:
        valor = input(f"{SALTOS_EXTENSO[i]}: ")
        try:
            if float(valor):
                valor = float(valor)
                saltos.append(valor)
                i += 1
        except:
            pass
        
    return saltos

def resultado(nome,saltos):
    media = mean(saltos)
    saltos_escrito = ' - '.join(map(str, saltos))
    print(f"\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos_escrito}")
    print(f"Média dos saltos: {media:.1f} m\n")

def main():
    nome = "a"
    saltos = []
    
    while(nome):
        nome = input("Atleta: ")
        if nome != "":
            saltos = entradaSaltos()
            resultado(nome,saltos)

    print("Programa finalizado.")

if __name__ == "__main__":
    main()