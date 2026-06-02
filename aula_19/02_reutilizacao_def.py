# Função para calcular o valor da pizza pelo tamanho
def calcular_preco_pizza(tamanho):
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    return tabela.get(tamanho, 0) # se tamanho não for uma chave de tabela, a função retorna 0