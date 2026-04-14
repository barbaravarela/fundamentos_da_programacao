print("Bem-vindo ao Estacionamento Inteligente")

idade = int(input("Informe a sua idade: "))
possui_cadastro = input("Informe se você possui cadastro no shopping (sim ou não): ")
tipo_veiculo = input("Informe o tipo do seu veículo (carro, moto, bicicleta, ônibus, van, caminhão): ")
cliente_vip = input("Informe se você é cliente VIP (sim ou não): ")

if idade < 20:
    print("\nMotorista jovem demais. Entrada negada automaticamente.")
elif cliente_vip == "sim":
    print("\nCliente VIP. Entrada autorizada automaticamente.")
elif tipo_veiculo in ["ônibus", "van", "caminhão"] and possui_cadastro == "sim":
    print("\nPossui cadastro, mas o veículo é muito grande. Entrada negada.")
else:
    print("\nEntrada negada.")