# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

TAXA_CRESCIMENTO_ANO = {
    "A": 0.03,
    "B": 0.015,
} 

populasao = {
    "A": 80000,
    "B": 200000,
}

anos = 0

while populasao["B"] > populasao["A"]:
    populasao["A"] = int(populasao["A"] * (1+TAXA_CRESCIMENTO_ANO["A"]))
    populasao["B"] = int(populasao["B"] * (1+TAXA_CRESCIMENTO_ANO["B"]))
    anos += 1

print(f"A: {populasao['A']}")
print(f"B: {populasao['B']}")
print(f"Com {anos} ano(s) a população A ira conseguir alcançar a população B")
