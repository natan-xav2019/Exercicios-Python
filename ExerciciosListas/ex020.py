# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
# a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
# Projeção de Gastos com Abono
# ============================ 
 
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
 
# Salário    - Abono     
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00
 
# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00
import locale
from statistics import mean

locale.setlocale(locale.LC_ALL,"pt_BR")

ABONO_PORCENTO = 0.2
ABONO_MINIMO = 100

class Funcionario:
    def __init__(self) -> None:
        self._salario:float = 0
        self._abono:float = 0

    @property
    def salario(self):
        return self._salario
    
    @property
    def abono(self):
        return self._abono

    @salario.setter
    def salario(self, salario):
        self._salario = salario
        self._abono = self.calculoAbono()

    def calculoAbono(self) -> float: 
        abonoCalculo = self._salario * ABONO_PORCENTO

        if abonoCalculo < ABONO_MINIMO:
            return ABONO_MINIMO
        
        return abonoCalculo

funcionarios:list[Funcionario] = []
quantidade_abonos = 0

while True:
    try:
        salario = input('Salário: ')
        salario = int(salario)
        if salario == 0:
            break
        elif salario > 0:
            funcionarios.append(Funcionario())
            funcionarios[len(funcionarios) - 1].salario = salario
    except:
        print("Entrada inválida. Informe um valor numérico.")

todos_abono = [funcionario.abono for funcionario in funcionarios]

quantidade_funcionarios = len(funcionarios)
maior = max(todos_abono)
soma = sum(todos_abono)
media = mean(todos_abono)

print(f"Salário    - Abono")
for funcionario in funcionarios:
    print(f"{locale.currency(funcionario.salario):10} - {locale.currency(funcionario.abono):10}")
    if (funcionario.abono == ABONO_MINIMO):
        quantidade_abonos += 1

print(f"\nForam processados {quantidade_funcionarios} colaboradores")
print(f"Total gasto com abonos: {locale.currency(soma)}")
print(f"Valor mínimo pago a {quantidade_abonos} colaboradores")
print(f"Maior valor de abono pago: {locale.currency(maior)}")
        