``FUNDAMENTOS DE PROGRAMAÇÃO - CICLO AVALIATIVO 02``

# DESCRIÇÃO DO PROJETO

Este projeto consiste no desenvolvimento de um sistema em Python para o gerenciamento de pacientes de uma clínica médica, aplicando os conceitos fundamentais da Programação Orientada a Objetos (POO). O sistema foi modelado utilizando os princípios de herança, encapsulamento e polimorfismo, permitindo representar diferentes tipos de pacientes que compartilham características em comum, mas possuem comportamentos específicos.

A estrutura do projeto é composta por:

Paciente: superclasse responsável por reunir os atributos e métodos comuns a todos os pacientes da clínica.
PacienteParticular: subclasse que herda de Paciente e representa pacientes que pagam diretamente pelo atendimento.
PacienteConvenio: subclasse que herda de Paciente e representa pacientes atendidos via plano de saúde.

# EXPLICAÇÃO DAS CLASSES, DOS ATRIBUTOS E DOS MÉTODOS

1. Classe Paciente
A classe Paciente é a superclasse do sistema e representa a estrutura básica de qualquer paciente cadastrado na clínica. Ela concentra as informações e funcionalidades comuns, servindo como base para as demais classes especializadas.

--> Atributos

A classe possui 6 atributos obrigatórios:

- nome (string): nome completo do paciente.
- data_nascimento (string): data de nascimento no formato DD/MM/AAAA.
- cpf (string): CPF do paciente.
- telefone (string): número de contato.
- tipo_sanguineo (string): tipo sanguíneo do paciente.
- numero_prontuario (string): identificador único do paciente na clínica.

Desses atributos, cpf e telefone são privados e, portanto, possuem encapsulamento.

--> Métodos

- registrar_atendimento(tipo: str, custo: flat)
Exibe a informação de que o paciente passou por um atendimento do tipo informado, com custo de tanto.
- exibir_informacoes(detalhado: bool)
Exibe as informações do paciente de acordo com o nível de detalhamento informado.
Se detalhado for False, apenas nome, tipo_sanguineo e numero_prontuario são exibidos. Se detalhado for True, todos os 6 atributos são exibidos.

2. Classe PacienteParticular

A classe PacienteParticular é uma subclasse que herda da classe Paciente e representa os pacientes que realizam o pagamento diretamente pelo atendimento. Além de reutilizar todos os atributos e métodos da sua superclasse, ela adiciona informações e comportamentos específicos relacionados à forma de pagamento e ao desconto por fidelidade.

--> Atributos adicionais

Além dos atributos herdados da superclasse, a classe possui os 2 atributos adicionais:

- forma_pagamento (string): forma de pagamento utilizada pelo paciente
- desconto_fidelidade (float): desconto concedido ao paciente por fidelidade

Considere que o desconto deve ser escrito na forma decimal. Por exemplo, 50% deve ser escrito como 0.5.

--> Métodos

- calcular_valor_final(valor_consulta: float, taxa_urgencia: float)
Calcula o valor final da consulta considerando possíveis cobranças adicionais e descontos.
Se o atendimento não é de urgência, taxa_urgência é 0.0 e o valor final é o resultado da aplicação de desconto_fidelidade sobre valor_consulta.
Se o atendimento é de urgência, taxa_urgência é diferente de 0.0, valor_consulta é alterado para ser a soma de valor_consulta recebido com taxa_urgencia (valor_consulta += taxa_urgencia) e o valor final é o resultado da aplicação de desconto_fidelidade sobre o novo valor_consulta (valor_final = valor_consulta * (1-self.desconto_fidelidade)).
- exibir_informacoes(detalhado: bool)
Sobrescreve o método exibir_informacoes(detalhado) da superclasse.
Chama super().exibir_informacoes(detalhado) para exibir as informações herdadas e, em seguida, acrescenta os atributos específicos da classe: forma_pagamento e desconto_fidelidade.

