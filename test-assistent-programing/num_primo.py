def is_primo(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que não possui
    divisores além de 1 e ele mesmo.

    Args:
        n: O número inteiro a ser verificado.

    Returns:
        True se n for primo, False caso contrário.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Verifica divisores ímpares até a raiz quadrada de n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


# --- Testes ---
if __name__ == "__main__":
    casos_de_teste = [0, 1, 2, 3, 4, 17, 18, 97, 100, 101]

    for numero in casos_de_teste:
        resultado = "primo" if is_primo(numero) else "não primo"
        print(f"{numero:>4} -> {resultado}")
