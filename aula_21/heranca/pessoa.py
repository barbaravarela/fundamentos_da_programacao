# Precisamos criar um molde de uma pessoa => class
# características => atributos -> variáveis
# ações => métodos -> funções

class Pessoa:
    # Construtor
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self.nome = nome # atributo público
        self._cpf = cpf # atributo privado
        self.data_nascimento = data_nascimento # atributo público

    # Método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}"
    
pessoa1 = Pessoa("Ana Lima", "123")
pessoa2 = Pessoa("Bruno Costa", "987")

print(pessoa1.apresentar())
print(pessoa2.apresentar())