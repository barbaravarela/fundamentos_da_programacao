print("Bem-vindo ao Sistema de Caixa de Supermercado!")

total = 0
quantidade = 0
media = 0

while True:
    valor_produto = float(input("Digite o valor do produto: "))
    if valor_produto == 0:
        if total > 100:
            print("O total da compra foi maior que R$100, então você recebeu 10% de desconto!")
            print(f"Total: {total*0.9}")
        else:
            print(f"Total: {total}")
        print(f"Quantidade: {quantidade}")
        print(f"Média: {media:.2f}")
        break
    quantidade += 1
    total += valor_produto
    media = total / quantidade