# Caixa Registradora de Mercado

qtd_produtos = 0
total = 0

while True:
    preco_produto = float(input("Informe o preço do produto: R$ "))
    if preco_produto < 0:
        print("Valor inválido! O preço não pode ser um valor negativo.")
    elif preco_produto == 0:
        print(f"Quantidade total de produtos: {qtd_produtos}")
        print(f"Valor total da compra: R$ {total:.2f}")
        break
    else:
        qtd_produtos += 1
        total += preco_produto