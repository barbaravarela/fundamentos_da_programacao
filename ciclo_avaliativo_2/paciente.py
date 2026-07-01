class Paciente:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    def registrar_atendimento(self, tipo: str, custo: float):
        return f'''
O paciente passou por um atendimento...
Tipo: {tipo}
Custo: R${custo:.2f}'''

    def exibir_informacoes(self, detalhado: bool):
        if detalhado:
            return f'''
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: {self.nome}
Data de nascimento: {self.data_nascimento}
CPF: {self._cpf}
Telefone: {self._telefone}
Tipo sanguíneo: {self.tipo_sanguineo}
Número do prontuário: {self.numero_prontuario}
'''
        else:
            return f'''
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: {self.nome}
Tipo sanguíneo: {self.tipo_sanguineo}
Número do prontuário: {self.numero_prontuario}
'''