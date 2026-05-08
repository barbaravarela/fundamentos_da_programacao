# Controle de Acesso por Senha

senha_correta = "ads2025"

for i in range(3):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso concedido.")
        break
    else:
        if i == 0:
            print("Senha incorreta. 2 tentativas restantes.")
        elif i == 1:
            print("Senha incorreta. 1 tentativa restante.")
        else:
            print("Senha incorreta. Você atingiu o limite máximo de 3 tentativas. Acesso bloqueado.")