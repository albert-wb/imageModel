# Atividades de Programação Assistida

Este repositório contém uma série de exercícios e demonstrações de código em Python com foco na aplicação de práticas de engenharia de software e princípios de **Clean Code**. As atividades abrangem algoritmos matemáticos, refatoração de código legado e técnicas de debugging (depuração).

Este projeto parece ter sido concebido para práticas guiadas e exercícios de Engenharia de Prompt, demonstrando como transformar códigos ruins em boas implementações, além de detalhar o processo de correção.

## 🗂️ Estrutura do Projeto

O projeto é dividido em 3 frentes principais de estudo. Cada frente contém o código-fonte em Python e um arquivo Markdown respectivo com a documentação pedagógica explicando o raciocínio por trás da lógica e as melhorias aplicadas.

### 1. Algoritmos e Otimização (`num_primos.py`)
- **Descrição**: Um script interativo que solicita números ao usuário e verifica se são primos.
- **Destaque Técnico**: A função de verificação `eh_primo` implementa um algoritmo matematicamente otimizado com complexidade de tempo `O(√n)`, além de aplicar o padrão *Early Return*.
- **Documentação**: Detalhado em [`explica_num_primo.md`](explica_num_primo.md).

### 2. Refatoração e Clean Code (`refatoracao.py`)
- **Descrição**: Demonstra a transformação de um código inelegível, mal estruturado e frágil em um código robusto, performático e limpo. Ele pega uma lista de números e retorna o total, média, maior e menor valor.
- **Destaque Técnico**: Consolidação de loops (`O(2n)` para `O(n)`), Type Hinting explícito, nomes semânticos, remoção do *anti-pattern* de usar `range(len())` e implementação de tratamento de exceções (*Guard Clauses*).
- **Documentação**: Detalhado em [`explica_refatorar.md`](explica_refatorar.md).

### 3. Debugging e Correção de Bugs (`debug.py`)
- **Descrição**: Um simulador financeiro focado no cálculo de compras (cálculo de subtotal de itens, acréscimo de imposto e desconto). O código foi projetado para expor erros comuns em Python.
- **Destaque Técnico**: Contém comentários inline detalhando o raciocínio de tomada de decisão. A documentação extra aponta e corrige os problemas sintáticos (`SyntaxError`), de tipo (`TypeError`) e estruturais (`IndentationError`) originais do arquivo.
- **Documentação**: Detalhado em [`explicacao-debug.md`](explicacao-debug.md).

## 🚀 Como Executar

Para executar os scripts individualmente, certifique-se de que possui o Python instalado na sua máquina (versão 3.6 ou superior, devido ao uso extensivo de F-Strings e Type Hints recentes).

Abra um terminal na pasta deste diretório e rode qualquer um dos arquivos:

```bash
# Executa a verificação interativa de números primos
python num_primos.py

# Executa o cálculo estatístico demonstrando o código refatorado
python refatoracao.py

# Tenta executar o simulador com bugs intencionais
python debug.py
```

## 🛠️ Boas Práticas Abordadas

Este conjunto de arquivos é um material excelente para entender na prática:
* Nomenclatura semântica de funções e variáveis (PEP 8).
* Utilização correta de *Type Hints* nativos da linguagem.
* Tratamento seguro de inputs do usuário via `try/except`.
* Condições de escape (*Guard Clauses*).
* Uso de F-Strings para formatação complexa (ex: valores monetários com `:.2f`).
* A importância da documentação explícita (Docstrings no padrão Google).
