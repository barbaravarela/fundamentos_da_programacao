from pessoa import Pessoa

# nome, cpf data de nascimento, ano de ingresso, notas, matrícula e se está ativo ou não
class Aluno(Pessoa): # Subclass porque recebe a herança
    def __innit__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matricula: str):
        super().__innit__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self.ativo = True
        self.notas = []

    # Métodos de notas
    def adicionar_notas(self, disciplina: str, nota: float):
        # nota precisa estar entre 0 e 10
        if not(0 <= nota <= 10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)