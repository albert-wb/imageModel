# Análise de Erros no Arquivo `debug.py`

Ao analisar o código fornecido, foram identificados os seguintes erros que impediam a execução correta do programa.

## 1. Erro de Sintaxe: Falta de Aspas na Função `input()`
* **Linha:** 6
* **Código Original:** `item1 = float(input(Preço do item 1? ))`
* **Causa:** O texto passado como argumento para a função `input()` deve ser uma string. No código original, faltavam as aspas ao redor do texto, o que causa um `SyntaxError` (erro de sintaxe).
* **Correção:** Adicionar aspas duplas (ou simples) ao redor da string:
  ```python
  item1 = float(input("Preço do item 1? "))
  ```

## 2. Erro de Tipo (TypeError): Falta de Conversão do Input
* **Linha:** 23
* **Código Original:** `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
* **Causa:** A função `input()` sempre retorna uma string (`str`). Na linha 24, essa variável é dividida por 100 (`desconto_cupom / 100`), e na linha 43 é comparada com um número (`desconto_cupom > 0`). Tentar fazer operações matemáticas com uma string em Python causa um `TypeError`.
* **Correção:** Converter o resultado do `input` para um número, usando `float()` ou `int()`. Usaremos `float` para permitir descontos de percentuais fracionados:
  ```python
  desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
  ```

## 3. Erro de Formatação de String: Falta do `f` antes da String
* **Linha:** 37
* **Código Original:** `print(" Item 2:        R$ {total_item2:.2f}")`
* **Causa:** Para interpolar variáveis (incluí-las) dentro de uma string em Python usando as chaves `{}`, é necessário usar uma f-string. Sem a letra `f` antes das aspas, o Python imprimirá a string literalmente como `{total_item2:.2f}`, sem substituir pelo valor calculado.
* **Correção:** Adicionar a letra `f` antes da string:
  ```python
  print(f" Item 2:        R$ {total_item2:.2f}")
  ```

## 4. Erro de Indentação: Bloco `if` não Indentado
* **Linhas:** 43 e 44
* **Código Original:** 
  ```python
  if desconto_cupom > 0: 
  print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
  ```
* **Causa:** Em Python, a estrutura do código é definida pela indentação. Todo bloco de código condicional (como o que é executado após um `if`) deve ser indentado (geralmente com 4 espaços ou 1 tab). A falta de indentação causa um `IndentationError`.
* **Correção:** Indentar corretamente a linha do `print` dentro do escopo do bloco `if`:
  ```python
  if desconto_cupom > 0: 
      print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
  ```

---

## Código Corrigido

Aqui está a versão completa e corrigida do seu arquivo de código:

```python
#                                      CÓDIGO CORRIGIDO                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? ")) # Corrigido: adicionadas aspas na string

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
# Corrigido: adicionado float() para converter a string de entrada para número
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}") # Corrigido: adicionado 'f' antes da string
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0: 
    # Corrigido: adicionada indentação exigida pelo Python
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```
