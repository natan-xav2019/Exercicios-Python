# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

import locale

locale.setlocale(locale.LC_ALL,"PT-br")

print("Lojas Tabajara")

while True :
    contador = 1
    total = 0
    while True :
        preso = float(input(f"Produto {contador}: R$ "))
        if preso :
            contador += 1
            total += preso
        elif preso == 0 :
            break
        else:
            print("Digite apenas numeros possitivos.")
    
    print(f"Total: {locale.currency(total)}")
    troco = 0

    while True :
        dinheiro = float(input(f"Dinheiro: R$ "))

        if dinheiro :
            if total == dinheiro :
                troco = 0
                break
            elif total < dinheiro :
                troco = dinheiro - total
                break
            else :
                print("Digité um valor de dinheiro igual o superior para oferecer o troco.")
        else :
            print("Digité um valor maior que 0.")

    print(f"Troco: {locale.currency(troco)}")
