from paciente import Paciente

class PacienteConvenio(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, nome_convenio: str, numero_carteirinha: str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    def registrar_autorizacao(self, procedimento: str, valor_glosa=0):
        return f'''
Procedimento autorizado: {procedimento}
Valor da glosa: R${valor_glosa:.2f}
'''

    def exibir_informacoes(self, detalhado: bool):
        info_paciente = super().exibir_informacoes(detalhado)
        return f'''{info_paciente}
-----------------------
INFORMAÇÕES DO CONVÊNIO
-----------------------
Nome do convênio: {self.nome_convenio}
Número da carteirinha: {self.numero_carteirinha}
'''