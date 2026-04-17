# Explicação da Refatoração (`refatorar.py`)

O código original cumpria o objetivo de calcular e retornar quatro métricas estatísticas (total, média, maior e menor) de uma lista. No entanto, ele possuía graves problemas de legibilidade, nomenclatura e ineficiência. Abaixo detalhamos as técnicas de *Clean Code* (Código Limpo) e as convenções da linguagem Python (PEP 8) que aplicamos para chegar à versão refatorada.

---

## 1. Nomenclatura Significativa (Semântica)

**Antes:**
```python
def c(l):
    t=0 ... m=t/len(l) ... mx=l[0] ... mn=l[0]
```
Letras soltas tornam o código um mistério para quem lê. Sem executar, é impossível saber de relance o que `c` ou `mx` significam.

**Depois:**
```python
def calcular_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    total = 0 ... maior_valor = numeros[0] ... menor_valor = numeros[0]
```
* Trocamos `c` por `calcular_estatisticas` (verbo + substantivo indicando a ação).
* Variáveis como `t` e `mx` viraram `total` e `maior_valor`, deixando a intenção óbvia.

---

## 2. Type Hints (Tipagem) e Documentação

**Antes:** Nenhuma indicação do tipo de dado esperado ou do que a função faz.
**Depois:** 
Adicionamos `(numeros: list[float]) -> tuple[...]` para o editor saber exatamente o que entra e o que sai. Também adicionamos uma **Docstring** (texto entre `"""`) logo abaixo do nome da função, o que documenta o método para a equipe e para ferramentas automáticas.

---

## 3. O Fim do "Anti-Pattern" de Laços (`for`)

**Antes:**
```python
for i in range(len(l)):
    t=t+l[i]
```
Esse é o jeito de programar em *C* ou *Java* antigo. Iterar pegando o tamanho da lista para depois extrair o valor pelo índice `l[i]` é considerado um *anti-pattern* (má prática) no Python moderno.

**Depois:**
```python
for numero in numeros:
    total += numero
```
Iteramos de forma pythônica e direta. A leitura fica parecida com o idioma humano: *"Para cada número nos números, o total recebe esse número"*. O operador `+=` substitui o redundante `t = t + l[i]`.

---

## 4. Otimização de Processamento (Consolidação de Laços)

**Antes:**
O código percorria a lista inteira do começo ao fim **duas vezes**! A primeira vez num `for` para calcular a soma e a segunda num outro `for` para achar os maiores e menores.

**Depois:**
Unificamos tudo em um **único laço de repetição**. Enquanto passamos pelo item para somar no total, já verificamos simultaneamente se ele é o maior ou o menor. Isso reduz o tempo de processamento pela metade (complexidade O(n) estrita).

---

## 5. Prevenção de Falhas (Exceções e Tratamento de Erros)

**Antes:**
Se a lista fornecida estivesse vazia (`x = []`), a linha `m=t/len(l)` tentaria dividir o total por zero, causando um estrondo fatal no programa (`ZeroDivisionError`). A linha `mx=l[0]` também falharia por tentar acessar uma posição inexistente.

**Depois:**
```python
if not numeros:
    raise ValueError("A lista de números não pode estar vazia.")
```
Adicionamos uma **Guard Clause** (Cláusula de Guarda). Se a lista estiver vazia, estouramos um erro amigável e controlado logo no começo da função, impedindo comportamentos caóticos.

---

## 6. F-Strings e Boas Práticas Estruturais

**Antes:**
```python
print("total:",a)
```
Variáveis globais penduradas no final do script (`x=[...]`) e concatenação de impressão básica com vírgulas.

**Depois:**
```python
if __name__ == "__main__":
    valores_teste = [...]
    soma, media, maior, menor = calcular_estatisticas(valores_teste)
    print(f"Média: {media:.2f}")
```
* **Escopo Protegido:** Colocamos a execução do teste dentro do bloco `if __name__ == "__main__":`. Isso significa que se outro programador usar `import refatorar`, ele aproveitará sua função sem disparar `prints` indevidos no terminal.
* **F-Strings:** Substituímos a vírgula pelo moderno `f"..."`, que permite injetar a variável direto no texto e arredondar as casas decimais usando o modificador matemático `:.2f` (duas casas decimais).
