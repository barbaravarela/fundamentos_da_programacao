print("Sistema de Empréstimo Bancário")

# Entrada dos dados
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário do cliente: "))
tempo_trabalhando = int(input("Digite o tempo de trabalho (em anos): "))

# Estruturas condicionais

if idade < 18:
    print("Empréstimo negado. Cliente menor de idade.")
elif salario >= 5000:
    print("Empréstmo aprovado automaticamente.")
elif idade >=18 and salario >= 2000 and tempo_trabalhando >= 2:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")