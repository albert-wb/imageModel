# Explicação do Código de Verificação de Números Primos (`num_primo.py`) - Refatorado com Clean Code

O algoritmo implementado é uma versão altamente otimizada de verificação de primos, rodando com complexidade de tempo **O(√n)**. Após a aplicação de princípios de **Clean Code**, o código tornou-se mais semântico, legível e modular. 

Abaixo está a explicação técnica e didática atualizada do que cada parte do código faz:

## 1. Assinatura, Nomenclatura e Documentação
```python
def eh_primo(numero: int) -> bool:
    """ ... """
```
* **Linha 1:** Define a função com o nome `eh_primo`. Em Clean Code, evitamos misturar idiomas (como o antigo `is_primo`), priorizando a consistência. O parâmetro foi renomeado de `n` para `numero` (nomes descritivos revelam a intenção da variável).
* Mantemos o *Type Hinting* (`numero: int` e `-> bool`) para facilitar a leitura e o uso em IDEs.
* **Linhas 2 a 13:** A *Docstring* continua sendo essencial para explicar rapidamente o que a função recebe, faz e retorna.

## 2. Tratamento Claro dos Casos Base (Early Returns)
```python
    if numero <= 1:
        return False
        
    if numero == 2:
        return True
        
    if numero % 2 == 0:
        return False
```
O conceito de **Early Return** (Retorno Antecipado) ou *Guard Clauses* ajuda a evitar aninhamentos profundos (muitos `ifs` e `elses` dentro um do outro).
* **Linhas 14-15:** Simplificamos a lógica matemática: qualquer número menor ou igual a 1 não é primo.
* **Linhas 17-18:** O número 2 é o único par que é primo, então já o liberamos como `True`.
* **Linhas 20-21:** O operador `%` retorna o resto da divisão. Se o número for divisível por 2 (resto 0), ele é par e, portanto, não é primo (retornando `False`). Isso economiza 50% do processamento do laço seguinte.

## 3. O Laço de Verificação (A Otimização O(√n))
```python
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True
```
* **Linha 24 (`divisor = 3`):** Em Clean Code, abandonamos a variável genérica `i` em favor do nome `divisor`, deixando explícito o papel desta variável no cálculo. Começamos do 3, pois os pares já foram descartados.
* **Linha 25 (`while divisor * divisor <= numero:`):** O "truque" matemático se mantém. Só precisamos testar os divisores até a raiz quadrada do `numero`. Se ele for composto (não-primo), obrigatoriamente um de seus fatores será menor ou igual à sua raiz quadrada. Expressar isso como `divisor * divisor <= numero` é melhor do que importar bibliotecas complexas para calcular raízes.
* **Linhas 26-27:** Se a divisão do `numero` pelo nosso `divisor` der exata, ele não é primo. Retornamos `False`.
* **Linha 28 (`divisor += 2`):** Pulamos os pares (testando 3, 5, 7, 9...).
* **Linha 30 (`return True`):** Passando ileso por todo o funil, confirma-se matematicamente que o número é primo.

## 4. Interação com o Usuário via Terminal
```python
def interagir_com_usuario() -> None:
    """Solicita um número ao usuário via terminal e verifica se é primo."""
    print("=== Verificador de Números Primos ===")
    while True:
        entrada = input("Digite um número inteiro (ou 'q' para sair): ")
        
        if entrada.lower() == 'q':
            print("Encerrando o programa...")
            break
            
        try:
            numero = int(entrada)
            status = "É PRIMO" if eh_primo(numero) else "NÃO É PRIMO"
            print(f"Resultado: O número {numero} {status}!\n")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números inteiros.\n")

if __name__ == "__main__":
    interagir_com_usuario()
```
* **Linhas 35-40 (Loop Interativo e Condição de Parada):** O `while True:` (linha 35) mantém o programa rodando para que o usuário possa testar vários números. A função nativa `input()` (linha 36) paralisa a execução esperando a digitação. Se a pessoa digitar `'q'` (ou `'Q'`, graças ao `.lower()` na linha 38), o comando `break` (linha 40) é acionado, encerrando o programa.
* **Linhas 42-47 (Tratamento de Exceções `try/except`):** Todo retorno do `input` é texto. Ao tentar converter esse texto para número na linha 43 (`int(entrada)`), o programa poderia "quebrar" caso o usuário digitasse uma letra (ex: "casa"). O bloco `try` tenta executar o código; se falhar (não for número), o erro `ValueError` é capturado pelo `except` na linha 46, exibindo um aviso amigável na linha 47 sem fechar o programa.
* **Linhas 49-50 (Ponto de Entrada Seguro):** `if __name__ == "__main__":` garante que o loop interativo só iniciará se o script for rodado diretamente pelo console, impedindo que o script trave se ele for importado por outro módulo do seu sistema.
