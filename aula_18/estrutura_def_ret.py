# Função que exibe os sabores, tamanhos e valores das pizzas
def exibir_cardapio():
    print("=== CARDÁPIO PIZZARIA DO CÓDIGO ===")
    print("Margherita - P: R$25 | M: R$35 | G: R$45")
    print("Calabresa - P: R$28 | M: R$38 | G: R$48")
    print("Frango - P: R$30 | M: R$40 | G: R$50")

# exibir_cardapio()

# Função para aplicar desconto, onde o preço e o percentual de desconto será passado no momento da invocação da função
valor_sem_desc = 40
def aplicar_desconto(preco, percentual):
    return preco * percentual

preco_final = valor_sem_desc - aplicar_desconto(valor_sem_desc, 0.10)
# print(f"Preço com desconto: R${preco_final:.2f}")

# Função que receberá por padrão que a borda não é recheada. Além disso, irá receber também o sabor e o tamanho da pizza com padrão "M"
def fazer_pedido(sabor, tamanho="M", borda_recheada=False):
    borda = "com borda recheada" if borda_recheada else "sem borda recheada"
    # variável = valor_se_True if condição_lógica else valor_se_False
    print(f"Pedido: {sabor} | {tamanho} | {borda}")

fazer_pedido("Margherita")
fazer_pedido("Frango", "G")
fazer_pedido("Calabresa", "P", True)