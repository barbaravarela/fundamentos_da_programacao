from pessoa import Pessoa

# nome, cpf data de nascimento, ano de ingresso, notas, matrícula e se está ativo ou não
class Aluno(Pessoa):
    def __innit__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matricula: str):
        super().__innit__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self.ativo = True
        self.notas = []