3. Classe PacienteConvenio

A classe PacienteConvenio é uma subclasse que herda da classe Paciente e representa os pacientes atendidos por meio de um plano de saúde. Além de reutilizar todos os atributos e métodos da sua superclasse, ela adiciona informações e comportamentos específicos relacionados ao convênio médico do paciente.

--> Atributos adicionais

Além dos atributos herdados da superclasse, a classe possui os 2 atributos adicionais:

- nome_convenio (string): nome do plano de saúde do paciente.
- numero_carteirinha (string): número da carteirinha do convênio.

--> Métodos

- registrar_autorizacao(procedimento: str, valor_glosa=0)
Exibe o procedimento autorizado pelo convênio e o valor da glosa.
Caso não exista glosa, o valor passado e exibido é 0.
- exibir_informacoes(detalhado: bool)
Sobrescreve o método exibir_informacoes(detalhado) da superclasse.
Chama super().exibir_informacoes(detalhado) para exibir as informações herdadas e, em seguida, acrescenta os atributos específicos da classe: nome_convenio e numero_carteirinha.

# EXEMPLOS DE EXECUÇÃO

1. Paciente Particular

paciente1 = PacienteParticular("Ana Borges Carvalho", "23/05/1989", "123.456.789-01", "994830574", "O+", "4597", "Pix", 0.25)

print(paciente1.exibir_informacoes(False))
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: Ana Borges Carvalho
Tipo sanguíneo: O+
Número do prontuário: 4597

------------------------
INFORMAÇÕES DO PAGAMENTO
------------------------
Forma de pagamento: Pix
Desconto por fidelidade: 25%

print(paciente1.exibir_informacoes(True))
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: Ana Borges Carvalho
Data de nascimento: 23/05/1989
CPF: 123.456.789-01
Telefone: 994830574
Tipo sanguíneo: O+
Número do prontuário: 4597

------------------------
INFORMAÇÕES DO PAGAMENTO
------------------------
Forma de pagamento: Pix
Desconto por fidelidade: 25%

print(paciente1.registrar_atendimento("Cirurgia Bariátirca", 5000))
O paciente passou por um atendimento...
Tipo: Cirurgia Bariátirca
Custo: R$5000.00

print(paciente1.calcular_valor_final(300, 50))
262.5

print(paciente1.calcular_valor_final(200, 0)) 
150.0

2. Paciente com Convênio

paciente2 = PacienteConvenio("Débora Eduarda Fontes Guerra", "04/12/2003", "485.309.216-73", "990682251", "AB-", "4261", "Unimed", "1245780")

print(paciente2.exibir_informacoes(False))
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: Débora Eduarda Fontes Guerra
Tipo sanguíneo: AB-
Número do prontuário: 4261

-----------------------
INFORMAÇÕES DO CONVÊNIO
-----------------------
Nome do convênio: Unimed
Número da carteirinha: 1245780

print(paciente2.exibir_informacoes(True))
-----------------------
INFORMAÇÕES DO PACIENTE
-----------------------
Nome: Débora Eduarda Fontes Guerra
Data de nascimento: 04/12/2003
CPF: 485.309.216-73
Telefone: 990682251
Tipo sanguíneo: AB-
Número do prontuário: 4261

-----------------------
INFORMAÇÕES DO CONVÊNIO
-----------------------
Nome do convênio: Unimed
Número da carteirinha: 1245780

print(paciente2.registrar_atendimento("Tratamento de unha encravada", 100))
O paciente passou por um atendimento...
Tipo: Tratamento de unha encravada
Custo: R$100.00

print(paciente2.registrar_autorizacao("Cirurgia cardiovascular", 200))
Procedimento autorizado: Cirurgia cardiovascular
Valor da glosa: R$200.00

print(paciente2.registrar_autorizacao("Redução de ombro"))
Procedimento autorizado: Redução de ombro
Valor da glosa: R$0.00

# NOME
Barbara Varela Bonfim




















