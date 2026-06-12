# EXERCÍCIO 1

def calcular_imc(peso_kg, altura_m):
    if peso_kg <= 0 or altura_m <= 0:
        return -1.0
    return round(peso_kg/(altura_m**2), 1)

# imc = calcular_imc(70, 1.75)
# print(f"IMC: {imc}")

# imc2 = calcular_imc(95, 1.70)
# print(f"IMC: {imc2}")

# invalido = calcular_imc(-5, 1.70)
# print(f"IMC: {invalido}")

# EXERCÍCIO 2

def classificar_imc(imc, verificar_risco=True):
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal ✅"
    elif imc <= 29.9:
        classificacao = "Sobrepeso ⚠️"
    else:
        classificacao = "Obesidade ❌"
    alerta = "Risco cardiovascular elevado 🚨" if (verificar_risco and imc >= 30.0) else ""
    return classificacao, alerta

# classif, alerta = classificar_imc(22.9)
# print(f"{classif} {alerta}")

# classif2, alerta2 = classificar_imc(32.9)
# print(f"{classif2} {alerta2}")

# classif3, alerta3 = classificar_imc(27.3, verificar_risco=False)
# print(f"{classif3} {alerta3}")

# EXERCÍCIO 3

def emitir_ficha(nome, idade, peso, altura):
    imc = calcular_imc(peso, altura)
    classificacao, alerta = classificar_imc(imc)
    print(f'''
====================================
   🏥 CLÍNICA VIDA+ — TRIAGEM
====================================
Paciente : {nome}
Idade    : {idade} anos
Peso/Alt : {peso} kg / {altura} m
------------------------------------
IMC      : {imc}
Classificação: {classificacao}  {alerta}
====================================
''')
    
# emitir_ficha("Maria Souza", 34, 70, 1.75)

# emitir_ficha("João Pedro", 45, 95, 1.70)

# EXERCÍCIO 4

def calcular_imc_medio(lista_imcs):
    if lista_imcs == []:
        return 0.0
    return round(sum(lista_imcs)/len(lista_imcs), 1)

def contar_classificacoes(lista_imcs):
    abaixo = normal = sobrepeso = obesidade = 0
    for imc in lista_imcs:
        classificacao, _ = classificar_imc(imc)
        if classificacao == "Abaixo do peso":
            abaixo += 1
        elif classificacao == "Peso normal ✅":
            normal += 1
        elif classificacao == "Sobrepeso ⚠️":
            sobrepeso += 1
        else:
            obesidade += 1
    return abaixo, normal, sobrepeso, obesidade

def relatorio_diario_clinica(nome_unidade, lista_imcs):
    imc_medio = calcular_imc_medio(lista_imcs)
    abaixo, normal, sobrepeso, obesidade = contar_classificacoes(lista_imcs)
    print(f'''
╔══════════════════════════════════╗
║  📊 RELATÓRIO — TURNO: {nome_unidade.upper()}     ║
╠══════════════════════════════════╣
''', end="")
    if lista_imcs == []:
        print("   Nenhum paciente triado ainda.")
    else:
        print(f"   Pacientes triados : {len(lista_imcs)}")
        print(f"   IMC médio         : {imc_medio}")
        print("   ───────────────────────────────")
        print(f"   Abaixo do peso    : {abaixo}")
        print(f"   Peso normal       : {normal}")
        print(f"   Sobrepeso         : {sobrepeso}")
        print(f"   Obesidade         : {obesidade}")
    print("╚══════════════════════════════════╝")

    
# imcs_manha = [22.9, 32.9, 19.5, 27.3, 24.0, 35.1, 21.0]
# relatorio_diario_clinica("Manhã", imcs_manha)

# relatorio_diario_clinica("Tarde", [])

# EXERCÍCIO 5

def verificar_pressao(sistolica, diastolica):
    if sistolica >= 180 or diastolica >= 120:
        return "Crise Hipertensiva 🚨"
    elif sistolica >= 140 or diastolica >= 90:
        return "Hipertensão ⚠️"
    elif sistolica >= 130 or diastolica >= 80:
        return "Pressão Elevada"
    else:
        return "Normal ✅"
    
def definir_prioridade(classif_imc, classif_pressao):
    if classif_pressao == "Crise Hipertensiva 🚨":
        return "URGENTE 🚨"
    elif classif_imc == "Obesidade ❌" or classif_pressao == "Hipertensão ⚠️":
        return "Prioritário ⚠️"
    else:
        return "Normal"
    
def emitir_ficha_completa(nome, idade, peso, altura, sistolica, diastolica):
    imc = calcular_imc(peso, altura)
    classif_imc, alerta = classificar_imc(imc)
    classif_pressao = verificar_pressao(sistolica, diastolica)
    prioridade = definir_prioridade(classif_imc, classif_pressao)
    print(f'''
====================================
  🏥 CLÍNICA VIDA+ — FICHA COMPLETA
====================================
Paciente   : {nome}
Idade      : {idade} anos
IMC        : {imc} — {classif_imc}
''', end="")
    if alerta:
        print(f"Alerta IMC : {alerta}")
    print(f"Pressão    : {sistolica}/{diastolica} mmHg — {classif_pressao}")
    print("------------------------------------")
    print(f"PRIORIDADE : {prioridade}")
    print("====================================")

# emitir_ficha_completa("Carlos Andrade", 58, 95, 1.70, 185, 110)

# emitir_ficha_completa("Beatriz Lima", 29, 60, 1.65, 118, 76)