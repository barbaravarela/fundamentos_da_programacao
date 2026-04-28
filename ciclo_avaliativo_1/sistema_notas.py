print("\n----------------------------------------------------------------")
print("--- Bem-vindo ao Sistema de Gerenciamento de Notas de Alunos ---")
print("----------------------------------------------------------------")

# Lista principal para guardar os dados da turma, inicialmente vazia
turma = []

# Perguntando ao usuário quantos alunos serão cadastrados
qtd_alunos = int(input("\nInforme a quantidade de alunos que serão cadastrados: "))

# Laço de repetição para solicitar os dados de cada aluno
for i in range(qtd_alunos):

    # Obtendo os dados do aluno
    nome = input("\nNome do aluno: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))

    # Calculando a média das notas do aluno
    media = (nota1 + nota2 + nota3) / 3

    # Estrutura condicional que determina a situação do aluno
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    # Armazenando os dados do aluno em uma lista ...
    dados_aluno = [nome, nota1, nota2, nota3, media, situacao]
    # ... e adicionando essa lista na lista principal da turma
    turma.append(dados_aluno)

print("\n-----------------------")
print("--- RESUMO DA TURMA ---")
print("-----------------------")

# Exibindo os dados de cada aluno da turma
for aluno in turma:
    print(f"\nNome: {aluno[0]}")
    print(f"Primeira nota: {aluno[1]}")
    print(f"Segunda nota: {aluno[2]}")
    print(f"Terceira nota: {aluno[3]}")
    print(f"Média: {aluno[4]:.2f}")
    print(f"Situação: {aluno[5]}")