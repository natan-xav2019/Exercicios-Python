# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio

from statistics import median

class Cidade:
    def __init__(self,codigo:int,quantidade_veiculo:int,quantidade_acidente:int) -> None:
        self.codigo:int = codigo
        self.quantidade_veiculo:int = quantidade_veiculo
        self.quantidade_acidente:int = quantidade_acidente
        self.indice_acidente:float = self.calculo_indice_acidente()
        pass
        
    def calculo_indice_acidente(self) -> float:
        if(self.quantidade_veiculo != 0):
            return (self.quantidade_acidente / self.quantidade_veiculo) * 100
        else:
            return 0
    
cidades:list[Cidade] = []
contador = 1

while contador <= 5:
    igual = False
    id_cidade = int(input("Digite o codigo da cidade: "))
    for cidade in cidades:
        if id_cidade == cidade.codigo:
            igual = True
            break
    
    if not igual:
        while True:
            quantidade_veiculo = int(input("Digite o quantidade de veiculos: "))
            quantidade_acidente = int(input("Digite a quantidada de acidentes: "))
            if quantidade_veiculo >= quantidade_acidente and quantidade_veiculo != 0:
                cidades.append(Cidade(id_cidade,quantidade_veiculo,quantidade_acidente))
                contador += 1
                break
            else:
                print("quantidade de veiculos não pode ser 0 e não pode ser menor que a quantidade de acidentes")
    else:
        print("Digite codigos difentes.")

cidade_veiculo = []
cidade_acidente = []
cidade_acidente_condicional = []
cidade_maior_acidente = 0
cidade_menor_acidente = 0


for indice,cidade in enumerate(cidades):
    cidade_veiculo.append(cidade.quantidade_veiculo)

    if cidade.quantidade_acidente >= cidades[cidade_maior_acidente].quantidade_acidente:
        cidade_maior_acidente = indice

    if cidade.quantidade_acidente <= cidades[cidade_menor_acidente].quantidade_acidente:
        cidade_menor_acidente = indice

    if cidade.quantidade_veiculo > 20000:
        cidade_acidente_condicional.append(cidade.quantidade_acidente)

media_veiculos = median(cidade_veiculo)
media_acidente_condicional = median(cidade_acidente_condicional)

print(f"Média de veiculo das 5 cidades e {media_veiculos:.2f}")
print(f"Média de acidente com mais de 20000 habitantes {media_acidente_condicional:.2f}")

print(f"A cidade com maior acidente.")
print(f"Codigo: {cidades[cidade_maior_acidente].codigo}")
print(f"Quantidade de veiculos: {cidades[cidade_maior_acidente].quantidade_veiculo}")
print(f"Quantidade de acidente: {cidades[cidade_maior_acidente].quantidade_acidente}")
print(f"Indice do acidente: {cidades[cidade_maior_acidente].indice_acidente}")

print(f"A cidade com menor acidente.")
print(f"Codigo: {cidades[cidade_menor_acidente].codigo}")
print(f"Quantidade de veiculos: {cidades[cidade_menor_acidente].quantidade_veiculo}")
print(f"Quantidade de acidente: {cidades[cidade_menor_acidente].quantidade_acidente}")
print(f"Indice do acidente: {cidades[cidade_menor_acidente].indice_acidente}")