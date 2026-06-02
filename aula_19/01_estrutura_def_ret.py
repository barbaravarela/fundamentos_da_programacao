# Parâmetros nomeados - ao nomear os argumentos, a ordem não importa mais.
def registrar_cliente(nome, telefone, endereco):
    print("=== DADOS DO CLIENTE ===")
    print(f"Cliente: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereco}")

# Argumentos nomeados — ordem não importa
# registrar_cliente(
#     telefone="21985653275",
#     nome="Ana Lima",
#     endereco="Rua das Pizzas, 42"
# )

# Retorno de valores - desempacotamento de retorno (unpacking) - devolve uma tupla com os returns
def resumo_pedido(itens, desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * (desconto / 100)
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total  # devolve um tupla (subtotal, valor_desconto, total)

# Invocando e desempacotando a função/retorno
# print(resumo_pedido([35.0, 12.0, 8.5], desconto=10))
sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
print(f"Subtotal: R$ {sub:.2f}")
print(f"Desconto: R$ {desc:.2f}")
print(f"Total: R$ {tot:.2f}")