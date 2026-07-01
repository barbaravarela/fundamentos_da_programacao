from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio

def main():
    paciente1 = PacienteParticular("Ana Borges Carvalho", "23/05/1989", "123.456.789-01", "994830574", "O+", "4597", "Pix", 0.25)
    print(paciente1.exibir_informacoes(False))
    print(paciente1.exibir_informacoes(True))
    print(paciente1.registrar_atendimento("Cirurgia Bariátirca", 5000))
    print(paciente1.calcular_valor_final(300, 50)) # com taxa de urgência
    print(paciente1.calcular_valor_final(200, 0)) # sem taxa de urgência

    paciente2 = PacienteConvenio("Débora Eduarda Fontes Guerra", "04/12/2003", "485.309.216-73", "990682251", "AB-", "4261", "Unimed", "1245780")
    print(paciente2.exibir_informacoes(False))
    print(paciente2.exibir_informacoes(True))
    print(paciente2.registrar_atendimento("Tratamento de unha encravada", 100))
    print(paciente2.registrar_autorizacao("Cirurgia cardiovascular", 200)) # com glosa
    print(paciente2.registrar_autorizacao("Redução de ombro")) # sem glosa

if __name__ == "__main__":
    main()