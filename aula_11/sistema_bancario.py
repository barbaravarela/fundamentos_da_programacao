print("Bem-vindo ao sistema de empréstimo bancário!")

idade = int(input("Informe a sua idade: "))
salario = int(input("Informe o seu salário: "))
tempo_trabalho = int(input("Informe o seu tempo de trabalho (em anos): "))

if idade < 18:
    print("Empréstimo negado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - a idade é menor que 18 anos, portanto o empréstimo é negado automaticamente.")
elif salario >= 5000:
    print("Empréstimo aprovado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - o salário é maior ou igual a R$ 5000, portanto o empréstimo é aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    print("Empréstimo aprovado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - todas as informações básicas foram atendidas, portanto o empréstimo é aprovado.")
else:
    print("Empréstimo negado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - uma ou mais informações básicas não foram atendidas, portanto o empréstimo é negado.")