# 🧮 Calculadora em Python

## Descrição do projeto

Este projeto consiste em uma calculadora básica desenvolvida em Python,
com execução via terminal e integração com Shell Script.

O projeto foi desenvolvido como atividade prática do módulo de Linux,
durante o curso de Analista de Dados da EBAC.

## Objetivos

- Praticar lógica de programação em Python.
- Aprender a executar scripts pelo terminal Linux.
- Utilizar Shell Script para execução de programas.
- Praticar versionamento de código com Git e GitHub.
- Desenvolver documentação técnica utilizando Markdown.

## Tecnologias utilizadas

- Python 3
- Linux
- Shell Script
- Jupyter Notebook
- Git
- GitHub
- Markdown

## Estrutura do projeto

```text
├── .gitattributes
├── calculadora.py
├── calculadoralogicaprogram.ipynb
├── executarcalculadora.sh
└── README.md
```

| Arquivo | Descrição |
|---|---|
| `calculadora.py` | Código-fonte da calculadora. |
| `calculadoralogicaprogram.ipynb` | Notebook de estudo da lógica de programação. |
| `executarcalculadora.sh` | Script Shell para execução da calculadora. |
| `.gitattributes` | Configuração dos atributos dos arquivos no Git. |
| `README.md` | Documentação do projeto. |

## Funcionalidades

A calculadora permite realizar quatro operações matemáticas:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)

O programa também informa quando o usuário digita uma operação inválida.

## Como executar o arquivo .sh

### Pré-requisitos

- Python 3 instalado.
- Linux ou ambiente compatível com Shell Script.

### Passo 1 — Acessar o diretório

Abra o terminal e acesse a pasta onde estão os arquivos do projeto.

### Passo 2 — Conceder permissão de execução

Execute o seguinte comando:

```bash
chmod +x executarcalculadora.sh
```

O comando `chmod +x` adiciona a permissão de execução ao arquivo.

### Passo 3 — Executar o Shell Script

```bash
./executarcalculadora.sh
```

O Shell Script inicia o programa da calculadora em Python.

### Execução alternativa

Também é possível executar o código Python diretamente:

```bash
python3 calculadora.py
```

## Explicação do código Python

### 1. Interpretador Python

```python
#!/usr/bin/env python3
```

Essa linha é conhecida como shebang e indica que o script deve
ser executado utilizando o interpretador Python 3 quando chamado
diretamente em um sistema compatível.

### 2. Inicialização do programa

```python
print("Iniciando Calculadora")
```

A função `print()` exibe uma mensagem no terminal,
informando que a calculadora foi iniciada.

### 3. Entrada de dados

```python
num1 = input('digite o primeiro número: ')
num2 = input('digite o segundo número: ')
```

A função `input()` permite que o usuário informe dois valores.

Os valores recebidos são armazenados nas variáveis `num1` e `num2`
inicialmente como strings (texto).

### 4. Conversão dos valores

```python
convert_valor1 = int(num1)
convert_valor2 = int(num2)
```

A função `int()` converte os valores recebidos em números inteiros,
permitindo a realização das operações matemáticas.

### 5. Escolha da operação matemática

```python
op = input('digite a operação (+, -, *, /): ')
```

O usuário informa qual operação deseja realizar.

A operação escolhida é armazenada na variável `op`.

### 6. Estruturas condicionais

```python
if op == '+':
    print('O valor da soma é de:', convert_valor1 + convert_valor2)
elif op == '-':
    print('O valor da subtração é de:', convert_valor1 - convert_valor2)
elif op == '*':
    print('O valor da multiplicação é de:', convert_valor1 * convert_valor2)
elif op == '/':
    print('O valor da divisão é de:', convert_valor1 / convert_valor2)
else:
    print('Operação inválida')
```

As estruturas condicionais `if`, `elif` e `else` são utilizadas
para verificar qual operação foi escolhida pelo usuário.

- `if`: verifica a primeira condição.
- `elif`: verifica condições alternativas.
- `else`: é executado quando nenhuma das condições anteriores é verdadeira.
- `==`: operador de comparação utilizado para verificar a igualdade.

Após identificar a operação, o programa realiza o cálculo
e apresenta o resultado utilizando a função `print()`.

Caso nenhuma operação válida seja informada, o programa
exibe a mensagem "Operação inválida".

## Exemplo de execução

```text
Iniciando Calculadora

digite o primeiro número: 10
digite o segundo número: 5
digite a operação (+, -, *, /): +

O valor da soma é de: 15
```

## Limitações atuais

- Aceita apenas números inteiros como entrada.
- Não possui tratamento de divisão por zero.
- Não possui tratamento de entradas não numéricas.
- Realiza uma operação por execução.


## Autor

Pedro

Projeto desenvolvido para fins educacionais durante o curso
de Analista de Dados da EBAC.
