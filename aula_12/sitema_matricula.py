print("Bem-vindo ao Sistema de Matrícula em Curso")

idade = int(input("Informe a sua idade: "))
nota_prova = float(input("Informa a nota da sua prova: "))
frequencia_escolar = float(input("Informe a sua frequência escolar (em %): "))

if idade < 18:
    print(f"O aluno tem {idade} anos, tirou {nota_prova} na prova e possui uma frequência escolar de {frequencia_escolar}%.")
    print("Aluno menor de idade - Matrícula negada automaticamente!")
elif nota_prova >= 9:
    print(f"O aluno tem {idade} anos, tirou {nota_prova} na prova e possui uma frequência escolar de {frequencia_escolar}%.")
    print("Nota da prova maior ou igual a 9 - Matrícula aprovada automaticamente!")
elif idade >= 18 and nota_prova >= 6 and frequencia_escolar >= 75:
    print(f"O aluno tem {idade} anos, tirou {nota_prova} na prova e possui uma frequência escolar de {frequencia_escolar}%.")
    print("Todos os requisitos básicos foram atendidos - Matrícula aprovada!")
else:
    print(f"O aluno tem {idade} anos, tirou {nota_prova} na prova e possui uma frequência escolar de {frequencia_escolar}%.")
    print("Um ou mais requisitos básicos não foram atendidos - Matrícula negada!")