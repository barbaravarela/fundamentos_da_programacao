print("Bem-vindo ao sistema de empréstimo bancário!")

idade = int(input("Informe a sua idade: "))
salario = int(input("Informe o seu salário: "))
tempo_trabalho = int(input("Informe o seu tempo de trabalho (em anos): "))
emprestimo = int(input("Informe o valor do empréstimo que deseja solicitar: "))

parcela = emprestimo/36
verficar_emprestimo = False

if idade < 18:
    print("Empréstimo negado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - a idade é menor que 18 anos, portanto o empréstimo é negado automaticamente.")
elif salario >= 5000:
    verficar_emprestimo = True
elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    verficar_emprestimo = True
else:
    print("Empréstimo negado!")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho - uma ou mais informações básicas não foram atendidas, portanto o empréstimo é negado.")

if verficar_emprestimo:
    if parcela > 0.3*salario:
        print("Empréstimo negado!")
        print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho.")
        print(f"Ele deseja solicitar um empréstimo de R$ {emprestimo} que deveria ser pago ao longo de 3 anos por meio de parcelas mensais de R$ {parcela:.2f} - o valor da parcela supera 30% do salário do cliente, portanto o empréstimo é negado.")
    else:
        print("Empréstimo aprovado!")
        print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho.") 
        print(f"Ele deseja solicitar um empréstimo de R$ {emprestimo} que deverá ser pago ao longo de 3 anos por meio de parcelas mensais de R$ {parcela:.2f} - o valor da parcela não supera 30% do salário do cliente, portanto o empréstimo é aprovado.")