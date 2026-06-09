# EXERCÍCIO 1

def calcular_media(nota1, nota2, nota3):
    for nota in [nota1, nota2, nota3]:
        if nota < 0 or nota > 10:
            return -1.0 # Entrada inválida
    media = (nota1*2 + nota2*3 + nota3*5)/10
    return round(media, 1)

# media = calcular_media(7.0, 8.0, 9.0)
# print(f"Média: {media}")

# media2 = calcular_media(5.0, 6.0, 4.0)
# print(f"Média: {media2}")

# invalida = calcular_media(5.0, 11.0, 8.0)
# print(f"Média: {invalida}")

# EXERCÍCIO 2

def verificar_situacao(media, verificar_honra=True):  
    if media >= 7.0:
        situacao = "Aprovado ✅"
    elif media >= 5:
        situacao = "Recuperação ⚠️"
    else:
        situacao = "Reprovado ❌"
    mensagem_honra = "Menção Honrosa 🏅" if (verificar_honra and media > 9.0) else ""
    return situacao, mensagem_honra

# sit, honra = verificar_situacao(9.2)
# print(f"{sit} {honra}")

# sit2, honra2 = verificar_situacao(6.1)
# print(f"{sit2} {honra2}")

# sit3, honra3 = verificar_situacao(3.8, verificar_honra=False)
# print(f"{sit3} {honra3}")

# EXERCÍCIO 3

def emitir_boletim(nome, turma, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    situacao, mensagem_honra = verificar_situacao(media)
    print(f'''
====================================
     🏫 COLÉGIO BYTE — BOLETIM
===================================
Aluno   : {nome}
Turma   : {turma}
1° Bim  : {nota1}   2° Bim: {nota2}   3° Bim: {nota3}
------------------------------------
Média   : {media}
Situação: {situacao}  {mensagem_honra}
''')
    
# emitir_boletim("Ana Lima", "3ºA", 9.0, 9.5, 9.8)

# emitir_boletim("Bruno Ramos", "3ºA", 5.0, 6.0, 5.5)
    
# EXERCÍCIO 4

def calcular_media_turma(medias):
    if medias == []:
        return 0.0
    media_turma = sum(medias)/len(medias)
    return round(media_turma, 1)

def contar_situacoes(medias):
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    for media_aluno in medias:
        situacao, _ = verificar_situacao(media_aluno)
        if situacao == "Aprovado ✅":
            aprovados += 1
        elif situacao == "Recuperação ⚠️":
            recuperacao += 1
        else:
            reprovados += 1
    return aprovados, recuperacao, reprovados

def relatorio_turma(nome_turma, medias):
    media_turma = calcular_media_turma(medias)
    aprovados, recuperacao, reprovados = contar_situacoes(medias)
    if medias == []:
        print(f'''
╔══════════════════════════════════╗
║   📊 RELATÓRIO DA TURMA — {nome_turma}    ║
╠══════════════════════════════════╣
  Nenhum aluno avaliado ainda.
╚══════════════════════════════════╝
''')
    else:
        print(f'''
╔══════════════════════════════════╗
║   📊 RELATÓRIO DA TURMA — {nome_turma}    ║
╠══════════════════════════════════╣
  Alunos avaliados : {len(medias)}
  Média da turma   : {media_turma}
  Maior média      : {max(medias)}
  Menor média      : {min(medias)}
─────────────────────────────── 
  Aprovados        : {aprovados}
  Recuperação      : {recuperacao}
  Reprovados       : {reprovados}
╚══════════════════════════════════╝
''')
        
# medias_3a = [9.7, 7.2, 5.7, 8.1, 4.3, 6.5, 9.1, 3.8]
# relatorio_turma("3ºA", medias_3a)

# relatorio_turma("3ºB", [])
        
# EXERCÍCIO 5

def calcular_media_final(media_anterior, nota_final):
    nova_media = (media_anterior + nota_final)/2
    return round(nova_media, 1)

def precisa_recuperacao(media):
    if 5.0 <= media < 7.0:
        return True
    else:
        return False

def verificar_nova_situacao(media):
    if media >= 5.0:
        situacao = "Aprovado ✅"
    else:
        situacao = "Reprovado ❌"
    return situacao
    
def emitir_boletim_final(nome, turma, nota1, nota2, nota3, nota_final=None):
    media = calcular_media(nota1, nota2, nota3)
    situacao, mensagem_honra = verificar_situacao(media)
    recuperacao = precisa_recuperacao(media)
    print(f'''
====================================
   🏫 COLÉGIO BYTE — BOLETIM FINAL
====================================
Aluno   : {nome}
Turma   : {turma}
1º Bim  : {nota1}   2º Bim: {nota2}   3º Bim: {nota3}
''', end="")
    
    if recuperacao:
        nova_media = calcular_media_final(media, nota_final)
        nova_situacao = verificar_nova_situacao(nova_media)
        print(f"Média   : {media}   → Recuperação ⚠️")
        print("------------------------------------")
        print(f"Prova Final    : {nota_final}")
        print(f"Média Final    : {nova_media}")
        print(f"Situação Final : {nova_situacao}")
        print("====================================")
    else:
        print(f"Média   : {media}")
        print("------------------------------------")
        print(f"Situação Final : {situacao}  {mensagem_honra}")
        print("====================================")
    
# emitir_boletim_final("Bruno Ramos", "3ºA", 5.0, 6.0, 5.5, 7.0)

# emitir_boletim_final("Ana Lima", "3ºA", 9.0, 9.5, 9.8)