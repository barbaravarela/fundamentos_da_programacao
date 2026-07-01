from paciente import Paciente

class PacienteParticular(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, forma_pagamento: str, desconto_fidelidade: float):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def calcular_valor_final(self, valor_consulta: float, taxa_urgencia: float):
        if taxa_urgencia != 0.0:
            valor_consulta += taxa_urgencia
        valor_final = valor_consulta * (1-self.desconto_fidelidade)
        return valor_final

    def exibir_informacoes(self, detalhado: bool):
        info_paciente = super().exibir_informacoes(detalhado)
        return f'''{info_paciente}
------------------------
INFORMAÇÕES DO PAGAMENTO
------------------------
Forma de pagamento: {self.forma_pagamento}
Desconto por fidelidade: {(self.desconto_fidelidade)*100:.0f}%
'''