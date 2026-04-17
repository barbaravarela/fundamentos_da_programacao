print("Bem-vindo ao Sistema de Controle de Entrada do Evento!")

while True:
    opcao = input("\nDigite validar caso deseja conferir se a sua entrada é permitida ou digite sair caso deseje sair do sistema: ")
    if opcao == "validar":
        nome = input("Informe o seu nome: ")
        idade = int(input("Informe a sua idade: "))
        convite = input("Informe de você possui convite (S/N): ")
        if idade < 16:
            print("Você tem menos de 16 anos. Entrada negada!")
        elif convite == "S":
            print("Você tem mais de 16 anos e possui convite. Entrada permitida!")
        else:
            print("Você não tem convite. Entrada negada!")
    elif opcao == "sair":
        break
    else:
        print("Você digitou uma opção inválida!")