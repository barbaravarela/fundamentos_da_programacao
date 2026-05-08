# Calcularadora de Tarifas de Energia Elétrica

while True:
    consumo_mensal = int(input("Informe o seu consumo mensal em kWh: "))
    if consumo_mensal < 0:
        print("Valor inválido! O consumo mensal deve ser um valor posiivo.")
    else:
        break

if consumo_mensal <= 100:
    valor = 0.4*consumo_mensal
    tarifa = "Até 100 kWh"
elif consumo_mensal <= 200:
    valor_ate_100 = 40
    consumo_restante = consumo_mensal - 100
    valor = valor_ate_100 + 0.6*consumo_restante
    tarifa = "De 101 a 200 kWh"
else:
    valor_ate_100 = 40
    valor_ate_200 = 60
    consumo_restante = consumo_mensal - 200
    valor = valor_ate_100 + valor_ate_200 + 0.9*consumo_restante
    tarifa = "Acima de 200 kWh"

print(f"Consumo: {consumo_mensal} kWh")
print(f"Faixa de tarifa aplicada: {tarifa}")
print(f"Valor total a pagar: R$ {valor:.2f}")