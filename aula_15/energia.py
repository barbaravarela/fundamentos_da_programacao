# ATIVIDADE 01 - Calculadora de Tarifas de Energia Elétrica

# Até 100 kWh → R$ 0,40 por kWh - 100 -> R$ 40
# De 101 a 200 kWh → R$ 0,60 por kWh - 40 + 60 -> R$ 100
# Acima de 200 kWh → R$ 0,90 por kWh
# Exibir ao final: o consumo informado, a faixa de tarifa aplicada e o valor total a pagar.
# Caso o consumo informado seja negativo, exibir uma mensagem de valor inválido.

# Declaração das variáveis globais
valor_ate_100kwh = 0.40
valor_ate_200kwh = 0.60
valor_acima_200kwh = 0.90

print("------ Seja bem-vindo ao programa de cálculo de energia elétrica ------")

while True:
    input_kwh = input("Digite a quantidade de kwh consumidos (ou 'sair' para encerrar): ")
    if input_kwh.lower() == "sair":
        print("Encerrando o programa. Obrigado por usar!\n")
        break
    elif not input_kwh.isdigit():
        print("Entrada inválida! Por favor, digite um número válido ou 'sair' para encerrar\n")
        continue
    else:
        kwh = int(input_kwh)
        if kwh <= 100:
            valor_total = kwh * valor_ate_100kwh
            print("A faixa de consumo é: 0 a 100 kwh.")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")
        elif kwh <= 200:
            valor_total = 100 * valor_ate_100kwh + (kwh - 100) * valor_ate_200kwh
            print("A faixa de consumo é: entre 100 a 200 kwh.")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")
        else:
            valor_total = 100 * valor_ate_100kwh + 100 * valor_ate_200kwh + (kwh - 200) * valor_acima_200kwh
            print("A faixa de consumo é: acima de 200 kwh.")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")