# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string
2. number int
3. number float
4. boolean

## Operadores matemátcos - básicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

## Operadores lógicos
and -> e -> Se duas condições forem verdadeiras, o resultadto é verdadeiro.
or -> ou -> Se pelo menos uma condição for verdadeira, o resultado é verdadeiro.
not -> Ele altera o valor booleano da condição.

## Métodos em python
1. print() -> Exibe informações no terminal
2. input() -> Captura uma informação do terminal.
3. lower() -> converte toda a string em minúscula
4. upper() -> converte toda a string em maiúscula
5. isdigit() -> verifica se a variável contém número

## Format em python
f"{variavel}" -> Insere variáveis dentro de uma string

## Estrutura condicional
``if (se)`` -> Verifica se uma condição é true (verdadeira). Se for, ele executa o código
``elif (senão se)`` -> Usado para testar várias condições. Ele só executa se todas as condições anteriores forem false (falsas)
``else (senão)`` -> Executa o código se a condição if for false (falsa)

## Laços de repetição

É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop ou Laços de iteração

``FOR`` -> uilizamos quando sabemos quantas vezes queremos repetir algo.
Sintaxe padrão:
for variavel in range(inicio,fim):
    comandos
[range()] -> Método que aceita geração de números.
[inicio] -> É inclusivo. É o primeiro número a ser usado.
[fim] -> É exclusivo. O número utilizado é o anterior a esse.

### Escopo das Variáveis
``Escopo Local`` -> A variável só é acessada dentro da estrutura na qual ele foi criada.
``Escopo Global`` -> A variável pode ser acessada por todo mundo.

### Variações das Variáveis
Variável em memória -> É declarada quando você não pretende utilizar essa variável em outros cenários.
Variável contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

``WHILE`` -> É usado quando não sabemos quantas vezes o progrma vai repetir. Ele repete enquanto um condição for verdadeira.
Sintaxe padrão:
while condicao:
    comandos

## Conversão de tipos em python
1. int() -> A gente vai incluir qual variável/dado que queremos converter para número inteiro.
2. float() -> A gente vai incluir qual variável/dado que queremos converter para número decimal.
3. str() -> A gente vai incluir qual variável/dado que queremos converter para texto.

## Boas Práticas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o camemlCase
2. Se vocÊ observar alguma estrutura tipo nome(), 90% de chance de ser uma função
3. Python não tem constante, porém utilizamos o padrão case UPPERCASE para simular que aquela variável não pode ser alterada

## Funções em Python
``def`` -> Define que uma função será declarada
``propriedade`` -> Variável em memória que irá receber um argumento
``argumento`` -> Valor que irá preencher o espaço da propriedade

## Estruturas de Dados
``list ou lista`` -> Armazena valores avulsos e pode ser heterogênea ou homogênea. Ou seja, pode guardar valores de um mesmo tipo ou de diferentes tipos.
Ex: list = [] // Lista vazia
list = ["William", 25, 1.82]
``dict ou dicionário`` -> Armazena conjuntos de valores (chave: valor). As chaves e valores podem ser heterogêneos ou homogêneos.
1. Para obter o valor de um conjunto em dict, você acessa pela chave.
Ex: dados_usuario = {} // Dicionário vazio
dados_usuario = {"nome": William, "cpf": 111456985-98, "idade": 25}
dados_usuario["nome"] => Devolve o valor, que é "William".

## POO
1. Em python, todo molde é declarado através de uma class => [class]
2. Qualquer característica dentro de uma classe é chamada de [atributo] e são declaradas como variáveis
3. As ações dentro de uma classe são chamadas de [métodos] e são declaradas como funções

4. [self] -> significa ele mesmo, o atributo da classe atual
5. [constructor] -> é a estrutura de como a classe será "copiada"

## Cases em Python
snake_case -> nome_aluno -> nome de variáveis, métodos (funções) e arquivos
cammelCase -> nomeAluno -> nome de variáveis e métodos (funções) -> ``mais atual``
PascalCase -> NomeAluno -> classes
kebab-case -> nome-aluno -> não utilizamos em python