# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m
posisao_estenso = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
salto = []
denovo = False
contador = 0

class Atleta:
    def __init__( self,nome:str,saltos:list[float] ) -> None:
        self.nome = nome
        self.saltos = list(saltos)
        array_calculo_media = list(saltos)

        self.maior = max(saltos)
        self.menor = min(saltos)

        array_calculo_media.remove(self.maior)
        array_calculo_media.remove(self.menor)

        self.media_salto = sum(array_calculo_media)/len(array_calculo_media)

    def status(self):
        contador = 0
        print(f"\nAtleta: {self.nome}")
        while contador < 5:
            print(f"{posisao_estenso[contador]} Salto: {self.saltos[contador]:.1f} m")
            contador += 1
        
        print(f"\nMelhor Salto: {self.maior:.1f} m")
        print(f"Pior Salto: {self.menor:.1f} m")
        print(f"Média dos demais Saltos: {self.media_salto:.1f} m")

atletas:list[Atleta] = []

while True:
    nome = input("Átleta: ")
    
    if nome != "":
        while contador < 5:
            if denovo:
                salto[contador] = float(input(f"{posisao_estenso[contador]} Salto: "))
            else:
                denovo = True
                salto.append(float(input(f"{posisao_estenso[contador]} Salto: ")))
            if salto[contador] > 0:
                contador += 1
                denovo = False
            else:
                print(f"Digite apenas numero possitivos.")
    else:
        break
    
    atletas.append(Atleta(nome,salto))
    salto.clear()
    contador = 0

maior_media = 0

for indice,atleta in enumerate(atletas):
    atleta.status()
    if atleta.media_salto > atletas[maior_media].media_salto:
        maior_media = indice

print("\nResultado final:")
print(f"{atletas[maior_media].nome}: {atletas[maior_media].media_salto:.1f} m")