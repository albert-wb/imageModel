def calcular_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma total, média, valor máximo e valor mínimo de uma lista de números.
    
    Args:
        numeros: Lista contendo os números a serem analisados.
        
    Returns:
        Uma tupla contendo (total, media, maior_valor, menor_valor).
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia.")

    total = 0
    maior_valor = numeros[0]
    menor_valor = numeros[0]

    # Itera diretamente sobre os valores (mais legível do que usar range(len(l)))
    # e consolida tudo em um único laço de repetição.
    for numero in numeros:
        total += numero
        
        if numero > maior_valor:
            maior_valor = numero
            
        if numero < menor_valor:
            menor_valor = numero

    media = total / len(numeros)

    return total, media, maior_valor, menor_valor


if __name__ == "__main__":
    valores_teste = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    # Desempacotamento semântico
    soma_total, media_calculada, valor_maximo, valor_minimo = calcular_estatisticas(valores_teste)
    
    print("=== Resultados Estatísticos ===")
    print(f"Total: {soma_total}")
    print(f"Média: {media_calculada:.2f}")
    print(f"Maior: {valor_maximo}")
    print(f"Menor: {valor_minimo}")