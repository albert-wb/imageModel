def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que não possui
    divisores além de 1 e ele mesmo.

    Args:
        numero: O número inteiro a ser verificado.

    Returns:
        True se o número for primo, False caso contrário.
    """
    if numero <= 1:
        return False
        
    if numero == 2:
        return True
        
    if numero % 2 == 0:
        return False

    # Verifica divisores ímpares até a raiz quadrada do número
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True

def executar_testes() -> None:
    """Executa casos de teste predefinidos para validar a função eh_primo."""
    casos_de_teste = [0, 1, 2, 3, 4, 17, 18, 97, 100, 101]

    for numero in casos_de_teste:
        status = "primo" if eh_primo(numero) else "não primo"
        print(f"{numero:>4} -> {status}")

if __name__ == "__main__":
    executar_testes()
