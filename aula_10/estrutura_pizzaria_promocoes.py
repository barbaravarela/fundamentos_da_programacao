# Variáveis da pizzaria
FRETE = 2 # constante fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ")
pizza_tamanho = input("Informe o tamanho da pizza - [pequena], [média], [grande]: ")
dia_semana = input("Informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]: ")
print(f"O sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}")

# Promoções -> Estruturas condicionais
# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito.
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.
# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratuito.
if dia_semana == "sábado":
    print(f"🍕 Pedido aceito com sucesso!") # Windows + . para colocar emoji
    print(f"O refri hoje é por conta da casa!")
elif dia_semana == "domingo":
    print(f"🍕 Pedido aceito com sucesso!")
    print(f"O frete e o refri hoje são por conta da casa!")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕 Pedido aceito com sucesso!")
    print(f"O frete hoje é por conta da casa!")