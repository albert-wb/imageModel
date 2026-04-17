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
